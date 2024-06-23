y=int(input())
beautifulY=str(y+1)
while(True):
    if beautifulY[0]!=beautifulY[1] and beautifulY[0]!=beautifulY[2] and beautifulY[0]!=beautifulY[3] and beautifulY[1]!=beautifulY[2] and beautifulY[1]!=beautifulY[3] and beautifulY[2]!=beautifulY[3]:
        print(beautifulY)
        break
    beautifulY=str((int(beautifulY)+1))