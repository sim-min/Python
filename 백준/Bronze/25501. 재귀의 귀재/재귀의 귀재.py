S = []
for i in range(int(input())):
    S.append(input())


def recursion(s, l, r, cnt):
    cnt[0] += 1

    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else:
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    cnt = [0]
    return recursion(s, 0, len(s)-1, cnt), cnt[0]

for i in S:
    print(" ".join(map(str ,isPalindrome(i))))