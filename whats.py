from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

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
        self.nav.get('https://web.whatsapp.com')
        while len(self.nav.find_elements(By.ID,'side')) < 1:
            time.sleep(1)
            
        #We need to find a way to scroll the whole contact list
            
    def get_all_contacts_web(self) -> list[WebElement]:
        # Get all visible contacts as WebElement objects (Name and last sent message)
        contacts = ''
        
        # Will await until the contacts are visible
        while len(contacts) < 1:
            contacts = self.nav.find_elements(By.CLASS_NAME, WhatsElementsClass.contact_text)
            time.sleep(1)
        
        return contacts
        
    # Send message to a contact or group
    def send_message_to():
        pass
    
    # Await for a message from any contact or a specific contact. Returns the contact
    def await_message():
        # Await until message notification
        pass