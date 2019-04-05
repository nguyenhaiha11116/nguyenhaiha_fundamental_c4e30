cau = {}
TEXT = str(input('Enter: '))
text = TEXT.lower()
bangchucai = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in bangchucai:
    cau[i] = text.count(i,0,100)
    if cau[i]==0:
        del cau[i]
for v in cau:
    print(v,cau[v])    
