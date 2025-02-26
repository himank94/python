lis=['a','b','c','d']
lis1=['himank',19,170,'mittal']
dctnry={}
for i in lis:
    dctnry.update({i:lis1[lis.index(i)]})
print(dctnry)