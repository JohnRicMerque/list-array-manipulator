# Seatwork 2 - DSA
# Merque, John Ric | BSCOE 2-6

# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array

Array = [2, 21, 7, 140, 80, 92, 12, 119, 350, 43]

def main():
    print(f'Array: {Array}')
    print("Menu:")
    print(" 1 -> Add an element")
    print(" 2 -> Insert an element")
    print(" 3 -> Modify an element")
    print(" 4 -> Delete an element")
    print(" 5 -> Arrange in ascending order")
    print(" 6 -> Arrange in descending order")
    methodIndex = input("What do you want to do? (1-6): ")
    manipulateArray(methodIndex)

def manipulateArray (method_index):
    match method_index:
        case "1":
            appendValue = int(input("Enter the value you want to add: "))
            Array.append(appendValue)
            print("The value has been added")
            print(f"This is the new Array: {Array}")
            return
        case "2":
            insertIndex = int(input("Enter the index you want to insert to: "))
            insertValue = int(input("Enter value:"))
            Array.insert(insertIndex, insertValue)
            print(f"This is the new Array: {Array}")
            return
        case _:
            return "Something's wrong with the internet"

def continueArrayManipulation():
    continueCondition = input("Do you wish to continue manipulating the array? (y/n): ")
    if continueCondition == "y":
        main()
    else: 
        print("Thank you user! Here's your final array:")
        print(Array)

    
# program start
main()
continueArrayManipulation()









