from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class WhatsElementsID:
    
    contacts = "pane-side"
    messages = "main"

class Whats:
    
    def __init__(self):
        self.nav = webdriver.Chrome(ChromeDriverManager().install())
        self.nav.get('https://web.whatsapp.com')
        while len(self.nav.find_elements(By.ID,'side')) < 1:
            time.sleep(1)
            
    
    # Send message to a contact or group
    def send_message_to():
        pass
    
    # Await for a message from any contact or a specific contact. Returns the contact
    def await_message():
        pass