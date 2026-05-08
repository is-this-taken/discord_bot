from random import choice, randint
import os
import math
from os import startfile
from playsound import playsound
#from youtube import Youtube

#The class per person
class Person:
    def __init__(self,id,mode,count,name,bet,cash,slot1,slot2,slot3,beer,sus,achivements,wordle,bank0,bank1,bank2,bank3,bank4,bank5,bank6,bank7,bank8,bank9,withdraws,VC2,VCAlone,VCGroup,profit):
         self.id = int(id)
         self.mode = int(mode)
         self.count = int(count)
         self.name = str(name)
         self.bet = int(bet)
         self.cash = int(cash)
         self.slot1 = int(slot1)
         self.slot2 = int(slot2)
         self.slot3 = int(slot3)
         self.beer = int(beer)
         self.sus = int(sus)
         self.achivements = str(achivements)
         self.wordle = int(wordle)
         self.bank0 = int(bank0)
         self.bank1 = int(bank1)
         self.bank2 = int(bank2)
         self.bank3 = int(bank3)
         self.bank4 = int(bank4)
         self.bank5 = int(bank5)
         self.bank6 = int(bank6)
         self.bank7 = int(bank7)
         self.bank8 = int(bank8)
         self.bank9 = int(bank9)
         self.withdraws = int(withdraws)
         self.VC2 = int(VC2)
         self.VCAlone = int(VCAlone)
         self.VCGroup = int(VCGroup)
         self.profit = int(profit)
    def tostr (self):
        #only used to write to file
        return f"{self.id},{self.mode},{self.count},{self.name},{self.bet},{self.cash},{self.slot1},{self.slot2},{self.slot3},{self.beer},{self.sus},{self.achivements},{self.wordle},{self.bank0},{self.bank1},{self.bank2},{self.bank3},{self.bank4},{self.bank5},{self.bank6},{self.bank7},{self.bank8},{self.bank9},{self.withdraws},{self.profit},{self.VC2},{self.VCAlone},{self.VCGroup}"
    
#The class per shop item
class Shop:
    def __init__(self,price,item,stock):
        self.price = int(price)
        self.item = item
        self.stock = int(stock)
    def tostr (self):
        return f"{self.price},{self.item},{self.stock}"

"""Show bak money"""
def bank(ID,lowered):

    array = getArray()
    place = getPlace(array)
    #subcommands:
    #List: List all banks  and their ID
    #info X:get info about bank X
    #Deposit/widthdraw X Y: Deposits or widthraws from bank X with amount Y
    #amount: List all your amounts in each bank
    #help: tell user of all commands

    if(lowered.count(" ") == 0):
        return "try [,bank help] for more information"
    command = lowered.split(" ") [1]
    if(command == "help"):
        return "Here are a list of sub-commands"    
    elif(command == "deposit"):
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
    elif(command == "widthdraw"):
        #if(array[place].widthdraws == 0):
        #    return "No Widthdraw tokens avaliable"
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
    elif(command == "amount"):
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
    elif(command == "list"):
        return "Here are the list of banks:\n1. Wordle Bank\n2. Wordle Shitter Bank\n3. Gambling bank\n4. Addict Bank\n5. Safe Bank\n6. Social Bank\n7. Achivement Bnk\n8. Cool Kid Bank\n9. Sleepy Bank\n10. Beef Dip Bank"
    elif(command == "info"):
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
        else:
            #Add Bank info here
            return {}[int(lowered.split(" ")[2])]
    else:
        return "try [,bank help] for more information"
    


    #old bank code
    #array = getArray()
    #place = getPlace(ID,array)
    #return f"You have ${array[place].bank0} in the bank"

def deposit(ID,amount):
    array = getArray()
    place = getPlace(ID,array)
    if(int(amount) < 0):
        return "bitch"
    if(array[place].cash < int(amount)):
        return "Not enough money to deposit"
    array[place].cash -= int(amount)
    array[place].bank0 += int(amount)
    saveArray(array)
    return "deposit sucsessful!"

def withdraw(ID,amount):
    array = getArray()
    place = getPlace(ID,array)
    if(int(amount) < 0):
        return "bitch"
    if(array[place].bank < int(amount)):
        return "Not enough money to withdrawal"
    if(array[place].withdraws == 0):
        return "No withdraws avaliable"
    array[place].cash += int(amount)
    array[place].bank0 -= int(amount)
    array[place].withdraws -= 1
    saveArray(array)
    return "withdrawal sucsessful!"

