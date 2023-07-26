#Fibonacci

first_number = 0
second_number = 1
temp_variable = 0

index = int(input("Put the index number that you want to run this program: "))

for i in range(0, index):
    temp_variable = first_number + second_number
    first_number = second_number
    second_number = temp_variable
    print(temp_variable)
