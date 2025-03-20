nums = list(map(int, input().split()))
i = min(nums)

while True:
    cnt = 0
    i += 1
    for j in nums:
        if i%j == 0:
            cnt += 1
    if cnt >= 3:
        break
print(i)