#!/bin/bash

#export OMP_NUM_THREADS=10
#echo "OMP_NUM_THREADS=" $OMP_NUM_THREADS

# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Asymptotic/Tourniquet/NonNewtonian
# MAC
# export 


for K in 1e4 ; do
  for NN in "NonNewtonian" ; do

    for dR in 1e-1 ; do

      for Nx in 100; do
        for xOrder in 2; do
          for dt in 1e-5 ; do
            for tOrder in 2 ; do
              for solver in "KIN_HAT"; do
                for HR in HRQ; do

                  export folderHR=${folderGeneral}/K=${K}/${NN}/dR=${dR}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                   python3 writeParameter.py -a ${HOME}${folderHR}/ -b Sane -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -k ${K} -l ${NN} -y ${dR}
                   bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                   python2.7 write.py -p ${HOME}${folderHR}/
		               #python3 plotPaper.py

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