"""Shows the leaderboard of money"""
def leaderboard_bank():
    array = getArray()
    text = ""
    length = len(array) 
    for i in range(length):
        top = -1
        by = ""
        spot = -1
        for j in range(len(array)):
            if int(array[j].bank0) > top:
                top = int(array[j].bank0)
                by = array[j].name
                spot=j
        text += f"{str(i+1)}. ${str(top)} by {by}\n"
        array.pop(spot)
    return text

"""beer leaderboard"""
def leaderboard_beer():
    array = getArray()
    text = ""
    length = len(array) 
    for i in range(length):
        top = -1
        by = ""
        spot = -1
        for j in range(len(array)):
            if int(array[j].beer) > top:
                top = int(array[j].beer)
                by = array[j].name
                spot=j
        text += f"{str(i+1)}. {str(top)} by {by}\n"
        array.pop(spot)
    return text

"""Slot game"""
def slots(ID):
    array = getArray()
    place = getPlace(ID, array)
    slots = ""

    print(array[place].slot1,array[place].slot2,array[place].slot3)

    if(array[place].slot3 != 0):
        array[place].slot1 = 0
        array[place].slot2 = 0
        array[place].slot3 = 0


    #First slot
    if (array[place].slot1 == 0):
        if(array[place].cash >= 3):
            array[place].cash -= 3
        else:
            return "You don't have the money. $3 please"
        banana = 1
        array[place].slot1 = randint(1,100)
        if(array[place].slot1 >= 91 and array[place].slot1 <= 95):
            slots += "You Got A Beer!\n"
            array[place].beer += 1
    elif (array[place].slot2 == 0):
        banana = 2
        array[place].slot2 = randint(1,100)
        if(array[place].slot2 >= 91 and array[place].slot2 <= 95):
            slots += "You Got A Beer!\n"
            array[place].beer += 1
    elif (array[place].slot3 == 0):
        banana = 3
        array[place].slot3 = randint(1,100)
        if(array[place].slot3 >= 91 and array[place].slot3 <= 95):
            slots += "You Got A Beer!\n"
            array[place].beer += 1


    saveArray(array)

    if(array[place].slot1 <= 30):
        slots += ":banana:"
    elif(array[place].slot1 <= 50):
        slots += ":strawberry:"
    elif(array[place].slot1 <= 70):
        slots += ":pineapple:"
    elif(array[place].slot1 <= 90):
        slots += ":cherries:"
    elif(array[place].slot1 <= 95):
        slots += ":beer:"
    elif(array[place].slot1 <= 99):
        slots += ":question_mark:"
    else:
        slots += ":seven:"    
    if(banana == 1):
        return slots
    
    if(array[place].slot2 <= 30):
        slots += ":banana:"
    elif(array[place].slot2 <= 50):
        slots += ":strawberry:"
    elif(array[place].slot2 <= 70):
        slots += ":pineapple:"
    elif(array[place].slot2 <= 90):
        slots += ":cherries:"
    elif(array[place].slot2 <= 95):
        slots += ":beer:"
    elif(array[place].slot2 <= 99):
        slots += ":question_mark:"
    else:
        slots += ":seven:"    
    if(banana == 2):
        return slots

    if(array[place].slot3 <= 30):
        slots += ":banana:"
    elif(array[place].slot3 <= 50):
        slots += ":strawberry:"
    elif(array[place].slot3 <= 70):
        slots += ":pineapple:"
    elif(array[place].slot3 <= 90):
        slots += ":cherries:"
    elif(array[place].slot3 <= 95):
        slots += ":beer:"
    elif(array[place].slot3 <= 99):
        slots += ":question_mark:"
    else:
        slots += ":seven:"    
    if(banana == 3):
        slots += "\n"
        #Win conditions
        seven = 0
        banna = 0
        straw = 0
        pineapple = 0
        cherry = 0
        beer = 0
        q = 0
        friut = 0


        if (array[place].slot1 <= 30):
            banna += 1
        elif (array[place].slot1 <= 50):
            straw += 1
        elif (array[place].slot1 <=70):
            pineapple += 1
        elif(array[place].slot1 <= 90):
            cherry += 1
        elif(array[place].slot1 <= 95):
            beer += 1
        elif(array[place].slot1 != 100):
            q += 1
        else:
            seven += 1

        if (array[place].slot2 <= 30):
            banna += 1
        elif (array[place].slot2 <= 50):
            straw += 1
        elif (array[place].slot2 <=70):
            pineapple += 1
        elif(array[place].slot2 <= 90):
            cherry += 1
        elif(array[place].slot2 <= 95):
            beer += 1
        elif(array[place].slot2 != 100):
            q += 1
        else:
            seven += 1


        if (array[place].slot3 <= 30):
            banna += 1
        elif (array[place].slot3 <= 50):
            straw += 1
        elif (array[place].slot3 <=70):
            pineapple += 1
        elif(array[place].slot3 <= 90):
            cherry += 1
        elif(array[place].slot3 <= 95):
            beer += 1
        elif(array[place].slot3 != 100):
            q += 1
        else:
            seven += 1

        if(seven != 0):
            seven += q
            q = 0
        elif(beer == 2 and q == 1) or (beer == 1 and q == 2):
            beer = 3
            q = 0
        elif(cherry != 0):
            cherry += q
            q = 0
        elif(pineapple != 0):
            pineapple += q
            q = 0
        elif(straw != 0):
            straw += q
            q = 0
        elif(banna != 0):
            banna += q
            q = 0        

        if(cherry == 1):
            friut += 1
        if(straw == 1):
            friut += 1
        if(banna == 1):
            friut += 1
        if(pineapple == 1):
            friut += 1



        if(banna == 3):
            slots += "bananas! +$50"
            array[place].cash += 50
        elif(straw == 3):
            slots += "Strawberries +$50"
            array[place].cash += 50
        elif(pineapple == 3):
            slots += "Pineapples +$50"
            array[place].cash += 50
        elif(cherry == 3):
            slots += "Cherries +$100"
            array[place].cash += 100
        elif(beer == 3):
            slots += "I got a beer in my beer +$500"
            array[place].cash += 500
        elif(seven == 3):
            slots += "Horse"
            array[place].cash += 777
        elif(q == 3):
            slots += "???"
            array[place].cash += 150

        saveArray(array)
        return slots

