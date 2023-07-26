#swapping numbers without a temporary variable

num1 = 10
num2 = 25

if num1 < num2:
     print("Before swap", num1, num2)

     num2 = num2 + num1 #35
     num1 = num2 - num1 #25
     num2 = num2 - num1 #10

     print("After swap", num1, num2)

else:
    print("Before swap", num1, num2)

    num1 = num1 + num2  # 35
    num2 = num1 - num2  # 10
    num1 = num1 - num2  # 25

    print("After swap", num1, num2)

