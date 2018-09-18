dictionaryTest = {
	"test1":"testA",
        "test2":"testB",
}

for key, value in dictionaryTest.items():
	print("%s: %s" % (key, value))

while True:
    cmd = input("Would you like to update or view dictionaryTest? Y or N: ")
    if cmd == ("Y" or "y" or "Yes"):
        while True:
            cmd2 = input("Update or View? U or V: ")
            if cmd2 == ("U" or "u" or "Update"):
                print("Test U")
                break
            elif cmd2 == ("V" or "v" or "View"):
                for key, value in dictionaryTest.items():
                    print("%s: %s" % (key, value))
                break
            else:
                print("Please enter a valid response." )
    elif cmd == ("N" or "n" or "No"):
        print("The program will now end.")
        break
    else:
        print("Please enter a valid response." )
    
