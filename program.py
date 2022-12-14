# Seatwork 2 - DSA
# Merque, John Ric | BSCOE 2-6

# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array
def main():
    print(f'Array: {Array}')
    methodIndex = input("What do you want to do? (1-10): ")
    manipulateArray(Array, methodIndex)
    print()
    
    continueCondition = input("Do you wish to continue manipulating the same array? (y/n): ")
    if continueCondition == "y":
        main()
    else: 
        print("___________________________________________________")
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
            insertElement = int(input("Enter element: "))
            array.insert(insertIndex, insertElement)
            print(f"\nThis is the new Array: {array}")
            return

        case "3":
            modifyIndex = int(input("Enter the index you want to modify: "))
            modifyValue = int(input("Enter element: "))
            array[modifyIndex] = modifyValue
            print(f"\nThis is the new Array: {array}")
            return

        case "4":
            removeElement = int(input("Enter element you want to delete: "))
            array.remove(removeElement)
            print(f"\nThis is the new Array: {array}")
            return

        case "5":
            array.sort()
            print(f"\nThis is the new Array: {array}")
            return

        case "6":
            array.sort(reverse=True)
            print(f"\nThis is the new Array: {array}")
            return

        case "7":
            minimumValue = min(array)
            print(f"\nThe minimum value is: {minimumValue}")
            return
        
        case "8":
            maximumValue = max(array)
            print(f"\nThe maximum value is: {maximumValue}")
            return

        case "9":
            total = sum(array)
            print(f"\nThe sum of all values is: {total}")
            return

        case "10":
            array = [2, 21, 7, 140, 80, 92, 12, 119, 350, 43]
            print(f"\nAlright we're back to our default Array: {array}")
            return
        case _:
            print("Invalid Input. Please enter a number from 1-10.")
            return 

# program start
Array = [2, 21, 7, 140, 80, 92, 12, 119, 350, 43]
print(f"Array: {Array}")
print("Menu:")
print(" 1 -> Add an element")
print(" 2 -> Insert an element")
print(" 3 -> Modify an element")
print(" 4 -> Delete an element")
print(" 5 -> Arrange in ascending order")
print(" 6 -> Arrange in descending order")
print(" 7 -> Find the minimum value")
print(" 8 -> Find the maximum value")
print(" 9 -> Find the sum of all values")
print(" 10 -> Revert to default array")
print()

main()










