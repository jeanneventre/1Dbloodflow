#!/bin/bash

export OMP_NUM_THREADS=12
# LINUX
export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/bloodflow/Examples/Clamping/9Arteries-Saito/Test/1artery
# MAC
#export folderGeneral=/Documents/Boulot/Thèse/code/bloodflow/Examples/Clamping/9Arteries-Saito/Sane

for K in 1e4 ; do
  for NN in "Newtonian" ; do
    for conj in "jS" ; do
      for nuv in "5e4" ; do 
        for Nx in 100 ; do #3 7   
          for xOrder in 2 ; do
            for dt in 1e-4 ; do
              for tOrder in 2 ; do
                for solver in "KIN_HAT"; do
                  for HR in HRQ; do
                     
                    export folderHR=${folderGeneral}/${NN}/${conj}/nuv=${nuv}/Nx=${Nx}/xOrder=${xOrder}/dt=${dt}/tOrder=${tOrder}/${solver}/${HR}

                      python3 writeParameter1.py -a ${HOME}${folderHR}/ -b Sane -c ${conj} -d ${solver} -k ${K} -e ${HR} -f ${Nx} -g ${xOrder} -i ${dt} -j ${tOrder} -l ${NN} -n ${nuv}
                      bloodflow -i ${HOME}${folderHR}/parameters_Sane/ -o ${HOME}${folderHR}/data/ -s Sane
                      python2.7 write1.py -p ${HOME}${folderHR}/
        
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

