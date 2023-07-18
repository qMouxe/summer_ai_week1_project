#Various import Statements can go here
from  social_network_classes import SocialNetwork, Person
import social_network_ui
import json
import os


ai_social_network = SocialNetwork()
            #The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()
    while True: 
        data = [ai_social_network.list_of_people,ai_social_network.friendList,ai_social_network.messages,ai_social_network.blockList,ai_social_network.check,ai_social_network.friendRequests,ai_social_network.name]
        with open('data.json', 'w') as p:  # rewind
            json.dump(data, p)
        p.close()
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account() 
        elif choice == "2":
            ai_social_network.login()
        elif choice == "3":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            if inner_menu_choice == "4":
                social_network_ui.mainMenu()
            elif inner_menu_choice == "1":
                ai_social_network.edit_details()
            elif inner_menu_choice == "2":
                friend_menu_choice = social_network_ui.friendMenu()
                if friend_menu_choice == "1":
                    ai_social_network.add_friend()
                elif friend_menu_choice == "2":
                    ai_social_network.view_Friends()
                elif friend_menu_choice == "3":
                    ai_social_network.check_Friends()
                elif friend_menu_choice == "4":
                    ai_social_network.block_User()
                elif friend_menu_choice == "5":
                    ai_social_network.unblock_User()
            elif inner_menu_choice == "3":
                msg_menu_choice = social_network_ui.msgMenu()
                if msg_menu_choice == "1":
                    ai_social_network.send_message()
                elif msg_menu_choice == "2":
                    ai_social_network.check_Messages()
        elif choice == "4":
            print("Thank you for visiting. Goodbye3")
            break
        elif choice == "5":
            ai_social_network.reset_data()
        else:
            print("Your input is invalid. Try Again!")
        choice = social_network_ui.mainMenu()
        with open('data.json', 'w') as p:  # rewind
            json.dump(data, p)
        p.close()

    
        



        
