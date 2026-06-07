from random import choice, randint
import os
import math
from os import startfile
#from playsound import playsound
#from youtube import Youtube

#The class per person
class Person:
    def __init__(self,id,mode,count,name,bet,cash,slot1,slot2,slot3,beer,sus,achivements,wordle,bank0,bank1,bank2,bank3,bank4,bank5,bank6,bank7,bank8,bank9,bank10,beefdip,VC2,VCAlone,VCGroup,profit,daysnogamble,withdrawTokens,caseCount,caseBuyCredits,caseItems,badges,marketPosted):
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
         self.bank10 = int(bank10)
         self.beefdip = str(beefdip)
         self.VC2 = int(VC2)
         self.VCAlone = int(VCAlone)
         self.VCGroup = int(VCGroup)
         self.profit = int(profit)
         self.daysnogamble = int(daysnogamble)

         #case variables - Javan
         self.withdrawTokens = int(withdrawTokens)
         self.caseCount = int(caseCount)
         self.caseBuyCredits = int(caseBuyCredits)
         self.caseItems = str(caseItems)
         self.badges = str(badges)
         self.marketPosted = str(marketPosted)
    def tostr (self):
        #only used to write to file
        return f"{self.id},{self.mode},{self.count},{self.name},{self.bet},{self.cash},{self.slot1},{self.slot2},{self.slot3},{self.beer},{self.sus},{self.achivements},{self.wordle},{self.bank0},{self.bank1},{self.bank2},{self.bank3},{self.bank4},{self.bank5},{self.bank6},{self.bank7},{self.bank8},{self.bank9},{self.bank10},{self.beefdip},{self.profit},{self.VC2},{self.VCAlone},{self.VCGroup},{self.daysnogamble},{self.withdrawTokens},{self.caseCount},{self.caseBuyCredits},{self.caseItems},{self.badges},{self.marketPosted}"
    
#The class per shop item
class Shop:
    def __init__(self,price,item,stock):
        self.price = int(price)
        self.item = item
        self.stock = int(stock)
    def tostr (self):
        return f"{self.price},{self.item},{self.stock}"


"""
    Market code
    Author: Javan
"""
def market(ID,lowered):
    array = getArray()
    place = getPlace(ID,array)
    #subcommands:
    #help: tell user of all commands
    #view: see whats on the market
    #post: add a listing to the market
    #buy: purchace item off the market
    #info: how the market works

    if(lowered.count(" ") == 0):
        return "try [,market help] for more information"
    command = lowered.split(" ") [1]
    if(command == "help"):
        return "Here are a list of sub-commands\nHelp: Show this\nView: See what's on the market\nPost [Item] [Quantity] [Price]: Add a listing to the market\nBuy [ItemID] [Price]: Purchace item from the market\nInfo: How the market works"  
    elif(command == "view"):
        return market_view(array)
    elif(command == "post"):
        return market_post(array,place,lowered)
    elif(command == "buy"):
        return market_buy(array,place, lowered)
    elif(command == "info"):
        return "Any user can place a item on the market for a price and any user can buy this item for the price listed.\nIf you have posted a listing on accident or would like to remove a listing, just use [,market buy] to buy the item from yourself."
    else:
        return "try [,market help] for more information"

def market_view(array):
    message = "[ID] [Price] for [Quantity] [Item Name]\n"
    marketList = []

    marketID = 0
    for i in range(len(array)):
        for j in range(len(array[i].marketPosted.split("|"))):
            marketList.append(array[i].marketPosted.split("|") [j])
        
        if array[i].marketPosted != "":
            #make message
            message += f"{array[i].name}'s listings are\n"
            for j in range(len(array[i].marketPosted.split("|"))):
                #item Name
                itemName = ""
                fin = open("caseContents.txt","r")
                linesRead = -1
                while True:
                    text = fin.readline().strip()
                    if text == "":
                        break
                    if int(marketList[marketID].split("-") [1]) == linesRead:
                        itemName = text
                    linesRead += 1
                fin.close()

                message += f"{marketID+1}. k${marketList[marketID].split("-") [2]} for {marketList[marketID].split("-") [0]} {itemName}\n"
                marketID += 1
    return message

