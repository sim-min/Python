digits = list(map(int, input()))

for i in range(len(digits)-1, 0, -1):
    if digits[i] >= 5:
        digits[i-1] += 1  
    digits[i] = 0
    if digits[0] == 10:
        digits[0] = 0
        digits = [1] + digits
print("".join(map(str, digits)))      