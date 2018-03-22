#set key

plot '7aorta_pre.txt' us 1:2 title "Pre Clamp " pointsize 2 pointtype 1 linecolor rgb "red"

f(x) = a
fit f(x) '7aorta_pre.txt' us 1:2 via a

replot f(x) title "Pre clamp mean value" lt 1 lw 3 linecolor rgb "red"

set title "Mean beat pressure over a cycle for Patient 7" font "Helvetica,Normal, 24"
set ylabel "Pressure (mmHg)" font "Helvetica,Normal,20"
set xlabel "Time (s)" font "Helvetica,Normal, 20"

replot '7aorta_post.txt' us 1:2 title "Post Clamp" pointsize 2 pointtype 2 linecolor rgb "blue"

g(x) = b
fit g(x) '7aorta_post.txt' us 1:2 via b

replot g(x) title "Post clamp mean value" lt 1 lw 3 linecolor rgb "blue"

set terminal postscript eps enhanced color font 'Helvetica,20'
set output 'Patient7.eps'
replot
reset
set term x11