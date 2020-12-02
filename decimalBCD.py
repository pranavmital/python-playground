#convert decimal numbers to BCD
#Pranav Mital

mapping = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001'}

usr_input = str(input("Please enter a decimal number: "))
output = ''

for i in usr_input:
    output += mapping[int(i)] + ' '

print(output)
