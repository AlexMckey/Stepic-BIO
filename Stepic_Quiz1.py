fr = open('step_q1.txt','r')
fw = open('step_q1.res.txt','w')
s = fr.readline().strip()
x = int(fr.readline().strip())
dict = {}
for i in range(0,len(s)-x+1):
    r = s[i:i+x]
    dict[r] = dict.get(r,0) + 1
m = max(dict.values())
l = map(lambda x: x[0],filter(lambda x: x[1] == m, dict.items()))
fw.write(' '.join(l))
print ' '.join(l)
fr.close()
fw.close()