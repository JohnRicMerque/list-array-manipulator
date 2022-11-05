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
    print(" 7 -> Revert to default array")
    print()
    methodIndex = input("What do you want to do? (1-7): ")
    manipulateArray(Array, methodIndex)
    print()
    
    continueCondition = input("Do you wish to continue manipulating the array? (y/n): ")
    if continueCondition == "y":
        main()
    else: 
        print("Thank you user! Here's your final array:")
        print(Array)


def manipulateArray(array, method_index):
    match method_index:
        case "1":
            appendElement = int(input("Enter the element you want to add: "))
            array.append(appendElement)
            print("The value has been added")
            print(f"\nThis is the new Array: {array}")
            return
        case "2":
            insertIndex = int(input("Enter the index you want to insert to: "))
            insertElement = int(input("Enter element:"))
            array.insert(insertIndex, insertElement)
            print(f"\nThis is the new Array: {array}")
        case "4":
            removeElement = int(input("Enter element you want to delete:"))
            array.remove(removeElement)
            print(f"\nThis is the new Array: {array}")
            return
        case "7":
            array = [2, 21, 7, 140, 80, 92, 12, 119, 350, 43]
            print(f"\nThis is the new Array: {array}")
            return
        
        case _:
            return "Something's wrong with the internet"

# program start
main()










