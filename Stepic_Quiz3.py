fr = open('step_q3.txt','r')
fw = open('step_q3.res.txt','w')
p = fr.readline().strip()
g = fr.readline().strip()
o = []
lg = len(g)
lp = len(p)
for i in range(0,lg-lp+1):
    if p == g[i:i+lp]:
    	o.append(i)
fw.write(' '.join(map(str,o)))
print ' '.join(map(str,o))
fr.close()
fw.close()