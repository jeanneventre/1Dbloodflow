fin = 100

plot [][0:1] 'Q_NH_amp0_0001.txt' i fin title "amp=0.0001" pointsize 2 pointtype 1 

set title "Flow in an hyperelastic artery" font "Helvetica,Normal, 24"
set ylabel "Q/Q0" font "Helvetica,Normal,20"
set xlabel "x" font "Helvetica,Normal, 20"

replot 'Q_NH_amp0_001.txt' i fin title "amp=0.001" pointsize 2 pointtype 1
replot 'Q_NH_amp0_01.txt' i fin title "amp=0.01" pointsize 2 pointtype 1
replot 'Q_NH_amp0_1.txt' i fin title "amp=0.1" pointsize 2 pointtype 1
replot 'Q_NH_amp1.txt' i fin title "amp=1" pointsize 2 pointtype 1
replot 'Q_NH_amp1_5.txt' i fin title "amp=1.5" pointsize 2 pointtype 1

#set terminal postscript eps enhanced color font 'Helvetica,20'
#set output 'Q_NHt1.eps'

#replot