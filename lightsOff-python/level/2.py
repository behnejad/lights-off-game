'''
f = open("2.txt","r")
a=f.read()
#print a
f.close()
f1 = open('edit.txt','w')
for i in a:
    if (i != '\n' and i != ' ' and i != '\t'):
        f1.write(i)
f1.close()
'''

f = open('2.txt','r')
t = open('temp.txt','w')
a = f.read()

f.close()

for i in a:
    if (i == '1' or i == '0'):
        t.write(i)


t.close()
