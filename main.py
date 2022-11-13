from whats import Whats

wts = Whats()

def main():
    # Test code, do NOT send to main
    contacts = wts.get_all_contacts_web()
    for c in contacts:
        print(c.text)

if __name__ == "__main__":
    main()