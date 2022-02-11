binary = "100101"
decimal = 0


for i in reversed(range(len(binary))):
    decimal = int(binary[-(i+1)])*(2**i) + decimal
print(decimal)
    
