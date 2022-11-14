from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager


import time
    
class WhatsElementsID:
    
    contacts = "side"
    messages = "main"
    
class WhatsElementsClass:
    
    #contact_text = "_3OvU8"
    contact_text = "_2nY6U.vq6sj"
    contact_name = "zoWT4"
    contact_mesg_desc = "Hy9nV"

class Whats:

    def __init__(self):
        self.nav = webdriver.Chrome(ChromeDriverManager().install())
        self.config = {'timeout' : 120}
        self.nav.get('https://web.whatsapp.com')
        #self.nav.execute_script("document.body.style.zoom='25%'")
        try:
            WebDriverWait(self.nav, self.config['timeout']).until(EC.visibility_of_element_located((By.ID,WhatsElementsID.contacts)))
        except Exception:
            print('Error: Timeout while connecting to whats')
            self.nav.quit()
        #We need to find a way to scroll the whole contact list
            
    def get_all_contacts_web(self) -> list[WebElement]:
        # Will await untill the contact text is visible
        try:
            contacts = WebDriverWait(self.nav, self.config['timeout']).until(EC.visibility_of_element_located((By.XPATH,'//div[@data-testid="cell-frame-container"]')))
        except Exception:
            print("Error at 'get_all_contacts_web()'. Did not found any contact.")
            return None
        
        contacts = self.nav.find_elements(By.XPATH,'//div[@data-testid="cell-frame-container"]')
        for c in contacts:
            print(c.text)
        return contacts
        
    # Send message to a contact or group
    def send_message_to(self,contact):
        contacts = self.get_all_contacts_web()
        if contacts:
            for c in contacts:
                    try:
                        cont = c.find_element(By.CLASS_NAME,WhatsElementsClass.contact_name).text
                        print('Name:',cont)
                    except Exception:
                        print('Contact not found')
                        print(c.text)
                        continue
                    
                    if cont == contact:
                        Hover = ActionChains(self.nav).move_to_element(c)
                        Hover.click().perform()
                        break
                        
        
    
    # Await for a message from any contact or a specific contact. Returns the contact
    def await_message(self, msg):    
        # Await until message notification
        contacts = self.get_all_contacts_web()
        if contacts:
            for c in contacts:
                if c.text == 'Arquivadas':
                    continue
                try:
                    last_msg = c.find_element(By.CLASS_NAME,WhatsElementsClass.contact_mesg_desc).text
                    print('message:',"".join(last_msg.split()))
                except Exception:
                    print('Message not found')
                    print(c.text)
                    continue
                try:
                    contact = c.find_element(By.CLASS_NAME, WhatsElementsClass.contact_name).text
                except Exception:
                    print('Contact of message not found')
                    print(c.text)
                    continue
                
                if "".join(last_msg.split()) == msg:
                    return contact
            
    def close(self):
        self.nav.quit()
    
