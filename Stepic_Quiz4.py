fr = open('step_q4.txt','r')
fw = open('step_q4.res.txt','w')
g = fr.readline().strip()
p = fr.readline().strip().split()
k = int(p[0])
l = int(p[1])
t = int(p[2])
o = []
for i in range(0,len(g)-k+1):
    r = g[i:i+k]
    if g[i:i+l].count(r) >= t:
    	o.append(r)
fw.write(' '.join(map(str,set(o))))
print ' '.join(map(str,set(o)))
fr.close()
fw.close()