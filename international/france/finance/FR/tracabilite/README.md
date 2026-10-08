# Traçabilité du chiffrage

Le chiffrage du programme « compile » : il échoue s'il est incohérent.

`matrice.yaml` relie chaque **exigence** du programme (son texte) à des **mesures**, et chaque mesure à des **lignes budgétaires**. `tools/finance_check.py` vérifie la chaîne, et la GitHub Action « Traçabilité du chiffrage » le lance à chaque modification.

## Ce qui bloque (erreur)

- une ligne de coût d'un pilier sans mesure dans la matrice, ou l'inverse ;
- une mesure rattachée à une exigence inconnue ;
- une ligne de recette ou de réaffectation sans mesure, sans unité valide, ou au-delà de son périmètre ;
- une ligne comptée dans le solde alors qu'elle contredit une exigence (ex. sortie de l'UE face à « Nous ne quittons pas l'Europe ») ;
- un coût évité compté comme une économie ;
- un total de pilier qui ne correspond pas à la somme de son tableau ;
- une `synthese.md` qui n'a pas été régénérée.

## Ce qui avertit sans bloquer

Les mesures `non_chiffre`, `a_reverifier` ou `a_justifier`, et les ventilations annuelles qui ne retombent pas sur le total. `--strict` les rend bloquantes.

## Contribuer

1. Modifier le tableau du pilier concerné (`01_…md` à `14_…md`) ou `matrice.yaml`.
2. Lancer `python3 tools/finance_check.py --write` (nécessite `pip install pyyaml`) : les totaux des piliers et `synthese.md` sont régénérés.
3. Lancer `python3 tools/finance_check.py` et corriger les erreurs avant de proposer la modification.
