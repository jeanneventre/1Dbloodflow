# 1Dbloodflow
## Installation et bases GIT

### Installation
Pour récupérer le dépôt utiliser la commande :
```
git clone git@gitlab.math.u-psud.fr:Poumon/2Balloons-model.git
```

### Mise à jour, modifications
Pour manipuler le dépot Git, il est possible d'utiliser soit une interface graphique (SourceTree - mac - ou Kraken - multi-plateforme) avint d'éviter l'apprentissage des commandes terminales.
Dans tous les cas, il faut :
0. Visualiser les modifications à l'aide de `git status`
1. Choisir les modifications à valider pour la prochaine version via `git add nom_fichier` ou la commande `stage`des interfaces graphiques (`git add -i` permet de valider les changements blocs par blocs via l'option patch)
2. Créer une nouvelle version à l'aide d'un commit (`git commit -m "Descriptif du commit"` ou le bouton `commit` sur les GUI)
3. Récupérer les modifications éventuelles faites par les autres contributeurs (via `git pull` ou le boutons du même nom ; les modifications que vous avez faites ne seront pas perdues)
4. Envoyer (pousser) sa (ses) dernière(s) version(s) sur le dépôt distant via `git push` ou le bouton associer.

Pour aller plus loin, voir le "gitbook" disponible en ligne, en anglais comme en français.