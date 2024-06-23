n=int(input())
s=map(int,input().split())
ban=True
for i in s:
    if i==1:
        print("HARD")
        ban=False
        break
if ban:
    print("EASY")