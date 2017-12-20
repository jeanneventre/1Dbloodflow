#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Sane
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "5e4" ; do # "1e4" "3e4" "5e4" "6e4" 
      for E in 0.45e7 ;do # 0.6e7 0.8e7 0.9e7 1e7 0.7e7 # 0.25e7 0.3e7 0.35e7 0.4e7 0.45e7 0.55e7 
        for Rt in 0.55  ; do #0 0.8 1  0.5 0.7 0.8  0.2 0.3 0.4 # 0.4 0.45 0.55 0.6 0.65 0.7 0.75 0.8
          for Nx in 5 ; do #3 7   
            for xOrder in 2 ; do
              for dt in 1e-4 ; do
                for tOrder in 2 ; do
                  for solver in "KIN_HAT"; do
                    for HR in HRQ; do
                     
                      export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/E=${E}/Rt=${Rt}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                       # python3 writeParameter.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -k ${E} -w ${Rt} #-m ${phi} -n ${Cv} 
                       # bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                       # python2.7 write.py -p ${HOME}${folderHR}/
                       python3 plot.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -k ${E} -w ${Rt} #-m ${phi} -n ${Cv} 
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
