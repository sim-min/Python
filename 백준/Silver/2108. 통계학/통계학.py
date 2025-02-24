import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]
dict_key = {}
for i in(num_list):
    try:
        dict_key[i] += 1
    except:
        dict_key[i] = 1

# 산술 평균
mean = round(sum(num_list)/len(num_list))
print(mean)
# 중앙값
sort_num_list = sorted(num_list)
mid = sort_num_list[int(len(sort_num_list)/2)]
print(mid)
# 최빈값
find_max = max(list(dict_key.values()))
max_value = [k for k, v in dict_key.items()if v == find_max]
if len(max_value) > 1:
    print(sorted(max_value)[1])
else:
    print(sorted(max_value)[0])
# 범위
rangee = max(num_list) - min(num_list)
print(rangee)