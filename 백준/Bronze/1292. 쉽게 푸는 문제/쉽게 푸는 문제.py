A, B =map(int, input().split())
nums = []
for i in range(1, 51):
    for j in range(i):
        nums.append(i)

ans = 0
for p in range(A, B+1):
    ans = ans+nums[p-1]
print(ans)