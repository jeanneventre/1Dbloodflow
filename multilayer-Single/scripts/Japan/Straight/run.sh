#!/bin/bash

# export OMP_NUM_THREADS=27
# echo "OMP_NUM_THREADS=" $OMP_NUM_THREADS

export folderGeneral=/Documents/UPMC/These/Codes/multilayerSingle/example/Well-Balance/Japan/Straight

for K in 211e4 ; do
  for NN in "Newtonian" ; do
    for Cv in 4360 ; do
      for Knl in 110000 ; do

        for drmax in 0.25 ; do
          for drmin in 0.01 ; do
            for Nx in 800 ; do
              for xOrder in 2 ; do
                for dt in 1e-4 ; do
                  for tOrder in 3 ; do
                    for solver in "KIN_HAT"; do
                      for HR in HRQ; do

                        export folderHR=${folderGeneral}/K=${K}/${NN}/Cv=${Cv}/Knl=${Knl}/drCoarse=${drmax}-drFine=${drmin}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                        # python2.7 writeParameter.py -p ${HOME}${folderHR}/ -l Sane -s ${solver} -y ${HR} -c ${drmax} -r ${drmin} -j ${Nx} -o ${xOrder} -t ${dt} -d ${tOrder} -k ${K} -n ${NN} -v ${Cv} -i ${Knl}
                        # multilayerSingle -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane -q
                        # python2.7 write.py -p ${HOME}${folderHR}/

                        # python2.7 plot.py -p ${HOME}${folderHR}/

                        # mkdir -p ${HOME}${folderHR}/Figures
                        # scp -r ${SSHACCOUNT}:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

                        mkdir -p ${HOME}${folderHR}/Figures
                        scp -r -P 2222 ghigo@localhost:${HOME_SSH}${folderHR}/Figures ${HOME}${folderHR}/

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