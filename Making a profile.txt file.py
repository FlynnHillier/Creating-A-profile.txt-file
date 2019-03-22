
Y = "Enter Y/N: "
T = "Type Here: "
print("Hi there! I'm going to help you make yourself a little profile \nabout yourself!\n")

#name questioning below

loop = 1
while loop == 1:
        name = "Unassigned"
        print("What is your first name and last name?\nexmpl. James Stevens")
        name = input(T)
        name = name.split()
        if len(name) == 2 and name[0].isalpha() == True and name[1].isalpha() == True:
            fullname = name[0].capitalize()+" "+name[1].capitalize()
            name = name[0].capitalize()
            loop = 2
            if fullname == "Flynn Hillier":
                print("your the best flynn, thanks for writing me.") 
            while loop == 2:
                print("\nYou entered: '{}', correct?".format(fullname))
                yn = input(Y)
                yn = ((yn).upper())
                loop = 1
                if yn == "Y":
                    loop = 0
                elif yn == "N":
                    print("\nOkay, lets try again.")
                    loop = 0
                    loop = 1
                else:
                    print("Please Enter 'Y' or 'N'")
                    loop = 0
                    loop = 2
                
        else:
            print("\nPlease enter only a valid first and last name. We'll try again.")
            loop = 0
            loop = 1


print("\nAlright "+(name)+", I've got some more questions for you, please answer them.\n")

#gender questioning below
loop = 1
while loop == 1:
        (gender) = "Unassigned"
        print("Please enter your gender?")
        (gender) = input("Enter 'female' or 'male':")
        loop = 2
        if gender == "male" or gender == "female":
            while loop == 2:
                gender = (gender.capitalize())
                print("\nYou entered: '"+(gender)+"', correct?")
                yn = input(Y)
                yn = ((yn).upper())
                loop = 1
                if yn == "Y":
                    loop = 0
                elif yn == "N":
                    print("\nOkay, lets try again.")
                    loop = 0
                    loop = 1
                else:
                    print("Please Enter 'Y' or 'N'")
                    loop = 0
                    loop = 2
        else:
            print("\nPlease enter one of the above genders. We'll try again.")
            loop = 0
            loop = 1
            
#age questioning below

loop = 1
while loop == 1:
        (age) = "Unassigned"
        print("\nHow old are you, "+(name)+"?")
        (age) = input(T)
        loop = 2
        if (age.isdigit()) == True:
            while loop == 2:
                print("\nYou entered: '"+(age)+"', correct?")
                yn = input(Y)
                yn = ((yn).upper())
                loop = 1
                if yn == "Y":
                    loop = 0
                elif yn == "N":
                    print("\nOkay, lets try again.")
                    loop = 0
                    loop = 1
                else:
                    print("\nPlease Enter 'Y' or 'N'")
                    loop = 0
                    loop = 2
        else:
            print("\nPlease enter a valid number. We'll try again.")
            loop = 0
            loop = 1

#hair questioning below

haircolours = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black","pink","brown","ginger","blonde"]
loop = 1
while loop == 1:
        (hair) = "Unassigned"
        print("\nYour Hair colour, "+(name)+"?")
        (hair) = input(T)
        loop = 2
        if hair.isalpha() == True:
            hair = hair.lower()
            if haircolours.count((hair)) > 0: 
                while loop == 2:
                    print("\nYou entered: '"+(hair)+"', correct?")
                    yn = input(Y)
                    yn = ((yn).upper())
                    loop = 1
                    if yn == "Y":
                        loop = 0
                    elif yn == "N":
                        print("\nOkay, lets try again.")
                        loop = 0
                        loop = 1
                    else:
                        print("\nPlease Enter 'Y' or 'N'")
                        loop = 0
                        loop = 2
            else:
                print("\nPlease enter a valid hair colour. We'll try again.")
                print("Valid colours:"+(str(haircolours)))
                loop = 0
                loop = 1
        else:
            print("\nPlease Enter a vaild hair colour.we'll try again.")
            print("Valid colours:"+(str(haircolours)))
            loop = 0
            loop = 1

#eye colour questioning

loop = 1
eyecolours = ["hazel","brown","blue","green"]
while loop == 1:
        (eye) = "Unassigned"
        print("\nYour eye colour, "+(name)+"?")
        (eye) = input(T)
        loop = 2
        if eye.isalpha() == True:
            eye = eye.lower()
            if eyecolours.count((eye)) > 0: 
                while loop == 2:
                    print("\nYou entered: '"+(eye)+"', correct?")
                    yn = input(Y)
                    yn = ((yn).upper())
                    loop = 1
                    if yn == "Y":
                        loop = 0
                    elif yn == "N":
                        print("\nOkay, lets try again.")
                        loop = 0
                        loop = 1
                    else:
                        print("\nPlease Enter 'Y' or 'N'")
                        loop = 0
                        loop = 2
            else:
                print("\nPlease enter a valid eye colour. We'll try again.")
                print("Valid colours:"+(str(eyecolours)))
                loop = 0
                loop = 1
        else:
            print("\nPlease Enter a vaild eye colour.we'll try again.")
            print("Valid colours:"+(str(eyecolours)))
            loop = 0
            loop = 1





