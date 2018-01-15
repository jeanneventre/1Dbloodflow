#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Test
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "5e4" ; do 
      for Rt in 0.65 ;do 
        for C in 0; do 
          for Nx in 10 ; do #3 7   
            for xOrder in 2 ; do
              for dt in 1e-4 ; do
                for tOrder in 2 ; do
                  for solver in "KIN_HAT"; do
                    for HR in HRQ; do
                     
                      export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/Rt=${Rt}/C=${C}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                       python3 writeParameter3.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -w ${Rt} -x ${C} #-k ${E} -w ${Rt} -y ${dR} -z ${dK} #-m ${phi} -n ${Cv} 
                       bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                       python2.7 write.py -p ${HOME}${folderHR}/
                       # python3 plot.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -w ${Rt} -x ${C} #-t ${Q} -p1 ${P1}  #-m ${phi} -n ${Cv} 
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

