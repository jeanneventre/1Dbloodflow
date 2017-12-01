set key
plot [][] 'A_remp_Varga_P0.txt' i 100 title "Q0 = 0" pointsize 1 pointtype 1 linecolor rgb "#ff0000"

set title "Q = Q0 + dQ * sin²(2*pi*w*t)" font "Helvetica,Normal, 24"
set ylabel "error" font "Helvetica,Normal,20"
set xlabel "dx" font "Helvetica,Normal, 20"

replot 'A_remp_Varga_P0.txt' i 200 title "Q0 = 0" pointsize 1 pointtype 1 linecolor rgb "#FF0000"
replot 'A_remp_Varga_P0.txt' i 300 title "Q0 = 0" pointsize 1 pointtype 1 linecolor rgb "#FF0000"
replot 'A_remp_Varga_P0.txt' i 400 title "Q0 = 0" pointsize 1 pointtype 1 linecolor rgb "#FF0000"
replot 'A_remp_Varga_P0.txt' i 500 title "Q0 = 0" pointsize 1 pointtype 1 linecolor rgb "#FF0000"
replot 'A_remp_Varga_P0.txt' i 600 title "Q0 = 0" pointsize 1 pointtype 1 linecolor rgb "#FF0000"

#replot 'A_remplissage.txt' i 100 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#0000FF"
#replot 'A_remplissage.txt' i 200 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#0000FF"
#replot 'A_remplissage.txt' i 300 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#0000FF"
#replot 'A_remplissage.txt' i 400 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#0000FF"
#replot 'A_remplissage.txt' i 500 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#0000FF"
#replot 'A_remplissage.txt' i 600 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#0000FF"

#replot 'A_remplissage_Varga_P5.txt' i 100 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#00FF00"
#replot 'A_remplissage_Varga_P5.txt' i 200 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#00FF00"
#replot 'A_remplissage_Varga_P5.txt' i 300 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#00FF00"
#replot 'A_remplissage_Varga_P5.txt' i 400 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#00FF00"
#replot 'A_remplissage_Varga_P5.txt' i 500 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#00FF00"
#replot 'A_remplissage_Varga_P5.txt' i 600 title "Q0 = 0.0001" pointsize 1 pointtype 1 linecolor rgb "#00FF00"


#set terminal postscript eps enhanced color font 'Helvetica,20'
#set output 'err_Nx.eps'
#replot