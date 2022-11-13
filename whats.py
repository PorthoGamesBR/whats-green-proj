from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


import time
    
class WhatsElementsID:
    
    contacts = "side"
    messages = "main"
    
class WhatsElementsClass:
    
    contact_text = "_3OvU8"
    
    contact_mesg_desc = "Hy9nV"

class Whats:
    

    def __init__(self):
        self.nav = webdriver.Chrome(ChromeDriverManager().install())
        self.config = {'timeout' : 120}
        self.nav.get('https://web.whatsapp.com')
        WebDriverWait(self.nav, self.config['timeout']).until(EC.visibility_of_element_located((By.ID,WhatsElementsID.contacts)))
            
        #We need to find a way to scroll the whole contact list
            
    def get_all_contacts_web(self) -> list[WebElement]:
        # Will await untill the contact text is visible
        WebDriverWait(self.nav, self.config['timeout']).until(EC.visibility_of_element_located((By.CLASS_NAME,WhatsElementsClass.contact_text)))
        
        # Get all visible contacts as WebElement objects (Name and last sent message)
        contacts = self.nav.find_elements(By.CLASS_NAME, WhatsElementsClass.contact_text)
        
        return contacts
        
    # Send message to a contact or group
    def send_message_to():
        pass
    
    # Await for a message from any contact or a specific contact. Returns the contact
    def await_message():
        # Await until message notification
        pass