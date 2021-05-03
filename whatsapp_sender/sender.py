from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import whatsapp_sender.constants as constants


class MessageSender:
    def __init__(self, browser: str):
        """
        :param browser: Defines the browser used by the user
        """
        try:
            if browser.lower() not in constants.SUPPORTED_BROWSERS:
                raise Exception(
                    "Please select a browser which supports. Supported browsers : Chrome, Firefox"
                )
            if browser.lower() == constants.BROWSER_CHROME:
                self.driver = webdriver.Chrome(
                    executable_path=constants.CHROMEDRIVER_PATH
                )
            if browser.lower() == constants.BROWSER_FIREFOX:
                self.driver = webdriver.Firefox(
                    executable_path=constants.GECKODRIVER_PATH
                )
        except Exception as error:
            print(error)
            return None

    def get_contact_title(self, contact: str):
        """
        :param contact: name of contact
        """
        try:
            wait = WebDriverWait(self.driver, 160)
            x_arg_2 = constants.SEARCH_TITLE_X_ARG
            search_title = wait.until(EC.presence_of_element_located((By.XPATH,x_arg_2)))
            search_title.send_keys(contact)
            x_arg = constants.GET_TITLE_QUERY.format(contact)
            return wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        except Exception as error:
            print(error)
            return None

    def type_message(self, message: str):
        """
        :param message: text to be sent
        """
        try:
            element = self.driver.find_element_by_css_selector(
                constants.MESSAGE_BOX_CSS_ATTRIBUTE
            )
            element.send_keys(message + Keys.ENTER)
        except Exception as error:
            print(error)
            return None

    def send_messages(self, contacts: list, message: str):
        """
        :params contacts : list of contacts to send messages, message : string to send
        """
        self.driver.get("https://web.whatsapp.com")
        print(contacts)
        for contact in contacts:
            contact_title = MessageSender.get_contact_title(self,contact)
            if contact_title == None:
                print(contact)
                continue
            contact_title.click()
            MessageSender.type_message(self,message)
        self.driver.quit()
        return True
