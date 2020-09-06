# Manual addition of two two-digit numbers
# Considering a hypothetical case in which Python is only capable of adding one-digit numbers
# Pranav Mital

temp_sum = 0
carry = 0
sum1 = 0 # one's place of sum
sum2 = 0 # remaining sum

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# computing one's place

temp_sum = num1%10 + num2%10
if temp_sum > 9:
    carry = int(str(temp_sum)[0])
    sum1 = int(str(temp_sum)[1])
else:
    sum1 = temp_sum

print("\nOne's place is:",sum1)
print("Carry is:",carry,"\n")

# computing remaining sum

temp_sum = ((num1 - num1%10)//10) + ((num2 - num2%10)//10) + carry
sum2 = temp_sum

if sum2 == 0:
    sum2 = '' # incase of one digit addition this will ensure cleaner output

print("The manually computed sum is: "+str(sum2)+str(sum1))



