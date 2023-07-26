def str_length(input_string):
    reversed_string = ''
    for i in input_string:
        reversed_string = i + reversed_string
    return reversed_string

input_string = str(input("Provide your string for count: "))

str_reverse = str_length(input_string)

print("The length of the given string is: ", str_reverse)