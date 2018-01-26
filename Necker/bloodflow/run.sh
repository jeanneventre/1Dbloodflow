#!/bin/bash

# export OMP_NUM_THREADS=27
# echo "OMP_NUM_THREADS=" $OMP_NUM_THREADS

export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Necker


for NN in "Newtonian" ; do
  for nuv in "5e4" ; do 
    for P1 in 50000 ; do 
      for Nx in 200 ; do
        for xOrder in 2 ; do
          for dt in 1e-5 ; do
            for tOrder in 2 ; do
              for solver in "KIN_HAT"; do
                for HR in HRQ; do

                  export folderHR=${folderGeneral}/${NN}/nuv=${nuv}/P1=${P1}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                  # python3 writeParameter.py -a ${HOME}${folderHR}/ -b Sane -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} --P1 ${P1}
                  # bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                  python2.7 write.py -p ${HOME}${folderHR}/

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