def market_post(array,place,lowered):
    message = "Sorry, something went wrong"

    #check for items
    if array[place].caseItems == "":
        return "You have no items, open some cases or buy items from the market!"

    #check for item index
    if (lowered.count(" ") == 1):
        return "Please add an item number to post"
    
    if (lowered.count(" ") == 2):
        return "Please add an amount of this item to post"
    
    if (lowered.count(" ") == 3):
        return "Please add a price to sell for"

    #partition message into vars
    itemIndex = int(lowered.split(" ") [2]) - 1
    itemUseAmount = int(lowered.split(" ") [3])
    itemPrice = int(lowered.split(" ") [4])
    itemsList = array[place].caseItems.split("|")
    if itemIndex < 0 or itemIndex >= len(itemsList):
        return "Sorry, you don't have an item for that item number"


    #get item ID and count
    itemCount = []
    itemID = []
    for i in range(len(itemsList)):
        itemCount.append(itemsList[i].split("-") [0])
        itemID.append(itemsList[i].split("-") [1])

    if int(itemCount[itemIndex]) < itemUseAmount:
        return "Sorry, you don't have enough of these items"

    #adds item to market
    marketCode = f"{itemUseAmount}-{itemID[itemIndex]}-{itemPrice}"
    if array[place].marketPosted == "":
        array[place].marketPosted = marketCode
    else:
        array[place].marketPosted += f"|{marketCode}"
    saveArray(array)

    #remove item from your inventory
    array[place].caseItems = ""
    for i in range(len(itemsList)):
        if int(itemID[i]) == int(itemID[itemIndex]):
            if int(itemCount[i]) - itemUseAmount > 0:
                itemNew = f"{int(itemCount[i]) - itemUseAmount}-{itemID[i]}"
                if array[place].caseItems == "":
                    array[place].caseItems += itemNew
                else:
                    array[place].caseItems += f"|{itemNew}"
        else:
            if array[place].caseItems == "":
                array[place].caseItems += itemsList[i]
            else:
                array[place].caseItems += f"|{itemsList[i]}"
    saveArray(array)

    #get item name
    itemName = ""
    fin = open("caseContents.txt","r")
    linesRead = 0
    while True:
        text = fin.readline().strip()
        if text == "":
            break
        if itemID[itemIndex] == linesRead:
            itemName = text
        linesRead += 1
    fin.close()

    if itemUseAmount == 1:
        return f"You have posted {itemUseAmount} {itemName} for k${itemPrice}"
    return f"You have posted {itemUseAmount} {itemName}s for k${itemPrice}"

def market_buy(array,place,lowered):
    message = "Sorry, something went wrong"

    #check for item index
    if (lowered.count(" ") == 1):
        return "Please add an item ID. This is the first number when you use [],market view]"
    
    if (lowered.count(" ") == 2):
        return "Please add the cost of the item"
    
    marketIndex = int(lowered.split(" ") [2]) - 1
    marketPrice = int(lowered.split(" ") [3])
    
    #check if you have enough
    if marketPrice > array[place].cash and array[place] != array[int(marketBuyList[marketIndex].split("-")[3])]:
        return  "Sorry, you don't have enough money to buy this item."

    #marketBuyList ID is formated Amount-ID-Price-CountToUser
    marketBuyList = []
    for i in range(len(array)):
        for j in range(len(array[i].marketPosted.split("|"))):
            if len(f"{array[i].marketPosted.split("|") [j]}-{i}") >= 6:
                marketBuyList.append(f"{array[i].marketPosted.split("|") [j]}-{i}")
    
    #check for items
    if marketBuyList == "":
        return "Sorry, there are no items on the market. Please come back later!"
    
    #check if itemID exists
    if marketIndex > len(marketBuyList):
        return "Sorry, there is not that many items in the market"
    
    if int(marketBuyList[marketIndex].split("-")[2]) == marketPrice:
        itemCode = f"{marketBuyList[marketIndex].split("-")[0]}-{marketBuyList[marketIndex].split("-")[1]}"
        #add item to inventory
        if array[place].caseItems == "":
            array[place].caseItems = itemCode
        else:
            array[place].caseItems += f"|{itemCode}"

        #remove price from buyers money
        array[place].cash -= marketPrice
        saveArray(array)
        orderItems(array,place)

        #give money to owner
        array[int(marketBuyList[marketIndex].split("-")[3])].cash += marketPrice

        checkForThis = array[int(marketBuyList[marketIndex].split("-")[3])].marketPosted.split("|") [marketIndex]
        #remove from market
        for i in range(len(array)):
            newMarket = ""
            for j in range(len(array[i].marketPosted.split("|"))):
                if array[i].marketPosted.split("|") [j] != checkForThis:
                    if newMarket == "":
                        newMarket = array[i].marketPosted.split("|") [j]
                    else:
                        newMarket += f"|{array[i].marketPosted.split("|") [j]}"

            array[i].marketPosted = newMarket
            saveArray(array)

        #get item name
        itemName = ""
        fin = open("caseContents.txt","r")
        linesRead = 0
        while True:
            text = fin.readline().strip()
            if text == "":
                break
            if int(marketBuyList[marketIndex].split("-")[1]) == linesRead:
                itemName = text
            linesRead += 1
        fin.close()

        if int(marketBuyList[marketIndex].split("-")[0]) != 1:
            itemName += "s"
        return f"You have bought {int(marketBuyList[marketIndex].split("-")[0])} {itemName} from {array[int(marketBuyList[marketIndex].split("-")[3])].name} for {marketPrice}"
    else:
        return "Sorry, your Purchace order has been cancelled as you did not enter the correct price. Please try again with the correct price."

"""
    Badges code
    Author: Javan
"""
""""Updates and organises all badges"""
def updateBadges(array):
    ID = 0
    for i in range(len(array)):
        place = getPlace(ID,array)
        #splits badge string into array of count-ID
        badgesID = array[place].badges.split("|")
        newBadgesID = []
        fileLen = 0

        #remove and badges that don't exist
        count = 0
        iBadges = 0
        fin = open("badgeList.txt","r")
        while True:
            line = fin.readline().strip()
            if line == "":
                break
            fileLen += 1
            
            if str(count) in badgesID:
                if line[0] == '0':
                    newBadgesID.append(badgesID[iBadges])
                iBadges += 1
            count += 1
        fin.close()

        #order badges
        badgesID = newBadgesID
        newBadgesID = []
        for i in range(fileLen):
            if str(i) in badgesID:
                newBadgesID.append(i)

        badgesID = newBadgesID
        array[place].badges = ""
        saveArray(array)
        for i in range(len(badgesID)):
            if array[place].badges == "":
                array[place].badges = str(badgesID[i])
            else:
                array[place].badges += f"|{badgesID[i]}"
        saveArray(array)
        ID += 1

