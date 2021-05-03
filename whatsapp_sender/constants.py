import os

BROWSER_CHROME = "chrome"
BROWSER_FIREFOX = "firefox"

SUPPORTED_BROWSERS = [
    BROWSER_CHROME,
    BROWSER_FIREFOX,
]

GET_TITLE_QUERY = '//span[contains(@title,"{}")]'
SEARCH_TITLE_X_ARG = '/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]'
MESSAGE_BOX_CSS_ATTRIBUTE = "div[data-tab='6']"

CHROMEDRIVER_PATH = 'whatsapp_sender/chromedriver'
GECKODRIVER_PATH = 'whatsapp_sender/geckodriver'