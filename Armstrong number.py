num = int(input("Enter a number: "))
order = len(str(num))
sum_of_digits = sum(int(digit) ** order for digit in str(num))

if num == sum_of_digits:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