"""Enter ID and get their Money and also the $3 hour bonus"""
def getMoney(ID):
    array = getArray()
    place = getPlace(ID, array)
    fin = open("hour.txt","r")
    e = fin.readline().strip()
    fin.close()
    if(e == "0"):
        return f"You have ${array[place].cash}"
    else: 
        fout = open("hour.txt","w")
        fout.write("0")
        fout.close()
        array[place].cash += (int(len(e))+1)
        saveArray(array)
        if(ID == 549031318139174916):
            return f"Here are your ${(int(len(e))+1)} Whoresey."
        elif(ID == 719250188228886620):
            return f"Here is your ${(int(len(e))+1)} of gambling money you slut"
        elif(ID == 552600422016090133):
            return f"Here is your ${(int(len(e))+1)} for Papa K you slave"
        else:
            return f"You got the Bonus ${(int(len(e))+1)} and now have ${array[place].cash}"

"""gets a number, fucks up my pc"""
def fuckComputer(num):
    if num == 1:
        playsound("Z:\Assets\Sounds\\vine-boom.mp3")
        return True
    elif num == 2:
        playsound("Z:\Assets\Voice Lines\\now-its-reyn-time.mp3")
        return True
    elif num == 3:
        playsound("Z:\Assets\Voice Lines\chicken-jockey.mp3")
        return True
    elif num == 6:
        startfile("Z:\Assets\Videos\Saul goodman 3d.mp4")
        return True
    elif num == 7:
        startfile("Z:\Assets\Videos\PARKOUR CIVILIZATION.mp4")
        return True
    elif num == 9:
        playsound("Z:\Assets\Voice Lines\\flint-and-steel.mp3")
        return True
    elif num == 10:
        return True
    elif num == 11:
        return True
    else:
        return False

"""Buys an Item from the shop"""
def buyShit(message, ID):
    array = getArray()
    place = getPlace(ID,array)
    item = int(message.split(" ") [1])
    shop = getShop()

    #check if they have the funds
    if(array[place].cash < shop[item-1].price):
        return "You do not have the funds to buy this"
    #check if it is instock
    if(shop[item-1].stock == 0):
        return "Sorry, this item is out of stock"

    checkOut = fuckComputer(item)

    if(checkOut):
        array[place].cash -= shop[item-1].price
        shop[item-1].stock -= 1
        saveArray(array)
        saveShop(shop)
        return f"You have bought {shop[item-1].item}"
    else:
        return "Something seems to have gone wrong, trolled!"

