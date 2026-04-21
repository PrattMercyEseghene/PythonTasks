failures = 1
sum = 0
while True:
    user_input = input("Enter number:")
    if user_input.lower() =='z':
        break
    number = int(user_input)

    if number != 1 and number != 2:
        failures+1
    else:
        sum = sum + failures
        print("the total sum is ", sum)
