s = [6,11,96,16,400,253,109,38,46]
print('Hello,my name is Ha and these are my sheep sizes:',s)

for i in range(3):
    print('MONTH',i+1,':')
    s2 = [50,50,50,50,50,50,50,50,50]
    s = [x+y for x,y in zip(s,s2)]
    print('One month has pass, now here is my flock',s)
    max = s[0]
    for a in s:
        if a > max:
            max = a
    print('Now my biggest sheep has the size',max,"Let's shear it")
    s.insert(s.index(max),8)
    s.pop(s.index(max))
    print('After shearing, here is my flock',s)

    print('My has size in total:',sum(s))
    print('I would get',sum(s),'* 2$ =',sum(s)*2,'\b$')
    