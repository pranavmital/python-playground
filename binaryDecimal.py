#convert binary to decimal
#Pranav Mital

usr_input = str(input("Please enter a binary number: "))

for i in usr_input:
    if (int(i) != 0) and (int(i) != 1):
        print("Number entered is not binary. Please try again.")
        exit()

converted_rev = list(usr_input)[::-1]
decimal_num = 0

for i in range(len(converted_rev)):
    decimal_num += (int(converted_rev[i]) * 2**int(i))

print(decimal_num)
