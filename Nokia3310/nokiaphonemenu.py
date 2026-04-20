while True:
    menu = input("""
    NOKIA PHONE MENU

1-> Phone book              
2-> Messages                
3-> Chat                    
4-> Call Register           
5-> Tones                   
6-> Settings               
7-> Call Divert             
8-> Games                   
9-> Calculator             
10-> Reminders              
11-> Clock                  
12-> Profiles               
13-> SIM services           
0-> Exit

Select option: """)

    if menu == '1':
        phoneBook= input("""
PHONE BOOK
1-> Search
2-> Service Nos.
3-> Add name
4-> Erase
Select option: """)

        if Phonebook== '1':
            print("Search Activated")
        elif Phonebook== '2':
            print("Service Numbers")
        elif Phonebook== '3':
            print("Add Name")
        elif Phonebook == '4':
            print("Erase Contact")
        else:
            print("Invalid option")

    elif menu == '2':
        msg = input("""
MESSAGES
1-> Write message
2-> Inbox
3-> Outbox
4-> Message settings
Select option: """)

        if msg == '1':
            print("Writing message...")
        elif msg == '2':
            print("Inbox opened")
        elif msg == '3':
            print("Outbox opened")
        elif msg == '4':
            setting = input("""
MESSAGE SETTINGS
1-> Set
2-> Common
Select option: """)

            if setting == '1':
                print("Message Centre / Sent As / Validity")
            elif setting == '2':
                print("Delivery Report / Reply via same centre")
            else:
                print("Invalid option")
        else:
            print("Invalid option")

    elif menu == '3':
        print("Chat feature coming soon...")


    elif menu == '4':
        call = input("""
CALL REGISTER
1-> Missed calls
2-> Received calls
3-> Dialled numbers
Select option: """)

        if call == '1':
            print("Missed Calls")
        elif call == '2':
            print("Received Calls")
        elif call == '3':
            print("Dialled Numbers")
        else:
            print("Invalid option")


    elif menu == '5':
        tone = input("""
TONES
1-> Ringing tone
2-> Volume
3-> Vibrate
Select option: """)

        if tone == '1':
            print("Ringing tone set")
        elif tone == '2':
            print("Volume adjusted")
        elif tone == '3':
            print("Vibration ON")
        else:
            print("Invalid option")


    elif menu == '6':
        sett = input("""
SETTINGS
1-> Call settings
2-> Phone settings
Select option: """)

        if sett == '1':
            print("Call settings opened")
        elif sett == '2':
            print("Phone settings opened")
        else:
            print("Invalid option")

    elif menu == '7':
        print("Call divert activated")

    elif menu == '8':
        print("Games loading...")

    elif menu == '9':
        print("Calculator")

    elif menu == '10':
        print("Reminder set")


    elif menu == '11':
        clock = input("""
CLOCK
1-> Alarm
2-> Date
3-> Stopwatch
Select option: """)

        if clock == '1':
            print("Alarm set")
        elif clock == '2':
            print("Date settings")
        elif clock == '3':
            print("Stopwatch started")
        else:
            print("Invalid option")

    elif menu == '12':
        print("Profiles updated")


    elif menu == '13':
        print("SIM services opened")


    elif menu == '0':
        print("Exiting phone...")
        break

    else:
        print("Invalid input")
