#Johsty Bach
#Project 2: Dictionaries
#Finished on 9/24/18

#Dictionary that is edited in the main code
myDict = {
	"test1":"testA",
        "test2":"testB",
}



'''Tests'''

#Testing coverting a dictionary to a list
dictTest = list_key_value = [ [k,v] for k, v in dict.items(myDict) ]
#print(list_key_value)


#Testing more stuff
def list1():
        dictTest1 = []
        count = 0
        for i in dictTest:
                if count % 2 == 0:
                        dictTest1.append(i)
                        count += 1
        return dictTest1

def list2():
        dictTest2 = []
        count = 0
        for i in dictTest:
                if count % 2 == 1:
                        dictTest2.append(i)
                        count += 1
        return dictTest2



'''Functions'''

#Function to add a new key and value
def addKeyValue():
        key = input("Enter a key to be added: ")
        if key in myDict:
                print("That key already exists. ")
        else:
                value = input("Enter the value for this key: ")
                myDict[key] = value
        return myDict

#Function to remove a key and it's value
def removeKeyValue(dictDelete):
        if dictDelete in myDict:
                del myDict[dictDelete]
        else:
                print("That key does not exist. ")
        return myDict

#Function to change a key and it's value
def changeKeyValue():
        key = input("Enter a key to have it's value changed: ")
        if key in myDict:
                value = input("Enter the new value for this key: ")
                myDict[key] = value
        else:
                print("That key does not exist. ")

#Function to print the dictionary
def printDict():
        for key, value in myDict.items():
                print("%s: %s" % (key, value))




#Prints the dictionary as it is before the main code starts, if anything is there
printDict()





#Main Code
while True:
    cmd = input("Would you like to update or view dictionaryTest? Y or N: ")
    if cmd == ("Y" or "y" or "Yes"):
        while True:
            cmd2 = input("Update or View? U or V: ")
            if cmd2 == ("U"):
                cmd3 = input("Would you like to [A]dd a new key and value, [R]emove an existing key and value, or [C]hange an existing key and value?: ")
                if cmd3 == ("A"):
                        addKeyValue()
                elif cmd3 == ("R"):
                        dictDelete = input("Please input a key to be deleted: ")
                        removeKeyValue(dictDelete)
                elif cmd3 == ("C"):
                        changeKeyValue()
                else:
                        print("Please enter a valid response." )
                break
            elif cmd2 == ("V"):
                printDict()
                break
            else:
                print("Please enter a valid response." )
    elif cmd == ("N"):
        print("The program will now end.")
        break
    else:
        print("Please enter a valid response." )
