from whats import Whats
from time import sleep

wts = Whats()
messages = ["""Você:!hello"""]

running = False
def main():
    running = True
    
    while running:
        sleep(10)
        contact = wts.await_message(messages[0])
        if contact:
            print('This contact send you hello:',contact)
            running = False
            wts.close()

if __name__ == "__main__":
    main()