from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
    
class WhatsElementsID:
    
    contacts = "side"
    messages = "main"
    
class WhatsElementsClass:
    
    contact_mesg_desc = "Hy9nV"

class Whats:
    
    def __init__(self):
        self.nav = webdriver.Chrome(ChromeDriverManager().install())
        self.nav.get('https://web.whatsapp.com')
        while len(self.nav.find_elements(By.ID,'side')) < 1:
            time.sleep(1)
            
        # Test code, get rid of it later        
        mesg_descs = ""
        while len(mesg_descs) < 1:
            mesg_descs = self.nav.find_elements(By.CLASS_NAME, WhatsElementsClass.contact_mesg_desc)
            time.sleep(1)
        
        print(len(mesg_descs))
        for msg in mesg_descs:
            print(msg.text)
        #We need to find a way to scroll the whole contact list
            
    
    # Send message to a contact or group
    def send_message_to():
        pass
    
    # Await for a message from any contact or a specific contact. Returns the contact
    def await_message():
        # Await until message notification
        pass