""""Show off your badges"""
def badges(ID):
    array = getArray()
    place = getPlace(ID,array)
    #splits badge string into array of count-ID
    badgesID = array[place].badges.split("|")
    newBadgesID = []

    #remove and badges that don't exist
    count = 0
    iBadges = 0
    fin = open("badgeList.txt","r")
    while True:
        line = fin.readline().strip()
        if line == "":
            break
        
        if str(count) in badgesID:
            if line[0] == '0':
                newBadgesID.append(badgesID[iBadges])
            iBadges += 1
        count += 1
    fin.close()

    badgesID = newBadgesID
    array[place].badges = ""
    saveArray(array)
    for i in range(len(badgesID)):
        if array[place].badges == "":
            array[place].badges = str(badgesID[i])
        else:
            array[place].badges += f"|{badgesID[i]}"
    saveArray(array)

    if array[place].badges == "":
        return "This idiot has no badges!"
    
    count = 0
    message = "Your badges are:\n"
    fin = open("badgeList.txt","r")
    while True:
        line = fin.readline().strip()
        if line == "":
            break
        if str(count) in badgesID:
            message += f"{line[5:]}\n"
        count += 1
    fin.close()
    
    return message

"""
    KFrat case code
    Author: Javan
"""
"""Defult case message"""
def case(ID,lowered):

    array = getArray()
    place = getPlace(ID,array)
    #subcommands:
    #help: tell user of all commands
    #amount: List amount of cases owned
    #open: Open a case
    #items: List all items owned
    #use [item]: Use an item
    #info: List all case drops and their chances

    if(lowered.count(" ") == 0):
        return "try [,case help] for more information"
    command = lowered.split(" ") [1]
    if(command == "help"):
        return "Here are a list of sub-commands\nHelp: Show this\nAmount: List amount of cases owned\nOpen: Open a case\nBuyCredits: See how many cases you can buy\nItems: List all items owned\nUse [itemNumber] [Optional - add amount to use]: Use an item\nInfo: List all case drops and their chances"  
    elif(command == "amount"):
        if (array[place].caseCount == 1):
            return f"You have {array[place].caseCount} case."
        return f"You have {array[place].caseCount} cases."
    elif(command == "open"):
        return case_open(ID,array,place)
    elif(command == "buycredits"):
        if (array[place].caseBuyCredits == 0):
            return f"You are unable to buy any cases right now.\nYou can try to buy a case credit from the market or wait until tomorrow."
        if (array[place].caseBuyCredits == 1):
            return f"You can buy {array[place].caseBuyCredits} case today."
        return f"You can buy {array[place].caseBuyCredits} cases today."
    elif(command == "items"):
        return case_items(ID,array,place)
    elif(command == "use"):
        return case_use(ID,array,place,lowered)
    elif(command == "info"):
        return "KFrat case drops:\n22% - 1 Common Badge Token\n 6% - 1 Epic Badge Token\n 2% - 1 Legendary Badge Token\n 6% - 1 Common Badge Breaker Token (destroy a random persons common badge)\n 4% - 1 Epic Badge Breaker Token (destroy a random persons epic badge)\n 2% - 1 Legendary Badge Breaker Token (destroy a random persons Legendary badge)\n 2% - 1 Special Badge Breaker Token (destroy a random persons Special badge)\n10% - 1 Withdraw Token\n 6% - 3 Withdraw Tokens\n 2% - 9 Withdraw Tokens\n10% - 1 0.1% Interest Token (gives 0.1% interest of your case bank balance)\n 6% - 1 0.5% Interest Token (gives 0.5% interest of your case bank balance)\n 2% - 1 1.0% Interest Token (gives 1.0% interest of your case bank balance)\n 6% - 3 Case Purchace Credits\n 2% - Robery Token (Steal 2% from all case banks)\n 6% - 1 CS2 Case\n 2% - 3 CS2 Case\n 2% - 1 KFrat Response Token (lets you add a response to KFrat)\n 2% - 1 KFrat DM Token (lets you DM someone though KFrat))"
    else:
        return "try [,case help] for more information"

"""Open a case and give the user a random item, also decrease case count by 1"""
def case_open(ID,array,place):
    #check for cases
    if (array[place].caseCount <= 0):
        return "You are out of cases, get more from the shop or the market!"
    #decrease case count
    array[place].caseCount -= 1
    saveArray(array)

    #randomly give item
    itemID = randint(1,50)
    fin = open("caseRolls.txt","r")
    for i in range(itemID):
        itemLine = fin.readline().strip()
    fin.close()

    #partition item
    itemID = itemLine[0]+itemLine[1]
    itemCount = itemLine[3]
    itemName = itemLine[5:]

    itemCode = itemCount + "-" + itemID

    #add item to inventory
    if array[place].caseItems == "":
        array[place].caseItems = itemCode
    else:
        array[place].caseItems += f"|{itemCode}"
    saveArray(array)

    orderItems(array,place)

    return f"Opening Case...\nNEW ITEM!: {itemCount} {itemName}"

