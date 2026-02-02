# SVT_IT_ANX_E — Schéma Territorial d'Implantation
## Plan de Souveraineté IT 2027-2047

---

**Document de référence** : SVT_IT_00, SVT_IT_ANX_00, SVT_IT_ANX_C, SVT_IT_ANX_D  
**Classification** : Public  
**Auteur** : Jeff / Jagrat  
**Date** : Janvier 2026  
**Version** : 0.1

---

## Sommaire

1. [Diagnostic Territorial Actuel](#1-diagnostic-territorial)
2. [Principes d'Aménagement](#2-principes-aménagement)
3. [Architecture Territoriale Cible](#3-architecture-cible)
4. [Fiches Pôles Territoriaux](#4-fiches-pôles)
5. [Infrastructures et Réseaux](#5-infrastructures)
6. [Équilibre et Cohésion Territoriale](#6-équilibre-territorial)
7. [Gouvernance Territoriale](#7-gouvernance)
8. [Plan d'Action et Investissements](#8-plan-action)

---

## 1. Diagnostic Territorial Actuel

### 1.1 Cartographie des Acteurs Existants

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IMPLANTATIONS SEMICONDUCTEURS FRANCE 2026                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                           ┌─────────┐                                       │
│                           │ HAUTS-  │                                       │
│                           │DE-FRANCE│                                       │
│                           │ (faible)│                                       │
│                           └────┬────┘                                       │
│         ┌──────────┐          │           ┌──────────┐                     │
│         │NORMANDIE │          │           │  GRAND   │                     │
│         │ (faible) │      ┌───┴───┐       │   EST    │                     │
│         └──────────┘      │  ILE  │       │ (faible) │                     │
│                           │  DE   │       └──────────┘                     │
│    ┌──────────┐           │FRANCE │                                        │
│    │ BRETAGNE │           │ ████  │       ┌──────────────────┐             │
│    │   ████   │           │Saclay │       │                  │             │
│    │  Rennes  │           │Thales │       │                  │             │
│    │  Lannion │           └───────┘       │                  │             │
│    └──────────┘                           │   AUVERGNE-      │             │
│         │            ┌──────────┐         │   RHÔNE-ALPES    │             │
│         │            │  CENTRE  │         │   ████████████   │             │
│    ┌────┴─────┐      │VAL LOIRE │         │   Grenoble ★★★   │             │
│    │  PAYS    │      │  Tours   │         │   Lyon           │             │
│    │DE LOIRE  │      │ (moyen)  │         │   STMicro        │             │
│    │ (faible) │      └──────────┘         │   CEA-Leti       │             │
│    └──────────┘                           │   Soitec         │             │
│                                           └──────────────────┘             │
│    ┌──────────────┐                              │                         │
│    │  NOUVELLE-   │      ┌──────────┐           │                         │
│    │  AQUITAINE   │      │ OCCITANIE│      ┌────┴─────┐                   │
│    │   Bordeaux   │      │   ████   │      │  PACA    │                   │
│    │   (moyen)    │      │ Toulouse │      │  ████    │                   │
│    └──────────────┘      │ Montpell.│      │  Sophia  │                   │
│                          └──────────┘      │ Marseille│                   │
│                                            └──────────┘                   │
│                                                                             │
│  LÉGENDE : ████ Présence forte │ ███ Moyenne │ █ Faible │ ★★★ Pôle majeur │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Concentration Actuelle par Région

| Région | Emplois semi 2026 | Part nationale | Acteurs majeurs |
|--------|-------------------|----------------|-----------------|
| **Auvergne-Rhône-Alpes** | 25 000 | 50% | STMicro, CEA-Leti, Soitec |
| **Île-de-France** | 10 000 | 20% | Thales, conception, sièges |
| **Occitanie** | 6 000 | 12% | NXP, Continental, spatial |
| **Bretagne** | 4 000 | 8% | STMicro Rennes, télécom |
| **PACA** | 3 000 | 6% | Sophia, conception |
| **Autres** | 2 000 | 4% | Dispersé |
| **TOTAL** | **50 000** | **100%** | |

### 1.3 Forces et Faiblesses Territoriales

#### Auvergne-Rhône-Alpes (Grenoble-Lyon)

| Forces | Faiblesses |
|--------|------------|
| ✓ Écosystème complet R&D-industrie | ✗ Saturation foncière Grenoble |
| ✓ CEA-Leti, référence mondiale | ✗ Coût de la vie élevé |
| ✓ STMicro Crolles, seule fab avancée | ✗ Concentration des risques |
| ✓ Universités et écoles d'excellence | ✗ Transports intra-région |
| ✓ Bassin d'emploi qualifié | ✗ Tensions recrutement |

#### Île-de-France (Saclay)

| Forces | Faiblesses |
|--------|------------|
| ✓ Concentration R&D (Polytechnique, CEA) | ✗ Pas de fab significative |
| ✓ Accès talents internationaux | ✗ Coût immobilier prohibitif |
| ✓ Proximité décideurs, financeurs | ✗ Congestion, transports |
| ✓ Start-ups, écosystème VC | ✗ Éloignement de l'industrie |

#### Occitanie (Toulouse)

| Forces | Faiblesses |
|--------|------------|
| ✓ Écosystème aérospatial mature | ✗ Orientation aéro, pas semi |
| ✓ Universités, ISAE, INSA | ✗ Peu d'acteurs semi majeurs |
| ✓ Qualité de vie attractive | ✗ Manque de fabs |
| ✓ Foncier disponible | ✗ Besoin de réorientation |

#### Bretagne (Rennes-Lannion)

| Forces | Faiblesses |
|--------|------------|
| ✓ Historique télécom et électronique | ✗ Écosystème semi limité |
| ✓ STMicro site de Rennes | ✗ Éloignement géographique |
| ✓ Cybersécurité, DGA | ✗ Taille critique insuffisante |
| ✓ Qualité de vie, coût modéré | ✗ Peu de formation spécialisée |

### 1.4 Infrastructures Critiques Existantes

| Type | Localisation | Capacité | État |
|------|--------------|----------|------|
| **Fab 300mm** | Crolles (STMicro) | 15K wafers/mois | Opérationnel |
| **Fab 200mm** | Crolles, Rousset, Tours | Variable | Opérationnel |
| **R&D centrale** | CEA-Leti Grenoble | 12 000 m² SB | Excellence |
| **Substrats** | Soitec Bernin | Leader mondial | Expansion |
| **Gaz électroniques** | Air Liquide (national) | Top 3 mondial | Expansion |
| **Packaging** | SET (Grenoble) | Niche | Croissance |

### 1.5 Ressources Critiques par Territoire

#### Eau

| Région | Disponibilité | Risque sécheresse | Commentaire |
|--------|---------------|-------------------|-------------|
| AuRA (Grenoble) | Excellente | Faible | Alpes, nappes abondantes |
| Île-de-France | Bonne | Moyen | Seine, mais tensions été |
| Occitanie | Moyenne | Élevé | Stress hydrique croissant |
| Bretagne | Excellente | Très faible | Pluviométrie |
| Grand Est | Bonne | Faible | Nappes, cours d'eau |
| Hauts-de-France | Bonne | Faible | Nappes artésiennes |

**Besoin d'une fab 300mm** : 500 000 - 1 000 000 m³/an

#### Énergie

| Région | Mix électrique | Disponibilité | Coût |
|--------|---------------|---------------|------|
| AuRA | Hydro + nucléaire | Excellente | Modéré |
| Grand Est | Nucléaire | Excellente | Faible |
| Hauts-de-France | Nucléaire + éolien | Bonne | Faible |
| Normandie | Nucléaire | Excellente | Faible |
| Occitanie | Mix | Moyenne | Modéré |

**Besoin d'une fab 300mm** : 150-200 MW (équivalent ville 100 000 hab.)

#### Foncier

| Région | Disponibilité >30 ha | Coût €/m² | Contraintes |
|--------|----------------------|-----------|-------------|
| Grenoble | Très limitée | 150-300 | Saturation |
| Saclay | Limitée | 200-400 | Urbanisation |
| Toulouse | Bonne | 80-150 | Zones disponibles |
| Grand Est | Excellente | 40-80 | Reconversion |
| Hauts-de-France | Excellente | 30-60 | Reconversion |
| Normandie | Excellente | 40-80 | Zones industrielles |

---

## 2. Principes d'Aménagement

### 2.1 Objectifs Stratégiques

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PRINCIPES D'AMÉNAGEMENT TERRITORIAL                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. CONSOLIDATION DES PÔLES D'EXCELLENCE                                   │
│     ─────────────────────────────────────                                  │
│     • Renforcer Grenoble comme cœur de la filière                         │
│     • Développer les synergies avec Lyon                                   │
│     • Éviter la dispersion des moyens                                      │
│                                                                             │
│  2. DIVERSIFICATION GÉOGRAPHIQUE MAÎTRISÉE                                 │
│     ──────────────────────────────────────                                 │
│     • Créer 2-3 pôles secondaires complémentaires                         │
│     • Réduire la concentration des risques                                 │
│     • Exploiter les atouts régionaux différenciés                         │
│                                                                             │
│  3. ÉQUILIBRE TERRITORIAL                                                  │
│     ────────────────────                                                   │
│     • Répartir les emplois sur le territoire                              │
│     • Intégrer les bassins en reconversion industrielle                   │
│     • Développer les territoires désindustrialisés                        │
│                                                                             │
│  4. ACCESSIBILITÉ ET CONNECTIVITÉ                                          │
│     ──────────────────────────────                                         │
│     • Proximité TGV et aéroports                                          │
│     • Connexions inter-pôles efficaces                                     │
│     • Accès international (clients, fournisseurs)                         │
│                                                                             │
│  5. DURABILITÉ ET RÉSILIENCE                                               │
│     ────────────────────────                                               │
│     • Accès garanti eau et énergie bas carbone                            │
│     • Résilience face aux risques (climat, approvisionnement)             │
│     • Intégration environnementale exemplaire                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Critères de Localisation

#### Critères Obligatoires (Éliminatoires)

| Critère | Seuil minimum | Justification |
|---------|---------------|---------------|
| Eau | 500 000 m³/an garantis | Process fab |
| Électricité | 150 MW disponibles | Consommation fab |
| Foncier | 30+ hectares d'un tenant | Emprise fab + extension |
| Risque sismique | Zone ≤ 3 | Protection équipements |
| Risque inondation | Hors zone inondable | Continuité activité |

#### Critères de Sélection (Scoring)

| Critère | Poids | Éléments d'évaluation |
|---------|-------|----------------------|
| Écosystème existant | 25% | R&D, fournisseurs, clients, formation |
| Bassin d'emploi | 20% | Disponibilité, compétences, coût |
| Accessibilité | 15% | TGV, aéroport international, autoroute |
| Coût global | 15% | Foncier, énergie, fiscalité, vie |
| Qualité de vie | 10% | Attractivité talents, cadre |
| Soutien régional | 10% | Engagement collectivités, aides |
| Résilience | 5% | Multi-sourcing eau/énergie, climat |

### 2.3 Modèle de Développement : Hub & Spokes

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MODÈLE HUB & SPOKES SEMICONDUCTEURS                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              ┌───────────┐                                  │
│                              │           │                                  │
│                         ┌────│  HUB      │────┐                            │
│                         │    │  CENTRAL  │    │                            │
│                         │    │ (Grenoble)│    │                            │
│                         │    │           │    │                            │
│                         │    └───────────┘    │                            │
│                         │          │          │                            │
│              ┌──────────┴──────────┼──────────┴──────────┐                 │
│              │                     │                     │                 │
│              ▼                     ▼                     ▼                 │
│       ┌───────────┐         ┌───────────┐         ┌───────────┐           │
│       │   SPOKE   │         │   SPOKE   │         │   SPOKE   │           │
│       │  Saclay   │         │ Toulouse  │         │   Nord    │           │
│       │(Conception│         │(Packaging │         │  (Fab 2)  │           │
│       │   R&D)    │         │   Test)   │         │           │           │
│       └───────────┘         └───────────┘         └───────────┘           │
│              │                     │                     │                 │
│              │                     │                     │                 │
│              ▼                     ▼                     ▼                 │
│       ┌───────────┐         ┌───────────┐         ┌───────────┐           │
│       │  ANTENNE  │         │  ANTENNE  │         │  ANTENNE  │           │
│       │  Rennes   │         │  Sophia   │         │   Lyon    │           │
│       │(Télécom,  │         │ (Design)  │         │(Équipements│           │
│       │  Cyber)   │         │           │         │ Matériaux)│           │
│       └───────────┘         └───────────┘         └───────────┘           │
│                                                                             │
│  FLUX PRINCIPAUX :                                                         │
│  ════════════════                                                          │
│  ───▶ Technologie, process, support technique                              │
│  ◀─── Talents, retour terrain, besoins spécifiques                        │
│  ◀──▶ Collaboration R&D, projets conjoints                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Architecture Territoriale Cible 2047

### 3.1 Vue d'Ensemble

| Pôle | Vocation principale | Emplois 2047 | Investissement |
|------|---------------------|--------------|----------------|
| **Grenoble-Alpes** | Hub central, fab avancée, R&D | 70 000 | 45 Md€ |
| **Paris-Saclay** | Conception, R&D amont, sièges | 40 000 | 15 Md€ |
| **Toulouse-Occitanie** | Packaging, test, spatial | 30 000 | 18 Md€ |
| **Nord-France** | Fab souveraine, reconversion | 25 000 | 25 Md€ |
| **Lyon-Métropole** | Équipements, matériaux | 18 000 | 8 Md€ |
| **Rennes-Bretagne** | Télécom, cybersécurité | 12 000 | 5 Md€ |
| **Sophia-PACA** | Design, photonique | 8 000 | 3 Md€ |
| **Autres** | Antennes, services | 7 000 | 2 Md€ |
| **TOTAL** | | **210 000** | **121 Md€** |

### 3.2 Carte Stratégique 2047

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IMPLANTATIONS SEMICONDUCTEURS FRANCE 2047                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                           ┌─────────────┐                                   │
│                           │ NORD-FRANCE │                                   │
│                           │  ████████   │                                   │
│                           │ ★ FAB 14nm  │                                   │
│                           │  25 000 emp │                                   │
│                           └──────┬──────┘                                   │
│         ┌──────────┐            │           ┌──────────┐                   │
│         │NORMANDIE │            │           │  GRAND   │                   │
│         │  Antenne │        ┌───┴───┐       │   EST    │                   │
│         │  1 000   │        │PARIS- │       │ Antenne  │                   │
│         └──────────┘        │SACLAY │       │  2 000   │                   │
│                             │████████│       └──────────┘                   │
│    ┌──────────────┐         │40 000 │                                      │
│    │   BRETAGNE   │         │Concept°│       ┌──────────────────┐          │
│    │   ████████   │         │R&D    │       │                  │          │
│    │   12 000     │         └───────┘       │   GRENOBLE-      │          │
│    │  Télécom,Cyber│              │         │   ALPES          │          │
│    └──────────────┘              │         │   ████████████   │          │
│           │            ┌─────────┴──┐      │   ★★★ HUB ★★★    │          │
│           │            │   CENTRE   │      │   70 000 emp     │          │
│    ┌──────┴─────┐      │ VAL LOIRE  │      │   Fab, R&D,      │          │
│    │  PAYS DE   │      │  Antenne   │      │   Équipements    │          │
│    │   LOIRE    │      │   2 000    │      └──────────────────┘          │
│    │  Antenne   │      └────────────┘              │                      │
│    │   1 000    │                          ┌───────┴───────┐              │
│    └────────────┘                          │     LYON      │              │
│                                            │   ████████    │              │
│    ┌──────────────┐      ┌──────────────┐  │   18 000      │              │
│    │  NOUVELLE-   │      │  OCCITANIE   │  │  Équipements  │              │
│    │  AQUITAINE   │      │  ██████████  │  └───────────────┘              │
│    │   Bordeaux   │      │  ★ TOULOUSE  │         │                       │
│    │   Antenne    │      │   30 000     │    ┌────┴─────┐                 │
│    │    2 000     │      │  Packaging   │    │  PACA    │                 │
│    └──────────────┘      │    Test      │    │ ████████ │                 │
│                          └──────────────┘    │  Sophia  │                 │
│                                              │  8 000   │                 │
│                                              │ Design   │                 │
│                                              └──────────┘                 │
│                                                                            │
│  LÉGENDE : ★★★ Hub central │ ★ Pôle majeur │ ████ Pôle secondaire        │
│            Chiffres = emplois directs semiconducteurs                     │
│                                                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 Spécialisation des Pôles

| Pôle | Spécialisation | Complémentarité |
|------|----------------|-----------------|
| **Grenoble** | Fab avancée (FDSOI, FinFET R&D), R&D process, intégration | Hub technologique central |
| **Saclay** | Architecture, conception SoC, R&D amont, IA | Cerveaux, innovation |
| **Toulouse** | Packaging avancé, test, spatial, aéronautique | Back-end, applications |
| **Nord** | Fab souveraine 14nm, production volume | Capacité industrielle |
| **Lyon** | Équipements, matériaux, chimie | Support chaîne de valeur |
| **Rennes** | RF/télécom, cybersécurité, systèmes | Applications sécurisées |
| **Sophia** | Design fabless, photonique, start-ups | Créativité, niches |

---

## 4. Fiches Pôles Territoriaux

### 4.1 Pôle Grenoble-Alpes (Hub Central)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Hub central national |
| **Périmètre** | Grenoble Métropole + Grésivaudan + Nord-Isère |
| **Population bassin** | 800 000 habitants |
| **Emplois semi 2026** | 25 000 |
| **Emplois semi 2047** | 70 000 |
| **Croissance** | +45 000 emplois (+180%) |
| **Investissement** | 45 Md€ |

#### Écosystème Actuel

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ÉCOSYSTÈME GRENOBLE-ALPES 2026                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  INDUSTRIE                      R&D                        FORMATION        │
│  ─────────                      ───                        ─────────        │
│  • STMicro Crolles (fab)        • CEA-Leti (1 900 pers.)  • Grenoble INP   │
│  • STMicro (R&D, 5 000)         • CNRS (LTM, LMGP, etc.)  • UGA            │
│  • Soitec (substrats)           • INRIA                    • IUT Grenoble  │
│  • SET (packaging)              • IRT Nanoelec            • Polytech       │
│  • RECIF (handling)             • 200+ thèses/an          • ENSE3          │
│  • 50+ PME/start-ups                                                       │
│                                                                             │
│  SUPPORT                        INFRASTRUCTURE             GOUVERNANCE      │
│  ───────                        ──────────────             ───────────      │
│  • Minalogic (pôle)             • GIANT campus            • Métropole      │
│  • BPI, banques                 • Presqu'île scientif.    • Région AURA    │
│  • Incubateurs (GRAIN)          • Polygone scientifique   • Préfecture     │
│  • Avocats PI, conseils         • Salle blanche 12 000 m² • État (DRARI)   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Plan de Développement 2027-2047

**Phase 1 (2027-2032) : Consolidation et Extension**

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| Extension STMicro Crolles | +20K wafers/mois, FDSOI 12nm | 7,5 Md€ | +3 000 |
| Campus Microélectronique Alpes | Extension formation, recherche | 300 M€ | +500 |
| Parc équipementiers Grésivaudan | Zone dédiée fournisseurs | 200 M€ | +2 000 |
| Renforcement CEA-Leti | Nouvelles lignes pilotes | 500 M€ | +300 |

**Phase 2 (2032-2039) : Montée en Puissance**

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| Pilote FDSOI 10nm | Ligne R&D vers production | 4 Md€ | +1 500 |
| Extension Soitec | Nouveaux substrats (SiC, GaN) | 1,5 Md€ | +1 500 |
| PackFrance 3D | Usine packaging avancé | 2 Md€ | +2 000 |
| Écosystème équipementiers | 10 ETI, 30 PME | 3 Md€ | +5 000 |

**Phase 3 (2039-2047) : Leadership**

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| Production FDSOI 10nm | Volume industriel | 6 Md€ | +3 000 |
| Centre d'excellence packaging | R&D mondiale | 1 Md€ | +500 |
| Consolidation écosystème | Croissance organique | 5 Md€ | +10 000 |

#### Contraintes et Solutions

| Contrainte | Impact | Solution |
|------------|--------|----------|
| Saturation foncière | Limite extension | Densification, Nord-Isère, Lyon |
| Tension immobilière | Attractivité talents | Programme logement dédié |
| Transports | Congestion | Prolongement tram, navettes |
| Eau | Besoins croissants | Recyclage, nouvelle ressource |

#### Gouvernance Locale

- **Pilotage** : Comité stratégique Grenoble-Alpes Semi
- **Membres** : Métropole, Région, État, STMicro, CEA, Soitec, UGA
- **Mission** : Coordination investissements, aménagement, formation

---

### 4.2 Pôle Paris-Saclay (Conception et R&D)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Pôle conception et R&D |
| **Périmètre** | Plateau de Saclay + Sud Paris |
| **Population bassin** | 3 000 000 habitants (IDF Sud) |
| **Emplois semi 2026** | 10 000 |
| **Emplois semi 2047** | 40 000 |
| **Croissance** | +30 000 emplois (+300%) |
| **Investissement** | 15 Md€ |

#### Vocation

- **Architecture et conception SoC** : Centres de design des grands groupes
- **R&D amont** : Recherche fondamentale (X, ENS, Centrale)
- **Start-ups fabless** : Écosystème RISC-V, IA
- **Sièges et fonctions support** : Direction, stratégie, finance

#### Écosystème Cible 2047

| Composante | Description | Emplois |
|------------|-------------|---------|
| Centres de design | STMicro, Thales, nouveaux entrants | 8 000 |
| Start-ups fabless | 50+ entreprises conception | 5 000 |
| R&D académique | Polytechnique, CEA-List, CNRS | 4 000 |
| Éditeurs EDA | Outils de conception | 1 500 |
| Services conception | Design houses, vérification | 6 000 |
| Sièges et support | Fonctions corporate | 8 000 |
| Formation | Campus, écoles | 2 500 |
| Autres | Conseil, juridique, finance | 5 000 |

#### Projets Structurants

| Projet | Description | Investissement | Calendrier |
|--------|-------------|----------------|------------|
| Campus Semi Saclay | Regroupement formation/recherche | 400 M€ | 2027-2032 |
| Incubateur RISC-V | Accélérateur start-ups conception | 100 M€ | 2027-2030 |
| Centre Thales Semi | Extension activités microélectronique | 500 M€ | 2028-2035 |
| Design Center STMicro | Nouveau centre 2 000 personnes | 300 M€ | 2029-2033 |
| Pôle EDA France | Éditeurs outils conception | 200 M€ | 2030-2038 |

---

### 4.3 Pôle Toulouse-Occitanie (Packaging et Test)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Pôle packaging, test, spatial |
| **Périmètre** | Toulouse Métropole + Montpellier |
| **Population bassin** | 1 500 000 habitants |
| **Emplois semi 2026** | 6 000 |
| **Emplois semi 2047** | 30 000 |
| **Croissance** | +24 000 emplois (+400%) |
| **Investissement** | 18 Md€ |

#### Vocation et Justification

| Argument | Détail |
|----------|--------|
| Écosystème aérospatial | Airbus, Thales Alenia Space, CNES = clients naturels |
| Compétences systèmes | Intégration, test, qualification bien établis |
| Foncier disponible | Zones d'activité extensibles |
| Formation | ISAE, INSA, université = vivier |
| Qualité de vie | Attractivité talents, coût modéré |

#### Spécialisation

1. **Packaging avancé** : Centre d'excellence 2.5D/3D, chiplets
2. **Test et caractérisation** : ATE, burn-in, qualification
3. **Applications spatiales** : Composants durcis radiation
4. **Intégration systèmes** : Modules, cartes, sous-ensembles

#### Projets Structurants

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| PackFrance Toulouse | Usine packaging avancé | 2,5 Md€ | 3 000 |
| Centre de test national | Plateforme mutualisée ATE | 500 M€ | 1 000 |
| OSAT Spatial | Packaging haute fiabilité espace | 400 M€ | 500 |
| Campus Semi Toulouse | Formation packaging/test | 250 M€ | — |
| Extension NXP/Continental | Croissance acteurs existants | 1 Md€ | 2 000 |

#### Synergie Aérospatiale

| Domaine | Synergie | Bénéfice |
|---------|----------|----------|
| Fiabilité | Expertise qualification aéro → semi | Standards, méthodes |
| Test | Équipements de test partagés | Mutualisation |
| Clients | Airbus, Thales = clients semi | Débouchés garantis |
| Talents | Ingénieurs systèmes disponibles | Reconversion facile |

---

### 4.4 Pôle Nord-France (Fab Souveraine)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Pôle industriel, fab souveraine |
| **Périmètre** | Hauts-de-France (Douaisis, Valenciennois, Dunkerquois) |
| **Population bassin** | 2 000 000 habitants |
| **Emplois semi 2026** | 500 (quasi néant) |
| **Emplois semi 2047** | 25 000 |
| **Croissance** | +24 500 emplois (création) |
| **Investissement** | 25 Md€ |

#### Justification Stratégique

| Argument | Détail |
|----------|--------|
| **Reconversion industrielle** | Région touchée par désindustrialisation |
| **Main d'œuvre** | Tradition industrielle, techniciens disponibles |
| **Foncier** | Vastes zones industrielles disponibles |
| **Eau** | Nappes abondantes, canaux |
| **Énergie** | Nucléaire (Gravelines), éolien offshore |
| **Logistique** | Ports (Dunkerque), rail, autoroutes, tunnel |
| **Europe** | Proximité Belgique, Pays-Bas, Allemagne |

#### Projet Phare : Fab France 14nm

| Caractéristique | Spécification |
|-----------------|---------------|
| Technologie | 14nm FinFET (licence Intel) |
| Capacité | 40 000 wafers 300mm / mois |
| Surface site | 50 hectares |
| Surface salle blanche | 35 000 m² |
| Investissement | 18 Md€ |
| Emplois directs | 5 000 |
| Emplois indirects | 12 000 |
| Calendrier | 2029-2038 |

#### Sélection du Site

**Critères d'évaluation**

| Site candidat | Eau | Énergie | Foncier | Accès | Main d'œuvre | Score |
|---------------|-----|---------|---------|-------|--------------|-------|
| Dunkerque | ★★★ | ★★★ | ★★★ | ★★★ | ★★ | 14/15 |
| Douai/Lens | ★★ | ★★ | ★★★ | ★★ | ★★★ | 12/15 |
| Valenciennes | ★★ | ★★ | ★★ | ★★ | ★★★ | 11/15 |
| Amiens | ★★ | ★★ | ★★★ | ★★ | ★★ | 11/15 |

**Recommandation** : Zone de Dunkerque (Grande-Synthe ou arrière-port)
- Eau : Canal, mer (désalinisation possible)
- Énergie : Centrale Gravelines (5,4 GW), éolien offshore
- Foncier : Zones portuaires et industrielles vastes
- Logistique : Port, rail, A16, tunnel sous la Manche

#### Écosystème à Créer

| Composante | Description | Emplois |
|------------|-------------|---------|
| Fab 14nm | Production semiconducteurs | 5 000 |
| Fournisseurs process | Gaz, chimie, consommables | 3 000 |
| Équipementiers | Maintenance, pièces | 2 000 |
| Sous-traitants | Services industriels | 4 000 |
| Formation | Campus, centres AFPA | 500 |
| R&D appliquée | Antenne CEA | 500 |
| Services | Support, logistique | 3 000 |
| Back-office | Administration, support | 2 000 |

#### Reconversion et Emploi Local

| Source | Profils | Potentiel | Formation nécessaire |
|--------|---------|-----------|---------------------|
| Automobile (PSA, Renault) | Techniciens production | 3 000 | 6-9 mois |
| Sidérurgie | Techniciens process | 1 000 | 6-12 mois |
| Chimie | Opérateurs, techniciens | 1 500 | 4-6 mois |
| Rail (Alstom) | Maintenance, qualité | 1 000 | 6-9 mois |
| Logistique | Opérateurs | 2 000 | 3-6 mois |
| Jeunes diplômés | BUT, BTS, ingénieurs | 5 000 | Formation initiale |

#### Calendrier de Développement

| Phase | Période | Actions | Investissement |
|-------|---------|---------|----------------|
| Préparation | 2027-2029 | Site, permis, recrutement équipe projet | 500 M€ |
| Construction | 2029-2033 | Bâtiments, infrastructure, utilities | 6 Md€ |
| Équipement | 2032-2036 | Installation équipements, qualification | 10 Md€ |
| Ramp-up | 2036-2038 | Montée en production | 1,5 Md€ |
| Extension | 2038-2045 | Doublement capacité possible | 6 Md€ |

---

### 4.5 Pôle Lyon-Métropole (Équipements et Matériaux)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Pôle équipements et matériaux |
| **Périmètre** | Métropole de Lyon + Saint-Étienne |
| **Population bassin** | 2 200 000 habitants |
| **Emplois semi 2026** | 3 000 |
| **Emplois semi 2047** | 18 000 |
| **Croissance** | +15 000 emplois (+500%) |
| **Investissement** | 8 Md€ |

#### Vocation

1. **Équipementiers process** : Gravure, dépôt, nettoyage
2. **Matériaux et chimie** : Précurseurs, gaz, slurries
3. **Mécanique de précision** : Composants pour équipements
4. **Support Grenoble** : Extension naturelle du hub

#### Justification

| Argument | Détail |
|----------|--------|
| Tradition industrielle | Mécanique, chimie, plasturgie |
| Proximité Grenoble | 1h, complémentarité naturelle |
| Formation | INSA Lyon, Centrale Lyon, CPE |
| Tissu PME | Base pour création équipementiers |
| Chimie | Couloir chimie Rhône = atout |

#### Projets Structurants

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| PlasmaFab | Équipementier gravure plasma | 800 M€ | 1 200 |
| DepotTech | Équipementier dépôt ALD/CVD | 600 M€ | 900 |
| Cluster chimie électronique | 5-7 PME précurseurs/chimie | 500 M€ | 1 500 |
| Centre mécanique précision | Sous-ensembles équipements | 300 M€ | 1 000 |
| Extension Air Liquide | Capacité gaz électroniques | 400 M€ | 500 |

---

### 4.6 Pôle Rennes-Bretagne (Télécom et Cybersécurité)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Pôle télécom, RF, cybersécurité |
| **Périmètre** | Rennes + Lannion |
| **Population bassin** | 700 000 habitants |
| **Emplois semi 2026** | 4 000 |
| **Emplois semi 2047** | 12 000 |
| **Croissance** | +8 000 emplois (+200%) |
| **Investissement** | 5 Md€ |

#### Vocation

1. **Composants RF/télécom** : 5G/6G, radar, satellite
2. **Cybersécurité hardware** : Puces sécurisées, DGA
3. **Systèmes embarqués** : Applications défense, navale
4. **Design services** : Conception sous contrat

#### Atouts Spécifiques

| Atout | Détail |
|-------|--------|
| Historique télécom | Orange Labs, Nokia (ex-Alcatel) |
| DGA | Direction générale de l'armement présente |
| STMicro Rennes | Site établi, R&D RF |
| Formation | INSA Rennes, Université, ENSTA |
| Cybersécurité | Pôle d'excellence cyber |

#### Projets Structurants

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| Extension STMicro RF | Capacité composants RF | 800 M€ | 1 500 |
| Centre sécurité hardware | R&D puces sécurisées | 300 M€ | 500 |
| Cluster télécom semi | Start-ups 5G/6G | 400 M€ | 1 500 |
| Design center défense | Conception systèmes DGA | 200 M€ | 500 |

---

### 4.7 Pôle Sophia-PACA (Design et Photonique)

---

#### Fiche d'Identité

| Caractéristique | Valeur |
|-----------------|--------|
| **Statut** | Pôle design, photonique |
| **Périmètre** | Sophia Antipolis + Marseille |
| **Population bassin** | 1 200 000 habitants |
| **Emplois semi 2026** | 3 000 |
| **Emplois semi 2047** | 8 000 |
| **Croissance** | +5 000 emplois (+167%) |
| **Investissement** | 3 Md€ |

#### Vocation

1. **Design fabless** : Conception de circuits
2. **Photonique intégrée** : Datacom, LiDAR
3. **Start-ups** : Innovation, niches
4. **Services** : Design services, vérification

#### Projets Structurants

| Projet | Description | Investissement | Emplois |
|--------|-------------|----------------|---------|
| Centre photonique PACA | Excellence photonique intégrée | 400 M€ | 800 |
| Incubateur design | Start-ups fabless | 150 M€ | 1 000 |
| Extension ARM France | Centre de design | 200 M€ | 500 |

---

## 5. Infrastructures et Réseaux

### 5.1 Infrastructures Mutualisées

#### Salles Blanches Partagées

| Site | Localisation | Surface | Accès | Investissement |
|------|--------------|---------|-------|----------------|
| SB Grenoble (CEA-Leti) | Grenoble | 12 000 m² | Partenaires | Existant + 200 M€ |
| SB Saclay | Saclay | 3 000 m² | Académique + PME | 150 M€ |
| SB Toulouse | Toulouse | 2 000 m² | Packaging/test | 100 M€ |
| SB Nord | Dunkerque | 1 000 m² | Formation | 80 M€ |

#### Centres de Calcul et Simulation

| Centre | Localisation | Capacité | Usage |
|--------|--------------|----------|-------|
| GENCI/IDRIS | Saclay | 30 PFlops | Simulation TCAD, EDA |
| Centre calcul Grenoble | Grenoble | 5 PFlops | R&D process |
| Centre IA semi | Toulouse | 10 PFlops | IA pour conception |

#### Plateformes de Test

| Plateforme | Localisation | Équipements | Accès |
|------------|--------------|-------------|-------|
| Test national | Toulouse | ATE Teradyne, Advantest | Mutualisé |
| Caractérisation | Grenoble | Équipements de pointe | CEA + industrie |
| Fiabilité | Rennes | Burn-in, stress | Défense + industrie |

### 5.2 Réseaux de Transport

#### Liaisons Inter-Pôles

| Liaison | Mode | Temps 2026 | Temps 2035 (objectif) |
|---------|------|------------|----------------------|
| Grenoble - Lyon | TER/TGV | 1h20 | 45 min (LGV) |
| Grenoble - Paris | TGV | 2h50 | 2h30 (LGV) |
| Paris - Toulouse | TGV | 4h10 | 3h10 (LGV GPSO) |
| Paris - Nord | TGV | 1h00 | 1h00 |
| Paris - Rennes | TGV | 1h30 | 1h30 |
| Lyon - Toulouse | TGV | 4h00 | 2h30 (LGV) |

#### Desserte Aérienne

| Pôle | Aéroport | Lignes directes internationales |
|------|----------|--------------------------------|
| Grenoble | Lyon-Saint-Exupéry (1h) | 100+ destinations |
| Saclay | Paris CDG/Orly | Hub mondial |
| Toulouse | Toulouse-Blagnac | 80+ destinations |
| Nord | Lille-Lesquin + Bruxelles | 50+ destinations |
| Rennes | Rennes-Saint-Jacques | 30 destinations |
| Sophia | Nice-Côte d'Azur | 100+ destinations |

#### Recommandations Transport

| Projet | Priorité | Impact |
|--------|----------|--------|
| LGV Lyon-Turin | Haute | Connexion Italie, fret |
| LGV GPSO (Toulouse) | Haute | Désenclavement Sud-Ouest |
| Amélioration Grenoble-Lyon | Haute | Fluidité hub central |
| Fret ferroviaire dédié | Moyenne | Logistique équipements |

### 5.3 Réseaux Numériques

| Infrastructure | Couverture | Débit | Investissement |
|----------------|------------|-------|----------------|
| Fibre optique THD | Tous pôles | 10 Gbps | Existant |
| Réseau privé semi | Inter-pôles | 100 Gbps | 50 M€ |
| 5G industrielle | Sites fab | Ultra-low latency | 100 M€ |
| Datacenter souverain | Grenoble + Saclay | 50 MW | 500 M€ |

### 5.4 Réseaux Énergétiques

#### Alimentation Électrique

| Pôle | Source principale | Puissance garantie | Backup |
|------|-------------------|-------------------|--------|
| Grenoble | Hydro + nucléaire | 300 MW | Double alimentation |
| Saclay | Nucléaire | 100 MW | Générateurs |
| Toulouse | Mix | 150 MW | Double alimentation |
| Nord | Nucléaire Gravelines | 250 MW | Offshore éolien |
| Lyon | Nucléaire + hydro | 100 MW | Double alimentation |

#### Production Décarbonée Dédiée

| Projet | Localisation | Puissance | Investissement |
|--------|--------------|-----------|----------------|
| Parc solaire Grenoble | Nord-Isère | 50 MW | 50 M€ |
| Éolien offshore Nord | Dunkerque | 100 MW | 200 M€ |
| PPA nucléaire | National | 500 MW | Contrats |

---

## 6. Équilibre et Cohésion Territoriale

### 6.1 Répartition des Emplois

| Région | Emplois 2026 | Emplois 2047 | Part 2026 | Part 2047 | Évolution |
|--------|--------------|--------------|-----------|-----------|-----------|
| Auvergne-Rhône-Alpes | 28 000 | 88 000 | 56% | 44% | -12 pts |
| Île-de-France | 10 000 | 40 000 | 20% | 20% | = |
| Occitanie | 6 000 | 30 000 | 12% | 15% | +3 pts |
| Hauts-de-France | 500 | 25 000 | 1% | 12% | +11 pts |
| Bretagne | 4 000 | 12 000 | 8% | 6% | -2 pts |
| PACA | 3 000 | 8 000 | 6% | 4% | -2 pts |
| Autres | 500 | 7 000 | 1% | 3% | +2 pts |
| **TOTAL** | **50 000** | **210 000** | **100%** | **100%** | |

**Objectif atteint** : Réduction de la concentration AuRA de 56% à 44%, création d'un nouveau pôle majeur dans le Nord (+24 500 emplois dans une région en difficulté).

### 6.2 Intégration des Territoires en Reconversion

#### Hauts-de-France : Transformation Industrielle

| Bassin | Emplois industriels perdus (2000-2025) | Emplois semi 2047 | Taux de compensation |
|--------|----------------------------------------|-------------------|---------------------|
| Dunkerquois | 8 000 | 15 000 | 188% |
| Douaisis | 6 000 | 5 000 | 83% |
| Valenciennois | 10 000 | 3 000 | 30% |
| Lens-Béthune | 12 000 | 2 000 | 17% |
| **Total HdF** | **36 000** | **25 000** | **69%** |

#### Mesures d'Accompagnement

| Mesure | Description | Budget |
|--------|-------------|--------|
| Reconversion professionnelle | Formation 10 000 personnes | 400 M€ |
| Aide à la mobilité | Déménagement, transport | 50 M€ |
| Revitalisation urbaine | Logement, services | 300 M€ |
| Soutien PME locales | Sous-traitance, services | 200 M€ |

### 6.3 Accessibilité Emplois Semi par Territoire

| Zone | Population à <1h d'un site semi | % population FR |
|------|--------------------------------|-----------------|
| Grenoble/Lyon | 3 000 000 | 4,5% |
| Saclay/IDF | 8 000 000 | 12% |
| Toulouse | 2 000 000 | 3% |
| Nord | 4 000 000 | 6% |
| Rennes | 1 000 000 | 1,5% |
| Sophia/PACA | 2 000 000 | 3% |
| **Total couvert** | **20 000 000** | **30%** |

### 6.4 Impact Territorial Global

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IMPACT TERRITORIAL DU PLAN 2027-2047                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EMPLOIS CRÉÉS                          INVESTISSEMENTS                     │
│  ─────────────                          ───────────────                     │
│                                                                             │
│  • 160 000 emplois directs nouveaux     • 121 Md€ investis sur le territoire│
│  • 320 000 emplois indirects            • Dont 25 Md€ dans le Nord         │
│  • 480 000 emplois induits              • Répartition équilibrée           │
│                                                                             │
│  TOTAL : ~1 000 000 emplois liés aux semiconducteurs                       │
│                                                                             │
│  RECONVERSION                           FORMATION                           │
│  ───────────                            ─────────                           │
│                                                                             │
│  • 50 000 reconversions industrie       • 500 000 personnes formées        │
│  • 25 000 emplois région Nord           • 5 campus créés                   │
│  • Compensation désindustrialisation    • Formations dans toutes régions   │
│                                                                             │
│  COHÉSION                               ATTRACTIVITÉ                        │
│  ────────                               ───────────                         │
│                                                                             │
│  • Réduction concentration (56%→44%)    • 7 pôles d'excellence             │
│  • Maillage territorial                 • Compétitivité internationale     │
│  • Désenclavement régions Nord          • Rayonnement technologique        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Gouvernance Territoriale

### 7.1 Architecture de Gouvernance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GOUVERNANCE TERRITORIALE SEMICONDUCTEURS                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                       ┌─────────────────────────┐                           │
│                       │   COMITÉ NATIONAL       │                           │
│                       │   SEMICONDUCTEURS       │                           │
│                       │   (Niveau stratégique)  │                           │
│                       │                         │                           │
│                       │ • Ministères (Industrie,│                           │
│                       │   Recherche, Territoires)│                          │
│                       │ • Régions (ARF)         │                           │
│                       │ • Industriels           │                           │
│                       └────────────┬────────────┘                           │
│                                    │                                        │
│              ┌─────────────────────┼─────────────────────┐                 │
│              │                     │                     │                 │
│              ▼                     ▼                     ▼                 │
│  ┌───────────────────┐ ┌───────────────────┐ ┌───────────────────┐        │
│  │ COMITÉ PÔLE       │ │ COMITÉ PÔLE       │ │ COMITÉ PÔLE       │        │
│  │ GRENOBLE-ALPES    │ │ NORD-FRANCE       │ │ TOULOUSE          │        │
│  │                   │ │                   │ │                   │        │
│  │ • Région AURA     │ │ • Région HdF      │ │ • Région Occitanie│        │
│  │ • Métropole       │ │ • Métropole Lille │ │ • Métropole       │        │
│  │ • Départements    │ │ • Communauté agglo│ │ • Départements    │        │
│  │ • Industriels     │ │ • Industriels     │ │ • Industriels     │        │
│  │ • Académiques     │ │ • Académiques     │ │ • Académiques     │        │
│  └───────────────────┘ └───────────────────┘ └───────────────────┘        │
│              │                     │                     │                 │
│              └─────────────────────┼─────────────────────┘                 │
│                                    ▼                                        │
│                       ┌─────────────────────────┐                           │
│                       │   AGENCE NATIONALE      │                           │
│                       │   SEMICONDUCTEURS       │                           │
│                       │   (Niveau opérationnel) │                           │
│                       │                         │                           │
│                       │ • Coordination projets  │                           │
│                       │ • Suivi investissements │                           │
│                       │ • Interface Europe      │                           │
│                       └─────────────────────────┘                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Rôles et Responsabilités

| Niveau | Acteur | Responsabilités |
|--------|--------|-----------------|
| **National** | État (SGPI, DGE) | Stratégie, financement, réglementation |
| **National** | Comité national semi | Arbitrages, coordination inter-pôles |
| **Régional** | Régions | Aménagement, formation, aides |
| **Régional** | Comités de pôle | Coordination locale, projets |
| **Local** | Métropoles, agglos | Foncier, urbanisme, services |
| **Opérationnel** | Agence nationale | Mise en œuvre, reporting |

### 7.3 Contrats de Pôle

**Contrats État-Région-Métropole** pour chaque pôle, incluant :

| Volet | Contenu |
|-------|---------|
| Investissements | Engagements chiffrés par partenaire |
| Emplois | Objectifs création d'emplois |
| Formation | Capacités de formation |
| Foncier | Réserves foncières, ZAC |
| Infrastructures | Transports, réseaux, utilités |
| Gouvernance | Instances, reporting, évaluation |

### 7.4 Articulation avec les CPER

| CPER | Volet semiconducteurs | Montant |
|------|----------------------|---------|
| CPER AURA 2028-2034 | Campus, infrastructures, R&D | 800 M€ |
| CPER IDF 2028-2034 | Campus Saclay, incubateurs | 500 M€ |
| CPER Occitanie 2028-2034 | Packaging, test, formation | 600 M€ |
| CPER HdF 2028-2034 | Fab, reconversion, formation | 1 200 M€ |
| CPER Bretagne 2028-2034 | Télécom, cyber, formation | 300 M€ |
| Autres CPER | Antennes, formation | 400 M€ |
| **Total CPER** | | **3 800 M€** |

---

## 8. Plan d'Action et Investissements

### 8.1 Synthèse des Investissements par Pôle

| Pôle | Phase 1 (2027-32) | Phase 2 (2032-39) | Phase 3 (2039-47) | Total |
|------|-------------------|-------------------|-------------------|-------|
| Grenoble-Alpes | 15 Md€ | 18 Md€ | 12 Md€ | 45 Md€ |
| Paris-Saclay | 5 Md€ | 6 Md€ | 4 Md€ | 15 Md€ |
| Toulouse | 5 Md€ | 8 Md€ | 5 Md€ | 18 Md€ |
| Nord-France | 7 Md€ | 12 Md€ | 6 Md€ | 25 Md€ |
| Lyon | 2 Md€ | 4 Md€ | 2 Md€ | 8 Md€ |
| Rennes | 1,5 Md€ | 2 Md€ | 1,5 Md€ | 5 Md€ |
| Sophia-PACA | 1 Md€ | 1,2 Md€ | 0,8 Md€ | 3 Md€ |
| Autres/National | 0,5 Md€ | 1 Md€ | 0,5 Md€ | 2 Md€ |
| **TOTAL** | **37 Md€** | **52,2 Md€** | **31,8 Md€** | **121 Md€** |

### 8.2 Sources de Financement Territorial

| Source | Part | Montant | Mécanismes |
|--------|------|---------|------------|
| Industriels | 35% | 42 Md€ | Investissements privés |
| État | 30% | 36 Md€ | France 2030, LFI, BPI |
| Europe | 20% | 24 Md€ | Chips Act, FEDER, IPCEI |
| Régions | 10% | 12 Md€ | CPER, aides régionales |
| Autres (banques, etc.) | 5% | 7 Md€ | Prêts, fonds |
| **Total** | **100%** | **121 Md€** | |

### 8.3 Calendrier Territorial

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CALENDRIER DÉPLOIEMENT TERRITORIAL                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  2027   2029   2031   2033   2035   2037   2039   2041   2043   2045   2047│
│    │      │      │      │      │      │      │      │      │      │      │ │
│                                                                             │
│  GRENOBLE-ALPES                                                            │
│  ══════════════════════════════════════════════════════════════════════    │
│  Extension STMicro████████████████████████████░░░░░░░░░░░░░░░░░░░░░░ Vol. │
│  FDSOI 12nm      ████████████████████████████████████████░░░░░░░░░░ Prod  │
│  FDSOI 10nm              R&D████████████████████████████████████░░░ Pilote│
│                                                                             │
│  NORD-FRANCE                                                               │
│  ══════════════════════════════════════════════════════════════════════    │
│  Site + permis   ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │
│  Construction          ████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │
│  Équipement                        ████████████████░░░░░░░░░░░░░░░░░░░░   │
│  Production                                    ████████████████████████    │
│                                                                             │
│  TOULOUSE                                                                  │
│  ══════════════════════════════════════════════════════════════════════    │
│  PackFrance      ██████████████████████████████████████████████████████    │
│  Centre test           ██████████████████████████░░░░░░░░░░░░░░░░░░░░░░   │
│                                                                             │
│  SACLAY                                                                    │
│  ══════════════════════════════════════════════════════════════════════    │
│  Campus Semi     ██████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │
│  Incubateur RISC-V ████████████████████████████████████████████████████    │
│                                                                             │
│  LYON                                                                      │
│  ══════════════════════════════════════════════════════════════════════    │
│  Équipementiers  ████████████████████████████████████████████████████████  │
│                                                                             │
│  RENNES                                                                    │
│  ══════════════════════════════════════════════════════════════════════    │
│  Extension RF    ████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░   │
│                                                                             │
│  LÉGENDE : ████ Réalisation │ ░░░░ Montée en charge/extension             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 8.4 Indicateurs de Suivi Territorial

| Indicateur | 2027 | 2032 | 2039 | 2047 |
|------------|------|------|------|------|
| Emplois semi total | 52 000 | 90 000 | 150 000 | 210 000 |
| Emplois hors AuRA+IDF | 12 000 | 35 000 | 65 000 | 82 000 |
| Part AuRA | 54% | 48% | 45% | 42% |
| Part Nord (HdF) | 1% | 5% | 10% | 12% |
| Investissements cumulés | 5 Md€ | 37 Md€ | 89 Md€ | 121 Md€ |
| Formations dispensées/an | 3 000 | 8 000 | 12 000 | 12 000 |
| Pôles actifs | 5 | 7 | 7 | 7 |

---

## Annexes

### A.1 Fiches Sites Potentiels Fab Nord-France

#### Site 1 : Grande-Synthe (Dunkerque)

| Critère | Évaluation |
|---------|------------|
| Surface disponible | 80 ha (zone industrialo-portuaire) |
| Eau | Canal, mer, usine désalinisation possible |
| Énergie | Gravelines 12 km (5,4 GW nucléaire) |
| Transport | Port, A16, gare Dunkerque |
| Main d'œuvre | Bassin 200 000 actifs |
| Fiscalité | Zone franche |
| **Score global** | ★★★★★ (Recommandé) |

#### Site 2 : Douvrin (Lens-Béthune)

| Critère | Évaluation |
|---------|------------|
| Surface disponible | 50 ha (ex-site PSA) |
| Eau | Canal, nappes |
| Énergie | Réseau THT, 50 km Gravelines |
| Transport | A1, A26, gare TGV Lens |
| Main d'œuvre | Bassin 300 000 actifs, tradition auto |
| **Score global** | ★★★★☆ |

### A.2 Cartographie Foncière Détaillée

| Pôle | Sites identifiés | Superficie totale | Disponibilité |
|------|------------------|-------------------|---------------|
| Grenoble | Crolles extension, Nord-Isère | 100 ha | Partielle |
| Saclay | Plateau de Saclay | 50 ha | Limitée |
| Toulouse | Francazal, Labège extension | 150 ha | Bonne |
| Nord | Grande-Synthe, Douvrin, Maubeuge | 300 ha | Excellente |
| Lyon | Est lyonnais, Saint-Priest | 80 ha | Moyenne |

### A.3 Besoins en Infrastructures par Pôle

| Pôle | Transports | Énergie | Eau | Télécom |
|------|-----------|---------|-----|---------|
| Grenoble | Tram extension, A480 | +100 MW | Recyclage | 5G indus |
| Saclay | Ligne 18 métro | +50 MW | Réseaux | Fibre THD |
| Toulouse | Rocade Est | +100 MW | Station dédiée | 5G indus |
| Nord | A16/port, fer | +200 MW | Désalinisation | Fibre THD |
| Lyon | A46, TER | +50 MW | Rhône | 5G indus |

---

*Document de référence — Version 0.1*  
*Projet GenToGen2027 / TOGAFrance*
