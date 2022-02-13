conv_type = 0 #sets the type of conversion 1 for binary, 2 for decimal
value = 0 #value from user input
binary = [] #sets up list for decimal to binary converter

#asks user whether they want to convert from binary to decimal or vice versa
def ask_user_choice():
    while True:
        try:    
            user_choice = int(input(("What conversion do you want to run?\n1: binary to decimal\n2: decimal to binary\nPlease enter number of your choice: ")))
            if user_choice != 1 and user_choice != 2:
                print("Please enter 1 or 2 to make your choice\n")
                continue
            break
        except ValueError:
            print("Please enter number\n")
    return user_choice
    
#gets number and checks if its binary      
def get_binary_in():
    while True:
        bin_input = input("Enter binary number: ")
        try:
            int(bin_input,2)
            break
        except ValueError:
            print("Please enter binary number")
    return bin_input

#gets number and checks if its positive integer                 
def get_decimal_in():
    while True:
        dec_input = input("Enter decimal number: ")
        try:
            value = int(dec_input)
            if value <= 0:
                print("Please enter positive integer")
                continue
            break
        except ValueError:
            print("Please enter number")
    return value

#function converts binary number to decimal number
def bin_to_dec(binary_num):
    binary_num = str(binary_num) #converts integer to string, for purpose of using len in next step
    decimal = 0
    for i in reversed(range(len(binary_num))):
        decimal = int(binary_num[-(i+1)])*(2**i) + decimal
    return decimal

#function converts decimal number to binary number
def dec_to_bin(decimal_num):
    while decimal_num > 0:
        residue = decimal_num%2
        decimal_num = decimal_num//2
        binary.append(residue)
    binary.reverse()
    return "".join(map(str,binary))

#function that decides what type of converter to run
def run_converter(choice):
    if choice == 1:
        value = get_binary_in() #calls function for binary input
        print(f"Your decimal number is: {bin_to_dec(value)}") #calls and prints binary to decimal converter
    if choice == 2:
        value = get_decimal_in() #calls function for decimal input
        print(f"Your binary number is: {dec_to_bin(value)}") #calls and prints binary to decimal converter

#defines type of conversion
conv_type = ask_user_choice()

#runs type of converter according tu users choice
run_converter(conv_type)