"""writes the array into a file"""
def saveShop(array):
    fout= open("shop.txt","w")
    for i in range(len(array)):
        fout.write(array[i].tostr()+"\n")
    fout.close()

"""Get's the array from the file"""
def getShop():
    fin = open("shop.txt","r")
    array = []
    count = 0
    #put it all into an array
    while True:
        text = fin.readline().strip()
        if text == "":
            break
        array.append(Shop(text.split(",") [0],text.split(",") [1],text.split(",") [2]))
        count +=1
    fin.close()
    return array

"""Shows the shop and all of their prices"""
def showShop():
    array = getShop()
    string = ""
    for i in range(len(array)):
        string += f"{i}. ${array[i].price}: {array[i].item}\n"
    return string

"""Get a players Place from their name, returns -1 if no ID is found"""
def getPlaceFromName(target):
    array = getArray()
    for i in range(len(array)):
        if (target == array[i].name.lower()):
            return i
    return -1

"""Give money to another player"""
def giveMoney(ID,target,amount):
    array = getArray()
    place = getPlace(ID, array)
    targetPlace = getPlaceFromName(target)

    if(amount <= 0):
        return "Please enter a valid amount"
    if(amount > array[place].cash):
        return f"You only have ${array[place].cash}"
    if (targetPlace == -1):
        return "Not a valid name"
    
    array[place].cash -= amount
    array[targetPlace].cash += amount
    saveArray(array)
    return "Money sent!"

"""Pay another player"""
def pay(ID,target,amount):
    array = getArray()
    place = getPlace(ID, array)
    targetPlace = getPlaceFromName(target)

    if(ID!=475196692807811074):
        return "For the boss to use only"

    if(amount <= 0):
        return "Please enter a valid amount"
    if (targetPlace == -1):
        return "Not a valid name"
    
    array[targetPlace].cash += amount
    saveArray(array)
    return "Payment successful!"

"""Charge another player"""
def charge(ID,target,amount):
    array = getArray()
    place = getPlace(ID, array)
    targetPlace = getPlaceFromName(target)

    if(ID!=475196692807811074):
        return "For the boss to use only"

    if(amount <= 0):
        return "Please enter a valid amount"
    if (targetPlace == -1):
        return "Not a valid name"
    
    array[targetPlace].cash -= amount
    saveArray(array)
    return "Charged successfully!"

"""Takes a bet amount and the players name and flips a coin to try and double it"""
def coinFlip(message, ID):
    array = getArray()
    place = getPlace(ID, array)
    win = randint(0,1)
    #make sure they exist
    if (place == -1):
        return "You are not registered, ask Nugit to register you."

    #make sure that they enter a proper amount
    try:
        bet = int(message.split(" ")[1].strip())
    except (IndexError, ValueError):
        return "Please enter a valid bet amount like \",coinflip 50\"."
    
    rig = False
    fin = open("achivement","r")
    rigg = fin.readline().strip()
    if (rigg.find("1") != -1):
        rig = True

    fout = open ("achivement","w")
    fout.write("0")
    fout.close()

    if (bet < 1):
        return "Nope"
    if (bet > array[place].cash):
        return f"Sorry, your bet is too high, your total amount of money is {array[place].cash}"
    elif(win == 1 and rig==False):
        array[place].cash -= bet
        saveArray(array)
        return f"You lost the coinflip and ${bet}"
    else:
        array[place].cash += bet
        saveArray(array)
        return f"You won the coinflip and ${bet}"

"""Enter an id an anmount and it will add that much money"""
def addMoney(ID, amount):
    array = getArray()
    place = getPlace(ID, array)
    array[place].cash += 1
    saveArray(array)

"""Shows the leaderboard of money"""
def leaderboard_money():
    array = getArray()
    text = ""
    length = len(array) 
    for i in range(length):
        top = -1
        by = ""
        spot = -1
        for j in range(len(array)):
            if int(array[j].cash) > top:
                top = int(array[j].cash)
                by = array[j].name
                spot=j
        text += f"{str(i+1)}. ${str(top)} by {by}\n"
        array.pop(spot)
    return text

