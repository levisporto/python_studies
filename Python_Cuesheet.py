# comment like this
print("Hello " + "world!")
# math is just like other programming languages
print(50/2)

# Primitive Data Type: Fixed size, predetermined by the programming language: string, integers, true/false (e.g., integer always takes 4 bytes). 
# Non-Primitive: Variable size, depending on the complexity of the data they hold

# Logical operators and booleans: not / and / true / false / or / if / else / elif
if(5 > 2 or 3 < 4):
    print("Condition is True")   
elif (100 == 101): 
    print("Condition is False")
else:
    print("Condition is False too")

#For loop (also using a f-string, a Formatted String Literal)
numbers = [1, 2, 3]
for num in numbers:
    print(f"Lets count using a for loop: {num}...")

# You can use format() to interpolate formatted strings
print("Lets count using a for loop: {}".format(num))
# Match-case statement (like switch-case in Javascript)
num = 1
match num:
    case 1:
        print("Your number is one")
    case 2 | 3:  # multiple options (OR pattern)
        print("Your number is two OR three")
    case code if num.isdigit():  # conditional
        print(f"The robot execute code: {code}")
    case _:  # _ is a wildcard that never fails (like default/else)
        print("Invalid number ❌")


# Comparison operators: < / > / == / != / <= / >=
#Bool is used to represent true/false values
x = bool(1)
y = bool(0)
z = bool(1==2)
print(x)    
print(y)    
print(z)        

#This is a Python list (non-primitive data type). If you want it immutable, use tuples (tup), if you would like to add or remove items use Sets (set)
a = [1, 2, 3, 4]
#append() adds an element to the end of the list
a.append(5)  
print(a)
#pop() removes the last element from the list
a.pop()
#::-1 for reverse order
print(a[::-1])
#1:3 for slicing the list
print(a[1:3])
#insert an element in the list. must specify index
viado = ["gay"]
viado.insert(1, "hehe")
#remove an element of the list
viado.remove("gay")
print(viado)
#you can concatenate lists
viado.extend(a)
print(viado)





#Dictionaries are used to store data values in key:value pairs
myDict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(myDict["name"])


#Len is a function to find the length
print(len("how many characters in this phrase?"))
s = "you can concatenate strings"
print("now see this: " + s)
#Can also be done with f-string and formatted string literals
print(f"now see this: {s}")

# input() function to capture user input
userInput = input("Enter and I will echo: ") 
print("You entered: " + userInput)
