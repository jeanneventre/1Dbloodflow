#!/bin/bash

export OMP_NUM_THREADS=8

export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/Wang/Pathological/Iliac

for NN in "Newtonian" ; do

  for conj in "jS"; do

    for nuv in "5e4" ; do

      for dR in "0.9" ; do #"-0.9"
        for dK in "0" ; do

          for Nx in 3 ; do
            for xOrder in 2 ; do
              for dt in 1e-5 ; do
                for tOrder in 2 ; do
                  for solver in "KIN_HAT"; do
                    for HR in HRQ; do

                      export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/dR=${dR}/dK=${dK}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                       python3 writeParameter.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -y ${dR} -z ${dK}
                       bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
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
  done
done
