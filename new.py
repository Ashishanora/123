
def climbingLeaderboard(ranked, player):
    dict=[]
    temp=ranked[0]
    key=1
    dict[key]=ranked[0]
    for i in range(len(ranked)):
        if temp>ranked[i]:
            key+=1
            temp=ranked[i]
            dict[key]=ranked[i]
        
            