"""
Orders Items in inventory when called
THERE MUST BE 1 ITEM IN array[place].caseItems
"""
def orderItems(array,place):
    itemsList = array[place].caseItems.split("|")
    itemCount = []
    itemID = []
    for i in range(len(itemsList)):
        itemCount.append(itemsList[i].split("-") [0])
        itemID.append(itemsList[i].split("-") [1])

    #get max ID value
    max = 0
    for i in range(len(itemID)):
        if int(itemID[i]) > max:
            max = int(itemID[i])
    
    sortedItemID = []
    sortedItemID = sorted(itemID)
    IDcount = 0
    array[place].caseItems = ""
    #search thought all item, adds counts of the same item ID
    for i in range(1,max+1):
        countInThisID = 0
        checkForThis = ""
        if i < 10:
            checkForThis += "0"
        checkForThis += str(i)
        if checkForThis in itemID:
            for j in range(len(itemsList)):
                if i == int(itemID[j]):
                    countInThisID += int(itemCount[j])
            
            itemCode = str(countInThisID) + "-" + checkForThis
            if array[place].caseItems == "":
                array[place].caseItems = itemCode
            else:
                array[place].caseItems += f"|{itemCode}"
            IDcount += 1
    saveArray(array)

"""Display all items owned by the user"""
def case_items(ID,array,place):
    #check for items
    if array[place].caseItems == "":
        return "You have no items, open some cases to get items!"
    
    #splits item string into array of count-ID
    itemsList = array[place].caseItems.split("|")
    itemString = "Your inventory is:\n"

    for i in range(len(itemsList)):
        itemCount = itemsList[i].split("-") [0]
        itemID = itemsList[i].split("-") [1]

        #open conetents names
        fin = open("caseContents.txt","r")
        for j in range(int(itemID)):
            itemName = fin.readline().strip()
        fin.close()

        #addes item index
        itemString += f"{i+1}. "

        #adds plural
        if itemCount == "1":
            itemString += f"{itemCount} {itemName}\n"
        else:
            itemString += f"{itemCount} {itemName}s\n"
        
    return itemString

"""All items in cases are opened here, Badge count must be updated manually"""
def case_use(ID,array,place,lowered):
    message = "Sorry, something went wrong"

    #check for items
    if array[place].caseItems == "":
        return "You have no items, open some cases or buy items from the market!"

    #check for item index
    if (lowered.count(" ") == 1):
        return "Please add an item number to use"
    itemIndex = int(lowered.split(" ") [2]) - 1
    itemsList = array[place].caseItems.split("|")
    if itemIndex < 0 or itemIndex >= len(itemsList):
        return "Sorry, you dont have an item for that item number"

    #check for item amount
    if (lowered.count(" ") == 3):
        itemUseAmount = int(lowered.split(" ") [3])
    else:
        itemUseAmount = 1

    #get item ID and count
    itemCount = itemsList[itemIndex].split("-") [0]
    itemID = itemsList[itemIndex].split("-") [1]

    if itemUseAmount > int(itemCount):
        return f"You don't have enought of those, you only have {itemCount} of that item"

    if itemID == "01":
        array[place].withdrawTokens += itemUseAmount
        saveArray(array)
        message = f"You have applied {itemUseAmount} Withdraw Token(s) to your account"

    elif itemID == "02":
        array[place].cash += int(0.1*array[place].bank10*itemUseAmount)
        saveArray(array)
        message = f"You have applied {itemUseAmount} 0.1% Intrest Token(s) to your account\nYou have gained ${int(0.1*array[place].bank10*itemUseAmount)}"

    elif itemID == "03":
        array[place].cash += int(0.5*array[place].bank10*itemUseAmount)
        saveArray(array)
        message = f"You have applied {itemUseAmount} 0.5% Intrest Token(s) to your account\nYou have gained ${int(0.1*array[place].bank10*itemUseAmount)}"

    elif itemID == "04":
        array[place].cash += int(array[place].bank10*itemUseAmount)
        saveArray(array)
        message = f"You have applied {itemUseAmount} 1.0% Intrest Token(s) to your account\nYou have gained ${int(0.1*array[place].bank10*itemUseAmount)}"

    elif itemID == "05":
        totalStolen = 0
        for i in range(len(array)):
            if i != place:
                array[place].cash += array[i].bank10*0.02*itemUseAmount
                totalStolen += array[i].bank10*0.02*itemUseAmount
                array[i].bank10 -= array[i].bank10*0.02*itemUseAmount
        saveArray(array)
        message = f"You have used {itemUseAmount} Robery Token(s)\nYou have stolen ${totalStolen} from other users case banks"

    elif itemID == "06":
        #array[place].cases += itemUseAmount
        #saveArray(array)
        message = f"You have gained {itemUseAmount} CS2 Case(s)"

    elif itemID == "07":
        message = f"You have used {itemUseAmount} KFrat Response Token(s)\nPlease DM Ivan to add your custom response(s)"

    elif itemID == "08":
        message = f"You have used {itemUseAmount} KFrat DM Token(s)\nPlease DM Ivan to add your custom DM(s)"

    elif itemID == "09":
        message = breakBadgeToken(itemUseAmount, "Common")
        if message.startswith("Sorry, no one owns any more "):
            itemUseAmount = 0
        updateBadges(array)
        
    elif itemID == "10":
        message = breakBadgeToken(itemUseAmount, "Epic")
        if message.startswith("Sorry, no one owns any more "):
            itemUseAmount = 0
        updateBadges(array)

    elif itemID == "11":
        message = breakBadgeToken(itemUseAmount, "Legendary")
        if message.startswith("Sorry, no one owns any more "):
            itemUseAmount = 0
        updateBadges(array)
        
    elif itemID == "12":
        message = breakBadgeToken(itemUseAmount, "Special")
        if message.startswith("Sorry, no one owns any more "):
            itemUseAmount = 0
        updateBadges(array)
        
    elif itemID == "13":
        message = ""
        if itemUseAmount != 1:
            message += "Sorry, you can only open 1 badge at a time.\n"
        itemUseAmount = 1
        addToMessage = openBadgeToken(array, place, "Common")
        if addToMessage.startswith("Sorry, there are no remaining "):
            itemUseAmount = 0
        message += addToMessage
        updateBadges(array)

    elif itemID == "14":
        message = ""
        if itemUseAmount != 1:
            message += "Sorry, you can only open 1 badge at a time.\n"
        itemUseAmount = 1
        addToMessage = openBadgeToken(array, place, "Epic")
        if addToMessage.startswith("Sorry, there are no remaining "):
            itemUseAmount = 0
        message += addToMessage
        updateBadges(array)

    elif itemID == "15":
        message = ""
        if itemUseAmount != 1:
            message += "Sorry, you can only open 1 badge at a time.\n"
        itemUseAmount = 1
        addToMessage = openBadgeToken(array, place, "Legendary")
        if addToMessage.startswith("Sorry, there are no remaining "):
            itemUseAmount = 0
        message += addToMessage
        updateBadges(array)

    elif itemID == "16":
        array[place].caseBuyCredits += itemUseAmount
        saveArray(array)
        message = f"You have used {itemUseAmount} Case Purchace Credit(s)\nYou can now buy {itemUseAmount} more cases from the shop today"

    #delete item from itemsList
    if itemUseAmount == int(itemCount):
        itemsList.pop(itemIndex)
    else:
        itemsList[itemIndex] = f"{int(itemCount) - itemUseAmount}-{itemID}"

    #update array
    if len(itemsList) == 0:
        array[place].caseItems = ""
    else:
        array[place].caseItems = "|".join(itemsList)
    saveArray(array)

    return message

