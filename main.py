from whats import Whats
from selenium.webdriver.common.by import By

wts = Whats()

def main():
    # Test code, do NOT send to main
    contacts = wts.get_all_contacts_web()
    if contacts:
        for c in contacts:
            print('Contact:',c.find_element(By.CLASS_NAME, "zoWT4").text)
            print('Last Sent Message',c.find_element(By.CLASS_NAME, "Hy9nV").text)
            print()

if __name__ == "__main__":
    main()