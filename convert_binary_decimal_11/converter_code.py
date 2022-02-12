binary_input = "111001010"
binary = ""


def ask_user_choice():
    while True:
        try:    
            user_choice = int(input(("What conversion do you want to run?\n1: binary to decimal\n2: decimal to binary\nPlease enter number of your choice:")))
            break
        except ValueError:
            print("Enter number 1 or 2 to make your choice:")
    if user_choice == 1:
        get_binary_in()
    if user_choice == 2:


#gets number and checks if its binary      
def get_binary_in():
    while True:
        try:
            bin_input = int(input("Enter binary number: "),2)
            break
        except ValueError:
            print('Number is not binary!')
    return bin_input
                
def get_decimal_in():
    


if binary_input[0]=="1":
    binary = binary_input[1:]
else:
    binary = binary_input
#function converts binary number to decimal number
def bin_to_dec(binary_num):
    decimal = 0
    for i in reversed(range(len(binary_num))):
        decimal = int(binary_num[-(i+1)])*(2**i) + decimal
    return decimal
print("-"+str(bin_to_dec(binary)))

decimal = "174"
decimal_num = int(decimal)
binary = []
binary_result = ""


    print(decimal_num//2)
    print(decimal_num%2)
    while decimal_num > 0:
        residue = decimal_num%2
        decimal_num = decimal_num//2
        binary.append(residue)
        print(residue,decimal_num)

binary.reverse()
print(binary)

    