def breakBadgeToken(itemUseAmount, rarity):
    message = ""
    amountLeft = itemUseAmount
    for i in range(itemUseAmount):
        #create array
        badgeArray = []
        fileLen = 0
        fin = open("badgeList.txt","r")
        while True:
            text = fin.readline().strip()
            if text== "":
                break
            fileLen += 1
            badgeArray.append([text[0],text[1],text[5:]])
        fin.close()


        available = 0
        for i in range(len(badgeArray)):
            if badgeArray[i][0] == "0" and badgeArray[i][1] == (rarity[0].lower()):
                available += 1
        
        #break on no badges
        if (available == 0):
            message += f"Sorry, no one owns any more {rarity} Badges, your token(s) have been returned to you."
            break

        badgeToTakeAway = randint(1,available)
        #make badge available
        fout = open("badgeList.txt","w")
        inUseBadgeCount = 0
        for i in range(fileLen):
            if badgeArray[i][0] == "0" and badgeArray[i][1] == (rarity[0].lower()):
                inUseBadgeCount += 1
            if inUseBadgeCount == badgeToTakeAway:
                fout.write("1"+badgeArray[i][1]+" - "+badgeArray[i][2]+"\n")
                inUseBadgeCount += 1
            else:
                fout.write(badgeArray[i][0]+badgeArray[i][1]+" - "+badgeArray[i][2]+"\n")
        fout.close()
        amountLeft -= 1

    message += f"You have used {itemUseAmount - amountLeft} {rarity} Badge Breaker Token(s)\n{itemUseAmount - amountLeft} {rarity} Badge(s) have been destroyed from a random users inventory"

    return message

"""Used to open a badge and apply to your profile"""
def openBadgeToken(array, place, rarity):
    message = ""
    numCommon = 0
    numEpic = 0
    numLegendary = 0

    #create array
    badgeArray = []
    fin = open("badgeList.txt","r")
    fileLen = 0
    while True:
        text = fin.readline().strip()
        fileLen += 1
        if text== "":
            break
        badgeArray.append([text[0],text[1],text[5:]])

        #gets how many of each rarity there is
        if text[1] == "c":
            numCommon += 1
        if text[1] == "e":
            numEpic += 1
        if text[1] == "l":
            numLegendary += 1
    fin.close()

    previousRarityCount = 0
    if rarity == "Epic":
        previousRarityCount = numCommon
    if rarity == "Legendary":
        previousRarityCount = numCommon + numEpic

    available = 0
    for i in range(len(badgeArray)):
        if badgeArray[i][0] == "1" and badgeArray[i][1] == (rarity[0].lower()):
            available += 1

    #break on no badges
    if (available == 0):
        return f"Sorry, there are no remaining {rarity} Badges, your token had been returned to you."

    randy = randint(0,available-1)
    count = 0
    badgeToAdd = 0
    for i in range(fileLen):
        if badgeArray[i][0] == "1":
            if count == randy+previousRarityCount:
                badgeToAdd = i
                break
            count += 1
    message += f"You have used a {rarity} Badge Token\nYou found the ...\n{badgeArray[badgeToAdd][2]} Badge"

    #add badge to account
    if array[place].badges == "":
        array[place].badges = str(badgeToAdd)
    else:
        array[place].badges += f"|{badgeToAdd}"
    saveArray(array)

    #make badge unavailable
    fout = open("badgeList.txt","w")
    for i in range(len(badgeArray)):
        if i == badgeToAdd:
            fout.write("0"+badgeArray[i][1]+" - "+badgeArray[i][2]+"\n")
        else:
            fout.write(badgeArray[i][0]+badgeArray[i][1]+" - "+badgeArray[i][2]+"\n")
    fout.close()

    return message

