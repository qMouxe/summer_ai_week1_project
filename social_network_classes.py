
import social_network_ui
import os
import json
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
        self.friendList = []
        self.messages = []     
        self.blockList = []                 # you can save objects of people on the network in this list
        self.check = "False"
        self.friendRequests = []
        self.name = ""
        self.data = [self.list_of_people,self.friendList,self.messages,self.blockList,self.check,self.friendRequests,self.name]
    ## For more challenge try this

    ## For more challenge try this

    def reset_data(self):
        ai_social_network = SocialNetwork()
        data = [ai_social_network.list_of_people,ai_social_network.friendList,ai_social_network.messages,ai_social_network.blockList,ai_social_network.check,ai_social_network.friendRequests,ai_social_network.name]
        os.remove("data.json")
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
        self.friendList = []
        self.messages = []     
        self.blockList = []                 # you can save objects of people on the network in this list
        self.check = "False"
        self.friendRequests = []
        self.name = ""
        with open("data.json", "w") as f:
            (json.dump(data,f))

    def load_Data(self):
        with open("data.json","w") as p:
            dd = json.load(p)
        self.list_of_people = dd[0]
        self.friendList = dd[1]
        self.messages = dd[2]     
        self.blockList = dd[3] 
        self.check = dd[4]
        self.friendRequests = dd[5]
        self.name = dd[6]
        p.close()

    def  create_account(self):
        #implement function that creates account here
        newID = input("Please enter your name: ")
        newPass = input("Please enter your Password")
        passCheck = input("Please reenter password: ")
        if passCheck == newPass:
            self.list_of_people.append([newID,newPass])
            self.id = newID
            self.friendList.append([])
            self.messages.append([])
            self.blockList.append([])
            print("Creating ...")
            print("Account created! Welcome, " + newID)
            print(self.list_of_people)
            print(self.blockList)
            
            pass
        else:
            print("Passwords do not match, please try again")
            return

    def edit_details(self):
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            accID = int(self.accID)
            temp = accID+1
            listOfPeople = self.list_of_people
            print("")
            print("You are now in the edit details menu")
            new_name = input("Enter new name: ")
            passCheck = input("Please enter old password: ")
            if passCheck == listOfPeople[accID][1]:
                newPass = input("Enter new password:")
                newData = [new_name, newPass]
                del listOfPeople[accID]
                listOfPeople.insert(accID,newData)
                print("********************************************************")
                print("Success! Your details have been changed")
                print("********************************************************")
                print(listOfPeople)
               
            else: 
                print("Incorrect password")
                return
            
        
    
    def login(self):
        passwordCheck = "No"
        existing = "False"
        accID = 0
        self.check = "False"
        listOfPeople = self.list_of_people
        print("")
        print(len(listOfPeople))
        self.name = input("What is the name of your account? ")
        name = self.name
        if len(listOfPeople) == 0:
            print("********************************************************")
            print("Please create an account first!")
            print("********************************************************")
        for i in range (len(listOfPeople)):
            if name == listOfPeople[i][0]:
                password = input("Enter the password: ")
                existing = "True"
                if password == listOfPeople[i][1]:
                    print("********************************************************")
                    print("Success! Logged in as: " + name)
                    print("********************************************************")
                    self.accID = i
                    self.check = "True"
                    passwordCheck = "True"
                    print(self.accID)
                    
                else:
                    passwordCheck = "False"
        if passwordCheck == "False":
            print("********************************************************")
            print("Password incorrect, please try again")
            print("********************************************************")
        elif existing == "False":
            print("********************************************************")
            print("Account not found, please try again")
            print("********************************************************")

    def add_friend(self):
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            check = "False"
            friendAccID = 0
            senderID = self.accID
            print("")
            friendName = input("What is the name of the user you want to add? ")
            for i in range (len(self.list_of_people)):
                if friendName == self.list_of_people[i][0]:
                    friendAccID = i
                    self.friendRequests.append([friendAccID, self.name, senderID])
                    print("********************************************************")
                    print("Friend Request sent!")
                    print("********************************************************")
                    check = True
            if check == "False":
                print("********************************************************")
                print("User not found, please try again")
                print("********************************************************")
            print(self.friendRequests)

    def check_Friends(self):
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            removedNum = []
            print("")
            print(self.name)
            check = "True"
            for i in range (len(self.friendRequests)):
                friendAccID = self.friendRequests[i][0]
                name = self.friendRequests[i][1]
                senderID = self.friendRequests[i][2]
                if self.accID == friendAccID:
                    print("You have a request from: " + name)
                    response = input("Input 'a' to accept, 'd' to decline: ")
                    if response == "a":
                        print("********************************************************")
                        print("Success! User " + name + " has been added to your friends list")
                        print("********************************************************")
                        self.friendList[self.accID].append(name)
                        self.friendList[senderID].append(self.name)
                        removedNum.append(i)
                        print(self.friendRequests)
                        print(self.friendList)
                        print(removedNum)
                    else:
                        removedNum.append(i)
                        return
            for a in range(len(removedNum)):
                del self.friendRequests[removedNum[a-1]]
            if len(self.friendRequests) == 0:
                print("You have no friend requests")
            
    
    def view_Friends(self):
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            print("")
            print("Your friends are: ")
            for i in range(len(self.friendList[self.accID])):
                print(self.friendList[self.accID][i])

    def send_message(self):
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            sender = self.name
            blocked = ""
            recipient = input("Input the recipient of the message: ")
            check = ""
            existing = "False"
            for a in range(len(self.list_of_people)):
                if recipient == self.list_of_people[a][0]:
                    existing = "True"
                    recipientID = a
            if existing == "False":
                print("User not found")
                return
                
            for i in range(len(self.blockList[recipientID])):
                if sender == self.blockList[recipientID][i]:
                    blocked = "True"
                else:
                    blocked = "False"
            if blocked == "True":
                print("********************************************************")
                print("You have been blocked by: " + recipient)
                print("********************************************************")
                return
                
            else:
                msgContent = input("Input your message: ")
                self.messages[recipientID].append(sender)
                self.messages[recipientID].append(msgContent)
                print("********************************************************")
                print("Message sent!")
                print("********************************************************")
           
    
    
    def check_Messages(self):
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            for i in range(len(self.messages)):
                if self.accID == i:
                    for a in range(len(self.messages[i])):
                        if a%2 == 0:
                            print("From: " + str(self.messages[i][a]) + ": ")
                        else:
                            print(str(self.messages[i][a]))
    
    def block_User(self):
        check = "False"
        if self.check == "False":
            print("********************************************************")
            print("Please log in first! ")
            print("********************************************************")
            social_network_ui.mainMenu()
        else:
            user = input("Enter the name of the user you would like to block: ")
            for i in range(len(self.friendList[self.accID])):
                if user == self.friendList[self.accID][i]:
                    blockedID = i
                    self.blockList[self.accID].append(user)
                    print("********************************************************")
                    print("Success! " + user + " has been blocked!")
                    print("********************************************************")
                    check = "True"
            if check == "False":
                print("User not found in friend list")
                return

    def unblock_User(self):
        target = input("Enter user you would like unblock: ")
        for i in range(len(self.blockList[self.accID])):
            if target == self.blockList[self.accID][i]:
                del self.blockList[self.accID][i]
                print("User " + target + " has been successfully unblocked!")
        print(self.blockList)
#Probs wont use these
class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        #implement sending message to friend here
        pass
    



