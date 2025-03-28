# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            # Collaborator1 enter Code For ADD here
	          # Include your Name/ID/Date in comments
 	          print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            # Collaborator2 enter Code For SUBTRACT here
	          # Include your Name/ID/Date in comments
            #
        elif choice == '3':
            # Collaborator3 enter Code For MULTIPLY here
	          # Include your Name/ID/Date in comments
            #
        elif choice == '4':
            # Collaborator4 enter Code For DIVIDE here
	          # Include your Name/ID/Date in comments
            # 
          
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