"""deposit monies"""
def bank_deposit(ID,bank,amount,array,place):
    if amount < 0:
        return "bitch"
    if(array[place].cash < amount):
        return "Not enough money"
    if(bank == 1):
        array[place].bank0 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 2):
        array[place].bank1 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 3):
        trol = randint(1,10)
        array[place].cash -= amount
        if(trol==1):
            saveArray(array)
            return "Where did the money go?"
        array[place].bank2 += amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 4):
        array[place].bank3 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 5):
        array[place].bank4 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 6):
        array[place].bank5 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 7):
        array[place].bank6 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 8):
        array[place].bank7 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 9):
        array[place].bank8 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 10):
        array[place].bank9 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"
    if(bank == 11):
        array[place].bank10 += amount
        array[place].cash -= amount
        saveArray(array)
        return "Deposited sucsessfully"

"""un-deposit monies"""
def bank_withdraw(ID,bank,amount,array,place):
    if amount < 0:
        return "bitch"
    if(bank == 1):
        if(array[place].bank0 < amount):
            return "Not enough funds"
        array[place].bank0 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 2):
        if(array[place].bank1 < amount):
            return "Not enough funds"
        array[place].bank1 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 3):
        if(array[place].bank2 < amount):
            return "Not enough funds"
        array[place].bank2 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 4):
        if(amount > array[place].bank3):
            return "Not enough funds"
        if(array[place].bank3 < amount*10) and (array[place].bank3 >= 10):
            return "Don't gamble"
        array[place].bank3 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank ==5):
        if(array[place].bank4 < amount):
            return "Not enough funds"
        array[place].bank4 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 6):
        if(array[place].bank5 < amount):
            return "Not enough funds"
        array[place].bank5 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 7):
        if(array[place].bank6 < amount):
            return "Not enough funds"
        array[place].bank6 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 8):
        if(array[place].bank7 < amount):
            return "Not enough funds"
        array[place].bank7 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 9):
        if(array[place].bank8 < amount):
            return "Not enough funds"
        array[place].bank8 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 10):
        if(array[place].bank9 < amount):
            return "Not enoug9h funds"
        array[place].bank9 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    if(bank == 11):
        if(array[place].bank10 < amount):
            return "Not enoug9h funds"
        array[place].bank10 -= amount
        array[place].cash += amount
        saveArray(array)
        return "Withdrawn sucsessfully"
    
"""Show bak money"""
def bank(ID,lowered):

    array = getArray()
    place = getPlace(ID,array)
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
        return "Here are a list of sub-commands\nHelp: show this\nDeposit [ID] [Amount]: Deposits money\nWithdraw [ID] [Amount]: Withdraws money\nList: Shows Bank list\nInfo [ID]: Shows Bank information\nAmount: Show all your bank values.\nStats: show other stats regarding the bank"  
    elif(command == "deposit"):
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
        if (lowered.count(" ") == 2):
            return "Please add an amount to deposit"
        return bank_deposit(ID,int(lowered.split(" ") [2]),int(lowered.split(" ") [3]),array,place)
    elif(command == "withdraw"):
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
        if (lowered.count(" ") == 2):
            return "Please add an amount to withdraw"
        return bank_withdraw(ID,int(lowered.split(" ") [2]),int(lowered.split(" ") [3]),array,place)
    elif(command == "list"):
        return "Here are the list of banks:\n1. Wordle Bank\n2. Wordle Shitter Bank\n3. Gambling bank\n4. Addict Bank\n5. Safe Bank\n6. Social Bank\n7. Achivement Bnk\n8. Cool Kid Bank\n9. Sleepy Bank\n10. Beef Dip Bank\n11. Case Bank"
    elif(command == "info"):
        if (lowered.count(" ") == 1):
            return "Please add a bank ID"
        else:
            #Add Bank info here
            return ["Wordle Bank: Get money based on how good you do in the wordle","Wordle Shitter Bank: Get money based on how bad you do in the wordle but don't fail","Gambling Bank: Have a chance to recover money when you lose a gamble but gamble each deposit","Addict Banks: Gain interest the longer you go without gambling","Safe Bank: Gain small interest every day\n[$1000 inveested] Get extra money when you get the hourly money","Social Bank: Get interest for being in voice calls with others","Achievement bank: Get more interest based on how many achievements you have","Cool Kid Bank: A massive amount of interest but it is split amoung each player invested in this bank","Sleepy Bank: Gain interest for time spent in a voice call by yourself","Beef Dip Bank: Interest gained when you beef dip depending on your beef dip tier","Case Bank: Get interest using Interest Tokens, but your money can be stolen with Robery Tokens"][int(lowered.split(" ")[2]) - 1]
    else:
        return "try [,bank help] for more information"
    


    #old bank code
    #array = getArray()
    #place = getPlace(ID,array)
    #return f"You have ${array[place].bank0} in the bank"

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

