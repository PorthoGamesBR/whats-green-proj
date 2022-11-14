from whats import Whats
from time import sleep

wts = Whats()
messages = ["""Você:!hello"""]

running = False
def main():
    running = True
    
    while running:
        # Check for special messages in contacts
        # If there is one, add contact to 'dialogue_list' at tier 1
        # Check for every dialogue open in 'dialogue_list'
        # If a valid response message has been sent, respond to it (based on tier) and up the tier of the contact
        # If a dialogue get to the end, notify the user somehow  
        sleep(10)
        contact = wts.await_message(messages[0])
        if contact:
            print('This contact send you hello:',contact)
            wts.send_message_to(contact)
            sleep(60)
            running = False
            wts.close()

if __name__ == "__main__":
    main()