# SVT_IT_ANX_B — Plan de Formation et Cursus
## Plan de Souveraineté IT 2027-2047

---

**Document de référence** : SVT_IT_00, SVT_IT_ANX_00, SVT_IT_ANX_A  
**Classification** : Public  
**Auteur** : Jeff / Jagrat  
**Date** : Janvier 2026  
**Version** : 0.1

---

## Sommaire

1. [Diagnostic de l'Offre Actuelle](#1-diagnostic-de-loffre-actuelle)
2. [Objectifs de Formation 2027-2047](#2-objectifs-de-formation)
3. [Nouveaux Cursus à Créer](#3-nouveaux-cursus-à-créer)
4. [Réforme des Cursus Existants](#4-réforme-des-cursus-existants)
5. [Formation Continue et Reconversion](#5-formation-continue-et-reconversion)
6. [Infrastructure de Formation](#6-infrastructure-de-formation)
7. [Attractivité et Talents Internationaux](#7-attractivité-internationale)
8. [Gouvernance et Pilotage](#8-gouvernance-et-pilotage)
9. [Budget et Financement](#9-budget-et-financement)

---

## 1. Diagnostic de l'Offre Actuelle

### 1.1 Cartographie des Formations Existantes

#### Niveau Doctorat (Bac+8)

| École Doctorale | Spécialités | Thèses/an | Localisation |
|-----------------|-------------|-----------|--------------|
| ED Électronique, Électrotechnique, Automatique (EEA) | Microélectronique, Conception | 80 | Grenoble |
| ED PHAST | Physique, Matériaux | 60 | Lyon |
| ED Interfaces | Nanoélectronique | 50 | Saclay |
| ED Sciences et Technologies de l'Information | Conception, Systèmes | 40 | Toulouse |
| ED Matière, Molécules, Matériaux | Matériaux semiconducteurs | 30 | Rennes |
| Autres ED | Divers | 90 | National |
| **TOTAL** | | **350** | |

**Constat** : 350 docteurs/an contre 700 nécessaires à terme. Gap de 100%.

#### Niveau Ingénieur/Master (Bac+5)

| Établissement | Formation | Diplômés/an | Spécificité |
|---------------|-----------|-------------|-------------|
| Grenoble INP - Phelma | Ingénieur Microélectronique | 120 | Référence nationale process |
| INSA Lyon | Ingénieur Génie Électrique | 80 | Double compétence |
| Polytech Grenoble | Ingénieur Microélectronique | 40 | Formation terrain |
| CentraleSupélec | Master Nanoélectronique | 35 | Excellence académique |
| Télécom Paris | Ingénieur Systèmes Électroniques | 50 | Systèmes et télécom |
| ENSEIRB-MATMECA | Ingénieur Électronique | 60 | Conception numérique |
| ENSEEIHT | Ingénieur Électronique | 45 | Systèmes embarqués |
| Université Grenoble Alpes | Master Microélectronique | 60 | Recherche |
| Université Paris-Saclay | Master Nanotech | 50 | Interdisciplinaire |
| Autres établissements | Divers | 200 | National |
| **TOTAL formations dédiées** | | **740** | |
| **TOTAL formations connexes** | | **1 800** | Électronique générale |

**Constat** : ~2 500 ingénieurs/an avec compétences mobilisables contre 4 500 nécessaires. Gap de 80%.

#### Niveau Technicien (Bac+2/3)

| Formation | Établissements | Diplômés/an | Adéquation |
|-----------|---------------|-------------|------------|
| BTS Systèmes Numériques | 150 lycées | 3 000 | Partielle |
| BUT GEII | 50 IUT | 2 500 | Partielle |
| BUT Mesures Physiques | 30 IUT | 1 200 | Bonne |
| BUT Chimie | 25 IUT | 800 | Partielle |
| Licence Pro Électronique | 20 universités | 400 | Bonne |
| **TOTAL mobilisable** | | **~3 000** | Après adaptation |

**Constat** : Formations existantes mais non spécialisées semiconducteurs. Besoin de spécialisation.

#### Niveau Opérateur (Bac/Bac Pro)

| Formation | Établissements | Diplômés/an |
|-----------|---------------|-------------|
| Bac Pro MELEC | 300 lycées | 8 000 |
| Bac Pro PLP | 100 lycées | 2 500 |
| Bac STI2D | 400 lycées | 15 000 |
| **TOTAL mobilisable** | | **~5 000** | Après formation complémentaire |

**Constat** : Vivier existant mais nécessite formation complémentaire salle blanche (3-6 mois).

### 1.2 Analyse des Lacunes Critiques

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CARTOGRAPHIE DES LACUNES DE FORMATION                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORMATIONS INEXISTANTES                    FORMATIONS INSUFFISANTES        │
│  ──────────────────────                    ─────────────────────────        │
│                                                                             │
│  ┌─────────────────────────────┐          ┌─────────────────────────────┐  │
│  │ • Conception d'équipements  │          │ • Architectes SoC/CPU       │  │
│  │   semiconducteurs           │          │   (35/an vs 150 nécessaires)│  │
│  │                             │          │                             │  │
│  │ • Ingénierie lithographie   │          │ • Process avancés           │  │
│  │   (hors ASML interne)       │          │   (80/an vs 250 nécessaires)│  │
│  │                             │          │                             │  │
│  │ • Packaging 3D/Avancé       │          │ • Conception RISC-V         │  │
│  │   (aucune formation)        │          │   (0/an vs 120 nécessaires) │  │
│  │                             │          │                             │  │
│  │ • Conception mémoires       │          │ • Techniciens salle blanche │  │
│  │   DRAM/HBM                  │          │   spécialisés               │  │
│  │                             │          │   (500/an vs 2000 nécess.)  │  │
│  │ • EDA/CAO semiconducteurs   │          │                             │  │
│  └─────────────────────────────┘          └─────────────────────────────┘  │
│                                                                             │
│  FORMATIONS MAL ADAPTÉES                   FORMATIONS BIEN POSITIONNÉES    │
│  ───────────────────────                   ────────────────────────────    │
│                                                                             │
│  ┌─────────────────────────────┐          ┌─────────────────────────────┐  │
│  │ • BTS/BUT trop généralistes │          │ • Phelma microélectronique  │  │
│  │   (pas de spé semiconducteur)│          │   (référence nationale)     │  │
│  │                             │          │                             │  │
│  │ • Masters recherche sans    │          │ • Masters conception        │  │
│  │   débouchés industriels     │          │   circuits (Saclay, Lyon)   │  │
│  │                             │          │                             │  │
│  │ • Écoles généralistes sans  │          │ • Doctorats CIFRE avec      │  │
│  │   modules semiconducteurs   │          │   STMicro, Soitec           │  │
│  └─────────────────────────────┘          └─────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Benchmark International

| Pays | Diplômés microélectronique/an | Population | Ratio /million hab. |
|------|------------------------------|------------|---------------------|
| Taïwan | 12 000 | 24 M | 500 |
| Corée du Sud | 15 000 | 52 M | 288 |
| États-Unis | 25 000 | 330 M | 76 |
| Chine | 200 000 | 1 400 M | 143 |
| Allemagne | 5 000 | 83 M | 60 |
| **France** | **2 500** | **68 M** | **37** |
| **Cible France 2040** | **10 000** | **68 M** | **147** |

**Constat** : La France doit quadrupler son ratio pour atteindre le niveau des pays leaders.

---

## 2. Objectifs de Formation 2027-2047

### 2.1 Trajectoire Globale

| Indicateur | 2026 (base) | 2032 | 2039 | 2047 |
|------------|-------------|------|------|------|
| Diplômés microélectronique/an | 2 500 | 6 000 | 9 500 | 10 200 |
| Dont Docteurs | 350 | 500 | 650 | 700 |
| Dont Ingénieurs/Masters | 750 | 2 500 | 4 000 | 4 500 |
| Dont Techniciens spécialisés | 500 | 2 000 | 3 350 | 3 500 |
| Dont Opérateurs formés | 900 | 1 000 | 1 500 | 1 500 |
| Reconversions professionnelles/an | 500 | 2 500 | 3 000 | 2 000 |
| **Total flux annuel** | **3 000** | **8 500** | **12 500** | **12 200** |

### 2.2 Objectifs par Famille de Métiers

| Famille | Flux 2026 | Flux 2032 | Flux 2039 | Flux 2047 | Cumul formés |
|---------|-----------|-----------|-----------|-----------|--------------|
| RD - Recherche | 400 | 800 | 1 000 | 1 000 | 18 000 |
| CO - Conception | 600 | 1 800 | 2 500 | 2 500 | 45 000 |
| FA - Fabrication | 1 200 | 3 500 | 5 000 | 5 000 | 90 000 |
| EQ - Équipements | 200 | 1 200 | 2 000 | 2 000 | 35 000 |
| PK - Packaging/Test | 300 | 1 000 | 1 500 | 1 500 | 25 000 |
| SU - Support | 300 | 700 | 1 000 | 1 000 | 17 000 |
| **TOTAL** | **3 000** | **9 000** | **13 000** | **13 000** | **230 000** |

### 2.3 Indicateurs de Succès

| KPI | 2026 | Cible 2032 | Cible 2039 | Cible 2047 |
|-----|------|------------|------------|------------|
| Taux d'insertion à 6 mois | 85% | 95% | 95% | 95% |
| Taux de remplissage formations | 70% | 90% | 95% | 95% |
| Satisfaction employeurs | N/A | 80% | 85% | 90% |
| Part femmes diplômées | 18% | 25% | 30% | 35% |
| Part alternance | 30% | 50% | 60% | 60% |
| Partenariats industriels actifs | 20 | 80 | 150 | 200 |

---

## 3. Nouveaux Cursus à Créer

### 3.1 Vue d'Ensemble des Créations

| Niveau | Nouveaux cursus | Capacité cible/an | Investissement |
|--------|-----------------|-------------------|----------------|
| Bac+8 | 4 programmes doctoraux | +350 | 150 M€ |
| Bac+5 | 12 formations ingénieur/master | +2 000 | 800 M€ |
| Bac+3 | 8 formations BUT/Licence Pro | +2 500 | 400 M€ |
| Bac+2 | 5 formations BTS | +1 500 | 200 M€ |
| Certifications | 15 certifications professionnelles | +3 000 | 100 M€ |
| **TOTAL** | **44 cursus** | **+9 350** | **1 650 M€** |

### 3.2 Formations Doctorales (Bac+8)

---

#### DOC-01 : Doctorat Architecture des Processeurs et Systèmes sur Puce

**Établissements porteurs** : Université Grenoble Alpes, Université Paris-Saclay, Université de Lyon

**Objectifs**
Former des chercheurs capables de concevoir les architectures de processeurs de demain (RISC-V, accélérateurs IA, processeurs quantiques classiques).

**Programme (3 ans)**

| Année | Contenu | Crédits |
|-------|---------|---------|
| A1 | Cours avancés architecture + début recherche | 60 ECTS |
| A2 | Recherche à temps plein + publications | — |
| A3 | Finalisation thèse + valorisation | — |

**Modules obligatoires**
- Architecture avancée des processeurs (microarchitecture, pipelines, caches)
- Écosystème RISC-V et extensions custom
- Conception basse consommation et haute performance
- Accélérateurs matériels pour l'IA
- Méthodologie de recherche et rédaction scientifique

**Partenariats industriels**
- STMicroelectronics, Kalray, SiPearl, Thales
- Laboratoires : CEA-List, TIMA, LIP6

**Capacité** : 50 doctorants/an (2032), 80/an (2040)

**Financement doctorants**
- 60% CIFRE (contrats industriels)
- 30% Contrats doctoraux ANR/État
- 10% Bourses européennes (ERC, MSCA)

**Débouchés**
- Architecte CPU/GPU en entreprise (60%)
- Chercheur académique (25%)
- Création de start-up (15%)

---

#### DOC-02 : Doctorat Procédés Avancés de Fabrication

**Établissements porteurs** : Université Grenoble Alpes, INSA Lyon, Université Paris-Saclay

**Objectifs**
Former des experts des procédés de fabrication pour les nœuds technologiques avancés (sub-10nm) : lithographie EUV, gravure atomique, dépôts conformes.

**Spécialisations**
1. Lithographie avancée (EUV, multi-patterning)
2. Gravure plasma et ALE (Atomic Layer Etching)
3. Dépôt de couches minces (ALD, CVD avancé)
4. Intégration 3D et packaging avancé

**Partenariats**
- STMicroelectronics (site Crolles)
- CEA-Leti
- Soitec
- Laboratoires CNRS (LTM, LMGP)

**Capacité** : 60 doctorants/an (2032), 100/an (2040)

---

#### DOC-03 : Doctorat Matériaux pour la Microélectronique

**Établissements porteurs** : Grenoble INP, INSA Lyon, École Polytechnique

**Objectifs**
Développer les compétences sur les matériaux émergents : semiconducteurs grand gap (SiC, GaN), matériaux 2D (graphène, TMD), matériaux pour le quantique.

**Axes de recherche**
- Croissance et caractérisation de matériaux III-V et III-N
- Intégration des matériaux 2D dans les filières CMOS
- Matériaux pour les qubits (supraconducteurs, défauts NV)
- Matériaux pour la photonique intégrée

**Capacité** : 40 doctorants/an (2032), 70/an (2040)

---

#### DOC-04 : Doctorat Industriel Équipements Semiconducteurs

**Établissements porteurs** : Arts et Métiers, INSA, Centrale Lyon

**Objectifs**
Former des docteurs-ingénieurs capables de concevoir les équipements de production de semiconducteurs — domaine critique pour la souveraineté.

**Spécificités**
- Thèse 100% en entreprise (équipementiers ou fabs)
- Orientation conception mécanique, optique, plasma, automatisation
- Double compétence : technologie + management de l'innovation

**Partenariats cibles**
- Futurs équipementiers français (à créer)
- Équipementiers européens (ASML via licence, SÜSS, Zeiss)
- CEA-Leti (plateforme de développement)

**Capacité** : 30 doctorants/an (2032), 50/an (2040)

---

### 3.3 Formations Ingénieur/Master (Bac+5)

---

#### ING-01 : Diplôme d'Ingénieur Architecte de Systèmes sur Puce

**Établissement** : Grenoble INP (nouvelle filière Phelma)

**Durée** : 3 ans (après prépa ou L2)

**Objectifs**
Former des architectes SoC capables de définir et implémenter des systèmes complexes intégrant processeurs, mémoires, accélérateurs et interfaces.

**Programme**

| Année | Semestre | Modules principaux | ECTS |
|-------|----------|-------------------|------|
| 1 | S1 | Fondamentaux électronique numérique, Programmation C/C++ | 30 |
| 1 | S2 | Architecture des ordinateurs, Systèmes d'exploitation | 30 |
| 2 | S3 | Conception RTL (Verilog/VHDL), Vérification UVM | 30 |
| 2 | S4 | Architecture processeurs, RISC-V, Mémoires | 30 |
| 3 | S5 | SoC avancé, Sécurité hardware, IA embarquée | 30 |
| 3 | S6 | Projet de fin d'études en entreprise | 30 |

**Compétences visées**
- Maîtrise de l'architecture des processeurs et SoC
- Expertise en conception et vérification RTL
- Connaissance de l'écosystème RISC-V
- Capacité à optimiser performance/consommation/surface

**Partenariats entreprises**
- STMicroelectronics, Thales, Kalray, SiPearl
- Start-ups conception (GreenWaves, Music not Noise)

**Capacité** : 60 diplômés/an (2030), 100/an (2040)

**Coût de création** : 25 M€

---

#### ING-02 : Diplôme d'Ingénieur Conception RISC-V et Architectures Ouvertes

**Établissement** : ENSIMAG + Phelma (formation conjointe)

**Durée** : 3 ans

**Objectifs**
Former des spécialistes de l'architecture ouverte RISC-V, capables de concevoir des cœurs processeurs et de contribuer à l'écosystème open source hardware.

**Spécificités**
- Formation centrée sur RISC-V (ISA, extensions, implémentations)
- Projets contributifs à des projets open source (CHIPS Alliance, OpenHW)
- Double compétence hardware/software (compilateurs, OS)

**Modules clés**
- Architecture RISC-V : ISA de base et extensions (M, A, F, D, C, V)
- Microarchitecture : pipelines, prédiction de branchement, caches
- Implémentation RTL de cœurs RISC-V
- Écosystème logiciel : GCC, LLVM, Linux pour RISC-V
- Sécurité et extensions custom

**Capacité** : 40 diplômés/an (2030), 80/an (2040)

**Coût de création** : 20 M€

---

#### ING-03 : Diplôme d'Ingénieur Procédés de Fabrication Semiconducteurs

**Établissement** : Grenoble INP - Phelma (renforcement filière existante)

**Durée** : 3 ans

**Objectifs**
Renforcer et moderniser la formation process pour couvrir les nœuds technologiques avancés et les nouvelles technologies (EUV, ALD, etc.).

**Évolutions par rapport à l'existant**
- Nouveaux modules lithographie EUV et multi-patterning
- Renforcement gravure atomique (ALE) et dépôt conforme (ALD)
- Module intégration 3D (TSV, hybrid bonding)
- Stage long obligatoire en fab (6 mois)

**Capacité** : De 120 à 200 diplômés/an

**Coût de renforcement** : 15 M€

---

#### ING-04 : Diplôme d'Ingénieur Conception d'Équipements Semiconducteurs

**Établissement** : Arts et Métiers + partenariat Grenoble INP

**Durée** : 3 ans

**Objectifs**
Créer LA formation française pour les futurs ingénieurs équipementiers — domaine où la France part de quasi-zéro.

**Programme**

| Domaine | Modules | Poids |
|---------|---------|-------|
| Mécanique de précision | Conception machines, Métrologie, Vibrations | 25% |
| Optique et photonique | Systèmes optiques, Sources UV/EUV, Détection | 20% |
| Plasmas et vide | Physique des plasmas, Technologies du vide | 20% |
| Automatisation | Contrôle-commande, Robotique, Vision | 20% |
| Intégration système | Architecture équipements, Normes SEMI | 15% |

**Partenariats**
- CEA-Leti (accès équipements)
- ASML (programme de formation, licences)
- Équipementiers japonais (TEL, SCREEN) via accords
- Industriels français (Air Liquide, Pfeiffer Vacuum)

**Capacité** : 50 diplômés/an (2032), 120/an (2040)

**Coût de création** : 50 M€ (inclut plateforme équipements)

---

#### ING-05 : Diplôme d'Ingénieur Packaging Avancé et Intégration 3D

**Établissement** : INSA Toulouse + partenariat STMicro

**Durée** : 3 ans

**Objectifs**
Former des spécialistes du packaging avancé (2.5D, 3D, chiplets), domaine en explosion avec la fin de la loi de Moore classique.

**Modules clés**
- Technologies de packaging (flip-chip, fan-out, embedded)
- Interconnexions avancées (TSV, µbumps, hybrid bonding)
- Gestion thermique des assemblages 3D
- Co-design package/puce
- Test et fiabilité des assemblages

**Capacité** : 40 diplômés/an (2032), 80/an (2040)

**Coût de création** : 30 M€

---

#### ING-06 : Master Conception de Mémoires Semiconducteurs

**Établissement** : Université Paris-Saclay + Université Grenoble Alpes

**Durée** : 2 ans (M1+M2)

**Objectifs**
Former des spécialistes de la conception de mémoires (SRAM, DRAM, Flash, mémoires émergentes) — compétence rare en France.

**Programme**

| Semestre | Modules |
|----------|---------|
| M1-S1 | Physique des dispositifs mémoires, Électronique analogique |
| M1-S2 | Architecture des mémoires, Conception de cellules |
| M2-S3 | DRAM/HBM avancé, Mémoires non-volatiles, Test mémoires |
| M2-S4 | Stage R&D (6 mois) |

**Capacité** : 30 diplômés/an (2035), 50/an (2040)

**Coût de création** : 15 M€

---

#### ING-07 : Master EDA et Outils de Conception Semiconducteurs

**Établissement** : Sorbonne Université + Télécom Paris

**Durée** : 2 ans

**Objectifs**
Former des ingénieurs capables de développer les outils logiciels de conception (EDA) — domaine dominé par Synopsys, Cadence et Siemens.

**Modules clés**
- Algorithmes de synthèse et optimisation
- Place & Route automatisé
- Analyse de timing et power
- Vérification formelle et simulation
- Machine learning pour l'EDA

**Capacité** : 25 diplômés/an (2035), 50/an (2040)

**Coût de création** : 12 M€

---

#### Autres formations Bac+5 à créer

| Réf. | Intitulé | Établissement | Capacité 2040 | Budget |
|------|----------|---------------|---------------|--------|
| ING-08 | Ingénieur Test et Caractérisation | ENSEEIHT | 60/an | 18 M€ |
| ING-09 | Master Photonique Intégrée | Institut d'Optique | 40/an | 15 M€ |
| ING-10 | Master Cybersécurité Hardware | Télécom Paris | 50/an | 12 M€ |
| ING-11 | Ingénieur Yield et Data Science Fab | ENSIMAG | 40/an | 10 M€ |
| ING-12 | Master Simulation et Modélisation TCAD | UGA + INSA | 30/an | 8 M€ |

---

### 3.4 Formations Technicien (Bac+2/3)

---

#### TECH-01 : BUT Fabrication Semiconducteurs

**Établissements** : Création dans 8 IUT

| Site | IUT | Capacité |
|------|-----|----------|
| Grenoble | IUT 1 | 72 |
| Lyon | IUT Lyon 1 | 48 |
| Toulouse | IUT Paul Sabatier | 48 |
| Rennes | IUT Rennes | 36 |
| Bordeaux | IUT Bordeaux | 36 |
| Saclay | IUT Orsay | 48 |
| Tours | IUT Tours | 36 |
| Lille | IUT Lille | 36 |
| **TOTAL** | | **360/an** |

**Durée** : 3 ans

**Programme**

| Année | Semestre | Contenu | Lieu |
|-------|----------|---------|------|
| BUT1 | S1-S2 | Fondamentaux physique, chimie, électronique | IUT |
| BUT2 | S3 | Procédés fabrication, métrologie | IUT + TP salle blanche |
| BUT2 | S4 | Spécialisation (litho, gravure, dépôt, CMP) | IUT + entreprise |
| BUT3 | S5-S6 | Alternance en entreprise | Entreprise |

**Référentiel de compétences**

| Bloc | Compétences | Certification |
|------|-------------|---------------|
| BC1 | Opérer en salle blanche | Habilitation SB niveau 2 |
| BC2 | Conduire les équipements de fabrication | Certifications constructeurs |
| BC3 | Réaliser les contrôles qualité | Certification métrologie |
| BC4 | Participer à l'amélioration continue | Lean/6 Sigma Yellow Belt |
| BC5 | Communiquer en contexte professionnel | Anglais B2 |

**Équipements requis par site**
- Salle blanche pédagogique (classe 1000) : 200 m²
- Équipements de démonstration (spinner, four, SEM)
- Simulateurs de procédés

**Investissement** : 8 M€/site = 64 M€ total

**Capacité totale 2040** : 800 diplômés/an

---

#### TECH-02 : BUT Packaging et Test Électronique

**Établissements** : Création dans 5 IUT

| Site | IUT | Capacité |
|------|-----|----------|
| Toulouse | IUT Paul Sabatier | 48 |
| Grenoble | IUT 1 | 36 |
| Tours | IUT Tours | 36 |
| Bordeaux | IUT Bordeaux | 36 |
| Rennes | IUT Rennes | 36 |
| **TOTAL** | | **192/an** |

**Programme spécifique**
- Technologies d'assemblage (wire bonding, flip chip, fan-out)
- Techniques de test (ATE, probe, burn-in)
- Analyse de défaillance
- Fiabilité et qualification

**Capacité totale 2040** : 400 diplômés/an

**Investissement** : 5 M€/site = 25 M€ total

---

#### TECH-03 : BTS Maintenance Équipements Semiconducteurs

**Établissements** : Création dans 10 lycées technologiques

| Région | Lycées | Capacité |
|--------|--------|----------|
| Auvergne-Rhône-Alpes | 3 | 90 |
| Île-de-France | 2 | 60 |
| Occitanie | 2 | 60 |
| Bretagne | 1 | 30 |
| Nouvelle-Aquitaine | 1 | 30 |
| Hauts-de-France | 1 | 30 |
| **TOTAL** | **10** | **300/an** |

**Durée** : 2 ans

**Programme**
- Maintenance électromécanique
- Technologies du vide et des plasmas
- Automatismes et PLC
- Diagnostic et dépannage
- Anglais technique

**Partenariats équipementiers**
- Formations certifiantes constructeurs intégrées
- Stages chez équipementiers ou en fab

**Investissement** : 3 M€/site = 30 M€ total

**Capacité totale 2040** : 600 diplômés/an

---

#### TECH-04 : Licence Professionnelle Métrologie et Caractérisation

**Établissements** : 6 universités partenaires

**Durée** : 1 an (après BTS/BUT)

**Objectifs**
Former des techniciens experts en métrologie semiconducteurs : CD-SEM, scatterométrie, XRD, SIMS, etc.

**Capacité** : 150 diplômés/an (2040)

**Investissement** : 3 M€/site = 18 M€ total

---

#### TECH-05 : Licence Professionnelle Chimie des Procédés Semiconducteurs

**Établissements** : 4 universités (Lyon, Grenoble, Bordeaux, Saclay)

**Objectifs**
Former des techniciens spécialistes des procédés chimiques : dépôt, gravure humide, nettoyage, CMP.

**Capacité** : 100 diplômés/an (2040)

**Investissement** : 12 M€ total

---

### 3.5 Certifications Professionnelles

| Réf. | Certification | Public cible | Durée | Capacité 2040 |
|------|--------------|--------------|-------|---------------|
| CERT-01 | Opérateur Salle Blanche Niveau 1 | Bac, reconversion | 3 mois | 1 500/an |
| CERT-02 | Opérateur Salle Blanche Niveau 2 | CERT-01 validé | 2 mois | 1 000/an |
| CERT-03 | Technicien Process Lithographie | BUT/BTS | 4 mois | 300/an |
| CERT-04 | Technicien Process Gravure/Dépôt | BUT/BTS | 4 mois | 300/an |
| CERT-05 | Technicien Maintenance Équipements Semi | BTS maintenance | 6 mois | 500/an |
| CERT-06 | Technicien Test ATE | BUT GEII | 3 mois | 200/an |
| CERT-07 | Technicien Métrologie Semi | Licence Pro | 3 mois | 200/an |
| CERT-08 | Ingénieur Process (mise à niveau) | Ingénieur autre domaine | 6 mois | 300/an |
| CERT-09 | Concepteur RTL (mise à niveau) | Ingénieur logiciel | 6 mois | 200/an |
| CERT-10 | Spécialiste RISC-V | Ingénieur conception | 3 mois | 150/an |
| CERT-11 | Expert Packaging Avancé | Ingénieur packaging | 4 mois | 100/an |
| CERT-12 | Lean Six Sigma Semi | Tous ingénieurs/tech | 2 mois | 500/an |
| CERT-13 | Sécurité Équipements (SEMI S2/S8) | Techniciens maint. | 1 mois | 800/an |
| CERT-14 | Habilitations Chimiques | Opérateurs, tech. | 1 mois | 1 000/an |
| CERT-15 | Anglais Technique Semi (B2+) | Tous | 6 mois | 2 000/an |

**Organismes certificateurs**
- Branches professionnelles (UIMM, FIEEC)
- Organismes de formation (AFPA, CNAM, GRETA)
- Entreprises (certifications internes reconnues)

---

## 4. Réforme des Cursus Existants

### 4.1 Principes de la Réforme

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AXES DE RÉFORME DES CURSUS EXISTANTS                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. SPÉCIALISATION SEMICONDUCTEURS                                          │
│     • Ajouter des modules dédiés dans les formations généralistes          │
│     • Créer des parcours "option semiconducteurs"                          │
│     • Développer les projets sur cas réels                                 │
│                                                                             │
│  2. RENFORCEMENT PRATIQUE                                                   │
│     • Minimum 50% du temps en situation professionnelle                    │
│     • Stages longs obligatoires (6 mois minimum en Bac+5)                  │
│     • Développement massif de l'alternance                                 │
│                                                                             │
│  3. OUVERTURE INTERNATIONALE                                                │
│     • Enseignements en anglais (30% minimum en Bac+5)                      │
│     • Mobilité internationale obligatoire (1 semestre)                     │
│     • Double diplômes avec universités partenaires                         │
│                                                                             │
│  4. COMPÉTENCES TRANSVERSES                                                 │
│     • Data science et programmation pour tous                              │
│     • Gestion de projet et travail en équipe                               │
│     • Sensibilisation aux enjeux de souveraineté                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Réformes par Niveau

#### Écoles d'Ingénieurs Généralistes

| École | Réforme proposée | Impact |
|-------|------------------|--------|
| Polytechnique | Création mineure "Semiconducteurs et Souveraineté" | +50 sensibilisés/an |
| CentraleSupélec | Parcours "Microélectronique et Systèmes" renforcé | +30 spécialisés/an |
| Mines Paris | Option "Technologies Stratégiques" incluant semi | +25 sensibilisés/an |
| ESPCI | Renforcement parcours nanosciences | +20 spécialisés/an |
| ENS | Agrégation physique + module semiconducteurs | +15 futurs enseignants/an |

#### IUT et BTS Existants

| Formation | Réforme proposée | Impact |
|-----------|------------------|--------|
| BUT GEII (50 IUT) | Module optionnel "Intro semiconducteurs" (60h) | +500 sensibilisés/an |
| BUT Mesures Physiques | Parcours "Métrologie semiconducteurs" | +200 spécialisés/an |
| BUT Chimie | Module "Chimie des matériaux électroniques" | +150 sensibilisés/an |
| BTS Systèmes Numériques | Option "Fabrication électronique" | +300 sensibilisés/an |

#### Masters Universitaires

| Master | Réforme proposée | Impact |
|--------|------------------|--------|
| Masters Physique | Parcours "Physique pour la microélectronique" | +100 spécialisés/an |
| Masters EEA | Renforcement modules conception/process | +150 spécialisés/an |
| Masters Matériaux | Spécialisation "Matériaux semiconducteurs" | +80 spécialisés/an |

### 4.3 Évolution des Maquettes Pédagogiques

#### Exemple : Réforme du BUT GEII

**Situation actuelle**
- Formation généraliste en électronique et informatique industrielle
- Pas de module semiconducteurs
- Stages variés (pas forcément en électronique)

**Maquette réformée (parcours Semiconducteurs)**

| Semestre | Nouveaux modules | Volume |
|----------|-----------------|--------|
| S3 | Introduction aux semiconducteurs | 40h |
| S4 | Procédés de fabrication (bases) | 60h |
| S4 | TP salle blanche (partenariat) | 20h |
| S5 | Spécialisation (litho/gravure/test) | 80h |
| S6 | Stage en entreprise semi (obligatoire) | 16 sem |

**Moyens nécessaires**
- Convention avec fab ou labo disposant de salle blanche
- Formation des enseignants (2 semaines/enseignant)
- Équipements pédagogiques (200 K€/IUT)

---

## 5. Formation Continue et Reconversion

### 5.1 Enjeux de la Reconversion

**Population cible** : 80 000 personnes à reconvertir sur 20 ans

| Secteur d'origine | Potentiel | Proximité compétences | Effort reconversion |
|-------------------|-----------|----------------------|---------------------|
| Automobile | 25 000 | Moyenne | 6-12 mois |
| Aéronautique | 15 000 | Bonne | 4-9 mois |
| Énergie/Nucléaire | 10 000 | Bonne | 4-9 mois |
| Chimie/Pharmacie | 10 000 | Moyenne | 6-12 mois |
| Mécanique générale | 10 000 | Faible | 9-18 mois |
| Informatique/Logiciel | 5 000 | Variable | 3-9 mois |
| Autres industries | 5 000 | Faible | 12-18 mois |

### 5.2 Parcours de Reconversion Types

---

#### RECONV-01 : Technicien Automobile → Technicien Salle Blanche

**Durée** : 6 mois

**Programme**

| Phase | Durée | Contenu | Lieu |
|-------|-------|---------|------|
| 1 | 2 sem | Découverte semiconducteurs, visite fab | Centre formation |
| 2 | 6 sem | Fondamentaux process et salle blanche | Centre formation |
| 3 | 4 sem | Spécialisation (1 domaine process) | Centre formation |
| 4 | 8 sem | Stage immersion en fab | Entreprise |
| 5 | 2 sem | Certification et bilan | Centre formation |

**Prérequis**
- Bac Pro ou BTS technique
- 3 ans d'expérience industrielle minimum
- Motivation validée (entretien + tests)

**Financement**
- Transitions Pro (ex-FONGECIF) : 70%
- Entreprise d'accueil : 20%
- Reste à charge : 10% (CPF)

**Capacité** : 3 000/an (2035)

---

#### RECONV-02 : Ingénieur Aéronautique → Ingénieur Process

**Durée** : 9 mois

**Programme**

| Phase | Durée | Contenu |
|-------|-------|---------|
| 1 | 1 mois | Fondamentaux microélectronique |
| 2 | 2 mois | Physique des procédés (plasma, CVD, etc.) |
| 3 | 2 mois | Intégration et caractérisation |
| 4 | 4 mois | Immersion en R&D ou production |

**Débouchés**
- Ingénieur process en fab
- Ingénieur intégration
- Ingénieur yield

**Capacité** : 500/an (2035)

---

#### RECONV-03 : Développeur Logiciel → Ingénieur Conception RTL

**Durée** : 9 mois

**Programme**

| Phase | Durée | Contenu |
|-------|-------|---------|
| 1 | 1 mois | Fondamentaux électronique numérique |
| 2 | 3 mois | Langages HDL (Verilog, SystemVerilog) |
| 3 | 2 mois | Méthodologie de conception et vérification |
| 4 | 3 mois | Projet tutoré + stage |

**Atouts du profil développeur**
- Maîtrise de la programmation
- Rigueur et débogage
- Familiarité avec les outils (Git, scripts)

**Capacité** : 300/an (2035)

---

### 5.3 Dispositifs de Financement Reconversion

| Dispositif | Public | Financement max | Conditions |
|------------|--------|-----------------|------------|
| Transitions Pro | Salariés CDI | 100% salaire + formation | Ancienneté 2 ans |
| Pro-A | Salariés peu qualifiés | Formation + maintien salaire | Accord branche |
| CPF de transition | Tous salariés | Selon droits acquis | Projet validé |
| CSP (licenciement éco) | Licenciés économiques | 12 mois + formation | PSE |
| POEI | Demandeurs d'emploi | Formation + allocation | Promesse d'embauche |
| Contrat pro adulte | Demandeurs d'emploi | Salaire + formation | Qualification visée |

### 5.4 Formation Continue des Salariés en Poste

#### Objectifs
- Mise à niveau technologique permanente
- Acquisition de nouvelles compétences (IA, data, nouveaux process)
- Préparation aux évolutions de poste

#### Modalités

| Format | Durée type | Public | Volume cible 2040 |
|--------|-----------|--------|-------------------|
| Modules courts (présentiel) | 2-5 jours | Tous | 15 000/an |
| Parcours certifiants | 2-6 mois | Techniciens, ingénieurs | 5 000/an |
| E-learning | Variable | Tous | 30 000/an |
| Conférences techniques | 1 jour | Ingénieurs, chercheurs | 10 000/an |
| Tutorat interne | Continu | Nouveaux embauchés | 8 000/an |

#### Plateforme Nationale de Formation Continue Semi

**Concept** : Plateforme mutualisée de ressources pédagogiques et de formations.

**Services**
- Catalogue de modules en ligne (MOOC, SPOC)
- Simulateurs de process et équipements
- Communauté d'experts et forums
- Certification des compétences

**Gouvernance** : GIE associant entreprises, branches, État

**Budget** : 50 M€ sur 5 ans

---

## 6. Infrastructure de Formation

### 6.1 Campus Microélectronique

#### Concept
Créer 5 campus dédiés regroupant formations, recherche et entreprises sur le modèle des clusters internationaux.

#### Implantations

| Campus | Localisation | Vocation principale | Capacité étudiants |
|--------|--------------|--------------------|--------------------|
| **Campus Alpes** | Grenoble (extension) | Fabrication, Process, R&D | 5 000 |
| **Campus Paris-Saclay** | Saclay (extension) | Conception, Architecture, Recherche | 4 000 |
| **Campus Sud-Ouest** | Toulouse (création) | Packaging, Test, Spatial | 2 500 |
| **Campus Ouest** | Rennes (création) | Télécom, Cybersécurité, Systèmes | 2 000 |
| **Campus Auvergne-Rhône** | Lyon (extension) | Équipements, Matériaux | 2 000 |

#### Modèle Campus Alpes (référence)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CAMPUS MICROÉLECTRONIQUE ALPES                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐         │
│   │   FORMATION     │   │    RECHERCHE    │   │   ENTREPRISES   │         │
│   │                 │   │                 │   │                 │         │
│   │ • Phelma        │   │ • CEA-Leti      │   │ • STMicro R&D   │         │
│   │ • IUT Grenoble  │   │ • CNRS-LTM      │   │ • Soitec        │         │
│   │ • UGA Masters   │   │ • INRIA         │   │ • Start-ups     │         │
│   │ • Centre AFPA   │   │ • Labos UGA     │   │ • Équipementiers│         │
│   └────────┬────────┘   └────────┬────────┘   └────────┬────────┘         │
│            │                     │                     │                   │
│            └─────────────────────┼─────────────────────┘                   │
│                                  ▼                                         │
│                    ┌─────────────────────────┐                             │
│                    │   INFRASTRUCTURES       │                             │
│                    │   MUTUALISÉES           │                             │
│                    │                         │                             │
│                    │ • Salle blanche péda    │                             │
│                    │ • Plateforme équipements│                             │
│                    │ • Data center calcul    │                             │
│                    │ • Espace coworking      │                             │
│                    │ • Incubateur            │                             │
│                    │ • Résidences étudiantes │                             │
│                    └─────────────────────────┘                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Budget Infrastructure Campus

| Campus | Investissement | Fonctionnement/an |
|--------|---------------|-------------------|
| Campus Alpes (extension) | 300 M€ | 80 M€ |
| Campus Paris-Saclay (extension) | 250 M€ | 70 M€ |
| Campus Sud-Ouest (création) | 400 M€ | 60 M€ |
| Campus Ouest (création) | 300 M€ | 50 M€ |
| Campus Auvergne-Rhône (extension) | 200 M€ | 50 M€ |
| **TOTAL** | **1 450 M€** | **310 M€/an** |

### 6.2 Salles Blanches Pédagogiques

#### Besoin
Former en conditions réelles nécessite l'accès à des salles blanches. Or les fabs de production ne peuvent pas accueillir massivement des étudiants.

#### Solution : Réseau de Salles Blanches Pédagogiques

| Type | Classe | Surface | Capacité | Nombre | Localisation |
|------|--------|---------|----------|--------|--------------|
| Salle blanche complète | 100-1000 | 500 m² | 50 étudiants/jour | 3 | Campus principaux |
| Salle blanche légère | 1000-10000 | 150 m² | 20 étudiants/jour | 10 | IUT, lycées |
| Démonstrateurs mobiles | N/A | Container | 10 étudiants/jour | 5 | Itinérant |

#### Équipements Types (Salle Complète)

| Équipement | Usage pédagogique | Coût unitaire |
|------------|-------------------|---------------|
| Spinner / coater | Enduction résine | 150 K€ |
| Aligneur de masque | Lithographie | 300 K€ |
| Four de diffusion | Recuit, oxydation | 400 K€ |
| Bâti de gravure RIE | Gravure plasma | 500 K€ |
| Bâti de dépôt CVD/PVD | Dépôt couches | 600 K€ |
| MEB (SEM) | Imagerie | 400 K€ |
| Profilomètre | Métrologie | 100 K€ |
| Station de test | Caractérisation | 200 K€ |
| **Total équipements** | | **~3 M€** |
| **Aménagement SB** | | **~5 M€** |
| **Total par salle complète** | | **~8-10 M€** |

#### Budget Total Salles Blanches Pédagogiques

| Poste | Investissement | Fonctionnement/an |
|-------|---------------|-------------------|
| 3 salles blanches complètes | 30 M€ | 6 M€ |
| 10 salles blanches légères | 30 M€ | 5 M€ |
| 5 démonstrateurs mobiles | 5 M€ | 1 M€ |
| **TOTAL** | **65 M€** | **12 M€/an** |

### 6.3 Plateformes Numériques

#### Plateforme Nationale de Simulation et E-Learning

**Fonctionnalités**
- Simulateurs de process (virtual fab)
- Outils EDA en mode cloud (licences mutualisées)
- MOOC et SPOC semiconducteurs
- Serious games de formation
- Bibliothèque de ressources pédagogiques

**Partenariats technologiques**
- Synopsys, Cadence, Siemens (licences académiques étendues)
- Silvaco, Coventor (simulation TCAD)
- Éditeurs français (à développer)

**Budget**
- Développement : 30 M€
- Licences logiciels : 10 M€/an
- Fonctionnement : 5 M€/an

---

## 7. Attractivité et Talents Internationaux

### 7.1 Diagnostic

**Situation actuelle**
- Fuite des cerveaux vers USA, Suisse, Asie
- Faible attractivité pour talents étrangers
- Salaires non compétitifs (vs TSMC, Intel, ASML)
- Complexité administrative (visa, reconnaissance diplômes)

**Flux actuels**

| Flux | Volume/an | Tendance |
|------|-----------|----------|
| Départs vers étranger (ingénieurs) | 1 500 | ↗ |
| Arrivées de l'étranger (ingénieurs) | 800 | → |
| Départs vers étranger (docteurs) | 600 | ↗ |
| Arrivées de l'étranger (docteurs) | 400 | → |
| **Solde net** | **-900** | **Négatif** |

### 7.2 Objectifs

| Indicateur | 2026 | 2032 | 2040 |
|------------|------|------|------|
| Recrutements internationaux/an | 800 | 2 500 | 5 000 |
| Rapatriements de Français expatriés/an | 200 | 800 | 1 500 |
| Solde migratoire qualifié | -900 | +1 000 | +3 000 |
| Part d'étrangers dans les formations | 15% | 25% | 30% |

### 7.3 Mesures d'Attractivité

#### Mesures Immédiates (2027-2029)

| Mesure | Description | Coût/an |
|--------|-------------|---------|
| **Passeport Talent Semi** | Visa accéléré (2 semaines) pour profils pénuriques | 2 M€ |
| **Prime d'installation** | 10 K€ pour chercheurs/ingénieurs étrangers | 25 M€ |
| **Guichet unique** | Accompagnement administratif personnalisé | 5 M€ |
| **Cours de français intensifs** | Gratuits pour recrutés et conjoints | 10 M€ |
| **Aide au logement** | Garantie locative + aide premier mois | 15 M€ |

#### Mesures Structurelles (2029-2035)

| Mesure | Description | Impact |
|--------|-------------|--------|
| **Formations en anglais** | 50% des masters en anglais | +50% candidats internationaux |
| **Double diplômes** | Accords avec universités étrangères (30) | +500 étudiants/an |
| **Chaires internationales** | 50 postes de professeurs étrangers | Effet d'entraînement |
| **Salaires compétitifs** | Alignement sur standards européens (+20%) | Rétention améliorée |
| **Reconnaissance diplômes** | Procédure accélérée équivalences | Réduction délais |

#### Cibles Géographiques Prioritaires

| Zone | Profils ciblés | Potentiel | Stratégie |
|------|----------------|-----------|-----------|
| **Inde** | Ingénieurs conception, docteurs | Très élevé | Partenariats IIT, salons |
| **Taïwan** | Ingénieurs process (retraités TSMC) | Élevé | Packages attractifs |
| **Europe de l'Est** | Ingénieurs, techniciens | Élevé | Accords universitaires |
| **Maghreb** | Techniciens, ingénieurs francophones | Moyen | Formations sur place |
| **Chine** | Chercheurs (diaspora) | Moyen | Sélectif, sécurité |
| **Corée du Sud** | Ingénieurs mémoires | Moyen | Partenariats industriels |

### 7.4 Programme de Rapatriement des Talents Français

**Cible** : Français expatriés dans les semiconducteurs (estimés à 5 000-8 000)

**Mesures incitatives**

| Mesure | Description | Impact |
|--------|-------------|--------|
| **Exonération fiscale** | 50% d'exonération IR pendant 5 ans | Fort |
| **Aide au retour** | Prise en charge déménagement (15 K€ max) | Moyen |
| **Réseau alumni** | Animation communauté Français à l'étranger | Moyen |
| **Offres d'emploi dédiées** | Plateforme "French Semi Talents Return" | Fort |
| **Reconnaissance expérience** | Validation acquis de l'expérience facilitée | Moyen |

**Objectif** : 1 500 rapatriements/an à horizon 2040

---

## 8. Gouvernance et Pilotage

### 8.1 Structure de Gouvernance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              GOUVERNANCE NATIONALE FORMATION SEMICONDUCTEURS                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                    ┌─────────────────────────────┐                          │
│                    │   COMITÉ STRATÉGIQUE        │                          │
│                    │   FORMATION SEMI            │                          │
│                    │                             │                          │
│                    │ • Ministères (MESR, Travail)│                          │
│                    │ • Branches professionnelles │                          │
│                    │ • Régions (ARF)             │                          │
│                    │ • Entreprises (STMicro...)  │                          │
│                    └──────────────┬──────────────┘                          │
│                                   │                                         │
│              ┌────────────────────┼────────────────────┐                    │
│              ▼                    ▼                    ▼                    │
│   ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐          │
│   │   PÔLE FORMATION │ │ PÔLE RECONVERSION│ │ PÔLE ATTRACTIVITÉ│          │
│   │   INITIALE       │ │ CONTINUE         │ │ INTERNATIONALE   │          │
│   │                  │ │                  │ │                  │          │
│   │ • Universités    │ │ • OPCO           │ │ • Campus France  │          │
│   │ • Écoles         │ │ • France Travail │ │ • Business France│          │
│   │ • IUT/Lycées     │ │ • Entreprises    │ │ • Consulats      │          │
│   └──────────────────┘ └──────────────────┘ └──────────────────┘          │
│              │                    │                    │                    │
│              └────────────────────┼────────────────────┘                    │
│                                   ▼                                         │
│                    ┌─────────────────────────────┐                          │
│                    │   AGENCE NATIONALE          │                          │
│                    │   COMPÉTENCES SEMI          │                          │
│                    │   (Opérateur)               │                          │
│                    │                             │                          │
│                    │ • Pilotage opérationnel     │                          │
│                    │ • Gestion des flux          │                          │
│                    │ • Certification             │                          │
│                    │ • Observatoire métiers      │                          │
│                    └─────────────────────────────┘                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Agence Nationale Compétences Semiconducteurs

**Statut** : GIP (Groupement d'Intérêt Public) ou EPA

**Missions**
1. Piloter la mise en œuvre du plan de formation
2. Coordonner les acteurs (universités, entreprises, régions)
3. Gérer les certifications professionnelles
4. Animer l'observatoire des métiers et compétences
5. Coordonner les programmes de reconversion
6. Piloter l'attractivité internationale

**Moyens**
- Effectifs : 80 ETP
- Budget fonctionnement : 15 M€/an
- Budget intervention : 100 M€/an

### 8.3 Indicateurs de Pilotage

| Catégorie | Indicateur | Fréquence | Source |
|-----------|------------|-----------|--------|
| **Flux** | Diplômés par niveau et spécialité | Annuelle | MESRI |
| **Flux** | Reconversions réalisées | Trimestrielle | France Travail |
| **Flux** | Recrutements internationaux | Annuelle | Ministère Intérieur |
| **Qualité** | Taux d'insertion à 6 mois | Annuelle | Enquêtes |
| **Qualité** | Satisfaction employeurs | Annuelle | Enquêtes |
| **Qualité** | Taux de remplissage formations | Annuelle | Établissements |
| **Capacité** | Places ouvertes par formation | Annuelle | Établissements |
| **Budget** | Consommation crédits | Trimestrielle | Agence |
| **Attractivité** | Candidatures / places | Annuelle | Parcoursup, etc. |
| **Parité** | % femmes par formation | Annuelle | Établissements |

### 8.4 Calendrier de Mise en Œuvre

| Phase | Période | Actions clés |
|-------|---------|--------------|
| **Lancement** | 2027 | Création Agence, premiers recrutements enseignants |
| **Déploiement** | 2028-2029 | Ouverture nouveaux cursus vague 1, premières reconversions |
| **Montée en charge** | 2030-2032 | Extension capacités, nouveaux campus opérationnels |
| **Cruiser** | 2033-2040 | Régime permanent, ajustements continus |
| **Consolidation** | 2041-2047 | Optimisation, pérennisation |

---

## 9. Budget et Financement

### 9.1 Budget Global Formation (2027-2047)

| Poste | Investissement | Fonctionnement (20 ans) | Total |
|-------|---------------|-------------------------|-------|
| Nouveaux cursus (création) | 1 650 M€ | 3 000 M€ | 4 650 M€ |
| Réforme cursus existants | 300 M€ | 1 500 M€ | 1 800 M€ |
| Infrastructure campus | 1 450 M€ | 6 200 M€ | 7 650 M€ |
| Salles blanches pédagogiques | 65 M€ | 240 M€ | 305 M€ |
| Plateformes numériques | 30 M€ | 300 M€ | 330 M€ |
| Reconversion professionnelle | — | 4 000 M€ | 4 000 M€ |
| Attractivité internationale | — | 1 500 M€ | 1 500 M€ |
| Agence nationale | 20 M€ | 2 300 M€ | 2 320 M€ |
| **TOTAL** | **3 515 M€** | **19 040 M€** | **22 555 M€** |

### 9.2 Budget Annuel Moyen

| Période | Budget annuel moyen |
|---------|---------------------|
| 2027-2032 (lancement) | 800 M€/an |
| 2032-2039 (montée en charge) | 1 200 M€/an |
| 2039-2047 (cruiser) | 1 300 M€/an |
| **Moyenne 20 ans** | **1 130 M€/an** |

### 9.3 Sources de Financement

| Source | Part | Montant 20 ans | Mécanisme |
|--------|------|----------------|-----------|
| État (MESRI, Travail) | 40% | 9 000 M€ | LFI, PIA, France 2030 |
| Régions | 20% | 4 500 M€ | CPER, compétence formation |
| Entreprises (taxe apprentissage + volontaire) | 25% | 5 600 M€ | OPCO, fondations, mécénat |
| Union Européenne | 10% | 2 300 M€ | FSE+, Erasmus+, Horizon |
| Apprenants (frais, CPF) | 5% | 1 100 M€ | Droits inscription, CPF |
| **TOTAL** | **100%** | **22 500 M€** | |

### 9.4 Retour sur Investissement

**Hypothèses**
- Coût moyen de formation : 80 K€/personne (cumul sur parcours)
- Salaire moyen des formés : 50 K€/an
- Durée de carrière : 35 ans
- Taux de cotisations et impôts : 50%

**Calcul ROI**

| Indicateur | Valeur |
|------------|--------|
| Personnes formées (20 ans) | 230 000 |
| Investissement total | 22,5 Md€ |
| Coût par personne | ~98 K€ |
| Recettes fiscales et sociales générées (carrière) | 875 K€/personne |
| Recettes totales générées | ~200 Md€ |
| **ROI** | **x9** |

**Autres bénéfices non quantifiés**
- Réduction dépendance stratégique
- Effet d'entraînement sur l'écosystème
- Innovation et brevets
- Attractivité du territoire

---

## Annexes

### A.1 Liste des Formations à Créer (Synthèse)

| Réf. | Niveau | Intitulé | Capacité 2040 |
|------|--------|----------|---------------|
| DOC-01 | Bac+8 | Doctorat Architecture Processeurs/SoC | 80/an |
| DOC-02 | Bac+8 | Doctorat Procédés Avancés | 100/an |
| DOC-03 | Bac+8 | Doctorat Matériaux Microélectronique | 70/an |
| DOC-04 | Bac+8 | Doctorat Industriel Équipements | 50/an |
| ING-01 | Bac+5 | Ingénieur Architecte SoC | 100/an |
| ING-02 | Bac+5 | Ingénieur Conception RISC-V | 80/an |
| ING-03 | Bac+5 | Ingénieur Procédés Fabrication (renfort) | 200/an |
| ING-04 | Bac+5 | Ingénieur Conception Équipements | 120/an |
| ING-05 | Bac+5 | Ingénieur Packaging Avancé | 80/an |
| ING-06 | Bac+5 | Master Conception Mémoires | 50/an |
| ING-07 | Bac+5 | Master EDA/Outils Conception | 50/an |
| ING-08 | Bac+5 | Ingénieur Test et Caractérisation | 60/an |
| ING-09 | Bac+5 | Master Photonique Intégrée | 40/an |
| ING-10 | Bac+5 | Master Cybersécurité Hardware | 50/an |
| ING-11 | Bac+5 | Ingénieur Yield et Data Science | 40/an |
| ING-12 | Bac+5 | Master Simulation TCAD | 30/an |
| TECH-01 | Bac+3 | BUT Fabrication Semiconducteurs | 800/an |
| TECH-02 | Bac+3 | BUT Packaging et Test | 400/an |
| TECH-03 | Bac+2 | BTS Maintenance Équipements Semi | 600/an |
| TECH-04 | Bac+3 | Licence Pro Métrologie | 150/an |
| TECH-05 | Bac+3 | Licence Pro Chimie Procédés Semi | 100/an |

### A.2 Partenariats Internationaux Cibles

| Pays | Établissement | Type de partenariat |
|------|---------------|---------------------|
| Taïwan | NTHU, NCTU | Double diplôme, échange chercheurs |
| Corée | KAIST, Seoul National | Double diplôme, recherche conjointe |
| États-Unis | MIT, Stanford, Berkeley | Échange chercheurs, cotutelles |
| Pays-Bas | TU Delft, TU Eindhoven | Double diplôme (lien ASML) |
| Allemagne | TU Dresden, TU Munich | Cursus conjoints, Erasmus+ |
| Belgique | KU Leuven, IMEC Academy | Formation continue, recherche |
| Japon | Tokyo Tech, Tohoku | Échange chercheurs, équipements |
| Inde | IIT (Bombay, Delhi, Madras) | Recrutement, double diplôme |

### A.3 Calendrier Détaillé Ouvertures de Formations

| Rentrée | Formations ouvertes |
|---------|---------------------|
| 2027 | ING-01 (Grenoble), TECH-01 (2 IUT), CERT-01 à 05 |
| 2028 | ING-02, ING-04, TECH-01 (3 IUT supplémentaires), TECH-03 (5 lycées) |
| 2029 | DOC-01, DOC-02, ING-05, TECH-02 (3 IUT) |
| 2030 | ING-03 renforcé, ING-06, ING-07, TECH-01 (complet) |
| 2031 | DOC-03, DOC-04, ING-08, ING-09 |
| 2032 | ING-10, ING-11, ING-12, TECH-04, TECH-05 |
| 2033+ | Montée en capacité de toutes les formations |

---

*Document de référence — Version 0.1*  
*Projet GenToGen2027 / TOGAFrance*
