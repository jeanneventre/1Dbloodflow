#!/bin/bash

export OMP_NUM_THREADS=27
# echo "OMP_NUM_THREADS=" $OMP_NUM_THREADS

export folderGeneral=/Documents/Boulot/Thèse/multilayer-Single/Example/Well-Balance/Asymptotic/Stenose/Pulsed/Cos/Rvar

for K in 1e5; do
  for Re in 100 ; do
    for a in 15 ; do
      for Sh in 1e-2 ; do
        for L in 25 ; do
          for dR in -0.4 ; do
            for Lst in 10 ; do
              for Rt in 0; do
                for la in 5 ; do
                  for Raf in 0 ; do
                    for J in 3200 ; do
                      for HR in HRQ ; do
                        for Order in 1 ; do
                          for solver in KIN_HAT; do
                            export folderHR=${folderGeneral}/K=${K}/Re=${Re}/a=${a}/L=${la}/Sh=${Sh}/Length=${L}/dR=${dR}/Lst=${Lst}/Rt=${Rt}/Raf=${Raf}/J=${J}/${HR}/Order=${Order}/${solver}

                              python3 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${la} -r ${Raf} -j ${J} -o ${Order} -k ${K} -e ${Re} -a ${a} -f ${Sh} -d ${L} -t ${dR} -w ${Lst} -b ${Rt}
                              multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                              # python2.7 write.py -p ${HOME}${folderHR}/

                              # export folderHR=${folderLst}/L=${la}/Raf=${Raf}/J=${J}/${HR}/Order=${Order}/${solver}
                              # python2.7 plot.py -p ${HOME}${folderHR}/

                              # mkdir -p ${HOME}${folderHR}/Figures
                              # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                              # mkdir -p ${HOME}${folderHR}/movies
                              # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/movies ${HOME}${folderHR}/

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
        done
      done
    done
  done
done
