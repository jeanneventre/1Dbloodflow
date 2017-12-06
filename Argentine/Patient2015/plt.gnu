plot 'Patient11_moyen.txt' us 1:4 title "Patient 11" pointsize 2 pointtype 1 

set title "Mean pressure over a cycle for right-popliteal clamps" font "Helvetica,Normal, 24"
set ylabel "Pressure" font "Helvetica,Normal,20"
set xlabel "time" font "Helvetica,Normal, 20"

#replot 'Patient07_moyen.txt' us 1:2 title "Patient 7" pointsize 2 pointtype 1 
#replot 'Patient09_moyen.txt' us 1:2 title "Patient 9" pointsize 2 pointtype 1
#replot 'Patient11_moyen.txt' us 1:2 title "Patient 11" pointsize 2 pointtype 1
#replot 'Patient15_moyen.txt' us 1:4 title "Patient 14" pointsize 2 pointtype 1
#replot 'Patient16_moyen.txt' us 1:4 title "Patient 16" pointsize 2 pointtype 1
#replot 'Patient17_moyen.txt' us 1:2 title "Patient 17" pointsize 2 pointtype 1


set terminal postscript eps enhanced color font 'Helvetica,20'
set output 'Right_Popliteal.eps'
replot
reset
set term x11