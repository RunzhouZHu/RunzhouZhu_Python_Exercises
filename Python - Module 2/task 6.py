import random

code1digit1 = str(random.randint(0, 9))
code1digit2 = str(random.randint(0, 9))
code1digit3 = str(random.randint(0, 9))
print(f"The 3-digit code is {code1digit1 + code1digit2 + code1digit3}")

code2digit1 = str(random.randint(1, 6))
code2digit2 = str(random.randint(1, 6))
code2digit3 = str(random.randint(1, 6))
code2digit4 = str(random.randint(1, 6))
print(f"The 3-digit code is {code2digit1 + code2digit2 + code2digit3 + code2digit4}")