import pytest
import allure
import selenium.webdriver.firefox.service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_firefox
from config.environment_allure import EnvironmentAllure
from fake_useragent import UserAgent


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function", autouse=True)
def driver(request, tmpdir):
    browser_name = request.config.getoption("browser_name")
    ua = UserAgent()
    us_ag = ua.random
    if browser_name == "chrome":
        options_chrome = Options_chrome()
        options_chrome.add_argument("--headless")
        options_chrome.add_argument("--window-size=1920,1080")
        options_chrome.add_argument("--disable-cache")
        options_chrome.add_argument('--ignore-certificate-errors')
        options_chrome.add_argument("--disable-blink-features=AutomationControlled")
        options_chrome.add_argument(f"user-agent={us_ag}")
        prefs = {
            "download.default_directory": str(tmpdir),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True
        }
        options_chrome.add_experimental_option("prefs", prefs)
        print("\nstart Chrome browser for test..")
        driver = webdriver.Chrome(options=options_chrome)
        request.cls.driver = driver
    elif browser_name == "firefox":
        options_firefox = Options_firefox()
        firefox_bin = "/snap/firefox/current/usr/lib/firefox/firefox"
        firefox_driver_bin = "/snap/firefox/current/usr/lib/firefox/geckodriver"
        options_firefox.binary_location = firefox_bin
        options_firefox.add_argument("--headless")
        options_firefox.add_argument("--window-size=1920,1080")
        options_firefox.add_argument("--disable-cache")
        options_firefox.add_argument('--ignore-certificate-errors')
        options_firefox.set_preference("dom.webdriver.enabled", False)
        options_firefox.set_preference("general.useragent.override", us_ag)
        service = selenium.webdriver.firefox.service.Service(executable_path=firefox_driver_bin)
        download_dir = str(tmpdir)
        options_firefox.set_preference("browser.download.folderList", 2)
        options_firefox.set_preference("browser.download.dir", download_dir)
        options_firefox.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        print("\nstart Firefox browser for test..")
        driver = webdriver.Firefox(service=service, options=options_firefox)
        request.cls.driver = driver
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        take_screenshot(driver, request.node.name)
    print("\nquit browser..")
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def take_screenshot(driver, test_name):
    screenshot_name = f"{test_name}.png"
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)


@pytest.fixture(autouse=True)
def environment_allure(driver):
    EnvironmentAllure.create_environment(driver)
