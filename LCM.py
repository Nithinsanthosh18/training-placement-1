import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = abs(a * b) // math.gcd(a, b)
print("LCM:", lcm)
