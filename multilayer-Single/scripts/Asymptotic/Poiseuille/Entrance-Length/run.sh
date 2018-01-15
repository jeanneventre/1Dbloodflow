#!/bin/bash

export folderGeneral=/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Poiseuille/Entrance-Length

for K in 1e6 1e7 1e8 ; do
  folderK=${folderGeneral}/K=${K}
  for Re in 100 ; do
    folderRe=${folderK}/Re=${Re}
    for U in 100 ; do
      export folderU=${folderRe}/U=${U}
      for L in 25 ; do
        export folderL=${folderU}/Length=${L}
        for la in 32 ; do
          for Raf in 0 ; do
            for J in 800 ; do
              for HR in HRQ ; do
                for Order in 1 ; do
                  for solver in KIN_HAT; do
                    export folderHR=${folderL}/L=${la}/Raf=${Raf}/J=${J}/${HR}/Order=${Order}/${solver}

                    # python2.7 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${la} -r ${Raf} -j ${J} -o ${Order} -k ${K} -u ${U} -e ${Re} -d ${L}
                    # multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                    # python2.7 write.py -p ${HOME}${folderHR}/ -u ${U} -r ${Re}

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
done
