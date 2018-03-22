#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Test/PhaseQ_Tej
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "31e4" ; do  
      for Q in 200 250 300 350 400 450 500 550 600 650 700 ; do 
        for P1 in 0.25 0.3 0.35 0.36 0.38 0.4 0.42 0.45 0.48 0.5 0.52 0.55; do 
          for R2 in 5000 ; do
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
            # 
            done 
            # 
          done 
          # python3 phase.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} --P2 ${R2} -x ${C}
        done
        # python3 phase2.py -a ${HOME}${folderHR}/ -b Sane -nc ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} --P2 ${R2} -x ${C}
      done
    done
  done 
done
python3 plotPhase.py
