fin = 159

plot [][0:1] 'Q_elastic2_amp0_0001.txt' i 120 title "amp=0.0001" pointsize 2 pointtype 1 

set title "Flow in an elastic artery"
set ylabel "Q/Q0" 
set xlabel "x"

replot 'Q_elastic2_amp0_001.txt' i 120 title "amp=0.001" pointsize 2 pointtype 1
replot 'Q_elastic2_amp0_01.txt' i 120 title "amp=0.01" pointsize 2 pointtype 1
replot 'Q_elastic2_amp0_1.txt' i 120title "amp=0.1" pointsize 2 pointtype 1
replot 'Q_elastic2_amp1.txt' i 120 title "amp=1" pointsize 2 pointtype 1

set term postscript eps enhanced color 
#set term png
set output "Q.eps"