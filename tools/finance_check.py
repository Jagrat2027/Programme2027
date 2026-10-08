#!/usr/bin/env python3
"""Contrôle de cohérence du chiffrage de Programme2027 (France).

Vérifie que chaque ligne budgétaire est tracée vers une mesure, chaque mesure
vers une exigence du programme, que les unités sont homogènes, qu'aucune ligne
comptée ne contredit une exigence, et que les totaux affichés correspondent
aux tableaux.

Usage :
    python3 tools/finance_check.py           # contrôle ; code 1 si erreur
    python3 tools/finance_check.py --strict  # les avertissements deviennent bloquants
    python3 tools/finance_check.py --write   # régénère synthese.md et les totaux des piliers
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIN = os.path.join(ROOT, "international", "france", "finance", "FR")
MATRICE = os.path.join(FIN, "tracabilite", "matrice.yaml")
SYNTHESE = os.path.join(FIN, "synthese.md")

UNITES = {"md_an"}
SCENARIOS = {"central", "conditionnel", "rupture", "memoire"}
TYPES = {"recette", "reaffectation", "cout_evite"}
STATUTS_AVERTIS = {"non_chiffre", "a_reverifier", "a_justifier"}


def num(s: str) -> float:
    return float(s.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "."))


def fr(x: float, dec: int = 1) -> str:
    s = f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")
    if dec:
        s = s.rstrip("0").rstrip(",")
    return s


def montant_md(m: float) -> str:
    """Montant en M€ → texte (milliards ou millions)."""
    if m >= 1000:
        v = m / 1000
        unite = "milliard" if v < 2 else "milliards"
        return f"{fr(v, 2)} {unite} €"
    return f"{fr(m, 0)} millions €"


def lire_piliers():
    piliers = {}
    for f in sorted(glob.glob(os.path.join(FIN, "[01][0-9]_*.md"))):
        code = os.path.basename(f)[:2]
        texte = open(f, encoding="utf-8").read()
        lignes = []
        for line in texte.splitlines():
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 7 and re.fullmatch(r"20\d\d", c[1] or ""):
                lignes.append({
                    "libelle": c[0],
                    "annees": [num(x) for x in c[2:-2]],
                    "basse": num(c[-2]),
                    "haute": num(c[-1]),
                })
        entete = {}
        for cle in ("basse", "haute"):
            m = re.search(rf"Fourchette {cle} : ([\d,]+) (milliards?|millions)", texte)
            if m:
                entete[cle] = num(m.group(1)) * (1000 if m.group(2).startswith("milliard") else 1)
        titre = re.search(r"^# (.+)$", texte, re.M)
        piliers[code] = {"fichier": f, "texte": texte, "lignes": lignes, "entete": entete,
                         "titre": titre.group(1).strip() if titre else code}
    return piliers


def controler(m, piliers):
    err, warn = [], []
    exig = {e["id"]: e for e in m["exigences"]}
    mesures = {x["id"]: x for x in m["mesures"]}
    if len(mesures) != len(m["mesures"]):
        err.append("Identifiant de mesure en double.")

    # Mesures ↔ tableaux des piliers
    vues = set()
    for code, p in piliers.items():
        for i, row in enumerate(p["lignes"], 1):
            mid = f"P{code}-M{i:02d}"
            mes = mesures.get(mid)
            if not mes or mes["libelle"] != row["libelle"]:
                err.append(f"[orpheline] Ligne de coût sans mesure : pilier {code}, « {row['libelle']} » (attendu {mid}).")
            vues.add(mid)
            if row["annees"] and abs(sum(row["annees"]) - row["basse"]) > 1:
                warn.append(f"[ventilation] Pilier {code}, « {row['libelle']} » : années = {fr(sum(row['annees']), 0)} M€, total bas = {fr(row['basse'], 0)} M€.")
        bas = sum(r["basse"] for r in p["lignes"])
        haut = sum(r["haute"] for r in p["lignes"])
        for cle, val in (("basse", bas), ("haute", haut)):
            ent = p["entete"].get(cle)
            if ent is None or abs(ent - val) > max(1, 0.005 * val):
                err.append(f"[total] Pilier {code} : fourchette {cle} affichée {fr(ent or 0, 0)} M€, somme du tableau {fr(val, 0)} M€.")
    for mid in mesures:
        if re.fullmatch(r"P\d\d-M\d\d", mid) and mid not in vues:
            err.append(f"[orpheline] Mesure {mid} sans ligne dans le tableau de son pilier.")

    for x in m["mesures"]:
        if x.get("exigence") not in exig:
            err.append(f"[exigence] Mesure {x['id']} rattachée à une exigence inconnue : {x.get('exigence')}.")
        if x.get("statut_chiffrage") in STATUTS_AVERTIS:
            warn.append(f"[{x['statut_chiffrage']}] {x['id']} — {x['libelle']}")

    # Lignes de recettes / réaffectations
    exclusions = {}
    for e in m["exigences"]:
        for h in e.get("exclut", []):
            exclusions.setdefault(h, []).append(e["id"])
    for l in m["lignes"]:
        lid = l["id"]
        if l.get("mesure") not in mesures:
            err.append(f"[orpheline] Ligne {lid} sans mesure connue ({l.get('mesure')}).")
        if l.get("unite") not in UNITES:
            err.append(f"[unité] Ligne {lid} : unité « {l.get('unite')} » ; attendu {sorted(UNITES)}.")
        if l.get("type") not in TYPES:
            err.append(f"[type] Ligne {lid} : type « {l.get('type')} » inconnu.")
        sc = l.get("scenario")
        if sc not in SCENARIOS:
            err.append(f"[scénario] Ligne {lid} : scénario « {sc} » inconnu.")
        if l["basse"] > l["haute"]:
            err.append(f"[fourchette] Ligne {lid} : basse > haute.")
        if "perimetre_max" in l and l["haute"] > l["perimetre_max"]:
            err.append(f"[périmètre] Ligne {lid} : {fr(l['haute'])} Md€ dépasse le périmètre de {fr(l['perimetre_max'])} Md€.")
        conflits = [ex for h in l.get("hypotheses", []) for ex in exclusions.get(h, [])]
        if conflits and sc != "rupture":
            err.append(f"[contradiction] Ligne {lid} comptée en « {sc} » mais contredit {', '.join(conflits)}.")
        if sc == "conditionnel" and l.get("condition") not in mesures:
            err.append(f"[condition] Ligne {lid} conditionnelle sans condition valide.")
        if sc == "central" and l.get("type") == "cout_evite":
            err.append(f"[nature] Ligne {lid} : un coût évité ne peut pas être compté dans le solde central.")
        if l.get("statut_chiffrage") in STATUTS_AVERTIS:
            warn.append(f"[{l['statut_chiffrage']}] ligne {lid}")
    return err, warn


def synthese(m, piliers) -> str:
    per = m["periodes_piliers"]
    chap = {e["id"]: e["chapitre"] for e in m["exigences"]}
    P = m["parametres"]
    lignes_p = []
    dep_b = dep_h = 0.0
    for code, p in piliers.items():
        b = sum(r["basse"] for r in p["lignes"]) / 1000
        h = sum(r["haute"] for r in p["lignes"]) / 1000
        n = per.get(code, per["default"])
        dep_b += b / n
        dep_h += h / n
        titre = chap.get(f"EX-{code}", p["titre"])
        lignes_p.append(f"| {titre} | {n} ans | {fr(b, 2)} | {fr(h, 2)} | {fr(b / n, 2)} | {fr(h / n, 2)} |")

    mes = {x["id"]: x for x in m["mesures"]}

    def table(filtre):
        out, sb, sh = [], 0.0, 0.0
        for l in m["lignes"]:
            if filtre(l):
                out.append(f"| {mes[l['mesure']]['libelle']} | {fr(l['basse'])} | {fr(l['haute'])} |")
                sb += l["basse"]
                sh += l["haute"]
        return out, sb, sh

    rec, rb, rh = table(lambda l: l["scenario"] == "central" and l["type"] == "recette")
    rea, ab, ah = table(lambda l: l["scenario"] == "central" and l["type"] == "reaffectation")
    rng = lambda l: fr(l["basse"]) if l["basse"] == l["haute"] else f"{fr(l['basse'])} – {fr(l['haute'])}"
    hors = [f"| {mes[l['mesure']]['libelle']} | {l['scenario']} | {rng(l)} |"
            for l in m["lignes"] if l["scenario"] != "central"]
    lib = {"non_chiffre": "non chiffré", "a_reverifier": "à revérifier", "a_justifier": "à justifier"}
    nc = [f"- {x['libelle']} — {lib[x['statut_chiffrage']]}"
          for x in m["mesures"] if x.get("statut_chiffrage") in STATUTS_AVERTIS]

    sol_b = rb + ab - dep_h   # cas prudent : recettes basses, dépenses hautes
    sol_h = rh + ah - dep_b
    d = P["deficit_md"]

    return f"""<!-- Fichier généré par tools/finance_check.py --write. Ne pas modifier à la main :
     modifier les tableaux des piliers ou tracabilite/matrice.yaml, puis régénérer. -->

