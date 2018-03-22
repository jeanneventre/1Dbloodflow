#!/bin/bash

export OMP_NUM_THREADS=12

# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Clamp
#MAC 
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Clamp

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "31e4" ; do 
      for Q in 700; do 
        for P1 in 0.5; do
          for R2 in 1000; do
            # if [ $R2 -gt $R1 ] ; then 
              for C in 1e-3; do
                for Nx in 10 ; do
                  for xOrder in 2 ; do
                    for dt in 1e-4 ; do
                      for tOrder in 2 ; do
                        for solver in "KIN_HAT"; do
                          for HR in HRQ; do
                             
                            export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/Q=${Q}/P1=${P1}/R2=${R2}/C=${C}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                             python3 writeParameter.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} --P1 ${P1} -t ${Q} -x ${C} --P2 ${R2}  #-m ${phi} -n ${Cv} 
                             bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                             python2.7 write.py -p ${HOME}${folderHR}/
                             python3 plot.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -t ${Q} --P1 ${P1} -x ${C} --P2 ${R2} #-m ${phi} -n ${Cv} 
                              
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
              # fi
            done
          done 
        done
      done
    done
  done 
done

# python3 min.py 