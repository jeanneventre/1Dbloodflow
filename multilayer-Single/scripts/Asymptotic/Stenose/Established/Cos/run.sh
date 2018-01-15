#!/bin/bash

# export OMP_NUM_THREADS=27
# echo "OMP_NUM_THREADS=" $OMP_NUM_THREADS

export folderGeneral=/Documents/Boulot/Thèse/multilayerSingle/Examples/Well-Balance/Asymptotic/Stenose/Established/Cos/Rvar

for K in 1e7; do
  folderK=${folderGeneral}/K=${K}

  for Re in 100 500 1000; do
    folderRe=${folderK}/Re=${Re}
    for U in 100 ; do
      export folderU=${folderRe}/U=${U}
      for L in 25 ; do
        export folderL=${folderU}/Length=${L}
        for dR in -0.4; do
          export folderdR=${folderL}/dR=${dR}
          for Lst in 10 ; do
            export folderLst=${folderdR}/Lst=${Lst}
            for la in 32 ; do
              for Raf in 0 ; do
                for J in 1600 ; do
                  for HR in HRQ ; do
                    for Order in 1 ; do
                      for solver in KIN_HAT; do
                        export folderHR=${folderLst}/L=${la}/Raf=${Raf}/J=${J}/${HR}/Order=${Order}/${solver}

                          python3 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${la} -r ${Raf} -j ${J} -o ${Order} -k ${K} -u ${U} -e ${Re} -d ${L} -t ${dR} -w ${Lst}
                          # multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                          # python2.7 write.py -p ${HOME}${folderHR}/ -r ${Re}

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
