#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Test/Phase_nuv
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "5e4" "10e4" "15e4" "20e4" "25e4" "30e4" "35e4" ; do  
      for Q in 300 ; do
        for P1 in 0.5 ; do 
          for R2 in 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000; do
            for C in 1e-6; do
              for Nx in 10 ; do #3 7   
                for xOrder in 2 ; do
                  for dt in 1e-4 ; do
                    for tOrder in 2 ; do
                      for solver in "KIN_HAT"; do
                        for HR in HRQ; do
                           
                          export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/Q=${Q}/P1=${P1}/R2=${R2}/C=${C}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                           # python3 writeParameter3.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} --P2 ${R2} -x ${C} #  --P1 ${R1} --P2 ${R2}  #-m ${phi} -n ${Cv} 
                           # bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                           # python2.7 write.py -p ${HOME}${folderHR}/
                           # python3 plot.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} --P2 ${R2} -x ${C} #-x ${C} --P1 ${R1} --P2 ${R2}  #-m ${phi} -n ${Cv} 
                          
                           # python3 puissance.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -x ${C} --P1 ${R1} --P2 ${R2}  #-m ${phi} -n ${Cv} 
                            
                            # mkdir -p ${HOME}${folderHR}/Figures
                            # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                            # mkdir -p ${HOME}${folderHR}/Figures         
                            # scp -r -P 2222 ghigo@localhost:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                        done
                      done
                    done 
                  done
                done
              done 
            done 
            # python3 phase.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} --P2 ${R2} -x ${C} 
          done 
        done
      done
      # python3 phase2.py -a ${HOME}${folderHR}/ -b Sane -nc ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} --P2 ${R2} -x ${C}
    done
  done 
done
# python3 min.py 
python3 plotPhase.py
