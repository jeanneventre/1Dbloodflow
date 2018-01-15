#!/bin/bash

export folderGeneral=/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Asymptotic/Reflection/Stenosis

for Sh in 1e-3 ; do
  for dRst in -0.5 ; do
    for dKst in 0 ; do
      for K in 1e4 ; do
        for Knl in 1e1 1e2 1e3; do

          for drmax in 0.25 ; do
            for drmin in 0.01 ; do
              for Nx in 800 ; do
                for xOrder in 2 ; do
                  for dt in 1e-5 ; do
                    for tOrder in 3 ; do
                      for solver in "KIN_HAT"; do
                        for HR in HRQ; do

                          export folderHR=${folderGeneral}/Sh=${Sh}/K=${K}/Knl=${Knl}/dRst=${dRst}/dKst=${dKst}/drCoarse=${drmax}-drFine=${drmin}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                          # python2.7 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${drmax} -r ${drmin} -j ${Nx} -o ${xOrder} -t ${dt} -d ${tOrder} -k ${K} -i ${Knl} -e ${Sh} -a ${dRst} -b ${dKst}
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
      done
    done
  done
done
