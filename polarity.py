from textblob import TextBlob



fp = open("clean.txt","r")
f2 = open("hate.txt","r")


line = fp.readline()
line2 = f2.readline()
op = []
ip = []
op1 = []
ip1 = []

i=0
while line:
    ip1.append(line2)
    ip.append(line)
    op1.append((TextBlob(line).sentiment))
    op.append((TextBlob(line).sentiment))
    line = fp.readline()
    line2 = f2.readline()

    
fp1 = open('abc.txt','w')
fp2 = open('abc2.txt','w')
fp1.seek(0)
for i in range(len(op)) 	:
	fp1.write(str(ip[i]))	
        fp1.write(str(op[i]))
	fp1.write("\n\n")
	fp2.write(str(ip1[i]))
	fp2.write(str(op1[i]))
	fp2.write("\n\n")



