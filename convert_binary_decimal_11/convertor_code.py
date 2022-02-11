binary_input = "111001010"
binary = ""
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
    
