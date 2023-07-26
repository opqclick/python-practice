# Collect numbers, and make list

def collectNumbers(total_numbers):
    print("Enter", total_numbers, "numbers:")
    for i in range(0, total_numbers):
        ele = float(input())
        my_list.append(ele)


def calculateAverage():
    total = 0
    for i in range(0, len(my_list)):
        total = total + my_list[i]
    return total / total_numbers


my_list = []
total_numbers = int(input("Average of how many numbers? "))

collectNumbers(total_numbers)  # Calling function to create list

average = calculateAverage()  # Calling function to calculate average
print("The average is: ", average)
