# Le Jeu de la vie
Ce dépôt logiciel contient un petit projet d'algorithmie et programmation. Il s'agit du projet compagnon de l'[intro à la programmation en Python](https://github.com/mpalenciaolivar/Intro-au-Python).

## Présentation
Le Jeu de la vie est à la fois un automate cellulaire et un jeu à zéro joueurs.
[Arté a fait une courte vidéo dessus](https://youtu.be/gKgAaZ7a5Bs), très
sympathique à regarder et qui en explique les principes et le contexte
d'apparition. Ce projet est tout autant une expérience de programmation qu'une
expérience esthétique, et je dirais même artistique : on peut faire des choses visuellement
très sympathiques avec le Jeu de la vie ! Il y a même des gens qui rivalisent
d'ingéniosité pour obtenir des [motifs tous plus attrayants les uns que les autres](https://youtu.be/C2vgICfQawE).

## Pré-requis
Ici encore, Python et un IDE, cf le projet de l'intro. 

**Pour les utilisateurs de Windows** (et seulement eux), il vous faudra aussi installer module `windows-curses`. Dans une console Python, tapez ceci :

```
python -m pip install windows-curses
```

## Consignes
Vous l'aurez compris : votre objectif est de faire votre propre implémentation du Jeu, avec les règles du voisinage de Moore.

Rassurez-vous: cela ne prendra pas un semestre pour le faire. Ce petit projet met en pratique toutes les notions de l'intro à la programmation Python (variables, fonctions, boucles). Vous trouverez le
guide pas à pas à la [page 54 de ce document, jusqu'à la page 59](https://funambule.org/lectures/linux-magazines/GNU_Linux_Magazine_n171___Rendez_vos_programmes_vivants_avec_les_algorithmes_genetiques___ed1_v1.pdf). La question du labyrinthe est exclue des consignes. Vous êtes vivement encouragés à essayer de faire ce projet par vous-mêmes à partir des règles, mais vous pouvez tout aussi bien vous laisser guider en codant en même temps. L'important est de progresser. Je propose également un corrigé dans le dossier `src` de ce dépôt; il s'agit pratiquement du même code que dans les consignes, mais modularisé (c'est-à-dire organisé) selon ma vision des choses. Par contre, ce n'est pas parce que je ne traite pas l'article jusqu'au bout que vous ne devriez pas continuer sur ce petit projet à partir de mon code de base : c'est de la connaissance bonus qui ne vous coûtera pas grand-chose, mais qui vous servira pendant un moment. Et puis, programmer présente un certain charme. C'est vous qui voyez pour vous mêmes; vous disposez de tout ce qu'il vous faut pour travailler et vous corriger.

Il suffira de lancer le fichier `main.py` pour faire fonctionner le jeu. **Attention** : il faudra le lancer depuis un terminal (PowerShell pour ceux qui utilisent Windows). Dans votre terminal favori, se placer dans le dossier `src` puis taper:

```
python main.py
```

Dans tous les cas, tapez sur espace pour faire faire les transitions aux cellules (il converge vers un état stationnaire) et appuyez sur Échap pour fermer le programme.
