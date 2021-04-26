import os

BROWSER_CHROME = "chrome"
BROWSER_FIREFOX = "firefox"

SUPPORTED_BROWSERS = [
    BROWSER_CHROME,
    BROWSER_FIREFOX,
]

GET_TITLE_QUERY = '//span[contains(@title,"{}")]'

MESSAGE_BOX_CSS_ATTRIBUTE = "div[data-tab='6']"

CHROMEDRIVER_PATH = 'whatsapp_sender/chromedriver'
GECKODRIVER_PATH = 'whatsapp_sender/geckodriver'