"""Enter ones new name to change"""
def changename(ID,message):
    if(message.count(",") != 1):
        return "Bitch"
    else:
        array = getArray()
        place = getPlace(ID, array)
        array[place].name = message.split(" ") [1]
        saveArray(array)
        return "Name change succsessful"

"""Turns someone ,quote points into cash and then returns the amount gained"""
def cashIn(ID):
    array = getArray()
    place = getPlace(ID,array)
    points = float(array[place].count)
    money = 0
    while points > 1.5:
        points /= 1.5
        money += 1
    array[place].count = 0
    array[place].cash += money
    saveArray(array)
    return money

"""Pulls a quote and sets up the quotegame"""
def quoteGame(ID, message):
    array = getArray()
    place = getPlace(ID,array)

    #make sure that they entered everything correctly
    if place == -1:
        return "You do not seem to be in our system, please ask Nugit to fix this"
    if(message.count(" ") != 1):
        return "Invalid format, please use this format\n,quote <wager amount>"
    if(message.split(" ")[1].strip() == "all"):
        bet = int(array[place].count)
    else:
        bet = int(message.split(" ")[1].strip())
    if int(str(bet)) < 0:
        return "Bro ..."
    if(int(str(bet)) > int(str(array[place].count))):
        return "You're bet is too high, your current maximum is "+str(array[place].count)+"\nYou can increase this by doing ,count"
    array[place].bet = str(bet)

    
    #pull the quote
    array[place].mode = str(randint(1,5))
    if array[place].mode == "1":
        fin = open("alex.txt","r")
    elif array[place].mode == "2":
        fin = open("kaelan.txt","r")
    elif array[place].mode == "3":
        fin = open("javan.txt","r")
    elif array[place].mode == "4":
        fin = open("josh.txt","r")
    elif array[place].mode == "5":
        fin = open("ivan.txt","r")

    #get text and send
    list = fin.read().splitlines()
    num = len(list) -1
    text = "your quote is: " + list [randint(0,num)]
    fin.close()
    saveArray(array)
    return text

"""Checks to see if they guessed the right person for the quote"""
def checkQuote(message,ID):
    array = getArray()
    place = getPlace(ID,array)
    names = ["Alex","Kaelan","Javan","Josh","Ivan"]

    #all winners
    if int(array[place].mode) == 1 and message == "alex":
        array[place].count += array[place].bet
        text = "Correct! it was Alex and you win "+str(array[place].bet)
    elif int(array[place].mode) == 2 and message == "kaelan":
        array[place].count += array[place].bet
        text = "Correct! it was Kaelan and you win "+str(array[place].bet)
    elif int(array[place].mode) == 3 and message == "javan":
        array[place].count += array[place].bet
        text = "Correct! it was Javan and you win "+str(array[place].bet)
    elif int(array[place].mode) == 4 and message == "josh":
        array[place].count += array[place].bet
        text = "Correct! it was Josh and you win "+str(array[place].bet)
    elif int(array[place].mode) == 5 and message == "ivan":
        array[place].count += array[place].bet
        text = "Correct! it was Ivan and you win "+str(array[place].bet)
    elif int(array[place].mode) == 6 and message == "philip":
        array[place].count += array[place].bet
        text = "Correct! it was Philip and you win "+str(array[place].bet)
    
    #getting it wrong
    elif (message == "alex" or message == "kaelan" or message == "javan" or message == "josh" or message == "ivan" or message == "philip"):
        text = f"Incorrect. It was actually {names [array[place].mode -1]} who said it, you lost {array[place].bet}"
        array[place].count -= array[place].bet

    #not valid
    else:
        return "Sorry, that is not a valid name. Valid names are: Alex, Kaelan, Javan, Josh, Ivan, and Philip"

    array[place].bet = 0
    array[place].mode = 0
    saveArray(array)
    return text

"""Give ID and array, will return where the ID is in it or a -1 if it is not found"""
def getPlace (ID,array):
    find =-1
    for i in range(len(array)):
        x = array [i]
        if(x.id == ID):
            find = i
            break
    return find

"""Shows the leaderboard of the hit ,count"""
def leaderboards():
    array = getArray()
    text = ""
    length = len(array) 
    for i in range(length):
        top = -1
        by = ""
        spot = -1
        for j in range(len(array)):
            if int(array[j].count) > top:
                top = int(array[j].count)
                by = array[j].name
                spot=j
        text += f"{str(i+1)}. {str(top)} by {by}\n"
        array.pop(spot)
    return text

