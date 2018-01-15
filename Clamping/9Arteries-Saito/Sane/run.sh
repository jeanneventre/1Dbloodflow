#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Sane
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "5e4" ; do 
      for E in 0.4e7 0.45e7 0.5e7 ;do 
        for Rt in 0.5 0.55 0.6 0.65 0.7; do
          for Q in 400 425 450 500 ; do
            for P1 in 0.3 0.325 0.35 0.375 ; do
              for Nx in 10 ; do #3 7   
                for xOrder in 2 ; do
                  for dt in 1e-4 ; do
                    for tOrder in 2 ; do
                      for solver in "KIN_HAT"; do
                        for HR in HRQ; do
                         
                          export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/E=${E}/Rt=${Rt}/Q=${Q}/P1=${P1}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                           python3 writeParameter.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -k ${E} -w ${Rt} -t ${Q} --P1 ${P1} #-m ${phi} -n ${Cv} 
                           bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                           python2.7 write.py -p ${HOME}${folderHR}/
                           # python3 plot.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -k ${E} -w ${Rt} -t ${Q} --P1 ${P1}  #-m ${phi} -n ${Cv} 
                           # python3 min.py 

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
          done
        done
      done
    done
  done 
done