"""Shows the leaderboard of money"""
def leaderboard_net():
    array = getArray()
    text = ""
    length = len(array) 
    for i in range(length):
        top = -1
        by = ""
        spot = -1
        for j in range(len(array)):
            if int(array[j].net) > top:
                top = int(array[j].net)
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

    array[place].daysnogamble = 0
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
        moneygain = (int(len(e))+1)
        if(array[place].bank4 >= 1000):
            moneygain += 5
        array[place].cash += moneygain
        saveArray(array)
        if(ID == 549031318139174916):
            return f"Here are your ${moneygain} Whoresey."
        elif(ID == 719250188228886620):
            return f"Here is your ${moneygain} of gambling money you slut"
        elif(ID == 552600422016090133):
            return f"Here is your ${moneygain} you dirty Spigru"
        else:
            return f"You got the Bonus ${moneygain} and now have ${array[place].cash}"

"""gets a number, fucks up my pc"""
def fuckComputer(num):
    if num == 1:
        #playsound("Z:\Assets\Sounds\\vine-boom.mp3")
        return True
    elif num == 2:
        #playsound("Z:\Assets\Voice Lines\\now-its-reyn-time.mp3")
        return True
    elif num == 3:
        #playsound("Z:\Assets\Voice Lines\chicken-jockey.mp3")
        return True
    elif num == 6:
        #startfile("Z:\Assets\Videos\Saul goodman 3d.mp4")
        return True
    elif num == 7:
        #startfile("Z:\Assets\Videos\PARKOUR CIVILIZATION.mp4")
        return True
    elif num == 9:
        #playsound("Z:\Assets\Voice Lines\\flint-and-steel.mp3")
        return True
    elif num == 10:
        return True
    elif num == 11:
        return True
    elif num == 12:
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
        print(item)
        if(item == 12):
            print(array[place].cases)
            array[place].cases += 1
            print(array[place].cases)
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
        return "You are not registered, do [,register] to register"

    #make sure that they enter a proper amount
    try:
        bet = int(message.split(" ")[1].strip())
    except (IndexError, ValueError):
        return "Please enter a valid bet amount like \",coinflip 50\"."
    if (bet < 1):
        return "Nope"
    if (bet > array[place].cash):
        return f"Sorry, your bet is too high, your total amount of money is {array[place].cash}"
    array[place].daysnogamble = 0
    if(win == 1):
        array[place].cash -= bet
        saveArray(array)
        banksave = randint(1,20)
        if banksave == 20:
            array[place].cash += min(bet,array[place].bank2)
            saveArray(array)
            return f"You lost the coinflip but the gamble bank came in clutch! You lost ${bet-min(bet,array[place].bank2)}"
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
        array.append(Person(text.split(",") [0],text.split(",") [1],text.split(",") [2],text.split(",") [3],text.split(",") [4],text.split(",") [5],text.split(",") [6],text.split(",") [7],text.split(",") [8],text.split(",") [9],text.split(",") [10],text.split(",") [11],text.split(",") [12],text.split(",") [13],text.split(",") [14],text.split(",") [15],text.split(",") [16],text.split(",") [17],text.split(",") [18],text.split(",") [19],text.split(",") [20],text.split(",") [21],text.split(",") [22],text.split(",") [23],text.split(",") [24],text.split(",") [25],text.split(",") [26],text.split(",") [27],text.split(",") [28],text.split(",") [29],text.split(",") [30],text.split(",") [31],text.split(",") [32],text.split(",") [33],text.split(",") [34],text.split(",") [35]))
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
    array.append(Person(str(ID),"0","0",message.split(" ") [1],"0","0","0","0","0","0","0","","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","","",""))
    saveArray(array)
    return "Resitered Sucsessfully"

def logVC(people):
    amount = len(people)
    array = getArray()
    large = (amount >= 8)

    if(len(people) == 1):
        place = getPlace(people [0],array)
        array[place].cash += array[place].bank8 /100000
        array[place].VCAlone += 1
    else:
        for i in range(len(people)):
            place = getPlace(people [i],array)
            if (randint(1,60) == 7):   
                array[place].cash += array[place].bank5 /100 * amount
                print(f"paid {array[place].name} {array[place].bank5 /100 * amount}")
            array[place].VC2 += 1
            if large:
                array[place].VCGroup += 1
    saveArray(array)

