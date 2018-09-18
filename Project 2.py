dictionaryTest = {
	"test1":"testA",
        "test2":"testB",
}

for key, value in dictionaryTest.items():
	print("%s: %s" % (key, value))

#Main Code
while True:
    cmd = input("Would you like to update or view dictionaryTest? Y or N: ")
    if cmd == ("Y" or "y" or "Yes"):
        while True:
            cmd2 = input("Update or View? U or V: ")
            if cmd2 == ("U"):
                cmd3 = input("Would you like to add a new key and value, remove an existing key and value, or change an existing one? A or R or C: ")
                if cmd3 == ("A"):
                        key = input("Enter a new key to add: ")
                        value = input("Enter a value for the new key: ")
                        dictionaryTest[key] = value
                elif cmd3 == ("R"):
                        dictDelete = input("Enter a key to be removed: ")
                        del dictionaryTest[dictDelete]
                elif cmd3 == ("C"):
                        key = input("Enter a key to have it's value changed: ")
                        value = input("Enter the new value for this key: ")
                        dictionaryTest[key] = value
                else:
                        print("Please enter a valid response." )
                break
            elif cmd2 == ("V"):
                for key, value in dictionaryTest.items():
                    print("%s: %s" % (key, value))
                break
            else:
                print("Please enter a valid response." )
    elif cmd == ("N"):
        print("The program will now end.")
        break
    else:
        print("Please enter a valid response." )
    
