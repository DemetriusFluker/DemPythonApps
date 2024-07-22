def main():
        print("\nHello Friend")
        print("Welcome to the game")
        import datetime as dt
        today = dt.date.today()
        print(today)
        
        def lonely():
                print("damn I know you must be lonely?")
                gay = str (input("are you LGBTQ? "))
                if gay == 'yes':
                        print("Okay, great! We have another forum for LGBTQ")
                        print("Check back later for our new forum on that community!")
                        print("You have a blessed day!")
                        print()
                        exit()
                else:
                        print("What's the deal, Everybody needs somebody?")
                        print()
          
        age = int
        wifeage = int
        trad = str

        listA = ["Dont act like a little bitch around her", "if she has a kid dont date her", "Dont lie to women, tell the truth", 
                 "find out about her past, it matters"]
        listB = ["If she doesnt know when to shut up dont marry her", "never let a woman control your son", "never let her control the bills",
                 "never let her talk over you"]
        listD = ["Never let a woman know your weakness", "use it against you", "know where you want to live and raise a family", "never let a woman decide where you live",
                 "Never allow a woman to dictate the money!"]
        listC = ["A man does not respond to feelings", "Women and boys respond to feelings"]
        listE = ["you need to dazzle them with your cloths", "you need to charm her with your words", "develop a powerful gaze", 
                 "play psychological games", "use soft words", "play the coquette", "master the feminine strategies"]

        boyname = str (input("\nwhat is your name? "))
        print("hello\n", *boyname)
        
        foundgirl = str (input("\ndo you have a girlfriend? "))
        if foundgirl == 'yes':
                print("good for you", *boyname)
        
        elif foundgirl == 'no':
                lonely()
                print()
                print("Not having a girlfriend sucks! \nevery straight man needs a woman", *boyname)
                print("you need to learn the art of seduction son\n") 
                learnseduction = str (input("would you like to learn? "))
                if learnseduction == 'yes':
                        print()
                        print("\nOkay, but when I'm done go meets some girls and come back after you learn these rules! \n\n", *boyname)
                        print()
                        learnseduction0 = str (input("Are you sure you're ready to start learning? "))
                        if learnseduction0 == 'yes':
                                for element in listE:
                                        print()
                                        print(*element)
                                        print()
                        else:
                                print("bye", *boyname)
                                print()
                                exit()
                        learnseduction1 = str (input("would you like to continue learning? "))
                        if learnseduction1 == 'yes':
                                for element in listA:
                                        print()
                                        print(*element)
                                        print()
                        else:
                                print("bye", *boyname)
                                print()
                                exit()
                        learnseduction2 = str (input("would you like to continue? "))
                        if learnseduction2 == 'yes':
                                for element in listB:
                                        print()
                                        print(*element)
                                        print()
                        else:
                                print("bye", *boyname)
                                print()
                                exit()
                        learnseduction4 = str (input("would you like to continue learning? "))
                        if learnseduction4 == 'yes':
                                for element in listD:
                                        print()
                                        print(*element)
                                        print()
                        else:
                                print("bye", *boyname)
                                print()
                                exit()
                        learnseduction3 = str (input("would you like to continue? "))
                        if learnseduction3 == 'yes':
                                for element in listC:
                                        print()
                                        print(*element)
                                        print()
                        else:
                                print("bye ol weak brokey")
                                print()
                        exit()
                else:
                        print("bye", boyname); print("lame ass brokey")
                        exit()
        else:
                print("bye bye")
                exit() 

        redpill = str (input("\nWould like to play redpill? "))
        if redpill == 'yes':
                print("very well then lets begin")
        else:
                print("see you later")
                exit()


        Fine = str (input("\nis your girlfriend fine? "))
        if Fine == 'yes': 
                print("lucky dog, oohhh she making me make choices")
        else:
                print("no thanks, not interested")
                exit()


        age = int (input("\nhow old are you? "))
        if age > 30:
                print("yes", boyname, "my son you are ready to marry")
        else:
                print("you are not really ready yet player, come back when you're old enough")
                exit()

        wifeage = int (input("\nhow old is your girl? "))
        
        if wifeage < 30 and wifeage >18:
                print("She is ready to be married")
        elif wifeage < 18:
                print("no way she's too young")
                exit()
        elif wifeage > 50:
                print("she's way too old for you fam")
                exit()
        else:
                print("hell no don't marry her, she's too old")
                exit()
        

        trad = str (input("\nis the girl traditional yes or no? "))

        if trad == 'yes':
                print("thank god she is trad!")
        else:
                print("nooooo, you're a modern woman! sorry baby, I just can't do it")
                print("sorry baby but we only date trad women")
                exit()

        ourage = age * wifeage
        print("\nyour combined age is", ourage)


        name = str (input("\nWhat is her name "))

        if ourage > 1000 and trad == 'yes':
                print("yawl's combined age is too high, this isn't going to work")
                print("sorry", name, "you're not the one because you're too old")
                exit()  

        elif ourage < 1000 and trad == 'yes': 
                print("\nyawl could start a beautiful relationship together")
        

        if wifeage < 30 and trad == 'yes':
                print("\nHello", name, "you might be the one for", boyname)
        
        repeat = (input("Would you like to play again? " ))
        if repeat == 'yes':
                main()
        else:
                print("bye bye")

main()

