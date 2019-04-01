from textblob import TextBlob
from collections import Counter
import operator

fp = open("clean.txt","r")

line = fp.readline()

op = []
op1 = []
ip1 = []
i=0

while line:
	line = line.rstrip()
        op.extend(line.split(" "))
        line = fp.readline()
c1 = Counter(op)
c1 = sorted(c1.items(), key=operator.itemgetter(1),reverse=True)

fp = open("hate.txt","r")
line = fp.readline()
        
while line:
	line = line.rstrip()
        op1.extend(line.split(" "))
        line = fp.readline()
c2 = Counter(op1)
c2 = sorted(c2.items(), key=operator.itemgetter(1),reverse=True)
	
fp = open('udictc.txt','w')
for ele in c1:
  fp.write(ele[0]+","+str(ele[1])+"\n")
fp.close()

fp = open('udicth.txt','w')
for ele in c2:
  fp.write(ele[0]+","+str(ele[1])+"\n")
fp.close()

print 'success !!!'
