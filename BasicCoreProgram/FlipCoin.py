import random
def FlipCoin():
    head = 0
    tail = 0
    headPercent = 0
    tailPercent = 0
    print("***head and tail*****")
    for i in range(1000):
        coin = random.randint(1,2)
        if coin==1:
            head+=1
        else:
            tail+=1
            
            headPercent = head / 10.0
            tailPercent = 100.0 - headPercent
            
            print("Heads Percent: " + str(headPercent))
            print("Tails Percent: " + str(tailPercent))
    FlipCoin()