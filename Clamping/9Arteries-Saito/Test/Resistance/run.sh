#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Test/Resistance/PostClamp/Qcst
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for NN in "Newtonian" ; do
  for conj in "jS" ; do
    for nuv in "5e4" ; do 
      for Nx in 10 ; do #3 7   
        for xOrder in 2 ; do
          for dt in 1e-4 ; do
            for tOrder in 2 ; do
              for solver in "KIN_HAT"; do
                for HR in HRQ; do
                   
                  export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                    python3 writeParameter2.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv}
                    bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                    python2.7 write.py -p ${HOME}${folderHR}/
                    # python3 res.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv}
                   # python3 min.py 
                    # python3 puissance.py  -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv} -x ${C} --P1 ${R1} --P2 ${R2}  #-m ${phi} -n ${Cv} 
                  
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

