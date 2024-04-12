import pytest
from pages.elements.text_box import TextBox
from pages.elements.checkbox import Checkbox
from pages.elements.radio_button import RadioButton
from pages.elements.buttons import Buttons
from pages.elements.dynamic_properties import DynamicProperties
from pages.elements.broken_links import BrokenLinks
from pages.elements.upload_download import UploadDownload
from pages.windows.windows import Windows
from pages.windows.alert import Alert
from pages.windows.iframe import Frame
from pages.windows.nested_frames import NestedFrames
from pages.windows.modal_dialogs import ModalDialogs
from pages.widgets.accordian import Accordian
from pages.widgets.auto_complete import AutoComplete
from pages.widgets.slider import Slider
from pages.widgets.progress_bar import ProgressBar
from pages.widgets.tabs import Tabs
from pages.widgets.tool_tips import ToolTips
from pages.widgets.menu import Menu
from pages.widgets.select_menu import SelectMenu
from pages.interactions.sortable import Sortable
from pages.interactions.selectable import Selectable
from pages.interactions.resizable import Resizable
from pages.interactions.droppable import Droppable
from pages.interactions.dragabble import Dragabble
from pages.forms.practice_form import PracticeForm
from pages.widgets.date_picker import DatePicker


class BaseTest:
    text_box: TextBox
    checkbox: Checkbox
    radio_button: RadioButton
    buttons: Buttons
    dynamic_properties: DynamicProperties
    broken_links: BrokenLinks
    upload_download: UploadDownload
    windows: Windows
    alert: Alert
    iframe: Frame
    nested_frames: NestedFrames
    modal_dialogs: ModalDialogs
    accordian: Accordian
    auto_complete: AutoComplete
    slider: Slider
    progress_bar: ProgressBar
    tabs: Tabs
    tool_tips: ToolTips
    menu: Menu
    select_menu: SelectMenu
    sortable: Sortable
    selectable: Selectable
    resizable: Resizable
    droppable: Droppable
    dragabble: Dragabble
    practice_form: PracticeForm
    date_picker: DatePicker

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box = TextBox(driver)
        request.cls.checkbox = Checkbox(driver)
        request.cls.radio_button = RadioButton(driver)
        request.cls.buttons = Buttons(driver)
        request.cls.dynamic_properties = DynamicProperties(driver)
        request.cls.broken_links = BrokenLinks(driver)
        request.cls.upload_download = UploadDownload(driver)
        request.cls.windows = Windows(driver)
        request.cls.alert = Alert(driver)
        request.cls.iframe = Frame(driver)
        request.cls.nested_frames = NestedFrames(driver)
        request.cls.modal_dialogs = ModalDialogs(driver)
        request.cls.accordian = Accordian(driver)
        request.cls.auto_complete = AutoComplete(driver)
        request.cls.slider = Slider(driver)
        request.cls.progress_bar = ProgressBar(driver)
        request.cls.tabs = Tabs(driver)
        request.cls.tool_tips = ToolTips(driver)
        request.cls.menu = Menu(driver)
        request.cls.select_menu = SelectMenu(driver)
        request.cls.sortable = Sortable(driver)
        request.cls.selectable = Selectable(driver)
        request.cls.resizable = Resizable(driver)
        request.cls.droppable = Droppable(driver)
        request.cls.dragabble = Dragabble(driver)
        request.cls.practice_form = PracticeForm(driver)
        request.cls.date_picker = DatePicker(driver)