def wordle(message):
    array = getArray()
    lines = message.split("\n")
    for i in range(len(lines)-1):
        if(lines[i+1] [0]== "👑" or lines[i+1].startswith(":crown:")):
            moneyGain = 0.025
            shitterGain = 0.002
            susadd = 5
        if(lines[i+1] [0]== "2"):
            moneyGain = 0.02
            shitterGain = 0.001
            susadd = 2
        if(lines[i+1] [0]== "3"):
            moneyGain = 0.01
            shitterGain = 0.00
            susadd = 0
        if(lines[i+1] [0]== "4"):
            moneyGain = 0.005
            shitterGain = 0.005
            susadd = -1
        if(lines[i+1] [0]== "5"):
            moneyGain = 0.0025
            shitterGain = 0.005
            susadd = -3 
        if(lines[i+1] [0]== "6"):
            moneyGain = 0
            shitterGain = 0.01
            susadd = -5
        if(lines[i+1] [0]== "X"):
            moneyGain = -0.05
            shitterGain = -0.1
            susadd = -10

        for j in range(lines[i+1].count("@")):
            if(lines[i+1].split("@")[j+1].count(">") == 1):
                ID = int(lines[i+1].split("@")[j+1].split(">")[0])
                place = getPlace(ID, array)
                if(place != -1):
                    array[place].cash += int(moneyGain*float(array[place].bank0))
                    array[place].cash += int(shitterGain*float(array[place].bank1))
                    array[place].sus += susadd
                    array[place].wordle += 1

        coolkid = 0
        #general interest for everyone
        for i in range(len(array)):
            array[i].daysnogamble += 1
            if (array[i].bank7 > 0): coolkid += 1
        if(coolkid == 0):
            coolkid = 1
        for i in range(len(array)):
            array[i].cash += array[i].bank3 * min(array[i].daysnogamble,30)/1000
            array[i].cash += array[i].bank4 * 0.01
            array[i].cash += array[i].bank6 * array[place].achivements.count("-")/1000
            array[i].cash += array[i].bank7 / 10 / coolkid

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
        string = "You have "+str(array[place].achivements.count("-"))+" achivements, they are:\n"
        for i in range(array[place].achivements.count("-")):
            string += array[place].achivements.split("-")[i]
            string += "\n"

        return string
    
def beef_dip(message,ID):
    array=getArray()
    place = getPlace(ID,array)
    if (array[place].beefdip != 5):
        return "Your Beef Dip Tier is Tier "+str(array[place].beefdip)
    for i in range(message.count("@")):
        tempid = int(message.split("@")[i+1].split(">")[0])
        tempplace = getPlace(tempid,array)
        array[tempplace].cash += array[tempplace].bank9 *array[tempplace].beefdip / 100
    saveArray(array)
    return "Your Beef Dip Tier is Tier "+str(array[place].beefdip)

def case(message,ID):
    array = getArray()
    place = getPlace(ID,array)
    print(place)
    print(array[place].cases)
    return f"You have {array[place].cases} cases"


#Response based on message sent
def get_response(user_input: str,username, nameID, channel) -> str:
    text = ""
    bot_list = ["john-bot","bot-commands","bot-commands-2"]
    lowered: str = user_input.lower()
    
    x = randint(1,100)
    print(x)
    #nameID == 1211781489931452447 and 
    if(lowered.startswith("**your group is on a ") and (nameID==475196692807811074 or nameID==1211781489931452447)):
        if(channel == "john-wordle"):
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
    elif lowered.startswith(",market"):
        text = market(nameID,lowered)
    elif lowered == ",badge" or lowered == ",badges":
        text = badges(nameID)
    elif lowered.startswith(",case"):
        text = case(nameID,lowered)
    elif lowered == ",beef dip":
        text = beef_dip(lowered,nameID)
    elif lowered.startswith(",bank"):
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
    elif lowered.startswith(",case") and channel in bot_list:
        text = case(lowered,nameID)
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
        elif lowered == ",leaderboard net":
            text = leaderboard_net()
        else:
            text = "leaderboards: count, money, beer, bank, net"
    elif ((lowered.find("what") != -1) & (len(lowered)>10) & (lowered.count(" ") > 4)) or(randint(1,1000) == 120):
        text = choice(["Ah shit, here we go again ...",
                      "Let's go, open up, it's time for parkour",
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
    #elif lowered == ",cash in":
        #if(array[place].count >= 1000):
            #text = f"You have cashed in and gained ${cashIn(nameID)}"
        #else: text = "Sorry buddy, but you need at least 1000 points to cash in. Bulk only"
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
    
    #bunch of random crap    
    elif lowered.find("help") != -1:
        num = lowered.count("serious")
        if(num==0):
            text = "In a bit"
        else:
            text = "give me "+str(5*num)+" minutes"


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
    if(array[place].achivements.find("Mr. Popular") == -1 and array[place].VCGroup >= 60):
        array[place].achivements += "Mr. Popular-"
        text += "\n\nAchivement Get: Mr. Popular"
    if(array[place].achivements.find("Forever Alone") == -1 and array[place].VCAlone >= 1440):
        array[place].achivements += "Forever Alone-"
        text += "\n\nAchivement Get: Forever Alone"
    if(array[place].achivements.find("Beef Dip Tier 1") == -1 and array[place].beefdip >= 1):
        array[place].achivements += "Beef Dip Tier 1-"
        text += "\n\nAchivement Get: Beef Dip Tier 1"
    if(array[place].achivements.find("Beef Dip Tier 2") == -1 and array[place].beefdip >= 2):
        array[place].achivements += "Beef Dip Tier 2-"
        text += "\n\nAchivement Get: Beef Dip Tier 2"
    if(array[place].achivements.find("Beef Dip Tier 3") == -1 and array[place].beefdip >= 3):
        array[place].achivements += "Beef Dip Tier 3-"
        text += "\n\nAchivement Get: Beef Dip Tier 3"
    if(array[place].achivements.find("Beef Dip Tier 4") == -1 and array[place].beefdip >= 4):
        array[place].achivements += "Beef Dip Tier 4-"
        text += "\n\nAchivement Get: Beef Dip Tier 4"
    if(array[place].achivements.find("Beef Dip Tier 5") == -1 and array[place].beefdip >= 5):
        array[place].achivements += "Beef Dip Tier 5-"
        text += "\n\nAchivement Get: Beef Dip Tier 5"
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