def str_length(input_string):
    len_count = 0
    for i in input_string:
        len_count = len_count + 1

    return len_count

input_string = str(input("Provide your string for count: "))

str_len = str_length(input_string)

print("The length of the given string is: ", str_len)