"""Adds a quote to the rspectives persons quotebook"""
def addQuote(quote):
    fout = open(quote[1]+".txt","a")
    fout.write(quote[0]+"\n")
    fout.close()

"""Get's the array from the file"""
def getArray():
    fin = open("count.txt","r")
    array = []
    count = 0
    #put it all into an array
    while True:
        text = fin.readline().strip()
        if text == "":
            break
        array.append(Person(text.split(",") [0],text.split(",") [1],text.split(",") [2],text.split(",") [3],text.split(",") [4],text.split(",") [5],text.split(",") [6],text.split(",") [7],text.split(",") [8],text.split(",") [9],text.split(",") [10],text.split(",") [11],text.split(",") [12],text.split(",") [13],text.split(",") [14],text.split(",") [15],text.split(",") [16],text.split(",") [17],text.split(",") [18],text.split(",") [19],text.split(",") [20],text.split(",") [21],text.split(",") [22],text.split(",") [23],text.split(",") [24],text.split(",") [25],text.split(",") [26],text.split(",") [27]))
        count +=1
    fin.close()
    return array

"""writes the array into a file"""
def saveArray(array):
    fout= open("count.txt","w")
    for i in range(len(array)):
        fout.write(array[i].tostr()+"\n")
    fout.close()

"""add's one to the players counter and returns just the number, or -1 if they are not there"""
def count (ID):
    array = getArray()
    
    #check if it is here
    found = getPlace(ID, array)
    if(found == -1):
        return -1

    array[found].count += 1

    #put the crap back into the file
    saveArray(array)

    return array[found].count

def musicAdd(Link):
    return "e"

"""Registers the user into the bot system"""
def register(message,ID):
    array = getArray()
    place = getPlace(ID,array)
    if(place!=-1):
        return "you are already registered nerd"
    array.append(Person(str(ID),"0","0",message.split(" ") [1],"0","0","0","0","0","0","0","","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"))
    saveArray(array)
    return "Resitered Sucsessfully"

def wordle(message):
    array = getArray()
    lines = message.split("\n")
    for i in range(len(lines)-1):
        if(lines[i+1] [0]== "👑" or lines[i+1].startswith(":crown:")):
            moneyGain = 2.5
            susadd = 5
        if(lines[i+1] [0]== "2"):
            moneyGain = 2.0
            susadd = 2
        if(lines[i+1] [0]== "3"):
            moneyGain = 1.0
            susadd = 0
        if(lines[i+1] [0]== "4"):
            moneyGain = .5
            susadd = -1
        if(lines[i+1] [0]== "5"):
            moneyGain = .25
            susadd = -3 
        if(lines[i+1] [0]== "6"):
            moneyGain = 0
            susadd = -5
        if(lines[i+1] [0]== "X"):
            moneyGain = -5.0
            susadd = -10

        for j in range(lines[i+1].count("@")):
            if(lines[i+1].split("@")[j+1].count(">") == 1):
                ID = int(lines[i+1].split("@")[j+1].split(">")[0])
                place = getPlace(ID, array)
                if(place != -1):
                    array[place].cash += int(moneyGain*float(array[place].bank0))
                    array[place].sus += susadd
                    array[place].wordle += 1
                    if(moneyGain == 2.5):
                        array[place].withdraws += 1


    saveArray(array)
    return "Money Gained!!"

def list_achivements():
    message = "Current achivements:\n"
    fin = open("achivements.txt","r")
    while True:
        text = fin.readline()
        if(text == ""): break
        message += (text.split(",")[0]+" - "+text.split(",")[1]+"\n")
    return message

def achivements(message,ID):
    if(message==",achievements list" or message==",achievement list" ):
        return list_achivements()
    if(message.startswith(",achievements <@") or message.startswith(",achievement <@")):
        return achivements(message.split(" ")[0],int(message.split("@")[1].split(">")[0]))

    array = getArray()
    place = getPlace(ID,array)
    if (place == -1):
        return "not registared"

    #Check for no achievements
    if(array[place].achivements.count("-") == 0):
        return "you have no achivements"
    else:
        string = "You have "+str({array[place].achivements.count("-")})+" achivements, they are:\n"
        for i in range(array[place].achivements.count("-")):
            string += array[place].achivements.split("-")[i]
            string += "\n"

        return string

