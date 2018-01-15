#!/bin/bash

# export OMP_NUM_THREADS=3
# echo "OMP_NUM_THREADS=" ${OMP_NUM_THREADS}

export folderGeneral=/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Womersley/T_12

  for wom in 5 ; do
		export folderWom=${folderGeneral}/a=${wom}

    for K in 1.e4 ; do
      for dR in 1e-3; do
        for la in 128 ; do
          for Raf in 0 ; do
            for J in 1600 ; do
              for Order in 1 ; do
                for HR in HRQ; do
                  for solver in KIN_HAT; do

                    export folderHR=${folderWom}/K=${K}/dR=${dR}/L=${la}/Raf=${Raf}/J=${J}/${HR}/Order=${Order}/${solver}

                    # python2.7 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${la} -r ${Raf} -j ${J} -o ${Order} -k ${K} -d ${dR} -w ${wom}
                    # multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                    # python2.7 write.py -p ${HOME}${folderHR}/

                    python2.7 plot.py -p ${HOME}${folderHR}/

                    # mkdir -p ${HOME}${folderHR}/Figures
                    # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                    # mkdir -p ${HOME}${folderHR}/movies
                    # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/movies ${HOME}${folderHR}/

                    # ssh -f -N -L 2222:${ACCOUNT}:22 ${SSHCHAGALL}
                    # mkdir -p ${HOME}${folderHR}/Figures
                    # scp -r -P 2222 ghigo@localhost:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                    # mkdir -p ${HOME}${folderHR}/Movies
                    # scp -r -P 2222 ghigo@localhost:${HOME_SSH}${folderHR}/Movies ${HOME}${folderHR}/

                  done
                done
              done
            done
				  done
        done
      done
    done
  done
