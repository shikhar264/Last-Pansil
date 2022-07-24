num_nt_numeric = True
 # This piece of line will make this program run inifinite times
print("How many pencils would you like to use:")
while True:
    # if in a case the variable 'num_nt_numeric' is still True
    if num_nt_numeric:
        
        number = input()
        numeric = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for i in number:    
            if i not in numeric:
                print("The number of pencils should be numeric")
                num_nt_numeric = True
                break
            else:
                num_nt_numeric = False
            
    if num_nt_numeric == False and int(number) == 0:
        print("The number of pencils should be positive")
        num_nt_numeric = True
            
    if num_nt_numeric == False:
        print("Who will be the first (John, Jack):")
        name = input()
        if name == 'John' or name == 'Jack':                    
             number = int(number)
             break
        else:
            print("Choose between John and Jack")

bot_turn = False
import random
while True:
    print("|" * number)
    print(f"{name}'s turn: ")
    if name == "Jack":
        if number == 1:
            pencils = 1
        else:
            # I have to substract 3 from 4 and 8
            # 2 from 3 and 7
            # and 1 from 2 and 6
            if number % 4 == 0:
                pencils = 3
            elif number % 4 == 3:
                pencils = 2
            elif number % 4 == 2:
                pencils = 1
            else:
                pencils = random.randint(1, 3)
        
        print(pencils)
        number -= pencils
                    
        name = "John"
    else:
        pencils = input()
        if pencils not in numeric:
            print("Possible values: '1', '2' or '3'")
        else:
            pencils = int(pencils)
            if pencils > 3 or pencils < 1:
                print("Possible values: '1', '2' or '3'")
            else:
                if number - pencils < 0:
                    print("Too many pencils were taken")
                else:
                    number -= pencils
                    
                    name = "Jack"
    if number == 0:
        print(f"{name} won!")
        break



