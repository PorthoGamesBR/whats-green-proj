from whats import Whats
from selenium.webdriver.common.by import By
from time import sleep

wts = Whats()

def main():
    # Test code, do NOT send to main
    sleep(30)
    contacts = wts.get_all_contacts_web()
    if contacts:
        for c in contacts:
            try:
                print('Contact:',c.find_element(By.CLASS_NAME, "zoWT4").text)
                print('Last Sent Message',c.find_element(By.CLASS_NAME, "Hy9nV").text)
                print()
            except Exception:
                print(c.text)
                print()

if __name__ == "__main__":
    main()