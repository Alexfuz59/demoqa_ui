import platform


class EnvironmentAllure:

    environment = {'OC': platform.platform(),
                   'Python': platform.python_version(),
                   'Allure-report version': '2.23.1'
                   }

    @staticmethod
    def create_environment(driver, env=environment):
        with open('environment.properties', 'w', encoding='utf-8') as file:
            for key, value in env.items():
                file.write(f'{key}: {value}' + '\n')
            file.write(f'Browser: {driver.capabilities["browserName"]}' + '\n')
            file.write(f'Browser_version: {driver.capabilities["browserVersion"]}' + '\n')


