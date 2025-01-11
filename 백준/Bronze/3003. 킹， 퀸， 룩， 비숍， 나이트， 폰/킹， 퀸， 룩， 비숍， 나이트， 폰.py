k, q, l, b, n, p = map(int, input().split())

if k > 1:
    f_k = -(k - 1)
elif k == 1:
    f_k = 0
else:
    f_k = 1-k

if q > 1:
    f_q = -(q - 1)
elif q == 1:
    f_q = 0
else:
    f_q = 1-q

if l > 2:
    f_l = -(l - 2)
elif l == 2:
    f_l = 0
else:
    f_l = 2-l

if b > 2:
    f_b = -(b - 2)
elif b == 2:
    f_b = 0
else:
    f_b = 2-b

if n > 2:
    f_n = -(n - 2)
elif n == 2:
    f_n = 0
else:
    f_n = 2-n

if p > 8:
    f_p = -(p - 8)
elif p == 8:
    f_p = 0
else:
    f_p = 8-p

print(f_k, f_q, f_l, f_b, f_n, f_p)