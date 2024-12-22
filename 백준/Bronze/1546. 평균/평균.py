n=int(input())
score=list(map(int, input().split()))
max_score=max(score)

fix_score= [(x/max_score)*100 for x in score]

print(sum(fix_score)/n)