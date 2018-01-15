#!/bin/bash

export folderGeneral=/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Effects/NonlinearElastic

for dR in 1e-1 ; do
  for K in 1e4 ; do
    for Knl in 0 1e3; do

      for Nr in 8 ; do
        for Raf in 3 ; do
          for Nx in 400 ; do
            for xOrder in 2 ; do
              for solver in "KIN_HAT"; do
                for HR in HRQ; do

                  export folderHR=${folderGeneral}/dR=${dR}/K=${K}/Knl=${Knl}/Nr=${Nr}/Raf=${Raf}/Nx=${Nx}/xOrder=${xOrder}/${solver}/${HR}

                  # python2.7 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${Nr} -r ${Raf} -j ${Nx} -o ${xOrder} -k ${K} -i ${Knl} -d ${dR}
                  # multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                  # python2.7 write.py -p ${HOME}${folderHR}/

                  # mkdir -p ${HOME}${folderHR}/Figures
                  # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

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