# Synthèse budgétaire du Programme 2027 (France)

Toutes les grandeurs sont ramenées en **milliards d'euros par an** (Md€/an), en euros constants.
Les coûts des piliers sont des cumuls pluriannuels, divisés par la durée de leur tableau ;
les recettes et les réaffectations sont des flux annuels.

## Solde annuel du scénario central

| | Prudent | Ambitieux |
| --- | --- | --- |
| Dépenses nouvelles | {fr(dep_h, 1)} | {fr(dep_b, 1)} |
| Recettes nouvelles | {fr(rb)} | {fr(rh)} |
| Réaffectations | {fr(ab)} | {fr(ah)} |
| **Solde** | **{fr(sol_b)}** | **{fr(sol_h)}** |
| Déficit public {P['annee_reference']} (Insee) | {fr(d)} | {fr(d)} |
| Déficit après programme, à périmètre constant | {fr(d - sol_b)} | {fr(d - sol_h)} |

Prudent = dépenses hautes, recettes basses ; ambitieux = l'inverse.
Ce solde **exclut** les mesures non chiffrées listées plus bas, dont plusieurs réduisent les recettes.
La réaffectation des aides aux entreprises représente l'essentiel du solde : elle doit être
ventilée dispositif par dispositif pour que le solde soit crédible.

