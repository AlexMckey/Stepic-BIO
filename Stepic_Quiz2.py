﻿from string import maketrans
fr = open("step_q2.txt",'r')
fw = open("step_q2.res.txt",'w')
#fr = open("rosalind_rna.sample.txt",'r')
#fw = open("rosalind_rna.sample.res.txt",'w')

st = fr.read().strip()
#st = 'AAAACCCGGT'
intbl 	= 'atcgATCG'
outtbl 	= 'tagcTAGC'
trtbl	= maketrans(intbl,outtbl)

sr = (st[::-1]).translate(trtbl)
fw.write(sr)
print st
print sr

fr.close()
fw.close()