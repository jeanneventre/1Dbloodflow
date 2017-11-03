k=k+1
plot[][-0.01:0.01] 'Q.txt' i k
replot 'Q2.txt' i k
#pause 1
if(k<999) reread