#Entering Height Below

loop = 1
while loop == 1:
    end = "n"
    print('\nEnter height\nexmpl. 6 11 , 5 9 , 5 0')
    height = input(T)
    if len(height) == 4:
        end = "y"
        height = list(height)
        if height[1] == ' ': 
            del height[1]

            #checks required characters are digits
            mcheck = 0 
            acheck = 0
            for i in (height):
                DigCheck = height[(mcheck)]
                mcheck += 1
                if DigCheck.isdigit() == False:
                    (1+1)
                else:
                    acheck +=1
                    
            #stops code if not all required characters are not digits
            if acheck == ((len(height))):

                #checks " are < 12
                mcheck = height[1]+height[2]
                mcheck = (int(mcheck))
                if mcheck > 11:
                    print("\nPlease enter correct characters")
                    loop = 0
                    loop = 1
                else:
                    loop = 2
                    while loop == 2:
                        height = height[0]+'ft '+height[1]+height[2]+'"'
                        print("\nYou entered: '"+(height)+"', correct?")
                        yn = input(Y)
                        yn = ((yn).upper())
                        loop = 1
                        if yn == "Y":
                            loop = 0
                            end = "y"
                        elif yn == "N":
                            print("\nOkay, lets try again.")
                            loop = 0
                            loop = 1
                        else:
                            print("\nPlease Enter 'Y' or 'N'")
                            loop = 0
                            loop = 2
            else:
                print('\nPlease enter correct characters')
                loop = 0
                loop = 1

            #if characters entered = 3. exmpl 5"1

        
    if len(height) == 3 and end == "n":
        height = list(height)
        if height[1] == ' ': 
            del height[1]
            FalseChecker = "NotFalse"
                
            #checks required characters are digits   
            mcheck = 0
            for i in (height):
                FalseCheck = height[(mcheck)]
                mcheck += 1
                if FalseCheck.isdigit() == False:
                    FalseChecker = "IsFalse"
                    
            if FalseChecker == "IsFalse":
                print("\nPlease enter correct characters")
            else:
                loop = 2
                while loop == 2:
                    height = height[0]+'ft '+height[1]+'"'
                    print("\nYou entered: '"+(height)+"', correct?")
                    yn = input(Y)
                    yn = ((yn).upper())
                    loop = 1
                    if yn == "Y":
                        loop = 0
                    elif yn == "N":
                        print("\nOkay, lets try again.")
                        loop = 0
                        loop = 1
                    else:
                        print("\nPlease Enter 'Y' or 'N'")
                        loop = 0
                        loop = 2
        else:
            print('\nPlease enter height in this format:\nexmpl. 6 10 or 4 8')
            loop = 0
            loop = 1

#Any extras below

loop = 1
while loop == 1:
        print("\nNow write anything else about yourself,\nsimply don't write anything and click enter, to skip this.")
        (extra) = input(T)
        loop = 2
        if extra == "":
            extra = "Non given."
            loop = 0   
        else:
            while loop == 2:
                print("\nYou entered: "+(extra)+" Correct?")
                yn = input(Y)
                yn = ((yn).upper())
                loop = 1
                if yn == "Y":
                    loop = 0
                elif yn == "N":
                    print("\nOkay, lets try again.")
                    loop = 0
                    loop = 1
                else:
                    print("Please Enter 'Y' or 'N'")
                    loop = 0
                    loop = 2

f = open("Profile of "+(fullname)+".txt","w+")
f.write ("Profile of "+(fullname)+"\n\nSex: "+(gender)+"\n\nHeight: "+(height)+"\n\nEye Colour: "+(eye)+"\n\nHair Colour: "+(hair)+"\n\nAge: "+(age)+"\n\nExtra Info: "+(extra)+"\n\n\nProfile written using Kalanz's Profile Creator")
f.close()

print("\nI've written your profile. \nCheck the folder in which this code is saved, you'll find it there")
print("\n\nThank you for using Kalanz's profile creator.")

loop = 1
while loop == 1:
    print("\n\nType 'Kill' to end program")
    kill = input(T)
    if kill.capitalize() == "Kill":
            loop = 0
    
        
#Written By Kalanz.






        
    

