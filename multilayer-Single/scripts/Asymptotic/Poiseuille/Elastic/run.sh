#!/bin/bash

export folderGeneral=/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Elastic

for K in 1e2 ; do
  folderK=${folderGeneral}/K=${K}
  for Sh in 1e-1 ; do
    folderSh=${folderK}/Sh=${Sh}
    for L in 10 ; do
      export folderL=${folderSh}/Length=${L}
      for la in 8 ; do
        for Raf in 0 ; do
          for J in 100  ; do
            for HR in HRQ ; do
              for Order in 1 ; do
                for solver in KIN_HAT; do
                  export folderHR=${folderL}/L=${la}/Raf=${Raf}/J=${J}/${HR}/Order=${Order}/${solver}

                  # python2.7 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${la} -r ${Raf} -j ${J} -o ${Order} -k ${K} -f ${Sh} -d ${L}
                  # multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                  # python2.7 write.py -p ${HOME}${folderHR}/

                  # mkdir -p ${HOME}${folderHR}/Figures
                  # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                  # ssh -f -N -L 2222:${ACCOUNT}:22 ${SSHCHAGALL}
                  mkdir -p ${HOME}${folderHR}/Figures
                  scp -r -P 2222 ghigo@localhost:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                done
              done
            done
          done
        done
      done
    done
  done
done