## Dépenses par pilier (Md€)

| Pilier | Période | Cumul bas | Cumul haut | Par an (bas) | Par an (haut) |
| --- | --- | --- | --- | --- | --- |
{chr(10).join(lignes_p)}
| **Total** | | | | **{fr(dep_b, 1)}** | **{fr(dep_h, 1)}** |

## Recettes nouvelles (Md€/an)

| Source | Basse | Haute |
| --- | --- | --- |
{chr(10).join(rec)}
| **Total** | **{fr(rb)}** | **{fr(rh)}** |

## Réaffectations comptées (Md€/an)

| Source | Basse | Haute |
| --- | --- | --- |
{chr(10).join(rea)}
| **Total** | **{fr(ab)}** | **{fr(ah)}** |

## Lignes hors solde (Md€/an)

| Ligne | Statut | Montant |
| --- | --- | --- |
{chr(10).join(hors)}

- **conditionnel** : compté quand sa condition est chiffrée.
- **rupture** : contredit une exigence du programme ; jamais compté.
- **memoire** : coût évité ou coût social, pas une ligne du budget de l'État.

## Mesures à chiffrer ou à revérifier

{chr(10).join(nc)}

Détail et justification de chaque ligne : `tracabilite/matrice.yaml`. Hypothèses : `hypotheses.md`.
"""


def ecrire_entetes(piliers):
    for code, p in piliers.items():
        t = p["texte"]
        for cle in ("basse", "haute"):
            val = sum(r[cle] for r in p["lignes"])
            t = re.sub(rf"(Fourchette {cle} : )[\d,]+ (?:milliards?|millions) €", lambda mm: mm.group(1) + montant_md(val), t, count=1)
        if t != p["texte"]:
            open(p["fichier"], "w", encoding="utf-8").write(t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    m = yaml.safe_load(open(MATRICE, encoding="utf-8"))
    piliers = lire_piliers()
    if a.write:
        ecrire_entetes(piliers)
        piliers = lire_piliers()
        open(SYNTHESE, "w", encoding="utf-8").write(synthese(m, piliers))

    err, warn = controler(m, piliers)
    if open(SYNTHESE, encoding="utf-8").read() != synthese(m, piliers):
        err.append("[synthèse] synthese.md n'est pas à jour : lancer `python3 tools/finance_check.py --write`.")

    for w in warn:
        print(f"AVERTISSEMENT {w}")
    for e in err:
        print(f"ERREUR {e}")
    print(f"\n{len(err)} erreur(s), {len(warn)} avertissement(s).")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as s:
            s.write(f"## Traçabilité du chiffrage\n\n{len(err)} erreur(s), {len(warn)} avertissement(s).\n\n")
            s.write("\n".join(f"- ❌ {e}" for e in err) + "\n" + "\n".join(f"- ⚠️ {w}" for w in warn) + "\n")
    sys.exit(1 if err or (a.strict and warn) else 0)


if __name__ == "__main__":
    main()