#Response based on message sent
def get_response(user_input: str,username, nameID, channel) -> str:
    print(user_input,username,nameID,channel)
    text = ""
    bot_list = ["john-bot","bot-commands","bot-commands-2"]
    lowered: str = user_input.lower()
    
    x = randint(1,100)
    print(x)
    #nameID == 1211781489931452447 and 
    if(lowered.startswith("**your group is on a ") and (nameID==475196692807811074 or nameID==1211781489931452447)):
        if(channel == 475196692807811074):
            return wordle(user_input)
        else:
            return "Fuck you Horsey"
    #For mode checker
    array = getArray()
    place = getPlace(nameID,array)
    if(place != -1):

        #quote game
        if(array[place].mode >= 1 and array[place].mode <= 5):
            return checkQuote(lowered,nameID)
        

    if lowered == '':
        text = "well, you're awfully silent..."
    elif 'hello' in lowered:
        text = 'Hi there!'
    
    #whole quotation system
    elif (str(channel) == "quotes"):
        if (lowered.count("-")) == 1 and ((lowered.count('"') == 2 or (lowered.count("”") == 1 and lowered.count("“") == 1))):
            quote = lowered.split("-")
            quote[0] = quote[0].strip()
            quote[1] = quote[1].strip()
            if (quote[1] == "alex" or quote[1] == "josh" or quote[1] == "javan" or quote[1] == "kaelan" or quote[1] == "ivan"):
                addQuote(quote)
                return "Quote added seccessfully"
            else:
                return "That name is not valid, current valid names are: Alex, Josh, Javan, and Kaelan"
        else:
            return "Invalid Quote format, please use this format:\n\"Quote text here\" - author"
        
    #bunch of random crap    
    elif lowered.find("help") != -1:
        num = lowered.count("serious")
        if(num==0):
            text = "In a bit"
        else:
            text = "give me "+str(5*num)+" minutes"

    #dice
    elif ',roll' == lowered [0:5]:
        dice = lowered [6:]
        total = 0
        if(dice.find("d") != -1):
            if(int(dice.split("d") [0]) >1000 or int(dice.split("d") [1] )> 1000):
                return "Money deleted"
            for i in range(int(dice.split("d") [0])):
                total += randint(1,int(dice.split("d") [1]))
            text = "You rolled a "+str(total)
        else:
            text = "that is not a valid dice roll"
    elif lowered == "ping":
        text = "<@"+str(nameID)+">"
    
    #commands
    elif lowered.startswith(",withdraw"):
        text = withdraw(nameID,lowered.split(" ") [1])
    elif lowered.startswith(",deposit"):
        text = deposit(nameID,lowered.split(" ") [1])
    elif lowered == ",bank":
        text = bank(nameID,lowered)
    elif lowered == ",rig":
        text = "coinflip rigged"
    elif lowered.startswith(",givemoney") and channel in bot_list:
        text = giveMoney(nameID,lowered.split(" ") [1],int(lowered.split(" ") [2]))
    elif lowered.startswith(",pay") and channel in bot_list:
        text = pay(nameID,lowered.split(" ") [1],int(lowered.split(" ") [2]))
    elif lowered.startswith(",charge") and channel in bot_list:
        text = charge(nameID,lowered.split(" ") [1],int(lowered.split(" ") [2]))
    elif lowered.startswith(",coinflip ") and channel in bot_list:
        text = coinFlip(lowered,nameID)
    elif lowered.startswith(",quote") and channel in bot_list:
        text = quoteGame(nameID,lowered)
    elif lowered == ",count":
        text = "Your counter is now at "+str(count(nameID))
    elif lowered.startswith(",leaderboard"):
        if lowered == ",leaderboard count":
            text = leaderboards()
        elif lowered == ",leaderboard money":
            text = leaderboard_money()
        elif lowered == ",leaderboard beer":
            text = leaderboard_beer()
        elif lowered == ",leaderboard bank":
            text = leaderboard_bank()
        else:
            text = "leaderboards: count, money, beer, bank"
    elif ((lowered.find("what") != -1) & (len(lowered)>10) & (lowered.count(" ") > 4)) or(randint(1,1000) == 120):
        text = choice(["Ah shit, here we go again ...",
                      "Let's go, open up, it's time for parkore",
                      "What will the next act entail?",
                      "It's becuase this amuses me",
                      "How many times has it been now...",
                      "Now then, play it out for me",
                      "I am afraid I cannot allow you to proceed",
                      "And that's the real battle here",
                      "You shall face dispair",
                      "Let's just hear him out",
                      "You must yeild",
                      "That's what it's all about",
                      "Must this go on?",
                      "Sometimes, it is better to simply not",
                      "Once more",
                      "Keep it Comming",
                      "What statistical value does this have",
                      "Why must things have to go this way?",
                      "Wow that was really cool :thumbs_up:",
                      "I am not crazy!",
                      "I know he swapped those numbers!",
                      "And there's nothing more American than shooting a man in this Walmart of a world",
                      "Check the internet lately?",
                      "You're not cringe. You're just fucking racist",
                      "The value of a human life is negative",
                      "Your IQ is the room tempature of Alaska",
                      "I am Papa's special fucking boy!",
                      "I can see sounds",
                      "I can hear colours",
                      "I forgot how to shit",
                      "Oh Stewie, I'm so full off poo",
                      "GORP!",
                      "Fish",
                      "gay",
                      "Error 420: KYS",
                      "This is why we can't have nice things",
                      "Why must you be like this?",
                      "Why can't you just be normal?",
                      "Someone grab the popcorn",
                      "Everybody do the flop",
                      "Cookie's are pretty tasty",
                      "0.25 A presses",
                      'Well TJ """"""""""Henry"""""""""" Yoshi',
                      "You need to update your home to the death barrier",
                      "Is that a mother fucking mistake edition reference?",
                      "Is that a Jojo's refernce",
                      "Where it all began...",
                      "Let's go back to 1-1",
                      "Preheat the oven to 350",
                      "I'm hot stuff",
                      "May be slow, no need to rush you",
                      "This is the end of it all as we know it",
                      "Just Lean",
                      "How can this be?",
                      "What is truely your plan here?",
                      "I am Retep",
                      "I am evil Peter",
                      "merry christmas",
                      "||Haste||",
                      "When Village Done?",
                      "No changes were made"
                      ])
    elif lowered == ",cash in":
        if(array[place].count >= 1000):
            text = f"You have cashed in and gained ${cashIn(nameID)}"
        else: text = "Sorry buddy, but you need at least 1000 points to cash in. Bulk only"
    elif lowered.startswith(",changename") and channel in bot_list:
        if(lowered.find(",") > 1):
            text = "Invalid name, no commas allowed"
        else:
            text = changename(nameID,user_input)
    elif lowered.startswith(",shop") and channel in bot_list:
        text = showShop()
    elif lowered.startswith(",buy") and channel in bot_list:
        text = buyShit(lowered,nameID)
    elif lowered == ",money" and channel in bot_list:
        text = getMoney(nameID)
    elif lowered == ",slots" and channel in bot_list:
        text = slots(nameID)
    elif lowered.startswith(",music add "):
        text = musicAdd(user_input)
    elif lowered.startswith(",register "):
        text = register(user_input,nameID)
    elif lowered.startswith(",achievements") or lowered.startswith(",achievement") or lowered=="sigma tokens for the coolest of people":
        text = achivements(lowered,nameID)
    #give them random money for chatting trol
    elif x == 1:
        addMoney(nameID,1)
        text = "You found a dollar on the ground!"
    


    #Invalid ccommand
    elif lowered.startswith(","):
        text = choice([
            "not valid",
            "Trolled Idiot",
            "gay",
            ":banana:"
        ])
    array = getArray()
    #Give achievements
    if(array[place].achivements.find("Ultra Lucky Man") == -1 and randint(1,1000000) == 550):
        array[place].achivements += "Ultra Lucky Man-"
        text += "\n\nAchivement Get: Ultra Lucky Man"
    if(array[place].achivements.find("Rich 1") == -1 and array[place].cash >=1000):
        array[place].achivements += "Rich 1-"
        text += "\n\nAchivement Get: Rich 1"
    if(array[place].achivements.find("Rich 2") == -1 and array[place].cash >=10000):
        array[place].achivements += "Rich 2-"
        text += "\n\nAchivement Get: Rich 2"
    if(array[place].achivements.find("Rich 3") == -1 and array[place].cash >=100000):
        array[place].achivements += "Rich 3-"
        text += "\n\nAchivement Get: Rich 3"
    if(array[place].achivements.find("Drunk") == -1 and array[place].beer >=100):
        array[place].achivements += "Drunk-"
        text += "\n\nAchivement Get: Drunk"
    saveArray(array)
    return text