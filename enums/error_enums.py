from enum import Enum


class ErrorElements(Enum):
    ERROR_IMAGE_NOT_DISPLAYED = 'Image not displayed on the page'
    ERROR_IMAGE_SIZE = 'Incorrect image size'
    ERROR_FAVICON = "Favicon, image failed to load"
    ERROR_IMAGE = "Image Error"
    ERROR_DOUBLE_CLICK = 'Double-click button broken'
    ERROR_RIGHT_CLICK = 'Right click button broken'
    ERROR_DYNAMIC_BUTTON = 'Dynamic button broken'
    ERROR_CHECKBOX_SELECTED = lambda index: f'Checkbox {index} not selected'
    ERROR_SELECTED_RADIOBUTTON = 'Radio button not selected'
    INVALID_PLACEHOLDER = lambda placeholder: f'Invalid placeholder: {placeholder}'
    INVALID_NAME = 'Invalid user name'
    INVALID_ADDRESS = 'Invalid address'
    INVALID_EMAIL = 'Invalid user email'
    ERROR_DOWNLOAD = "File didn't download"
    ERROR_UPLOAD = 'File did not upload to the site'
    INVALID_FILE_FORMAT = lambda format: f'Invalid file format, format:{format}'


class ErrorWindows(Enum):
    ERROR_MESSAGE_ALERT = lambda alert_message: f'Invalid message in the alerts, message: {alert_message}'
    ERROR_ALERT_RESULT = 'Incorrect result of the alerts'
    ERROR_ALERT_VALUE = lambda name, result_alert: f'Invalid value:{name} entered the alerts:{result_alert}'
    INVALID_MESSAGE_FRAME = 'Invalid message to frame'
    INVALID_MESSAGE_MODAL = 'Invalid message to modal dialogs'
    ERROR_FRAME = 'Invalid frame'
    ERROR_NEW_TAB = 'New tab did not open'
    ERROR_OPEN_TAB = 'Wrong tab opened'
    ERROR_NEW_WINDOW = "New window didn't open"
    ERROR_OPEN_WINDOW = 'Wrong window opened'
    ERROR_OPEN_WINDOW_MESSAGE = 'Wrong message window opened'


class ErrorWidgets(Enum):
    ERROR_SECTION_OPENED = 'Wrong section opened'
    ERROR_MULTISELECT_EMPTY = 'Multiselect is not empty'
    ERROR_MULTISELECT_VALUE = lambda color: f'Value {color} is not selected in Multiselect'
    ERROR_MULTISELECT_SINGLE = lambda color: f'Value {color} is not selected in Multiselect single color'
    ERROR_DATE = 'Wrong date on the calendar'
    ERROR_DATE_TIME = 'Wrong date and time on the calendar'
    ERROR_PROGRESS_BAR_START = 'The progress bar did not start'
    ERROR_PROGRESS_BAR_STOP = 'Progress bar loading has not stopped'
    ERROR_PROGRESS_BAR_RESTART = 'Progress bar did not load all the way'
    ERROR_PROGRESS_BAR_VALUE0 = 'Progress bar did not update to 0'
    ERROR_VALUE_DROPDOWN = lambda value:  f'No value {value} in dropdown'
    ERROR_LEN_DROPDOWN = lambda len: f'Wrong number of options in dropdown: {len}'
    ERROR_SLIDER = 'Wrong slider value'
    INVALID_MESSAGE_TAB = 'Invalid message in the tab'
    ERROR_ACTIV_TAB = 'Tab more active'
    ERROR_TOOLTIP = 'Wrong tooltip'


class ErrorForm(Enum):
    ERROR_OPEN_FORM = 'Submitted form did not open'
    ERROR_SUBJECTS = lambda subject: f'Wrong subjects: {subject}'
    ERROR_HOBBIES = lambda hobby: f'Wrong hobbies: {hobby}'
    ERROR_CITY_STATE = lambda state, city:  f'Wrong state:{state} and city:{city}'
    ERROR_FIRST_NAME = lambda FirstName:  f'Wrong first_name: {FirstName}'
    ERROR_LAST_NAME = lambda LastName:  f'Wrong last_name: {LastName}'
    ERROR_STUDENT_EMAIL = lambda email: f'Wrong user email: {email}'
    ERROR_GENDER = lambda gender: f'Wrong gender: {gender}'
    ERROR_MOBILE = lambda mobile: f'Wrong phone number: {mobile}'
    ERROR_PICTURE = lambda picture: f'Wrong picture'
    ERROR_BIRTHDAY = lambda birthday: f'Wrong birthday: {birthday}'
    ERROR_ADDRESS = lambda address: f'Wrong address: {address}'


class ErrorInter(Enum):
    INVALID_HEIGHT = lambda height: f'Invalid height:{height}'
    INVALID_WIDTH = lambda width: f'Invalid width: {width}'
    ERROR_HEIGHT_CONTAINER = lambda height, container: f'Height {height} is greater than the height {container} of the container'
    ERROR_WIDTH_CONTAINER = lambda width, container: f'Width {width} is greater than the width {container} of the container'
    ERROR_DROP_INACTIVE = 'drop from inactive'
    ERROR_DROP_ACTIVE = 'drop from active'
    ERROR_VALUE_DROP = lambda value : f'Incorrect value in drop: {value}'
    ERROR_HEIGHT_REVERT = 'Incorrect height when dragging an object with revert'
    ERROR_WITH_REVERT = 'Incorrect width when dragging an object with revert'
    ERROR_SELECTED_LINE = 'Line not selected'
    ERROR_SELECTED_CELL = 'Cell not selected'
    ERROR_SORTING_DESC = 'Incorrect descending sorting'





