fr = open('E-coli.txt','r')
fw = open('E-coli.res.txt','w')
g = fr.readline().strip()
#p = fr.readline().strip().split()
k = 9
l = 500
t = 3
o = []
for i in range(0,len(g)-k-l+1):
    r = g[i:i+k]
    if g[i:i+l].count(r) >= t:
    	o.append(r)
fw.write(' '.join(map(str,set(o))))
print ' '.join(map(str,set(o)))
print len(o)
print len(set(o))
fr.close()
fw.close()