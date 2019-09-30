from cards import *
ntrials = 1000
alist=[]
ptrials = 28
for i in range(ntrials):
    adeck=deck()
    bdeck=deck()
    adeck.shuffle()
    bdeck.shuffle()
    p1=0
    p2=0
    while adeck.cardsleft() >0:
        ccard=adeck.dealcard()
        dcard=bdeck.dealcard()
        if ccard.value() > dcard.value() :
            p1+= 2
        if dcard.value() > ccard.value() :
            p2 += 2
        if ccard.value() == dcard.value() :
            p1 +=1
            p2 +=1
    p1 = abs(p1-52)
    alist.append(p1)
for i in range(27):
    print( i*2,alist.count(i*2)/ntrials)
    
