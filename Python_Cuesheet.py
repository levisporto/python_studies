# comment like this
#print("Hello " + "world!")
# math is just like other programming languages
#print(50/2)

# Primitive Data Type: Fixed size, predetermined by the programming language: string, integers, true/false (e.g., integer always takes 4 bytes). 
# Non-Primitive: Variable size, depending on the complexity of the data they hold

# Logical operators and booleans: not / and / true / false / or / if / else / elif
#if(5 > 2 or 3 < 4):
#    print("Condition is True")   
#elif (100 == 101): 
#    print("Condition is False")
#else:
#    print("Condition is False too")

#For loop (also using a f-string, a Formatted String Literal)
#numbers = [1, 2, 3]
#for num in numbers:
#    print(f"Lets count using a for loop: {num}...")

# You can use format() to interpolate formatted strings
#print("Lets count using a for loop: {}".format(num))
# Match-case statement (like switch-case in Javascript)
#num = 1
#match num:
#    case 1:
#        print("Your number is one")
#    case 2 | 3:  # multiple options (OR pattern)
#        print("Your number is two OR three")
#    case code if num.isdigit():  # conditional
#        print(f"The robot execute code: {code}")
#    case _:  # _ is a wildcard that never fails (like default/else)
#        print("Invalid number ❌")


# Comparison operators: < / > / == / != / <= / >=
#Bool is used to represent true/false values
#x = bool(1)
#y = bool(0)
#z = bool(1==2)
#print(x)    
#print(y)    
#print(z)        

#This is a Python list (non-primitive data type). If you want it immutable, use tuples (tup), if you would like to add or remove items use Sets (set)
#a = [1, 2, 3, 4]
#append() adds an element to the end of the list
#a.append(5)  
#print(a)
#pop() removes the last element from the list
#a.pop()
#::-1 for reverse order
#print(a[::-1])
#1:3 for slicing the list
#print(a[1:3])
#insert an element in the list. must specify index
#viado = ["gay"]
#viado.insert(1, "hehe")
#remove an element of the list
#viado.remove("gay")
#print(viado)
#you can concatenate lists
#viado.extend(a)
#print(viado)





#Dictionaries are used to store data values in key:value pairs
#myDict = {
#    "name": "Alice",
#    "age": 30,
#    "city": "New York"
#}
#print(myDict["name"])


#Len is a function to find the length
#print(len("how many characters in this phrase?"))
#s = "you can concatenate strings"
#print("now see this: " + s)
#Can also be done with f-string and formatted string literals
#print(f"now see this: {s}")

# input() function to capture user input
#userInput = input("Enter and I will echo: ") 
#print("You entered: " + userInput)

#Python is batteries included, so you can import modules without installing anything extra:
#import datetime
#now = datetime.datetime.now()
#print(f"The current time is: {now}")

#This is a little Single-Player Russian Rollete game for studying Python loops and conditionals:
#import random       
#russian_roullete = random.randint(1, 6)
#times = 1
#while russian_roullete  !=1:
        
#        if times == 1:
#            print("What a Miracle! You are alive!")
#            print(f"You survived {times} time.")
#        else:
#            print("What a Miracle! You are still alive!")
#            print(f"You survived {times} times.")
#        print("Let's try again...")
#        russian_roullete = random.randint(1, 6)
#        times += 1
#else:
#        print("Oops! You died! Sorry.")
       

#This is a little Player vs COM Russian Rollete game for studying Python loops and conditionals:

#import random
#decide_player = random.randint(0, 1)
#if decide_player == 0:
#    print("You start first!")
#    userPhase = True
#else:
#    print("Computer starts first!")   
#    userPhase = False

#if userPhase:
#    player = "You"
#else:
#     player = "Computer"

#russian_roullete = random.randint(1, 6)
#round = 1



#while russian_roullete  !=1:
#            print(f"This is Round {round}. {player} are now spinning the cylinder...")
#            print(f"What a Miracle! {player} pull the trigger but nothing happens!")
#            round += 1
#            if player == "You" :
#               player = "Computer"
#            else:
#                 player = "You"
#            print(f"Now it's {player}!")
#            russian_roullete = random.randint(1, 6)
        
#else:
#        print(f"This is Round {round}. {player} is now spinning the cylinder...")
#        print(f"Oops! {player} died! Oh my god!")



import urllib.request
import json

url = "https://bored-api.appbrewery.com/random"

try:
    with urllib.request.urlopen(url) as response:
        raw_data = response.read().decode('utf-8')
        data = json.loads(raw_data)
        
        # Debugging step: see the whole dictionary
        # print(data) 
        
        # The Bored API has 'activity' at the top level
        activity = data['activity']
        print(f"I was bored, so the computer told me to: {activity}")

except Exception as e:
    print(f"Failed to get data: {e}")

