# SVT_IT_ANX_A — Référentiel des Métiers et Compétences
## Plan de Souveraineté IT 2027-2047

---

**Document de référence** : SVT_IT_00, SVT_IT_ANX_00  
**Classification** : Public  
**Auteur** : Jeff / Jagrat  
**Date** : Janvier 2026  
**Version** : 0.1

---

## Sommaire

1. [Introduction et Méthodologie](#1-introduction-et-méthodologie)
2. [Nomenclature des Familles de Métiers](#2-nomenclature-des-familles-de-métiers)
3. [Fiches Métiers Détaillées](#3-fiches-métiers-détaillées)
4. [Matrice des Compétences](#4-matrice-des-compétences)
5. [Gap Analysis : Situation Actuelle vs Cible](#5-gap-analysis)
6. [Pyramide des Qualifications](#6-pyramide-des-qualifications)
7. [Tensions et Priorités de Formation](#7-tensions-et-priorités)

---

## 1. Introduction et Méthodologie

### 1.1 Objectif du Référentiel

Ce référentiel définit l'ensemble des métiers nécessaires à la mise en œuvre du plan de souveraineté IT. Il constitue la base pour :

- Dimensionner les besoins en formation (ANX_B)
- Orienter les créations d'entreprises (ANX_C)
- Piloter les politiques d'attractivité des talents
- Mesurer les progrès via des indicateurs RH

### 1.2 Périmètre

Le référentiel couvre la chaîne de valeur complète des semiconducteurs :

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PÉRIMÈTRE DU RÉFÉRENTIEL                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐     │
│   │RECHERCHE│──▶│CONCEPTION│──▶│FABRICATION│──▶│PACKAGING│──▶│INTÉGRATION│   │
│   │   R&D   │   │  DESIGN  │   │ FONDERIE │   │  TEST   │   │ SYSTÈMES │   │
│   └─────────┘   └─────────┘   └─────────┘   └─────────┘   └─────────┘     │
│        │             │             │             │             │           │
│        └─────────────┴─────────────┴─────────────┴─────────────┘           │
│                                    │                                        │
│                          ┌─────────┴─────────┐                             │
│                          │      SUPPORT      │                             │
│                          │ Équipements, Infra│                             │
│                          │ Qualité, Supply   │                             │
│                          └───────────────────┘                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Structure des Fiches Métiers

Chaque fiche métier suit un format standardisé :

| Champ | Description |
|-------|-------------|
| Code métier | Identifiant unique (FAM-XXX) |
| Intitulé | Nom du métier |
| Famille | Catégorie principale |
| Niveau | Qualification requise |
| Mission | Description synthétique |
| Activités principales | Liste des tâches clés |
| Compétences techniques | Hard skills requis |
| Compétences transverses | Soft skills requis |
| Formation type | Parcours recommandé |
| Expérience | Années requises (junior/confirmé/senior) |
| Salaire indicatif | Fourchette en K€ brut annuel |
| Volume cible 2047 | Effectif national visé |
| Tension actuelle | Critique / Élevée / Moyenne / Faible |
| Évolution | Passerelles possibles |

---

## 2. Nomenclature des Familles de Métiers

### 2.1 Vue d'Ensemble

| Code | Famille | Sous-familles | Métiers | Volume 2047 |
|------|---------|---------------|---------|-------------|
| **RD** | Recherche & Développement | 3 | 12 | 18 000 |
| **CO** | Conception & Design | 4 | 16 | 35 000 |
| **FA** | Fabrication & Process | 5 | 22 | 65 000 |
| **EQ** | Équipements & Maintenance | 3 | 10 | 28 000 |
| **PK** | Packaging & Test | 3 | 9 | 22 000 |
| **SU** | Support & Fonctions Transverses | 4 | 12 | 32 000 |
| **TOTAL** | | **22** | **81** | **200 000** |

### 2.2 Arborescence Détaillée

```
MÉTIERS DE LA SOUVERAINETÉ IT
│
├── RD — RECHERCHE & DÉVELOPPEMENT
│   ├── RD-REC — Recherche Fondamentale
│   │   ├── RD-REC-001 Chercheur Physique des Semiconducteurs
│   │   ├── RD-REC-002 Chercheur Matériaux Avancés
│   │   └── RD-REC-003 Chercheur Architectures Émergentes
│   ├── RD-APP — Recherche Appliquée
│   │   ├── RD-APP-001 Ingénieur R&D Process
│   │   ├── RD-APP-002 Ingénieur R&D Intégration
│   │   ├── RD-APP-003 Ingénieur R&D Caractérisation
│   │   └── RD-APP-004 Ingénieur R&D Packaging Avancé
│   └── RD-TRA — Transfert Technologique
│       ├── RD-TRA-001 Ingénieur Industrialisation
│       ├── RD-TRA-002 Chef de Projet Pilote
│       ├── RD-TRA-003 Responsable Propriété Intellectuelle
│       └── RD-TRA-004 Business Developer Techno
│
├── CO — CONCEPTION & DESIGN
│   ├── CO-ARC — Architecture
│   │   ├── CO-ARC-001 Architecte SoC
│   │   ├── CO-ARC-002 Architecte CPU/GPU
│   │   ├── CO-ARC-003 Architecte Mémoires
│   │   └── CO-ARC-004 Architecte Sécurité Hardware
│   ├── CO-RTL — Conception Logique
│   │   ├── CO-RTL-001 Ingénieur Conception RTL
│   │   ├── CO-RTL-002 Ingénieur Conception RISC-V
│   │   ├── CO-RTL-003 Ingénieur IP Design
│   │   └── CO-RTL-004 Ingénieur Synthèse Logique
│   ├── CO-PHY — Conception Physique
│   │   ├── CO-PHY-001 Ingénieur Place & Route
│   │   ├── CO-PHY-002 Ingénieur Timing Closure
│   │   ├── CO-PHY-003 Ingénieur DFM/DFT
│   │   └── CO-PHY-004 Ingénieur Layout Analogique
│   └── CO-VER — Vérification
│       ├── CO-VER-001 Ingénieur Vérification Fonctionnelle
│       ├── CO-VER-002 Ingénieur Vérification Formelle
│       ├── CO-VER-003 Ingénieur Émulation/Prototypage
│       └── CO-VER-004 Ingénieur Validation Silicium
│
├── FA — FABRICATION & PROCESS
│   ├── FA-LIT — Lithographie
│   │   ├── FA-LIT-001 Ingénieur Process Lithographie
│   │   ├── FA-LIT-002 Technicien Lithographie
│   │   ├── FA-LIT-003 Ingénieur Masques/Réticules
│   │   └── FA-LIT-004 Spécialiste OPC/RET
│   ├── FA-GRA — Gravure & Dépôt
│   │   ├── FA-GRA-001 Ingénieur Process Gravure Plasma
│   │   ├── FA-GRA-002 Ingénieur Process Dépôt CVD/PVD
│   │   ├── FA-GRA-003 Ingénieur Process ALD
│   │   ├── FA-GRA-004 Technicien Gravure
│   │   └── FA-GRA-005 Technicien Dépôt
│   ├── FA-IMP — Implantation & Diffusion
│   │   ├── FA-IMP-001 Ingénieur Process Implantation
│   │   ├── FA-IMP-002 Ingénieur Process Diffusion/Recuit
│   │   └── FA-IMP-003 Technicien Implantation/Diffusion
│   ├── FA-CMP — Planarisation & Nettoyage
│   │   ├── FA-CMP-001 Ingénieur Process CMP
│   │   ├── FA-CMP-002 Ingénieur Process Nettoyage
│   │   ├── FA-CMP-003 Technicien CMP
│   │   └── FA-CMP-004 Technicien Chimie/Wet
│   └── FA-INT — Intégration & Yield
│       ├── FA-INT-001 Ingénieur Intégration Process
│       ├── FA-INT-002 Ingénieur Yield Enhancement
│       ├── FA-INT-003 Ingénieur Métrologie
│       ├── FA-INT-004 Ingénieur Défectivité
│       ├── FA-INT-005 Technicien Métrologie
│       └── FA-INT-006 Opérateur Salle Blanche
│
├── EQ — ÉQUIPEMENTS & MAINTENANCE
│   ├── EQ-DEV — Développement Équipements
│   │   ├── EQ-DEV-001 Ingénieur Conception Équipements
│   │   ├── EQ-DEV-002 Ingénieur Systèmes Optiques
│   │   ├── EQ-DEV-003 Ingénieur Plasma/Vide
│   │   └── EQ-DEV-004 Ingénieur Automatisation Équipements
│   ├── EQ-MAI — Maintenance
│   │   ├── EQ-MAI-001 Ingénieur Maintenance
│   │   ├── EQ-MAI-002 Technicien Maintenance Équipements
│   │   └── EQ-MAI-003 Technicien Facilities/Utilités
│   └── EQ-INS — Installation & Qualification
│       ├── EQ-INS-001 Ingénieur Installation
│       ├── EQ-INS-002 Ingénieur Qualification
│       └── EQ-INS-003 Technicien Installation
│
├── PK — PACKAGING & TEST
│   ├── PK-ASS — Assemblage
│   │   ├── PK-ASS-001 Ingénieur Process Packaging
│   │   ├── PK-ASS-002 Ingénieur Packaging 3D/Avancé
│   │   └── PK-ASS-003 Technicien Assemblage
│   ├── PK-TST — Test
│   │   ├── PK-TST-001 Ingénieur Test Produit
│   │   ├── PK-TST-002 Ingénieur Développement Test
│   │   ├── PK-TST-003 Technicien Test
│   │   └── PK-TST-004 Ingénieur Analyse de Défaillance
│   └── PK-FIA — Fiabilité
│       ├── PK-FIA-001 Ingénieur Fiabilité
│       └── PK-FIA-002 Ingénieur Qualification Produit
│
└── SU — SUPPORT & FONCTIONS TRANSVERSES
    ├── SU-QUA — Qualité & Conformité
    │   ├── SU-QUA-001 Ingénieur Qualité Process
    │   ├── SU-QUA-002 Ingénieur Qualité Produit
    │   └── SU-QUA-003 Responsable Conformité/Normes
    ├── SU-SUP — Supply Chain
    │   ├── SU-SUP-001 Responsable Supply Chain
    │   ├── SU-SUP-002 Acheteur Technique
    │   └── SU-SUP-003 Planificateur Production
    ├── SU-HSE — Hygiène Sécurité Environnement
    │   ├── SU-HSE-001 Ingénieur HSE
    │   ├── SU-HSE-002 Responsable Environnement
    │   └── SU-HSE-003 Technicien HSE
    └── SU-MAN — Management & Gestion
        ├── SU-MAN-001 Chef de Projet Technique
        ├── SU-MAN-002 Responsable Production
        └── SU-MAN-003 Directeur de Site/Fab
```

---

## 3. Fiches Métiers Détaillées

### 3.1 Famille RD — Recherche & Développement

---

#### RD-REC-001 — Chercheur Physique des Semiconducteurs

| Champ | Valeur |
|-------|--------|
| **Code** | RD-REC-001 |
| **Intitulé** | Chercheur Physique des Semiconducteurs |
| **Famille** | Recherche & Développement |
| **Sous-famille** | Recherche Fondamentale |
| **Niveau** | Bac+8 (Doctorat) |

**Mission**

Conduire des travaux de recherche fondamentale sur les propriétés physiques des matériaux semiconducteurs et les phénomènes quantiques associés, en vue d'applications industrielles à moyen/long terme.

**Activités principales**

- Définir et conduire des programmes de recherche sur les matériaux émergents (SiC, GaN, 2D materials)
- Modéliser les phénomènes physiques aux échelles nanométriques
- Publier dans des revues scientifiques de rang A
- Encadrer doctorants et post-doctorants
- Participer aux consortiums de recherche européens
- Assurer la veille scientifique internationale

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Physique quantique et du solide | Expert |
| Simulation ab initio (DFT, Monte-Carlo) | Expert |
| Caractérisation avancée (TEM, SIMS, XPS) | Avancé |
| Programmation scientifique (Python, C++) | Avancé |
| Rédaction scientifique anglais | Expert |

**Compétences transverses**

- Créativité et curiosité scientifique
- Rigueur méthodologique
- Communication scientifique
- Travail en réseau international
- Encadrement d'équipe

**Formation type**

- Doctorat en physique des semiconducteurs, physique du solide ou science des matériaux
- Post-doctorat international recommandé (2-3 ans)
- Établissements : ENS, Polytechnique, universités (Grenoble, Saclay, Bordeaux)

**Expérience**

| Niveau | Années | Responsabilités |
|--------|--------|-----------------|
| Junior | 0-3 | Chercheur associé, thèmes définis |
| Confirmé | 3-8 | Responsable de thème, encadrement |
| Senior | 8+ | Directeur de recherche, stratégie |

**Rémunération indicative**

| Niveau | Secteur public | Secteur privé |
|--------|---------------|---------------|
| Junior | 35-45 K€ | 45-55 K€ |
| Confirmé | 45-60 K€ | 55-75 K€ |
| Senior | 60-80 K€ | 75-120 K€ |

**Volume cible 2047** : 2 500

**Tension actuelle** : Élevée

**Évolutions possibles**

- Directeur de laboratoire
- Chief Scientist industrie
- Consultant expert
- Entrepreneur deep tech

---

#### RD-REC-002 — Chercheur Matériaux Avancés

| Champ | Valeur |
|-------|--------|
| **Code** | RD-REC-002 |
| **Intitulé** | Chercheur Matériaux Avancés |
| **Famille** | Recherche & Développement |
| **Sous-famille** | Recherche Fondamentale |
| **Niveau** | Bac+8 (Doctorat) |

**Mission**

Développer et caractériser de nouveaux matériaux pour les générations futures de composants : matériaux 2D (graphène, MoS2), matériaux III-V, oxydes fonctionnels, matériaux pour le quantique.

**Activités principales**

- Synthétiser et caractériser des matériaux émergents
- Développer des procédés de croissance (MBE, MOCVD, ALD)
- Étudier les interfaces et hétérostructures
- Évaluer le potentiel d'intégration industrielle
- Collaborer avec les équipes process et intégration
- Protéger les innovations (brevets)

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Science des matériaux | Expert |
| Techniques de croissance cristalline | Expert |
| Caractérisation structurale (XRD, AFM) | Expert |
| Caractérisation électrique | Avancé |
| Thermodynamique des matériaux | Avancé |

**Compétences transverses**

- Approche expérimentale rigoureuse
- Patience et persévérance
- Collaboration interdisciplinaire
- Sensibilité aux enjeux industriels

**Formation type**

- Doctorat en science des matériaux, chimie du solide ou physique
- Spécialisation matériaux pour la microélectronique
- Établissements : Grenoble INP, INSA Lyon, Centrale Lyon

**Volume cible 2047** : 2 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 40-100 K€ selon niveau et secteur

---

#### RD-APP-001 — Ingénieur R&D Process

| Champ | Valeur |
|-------|--------|
| **Code** | RD-APP-001 |
| **Intitulé** | Ingénieur R&D Process |
| **Famille** | Recherche & Développement |
| **Sous-famille** | Recherche Appliquée |
| **Niveau** | Bac+5 / Bac+8 |

**Mission**

Développer et optimiser les procédés de fabrication pour les nœuds technologiques futurs, en assurant la transition entre recherche et production.

**Activités principales**

- Concevoir et réaliser des expériences sur les procédés (DOE)
- Caractériser les performances des procédés
- Optimiser les fenêtres de process
- Rédiger les spécifications pour le transfert industriel
- Collaborer avec les équipementiers
- Former les équipes de production

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Physique des procédés (plasma, CVD, etc.) | Expert |
| Plans d'expériences (DOE) | Expert |
| Statistiques industrielles (SPC, Cpk) | Avancé |
| Métrologie semiconducteurs | Avancé |
| Simulation procédés (TCAD) | Intermédiaire |

**Compétences transverses**

- Esprit analytique
- Orientation résultats
- Communication technique
- Travail en équipe projet

**Formation type**

- Ingénieur + Master spécialisé microélectronique
- Doctorat apprécié pour R&D avancée
- Établissements : Phelma, INSA, Polytechnique, CentraleSupélec

**Volume cible 2047** : 5 000

**Tension actuelle** : Critique

**Rémunération indicative** : 42-90 K€

---

#### RD-TRA-001 — Ingénieur Industrialisation

| Champ | Valeur |
|-------|--------|
| **Code** | RD-TRA-001 |
| **Intitulé** | Ingénieur Industrialisation |
| **Famille** | Recherche & Développement |
| **Sous-famille** | Transfert Technologique |
| **Niveau** | Bac+5 |

**Mission**

Assurer le passage à l'échelle industrielle des procédés et technologies développés en R&D, en garantissant reproductibilité, rendement et coût.

**Activités principales**

- Piloter les transferts R&D → Production
- Définir les gammes de fabrication industrielles
- Qualifier les procédés en volume
- Optimiser les rendements (yield ramp)
- Gérer les interfaces R&D / Production / Équipementiers
- Documenter les procédures et former les équipes

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Procédés de fabrication semiconducteurs | Expert |
| Gestion de projet technique | Expert |
| Lean manufacturing | Avancé |
| Analyse de rendement | Expert |
| Gestion de la qualité | Avancé |

**Compétences transverses**

- Leadership transversal
- Gestion des priorités
- Communication multi-niveaux
- Résolution de problèmes complexes

**Formation type**

- Ingénieur généraliste + spécialisation microélectronique
- Expérience en fab indispensable
- MBA ou formation management appréciée

**Volume cible 2047** : 3 500

**Tension actuelle** : Critique

**Rémunération indicative** : 50-95 K€

---

### 3.2 Famille CO — Conception & Design

---

#### CO-ARC-001 — Architecte SoC

| Champ | Valeur |
|-------|--------|
| **Code** | CO-ARC-001 |
| **Intitulé** | Architecte SoC (System-on-Chip) |
| **Famille** | Conception & Design |
| **Sous-famille** | Architecture |
| **Niveau** | Bac+5 / Bac+8 |

**Mission**

Définir l'architecture globale des circuits intégrés complexes (SoC), en optimisant performances, consommation, surface et coût pour répondre aux spécifications système.

**Activités principales**

- Analyser les spécifications système et définir l'architecture
- Partitionner les fonctions hardware/software
- Sélectionner et intégrer les IP (processeurs, mémoires, interfaces)
- Définir l'architecture mémoire et les interconnexions
- Modéliser et simuler les performances système
- Piloter les équipes de conception détaillée

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Architecture des processeurs | Expert |
| Protocoles de communication (AMBA, PCIe, etc.) | Expert |
| Modélisation système (SystemC, TLM) | Expert |
| Conception basse consommation | Expert |
| Sécurité hardware | Avancé |

**Compétences transverses**

- Vision système
- Capacité d'abstraction
- Leadership technique
- Négociation (trade-offs)

**Formation type**

- Ingénieur électronique/informatique + spécialisation conception
- Doctorat en architecture des systèmes apprécié
- Établissements : Phelma, ENSIMAG, Télécom Paris, ISAE

**Volume cible 2047** : 3 000

**Tension actuelle** : Critique

**Rémunération indicative** : 55-130 K€

---

#### CO-ARC-002 — Architecte CPU/GPU

| Champ | Valeur |
|-------|--------|
| **Code** | CO-ARC-002 |
| **Intitulé** | Architecte CPU/GPU |
| **Famille** | Conception & Design |
| **Sous-famille** | Architecture |
| **Niveau** | Bac+5 / Bac+8 |

**Mission**

Concevoir l'architecture des processeurs (CPU, GPU, accélérateurs IA), en définissant le jeu d'instructions, le pipeline, les caches et les unités de calcul.

**Activités principales**

- Définir l'ISA (Instruction Set Architecture) ou implémenter RISC-V
- Concevoir les pipelines d'exécution
- Optimiser les hiérarchies de cache
- Développer les unités vectorielles et matricielles (IA)
- Analyser les benchmarks et optimiser les performances
- Collaborer avec les équipes compilateurs et OS

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Architecture des processeurs (pipeline, cache) | Expert |
| Jeux d'instructions (x86, ARM, RISC-V) | Expert |
| Microarchitecture | Expert |
| Simulation de performance | Expert |
| Compilation et optimisation | Avancé |

**Compétences transverses**

- Pensée algorithmique
- Créativité architecturale
- Veille technologique permanente
- Collaboration internationale

**Formation type**

- Doctorat en architecture des ordinateurs fortement recommandé
- École d'ingénieur informatique/électronique
- Parcours recherche ou R&D industrie

**Volume cible 2047** : 2 000

**Tension actuelle** : Critique

**Rémunération indicative** : 60-150 K€

---

#### CO-RTL-001 — Ingénieur Conception RTL

| Champ | Valeur |
|-------|--------|
| **Code** | CO-RTL-001 |
| **Intitulé** | Ingénieur Conception RTL |
| **Famille** | Conception & Design |
| **Sous-famille** | Conception Logique |
| **Niveau** | Bac+5 |

**Mission**

Concevoir et coder les blocs fonctionnels des circuits intégrés au niveau RTL (Register Transfer Level) en Verilog ou VHDL.

**Activités principales**

- Traduire les spécifications en code RTL synthétisable
- Concevoir les machines d'état et chemins de données
- Optimiser pour la surface, la vitesse et la consommation
- Réaliser les simulations fonctionnelles
- Collaborer avec les équipes vérification et physique
- Documenter les designs

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Langages HDL (Verilog, SystemVerilog, VHDL) | Expert |
| Conception synchrone | Expert |
| Synthèse logique | Avancé |
| Protocoles standards (AXI, APB, I2C, SPI) | Avancé |
| Outils EDA (Synopsys, Cadence) | Avancé |

**Compétences transverses**

- Rigueur et attention aux détails
- Capacité de débogage
- Travail en équipe
- Documentation technique

**Formation type**

- Ingénieur électronique numérique
- Master conception de circuits intégrés
- Établissements : Phelma, ENSEIRB, ENSEEIHT, Polytech

**Volume cible 2047** : 8 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 40-80 K€

---

#### CO-RTL-002 — Ingénieur Conception RISC-V

| Champ | Valeur |
|-------|--------|
| **Code** | CO-RTL-002 |
| **Intitulé** | Ingénieur Conception RISC-V |
| **Famille** | Conception & Design |
| **Sous-famille** | Conception Logique |
| **Niveau** | Bac+5 |

**Mission**

Concevoir et implémenter des cœurs processeurs basés sur l'architecture ouverte RISC-V, contribuant à la souveraineté technologique.

**Activités principales**

- Implémenter des cœurs RISC-V (RV32/RV64)
- Développer des extensions custom (accélération, sécurité)
- Optimiser les performances et la consommation
- Contribuer à l'écosystème open source RISC-V
- Intégrer les cœurs dans des SoC
- Assurer la compatibilité avec les chaînes de compilation

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Architecture RISC-V (ISA, extensions) | Expert |
| Conception RTL avancée | Expert |
| Microarchitecture processeurs | Avancé |
| Écosystème open source hardware | Avancé |
| Outils de vérification | Avancé |

**Compétences transverses**

- Esprit communautaire (open source)
- Autonomie
- Veille technologique
- Communication en anglais

**Formation type**

- Ingénieur électronique/informatique
- Spécialisation architecture des processeurs
- Contribution open source appréciée

**Volume cible 2047** : 2 500

**Tension actuelle** : Critique (compétence rare)

**Rémunération indicative** : 45-95 K€

---

#### CO-PHY-001 — Ingénieur Place & Route

| Champ | Valeur |
|-------|--------|
| **Code** | CO-PHY-001 |
| **Intitulé** | Ingénieur Place & Route |
| **Famille** | Conception & Design |
| **Sous-famille** | Conception Physique |
| **Niveau** | Bac+5 |

**Mission**

Réaliser l'implémentation physique des circuits intégrés : placement des cellules, routage des interconnexions, optimisation du timing et de la consommation.

**Activités principales**

- Définir le floorplan et la stratégie de placement
- Réaliser le placement et le routage automatisés
- Optimiser le timing (setup, hold) et la consommation
- Gérer les contraintes physiques (IR drop, congestion)
- Générer les fichiers pour la fabrication (GDS)
- Collaborer avec les équipes RTL et foundry

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Outils P&R (Innovus, ICC2) | Expert |
| Analyse de timing statique (STA) | Expert |
| Conception basse consommation (UPF/CPF) | Avancé |
| DRC/LVS et règles de design | Avancé |
| Scripting (Tcl, Python) | Avancé |

**Compétences transverses**

- Patience et persévérance
- Sens de l'optimisation
- Rigueur méthodologique
- Travail itératif

**Formation type**

- Ingénieur électronique
- Master conception physique
- Formation outils EDA indispensable

**Volume cible 2047** : 4 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 42-85 K€

---

#### CO-VER-001 — Ingénieur Vérification Fonctionnelle

| Champ | Valeur |
|-------|--------|
| **Code** | CO-VER-001 |
| **Intitulé** | Ingénieur Vérification Fonctionnelle |
| **Famille** | Conception & Design |
| **Sous-famille** | Vérification |
| **Niveau** | Bac+5 |

**Mission**

Vérifier le bon fonctionnement des designs RTL par simulation, en développant des environnements de test et en assurant la couverture fonctionnelle.

**Activités principales**

- Développer les plans de vérification
- Créer les environnements de test (UVM)
- Écrire les testbenches et assertions
- Analyser la couverture fonctionnelle et de code
- Déboguer les designs en collaboration avec les concepteurs
- Documenter les résultats de vérification

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Méthodologie UVM | Expert |
| SystemVerilog pour la vérification | Expert |
| Assertions (SVA) | Avancé |
| Outils de simulation (VCS, Xcelium) | Expert |
| Couverture fonctionnelle | Expert |

**Compétences transverses**

- Esprit critique et scepticisme constructif
- Rigueur et exhaustivité
- Communication avec les concepteurs
- Documentation

**Formation type**

- Ingénieur électronique numérique
- Certification UVM appréciée
- Établissements : écoles d'ingénieurs électronique

**Volume cible 2047** : 6 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 42-85 K€

---

### 3.3 Famille FA — Fabrication & Process

---

#### FA-LIT-001 — Ingénieur Process Lithographie

| Champ | Valeur |
|-------|--------|
| **Code** | FA-LIT-001 |
| **Intitulé** | Ingénieur Process Lithographie |
| **Famille** | Fabrication & Process |
| **Sous-famille** | Lithographie |
| **Niveau** | Bac+5 |

**Mission**

Développer et optimiser les procédés de photolithographie pour définir les motifs nanométriques sur les wafers avec la précision requise.

**Activités principales**

- Développer les procédés de résine et exposition
- Optimiser les paramètres d'exposition (focus, dose)
- Qualifier les nouvelles technologies (EUV, immersion)
- Collaborer avec les fournisseurs de résines et équipements
- Analyser les défauts et améliorer les rendements
- Former les techniciens

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Optique et photochimie | Expert |
| Procédés lithographiques (DUV, EUV) | Expert |
| Métrologie dimensionnelle (CD-SEM, scatterometry) | Expert |
| Statistiques et DOE | Avancé |
| OPC et computational lithography | Intermédiaire |

**Compétences transverses**

- Rigueur expérimentale
- Résolution de problèmes
- Collaboration équipementiers
- Gestion de projets

**Formation type**

- Ingénieur physique ou matériaux
- Spécialisation microélectronique
- Établissements : Phelma, INSA, Centrale

**Volume cible 2047** : 3 500

**Tension actuelle** : Critique

**Rémunération indicative** : 45-90 K€

---

#### FA-LIT-002 — Technicien Lithographie

| Champ | Valeur |
|-------|--------|
| **Code** | FA-LIT-002 |
| **Intitulé** | Technicien Lithographie |
| **Famille** | Fabrication & Process |
| **Sous-famille** | Lithographie |
| **Niveau** | Bac+2/3 |

**Mission**

Opérer et maintenir les équipements de lithographie en salle blanche, réaliser les procédés selon les gammes établies et assurer la qualité des opérations.

**Activités principales**

- Opérer les équipements de lithographie (scanner, track)
- Réaliser les contrôles qualité (CD, overlay)
- Effectuer les maintenances de premier niveau
- Remonter les dérives et anomalies
- Participer aux qualifications de procédés
- Respecter les protocoles salle blanche

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Conduite équipements lithographie | Expert |
| Protocoles salle blanche | Expert |
| Métrologie de base | Avancé |
| Maintenance préventive | Avancé |
| Lecture de gammes de fabrication | Expert |

**Compétences transverses**

- Rigueur et discipline
- Attention aux détails
- Travail en équipe postée
- Réactivité

**Formation type**

- BTS/DUT électronique, physique ou chimie
- Formation interne salle blanche (3-6 mois)
- Certification équipements

**Volume cible 2047** : 8 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 28-45 K€

---

#### FA-GRA-001 — Ingénieur Process Gravure Plasma

| Champ | Valeur |
|-------|--------|
| **Code** | FA-GRA-001 |
| **Intitulé** | Ingénieur Process Gravure Plasma |
| **Famille** | Fabrication & Process |
| **Sous-famille** | Gravure & Dépôt |
| **Niveau** | Bac+5 |

**Mission**

Développer et optimiser les procédés de gravure plasma (RIE, ICP) pour transférer les motifs dans les différentes couches du circuit.

**Activités principales**

- Développer les recettes de gravure pour différents matériaux
- Optimiser les profils de gravure (anisotropie, sélectivité)
- Caractériser les plasmas et comprendre les mécanismes
- Résoudre les problèmes de défectivité liés à la gravure
- Collaborer avec les équipementiers
- Qualifier les nouveaux équipements

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Physique des plasmas | Expert |
| Procédés de gravure (Si, métaux, diélectriques) | Expert |
| Diagnostics plasma (OES, endpoint) | Avancé |
| Métrologie de profil | Avancé |
| DOE et optimisation | Avancé |

**Compétences transverses**

- Esprit analytique
- Rigueur scientifique
- Collaboration interdisciplinaire
- Pédagogie

**Formation type**

- Ingénieur physique ou chimie
- Spécialisation plasmas ou microélectronique
- Doctorat apprécié

**Volume cible 2047** : 3 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 45-85 K€

---

#### FA-INT-002 — Ingénieur Yield Enhancement

| Champ | Valeur |
|-------|--------|
| **Code** | FA-INT-002 |
| **Intitulé** | Ingénieur Yield Enhancement |
| **Famille** | Fabrication & Process |
| **Sous-famille** | Intégration & Yield |
| **Niveau** | Bac+5 |

**Mission**

Améliorer continuellement les rendements de fabrication en identifiant et éliminant les causes de pertes (défauts, variations de process).

**Activités principales**

- Analyser les données de rendement (yield) et identifier les pertes
- Corréler les défauts aux étapes de process
- Piloter les plans d'amélioration du rendement
- Développer les modèles prédictifs de yield
- Collaborer avec toutes les équipes process
- Reporter les indicateurs de performance

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Analyse de données massives (data mining) | Expert |
| Statistiques industrielles | Expert |
| Process de fabrication semiconducteurs | Avancé |
| Outils de yield management | Expert |
| Programmation (Python, SQL) | Avancé |

**Compétences transverses**

- Esprit de synthèse
- Communication transverse
- Orientation résultats
- Persévérance

**Formation type**

- Ingénieur généraliste ou électronique
- Compétences data science
- Expérience fab indispensable

**Volume cible 2047** : 2 500

**Tension actuelle** : Élevée

**Rémunération indicative** : 48-90 K€

---

#### FA-INT-006 — Opérateur Salle Blanche

| Champ | Valeur |
|-------|--------|
| **Code** | FA-INT-006 |
| **Intitulé** | Opérateur Salle Blanche |
| **Famille** | Fabrication & Process |
| **Sous-famille** | Intégration & Yield |
| **Niveau** | Bac / Bac Pro |

**Mission**

Réaliser les opérations de fabrication en salle blanche selon les gammes établies, en respectant les protocoles de qualité et de sécurité.

**Activités principales**

- Charger/décharger les wafers sur les équipements
- Suivre les gammes de fabrication
- Réaliser les contrôles visuels et mesures de routine
- Remonter les anomalies
- Maintenir la propreté de l'environnement
- Participer aux inventaires et à la traçabilité

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Protocoles salle blanche | Expert |
| Manipulation wafers | Expert |
| Lecture de gammes | Avancé |
| Utilisation des systèmes MES | Avancé |
| Contrôles visuels | Avancé |

**Compétences transverses**

- Rigueur et discipline
- Respect des consignes
- Travail en équipe
- Résistance au travail posté

**Formation type**

- Bac Pro ou Bac technologique
- Formation interne salle blanche (2-4 mois)
- Habilitations spécifiques

**Volume cible 2047** : 15 000

**Tension actuelle** : Moyenne

**Rémunération indicative** : 24-35 K€

---

### 3.4 Famille EQ — Équipements & Maintenance

---

#### EQ-DEV-001 — Ingénieur Conception Équipements

| Champ | Valeur |
|-------|--------|
| **Code** | EQ-DEV-001 |
| **Intitulé** | Ingénieur Conception Équipements Semiconducteurs |
| **Famille** | Équipements & Maintenance |
| **Sous-famille** | Développement Équipements |
| **Niveau** | Bac+5 |

**Mission**

Concevoir et développer les équipements de fabrication de semiconducteurs (gravure, dépôt, lithographie, métrologie).

**Activités principales**

- Concevoir les sous-systèmes mécaniques, électriques, fluidiques
- Développer les chambres de process (plasma, vide)
- Intégrer les systèmes de contrôle et automatisation
- Réaliser les prototypes et les valider
- Collaborer avec les clients (fabs) pour le cahier des charges
- Assurer le transfert en production

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Conception mécanique (CAO 3D) | Expert |
| Techniques du vide et plasmas | Expert |
| Automatisation et contrôle | Avancé |
| Thermique et fluidique | Avancé |
| Normes semi-conducteurs (SEMI) | Avancé |

**Compétences transverses**

- Créativité technique
- Vision système
- Gestion de projet
- Relation client

**Formation type**

- Ingénieur mécanique, physique ou généraliste
- Spécialisation vide/plasmas appréciée
- Établissements : Arts et Métiers, INSA, Centrale

**Volume cible 2047** : 5 000

**Tension actuelle** : Critique (filière à créer)

**Rémunération indicative** : 45-90 K€

---

#### EQ-MAI-002 — Technicien Maintenance Équipements

| Champ | Valeur |
|-------|--------|
| **Code** | EQ-MAI-002 |
| **Intitulé** | Technicien Maintenance Équipements |
| **Famille** | Équipements & Maintenance |
| **Sous-famille** | Maintenance |
| **Niveau** | Bac+2/3 |

**Mission**

Assurer la maintenance préventive et corrective des équipements de production pour garantir leur disponibilité et leurs performances.

**Activités principales**

- Réaliser les maintenances préventives planifiées
- Diagnostiquer et réparer les pannes
- Remplacer les pièces et consommables
- Qualifier les équipements après intervention
- Documenter les interventions (GMAO)
- Participer aux améliorations continues

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Maintenance électromécanique | Expert |
| Systèmes de vide | Avancé |
| Automatismes et PLC | Avancé |
| Diagnostic de pannes | Expert |
| Utilisation GMAO | Avancé |

**Compétences transverses**

- Réactivité
- Méthode et organisation
- Travail sous pression
- Communication avec la production

**Formation type**

- BTS/DUT maintenance industrielle, électrotechnique ou GEII
- Formation constructeur (6-12 mois)
- Habilitations électriques

**Volume cible 2047** : 12 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 30-50 K€

---

### 3.5 Famille PK — Packaging & Test

---

#### PK-ASS-002 — Ingénieur Packaging 3D/Avancé

| Champ | Valeur |
|-------|--------|
| **Code** | PK-ASS-002 |
| **Intitulé** | Ingénieur Packaging 3D/Avancé |
| **Famille** | Packaging & Test |
| **Sous-famille** | Assemblage |
| **Niveau** | Bac+5 |

**Mission**

Développer les technologies de packaging avancé (2.5D, 3D, chiplets) permettant d'intégrer plusieurs puces dans un même boîtier.

**Activités principales**

- Concevoir les architectures de packaging 3D
- Développer les procédés d'interconnexion (TSV, µbumps, hybrid bonding)
- Optimiser les performances thermiques et électriques
- Caractériser la fiabilité des assemblages
- Collaborer avec les équipes design et fab
- Suivre les évolutions technologiques

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Technologies de packaging avancé | Expert |
| Interconnexions (TSV, RDL, bumping) | Expert |
| Thermique des boîtiers | Avancé |
| Simulation (thermique, mécanique) | Avancé |
| Fiabilité des assemblages | Avancé |

**Compétences transverses**

- Innovation
- Vision système
- Collaboration internationale
- Veille technologique

**Formation type**

- Ingénieur matériaux, mécanique ou électronique
- Spécialisation packaging
- Doctorat apprécié pour R&D

**Volume cible 2047** : 3 000

**Tension actuelle** : Critique (compétence rare)

**Rémunération indicative** : 48-95 K€

---

#### PK-TST-001 — Ingénieur Test Produit

| Champ | Valeur |
|-------|--------|
| **Code** | PK-TST-001 |
| **Intitulé** | Ingénieur Test Produit |
| **Famille** | Packaging & Test |
| **Sous-famille** | Test |
| **Niveau** | Bac+5 |

**Mission**

Développer et optimiser les programmes de test pour valider le bon fonctionnement des circuits intégrés en production.

**Activités principales**

- Développer les programmes de test (ATE)
- Définir les stratégies de test (couverture, coût)
- Analyser les données de test et le rendement
- Optimiser le temps de test et le coût
- Déboguer les problèmes de test vs design
- Qualifier les nouveaux produits

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Programmation ATE (Teradyne, Advantest) | Expert |
| Conception de test (DFT, BIST) | Avancé |
| Analyse de données | Avancé |
| Électronique analogique et numérique | Avancé |
| Statistiques de test | Avancé |

**Compétences transverses**

- Rigueur analytique
- Optimisation coût/qualité
- Collaboration design/production
- Gestion des priorités

**Formation type**

- Ingénieur électronique
- Spécialisation test ou conception
- Établissements : ENSEEIHT, ENSEIRB, Polytech

**Volume cible 2047** : 4 000

**Tension actuelle** : Élevée

**Rémunération indicative** : 42-80 K€

---

### 3.6 Famille SU — Support & Fonctions Transverses

---

#### SU-QUA-001 — Ingénieur Qualité Process

| Champ | Valeur |
|-------|--------|
| **Code** | SU-QUA-001 |
| **Intitulé** | Ingénieur Qualité Process |
| **Famille** | Support & Fonctions Transverses |
| **Sous-famille** | Qualité & Conformité |
| **Niveau** | Bac+5 |

**Mission**

Garantir la qualité des procédés de fabrication en définissant les standards, auditant les pratiques et pilotant l'amélioration continue.

**Activités principales**

- Définir et maintenir le système qualité (ISO, IATF)
- Auditer les procédés et les pratiques
- Analyser les non-conformités et piloter les actions correctives
- Qualifier les nouveaux procédés et équipements
- Former les équipes aux standards qualité
- Gérer les relations qualité avec les clients

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Systèmes de management qualité | Expert |
| Outils qualité (8D, FMEA, SPC) | Expert |
| Audit interne et fournisseurs | Expert |
| Normes sectorielles (IATF 16949, etc.) | Expert |
| Statistiques appliquées | Avancé |

**Compétences transverses**

- Rigueur et exigence
- Pédagogie
- Communication assertive
- Gestion des conflits

**Formation type**

- Ingénieur généraliste ou spécialisé
- Formation qualité (Green/Black Belt)
- Expérience production appréciée

**Volume cible 2047** : 3 000

**Tension actuelle** : Moyenne

**Rémunération indicative** : 45-80 K€

---

#### SU-MAN-002 — Responsable Production

| Champ | Valeur |
|-------|--------|
| **Code** | SU-MAN-002 |
| **Intitulé** | Responsable Production |
| **Famille** | Support & Fonctions Transverses |
| **Sous-famille** | Management & Gestion |
| **Niveau** | Bac+5 + expérience |

**Mission**

Piloter une unité de production (module ou zone) en assurant la performance en termes de volume, qualité, coût et délai.

**Activités principales**

- Manager les équipes de production (30-100 personnes)
- Planifier et suivre la production
- Garantir les objectifs de rendement et qualité
- Piloter l'amélioration continue
- Gérer les ressources (équipes, équipements, budget)
- Reporter à la direction

**Compétences techniques**

| Compétence | Niveau requis |
|------------|---------------|
| Management d'équipes | Expert |
| Lean manufacturing | Expert |
| Gestion de production | Expert |
| Process semiconducteurs | Avancé |
| Outils de pilotage (MES, KPI) | Expert |

**Compétences transverses**

- Leadership
- Prise de décision
- Gestion du stress
- Communication multi-niveaux

**Formation type**

- Ingénieur + expérience fab (5-10 ans)
- Formation management
- MBA apprécié

**Volume cible 2047** : 1 500

**Tension actuelle** : Élevée

**Rémunération indicative** : 70-120 K€

---

## 4. Matrice des Compétences

### 4.1 Compétences Techniques Transversales

| Compétence | RD | CO | FA | EQ | PK | SU |
|------------|:--:|:--:|:--:|:--:|:--:|:--:|
| Physique des semiconducteurs | ●●● | ●● | ●●● | ●● | ● | ○ |
| Chimie des matériaux | ●●● | ○ | ●●● | ●● | ●● | ○ |
| Électronique numérique | ●● | ●●● | ● | ● | ●● | ○ |
| Électronique analogique | ●● | ●●● | ● | ● | ●● | ○ |
| Programmation (Python, C++) | ●●● | ●●● | ●● | ●● | ●● | ● |
| Statistiques / Data science | ●●● | ●● | ●●● | ● | ●● | ●● |
| CAO électronique (EDA) | ● | ●●● | ○ | ○ | ● | ○ |
| Métrologie | ●●● | ● | ●●● | ●● | ●● | ●● |
| Techniques du vide | ●● | ○ | ●●● | ●●● | ● | ○ |
| Automatisation/PLC | ● | ○ | ●● | ●●● | ●● | ○ |

Légende : ●●● Critique | ●● Important | ● Utile | ○ Non requis

### 4.2 Compétences Comportementales Clés

| Compétence | Description | Métiers concernés |
|------------|-------------|-------------------|
| **Rigueur scientifique** | Méthode, reproductibilité, documentation | RD, FA, CO, PK |
| **Résolution de problèmes** | Analyse root cause, créativité solutions | Tous |
| **Travail en équipe** | Collaboration, communication, partage | Tous |
| **Gestion de projet** | Planning, ressources, reporting | RD, CO, SU |
| **Leadership** | Vision, motivation, décision | SU, seniors |
| **Adaptabilité** | Changement, apprentissage continu | Tous |
| **Communication technique** | Oral, écrit, anglais | Tous |
| **Orientation client** | Écoute, service, réactivité | SU, EQ |

### 4.3 Niveaux de Maîtrise

| Niveau | Description | Indicateurs |
|--------|-------------|-------------|
| **1 - Initié** | Connaissances de base, travail supervisé | Formation initiale, <1 an expérience |
| **2 - Intermédiaire** | Autonomie sur tâches courantes | 1-3 ans expérience |
| **3 - Avancé** | Expertise technique, résolution problèmes complexes | 3-7 ans expérience |
| **4 - Expert** | Référent, innovation, formation autres | 7+ ans expérience |
| **5 - Maître** | Reconnaissance internationale, thought leader | 15+ ans, publications, brevets |

---

## 5. Gap Analysis : Situation Actuelle vs Cible

### 5.1 Synthèse Globale

| Famille | Effectif 2026 | Cible 2047 | Gap | Taux de croissance |
|---------|---------------|------------|-----|-------------------|
| RD - Recherche | 8 000 | 18 000 | +10 000 | +125% |
| CO - Conception | 12 000 | 35 000 | +23 000 | +192% |
| FA - Fabrication | 25 000 | 65 000 | +40 000 | +160% |
| EQ - Équipements | 5 000 | 28 000 | +23 000 | +460% |
| PK - Packaging/Test | 8 000 | 22 000 | +14 000 | +175% |
| SU - Support | 12 000 | 32 000 | +20 000 | +167% |
| **TOTAL** | **70 000** | **200 000** | **+130 000** | **+186%** |

### 5.2 Métiers en Tension Critique

| Rang | Métier | Gap | Difficulté formation | Concurrence internationale |
|------|--------|-----|---------------------|---------------------------|
| 1 | Ingénieur Conception Équipements | +4 500 | Très élevée | Faible (niche) |
| 2 | Architecte CPU/GPU | +1 800 | Très élevée | Très élevée |
| 3 | Ingénieur RISC-V | +2 300 | Élevée | Élevée |
| 4 | Ingénieur Process Lithographie | +3 000 | Élevée | Élevée |
| 5 | Ingénieur Packaging 3D | +2 700 | Élevée | Moyenne |
| 6 | Architecte SoC | +2 500 | Très élevée | Très élevée |
| 7 | Ingénieur R&D Process | +4 200 | Élevée | Élevée |
| 8 | Technicien Maintenance Équipements | +10 000 | Moyenne | Faible |
| 9 | Technicien Salle Blanche | +15 000 | Moyenne | Faible |
| 10 | Ingénieur Yield Enhancement | +2 000 | Élevée | Moyenne |

### 5.3 Analyse par Niveau de Qualification

| Niveau | 2026 | 2047 | Gap | % du total |
|--------|------|------|-----|------------|
| Bac+8 (Doctorat) | 5 000 | 15 000 | +10 000 | 7.5% |
| Bac+5 (Ingénieur/Master) | 30 000 | 85 000 | +55 000 | 42.5% |
| Bac+2/3 (Technicien) | 25 000 | 70 000 | +45 000 | 35% |
| Bac/Bac Pro (Opérateur) | 10 000 | 30 000 | +20 000 | 15% |
| **TOTAL** | **70 000** | **200 000** | **+130 000** | **100%** |

### 5.4 Pyramide des Âges et Renouvellement

**Problématique** : 30% des effectifs actuels partiront en retraite d'ici 2040.

| Tranche d'âge | % effectif 2026 | Départs 2027-2040 | Départs 2040-2047 |
|---------------|-----------------|-------------------|-------------------|
| 55-65 ans | 15% | 10 500 | — |
| 45-54 ans | 25% | — | 17 500 |
| 35-44 ans | 30% | — | — |
| 25-34 ans | 25% | — | — |
| <25 ans | 5% | — | — |

**Besoin total en recrutements 2027-2047** : 130 000 (croissance) + 28 000 (renouvellement) = **158 000 personnes**

---

## 6. Pyramide des Qualifications

### 6.1 Structure Cible 2047

```
                          ┌───────────────┐
                          │   DOCTORAT    │
                          │    15 000     │
                          │     7.5%      │
                          └───────┬───────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │      INGÉNIEUR/MASTER     │
                    │          85 000           │
                    │           42.5%           │
                    └─────────────┬─────────────┘
                                  │
              ┌───────────────────┴───────────────────┐
              │           TECHNICIEN (Bac+2/3)        │
              │                70 000                 │
              │                 35%                   │
              └───────────────────┬───────────────────┘
                                  │
        ┌─────────────────────────┴─────────────────────────┐
        │              OPÉRATEUR (Bac/Bac Pro)              │
        │                      30 000                       │
        │                        15%                        │
        └───────────────────────────────────────────────────┘
```

### 6.2 Ratios par Type d'Activité

| Activité | Docteurs | Ingénieurs | Techniciens | Opérateurs |
|----------|----------|------------|-------------|------------|
| R&D | 30% | 55% | 15% | 0% |
| Conception | 10% | 75% | 15% | 0% |
| Fabrication | 3% | 25% | 45% | 27% |
| Équipements | 5% | 40% | 45% | 10% |
| Packaging/Test | 5% | 35% | 45% | 15% |
| Support | 2% | 45% | 40% | 13% |

### 6.3 Flux de Formation Annuel Requis

Pour atteindre les objectifs, les flux de formation doivent évoluer :

| Période | Docteurs/an | Ingénieurs/an | Techniciens/an | Opérateurs/an | Total/an |
|---------|-------------|---------------|----------------|---------------|----------|
| 2027-2032 | 400 | 2 500 | 2 000 | 1 000 | 5 900 |
| 2032-2039 | 600 | 4 000 | 3 500 | 1 500 | 9 600 |
| 2039-2047 | 700 | 4 500 | 3 500 | 1 500 | 10 200 |

---

## 7. Tensions et Priorités de Formation

### 7.1 Matrice Tension / Difficulté de Formation

```
                        DIFFICULTÉ DE FORMATION
                    Faible    Moyenne    Élevée    Très élevée
                 ┌─────────┬──────────┬──────────┬─────────────┐
         Critique│         │Tech Maint│Ing Litho │Archi CPU/GPU│
                 │         │Tech SB   │Ing RISC-V│Archi SoC    │
    TENSION      │         │          │Ing R&D   │Ing Concept  │
                 │         │          │Ing Pkg3D │Équipements  │
                 ├─────────┼──────────┼──────────┼─────────────┤
         Élevée  │Op. SB   │Tech Test │Ing RTL   │Chercheurs   │
                 │         │Tech Litho│Ing Verif │             │
                 │         │          │Ing P&R   │             │
                 ├─────────┼──────────┼──────────┼─────────────┤
         Moyenne │         │Tech HSE  │Ing Quali │             │
                 │         │Planif.   │Ing Test  │             │
                 ├─────────┼──────────┼──────────┼─────────────┤
         Faible  │         │          │          │             │
                 └─────────┴──────────┴──────────┴─────────────┘

LÉGENDE ACTIONS :
■ Zone critique-très élevée : Programmes spéciaux urgents
■ Zone critique-élevée : Renforcement massif des cursus
■ Zone élevée : Augmentation capacités existantes
□ Zone moyenne/faible : Ajustements marginaux
```

### 7.2 Priorités de Formation (Ordre d'Urgence)

**Priorité 1 — Actions immédiates (2027-2029)**

| Action | Métiers ciblés | Mécanisme | Volume |
|--------|---------------|-----------|--------|
| Création Masters spécialisés | Archi CPU, RISC-V, Équipements | Universités + Écoles | 500/an |
| Chaires industrielles | Conception, Lithographie | Partenariats entreprises | 30 chaires |
| Programmes reconversion accélérés | Techniciens maintenance | AFPA, GRETA, entreprises | 2 000/an |
| Attractivité talents internationaux | Tous profils critiques | Visa talent, packages | 500/an |

**Priorité 2 — Montée en puissance (2029-2035)**

| Action | Métiers ciblés | Mécanisme | Volume |
|--------|---------------|-----------|--------|
| Nouveaux campus microélectronique | Tous | Création établissements | 3 campus |
| Scaling IUT/BUT | Techniciens | Extension capacités | +3 000/an |
| Doctorats industriels | R&D, Conception | CIFRE renforcé | +300/an |
| Certifications professionnelles | Équipements, Process | Branches + État | 10 certifications |

**Priorité 3 — Consolidation (2035-2047)**

| Action | Métiers ciblés | Mécanisme | Volume |
|--------|---------------|-----------|--------|
| Pérennisation flux | Tous | Stabilisation système | 10 000/an |
| Formation continue | Mise à jour compétences | CPF, plan entreprise | 20 000/an |
| Excellence internationale | Chercheurs, Architectes | Instituts d'excellence | 5 instituts |

### 7.3 Passerelles et Mobilités

| Profil d'origine | Métier cible | Formation passerelle | Durée |
|------------------|--------------|---------------------|-------|
| Technicien auto | Technicien salle blanche | Certification SB + stage | 6 mois |
| Ingénieur aéro | Ingénieur process | Master spécialisé | 12 mois |
| Développeur logiciel | Ingénieur conception RTL | Formation HDL + stage | 9 mois |
| Physicien recherche | Ingénieur R&D process | Immersion industrielle | 6 mois |
| Technicien chimie | Technicien wet/CMP | Formation process + stage | 4 mois |
| Ingénieur électronique | Ingénieur test | Formation ATE | 3 mois |

---

## Annexes du Référentiel

### A.1 Glossaire des Termes Techniques

| Terme | Définition |
|-------|------------|
| ALD | Atomic Layer Deposition - dépôt couche atomique |
| ATE | Automatic Test Equipment - testeur automatique |
| CVD | Chemical Vapor Deposition - dépôt chimique en phase vapeur |
| DFT | Design For Test - conception pour la testabilité |
| DOE | Design Of Experiments - plans d'expériences |
| EDA | Electronic Design Automation - outils CAO électronique |
| EUV | Extreme Ultra-Violet - lithographie UV extrême |
| FDSOI | Fully Depleted Silicon On Insulator |
| HDL | Hardware Description Language (Verilog, VHDL) |
| IP | Intellectual Property - bloc de propriété intellectuelle |
| MES | Manufacturing Execution System |
| OPC | Optical Proximity Correction |
| OSAT | Outsourced Semiconductor Assembly and Test |
| P&R | Place & Route - placement et routage |
| RIE | Reactive Ion Etching - gravure ionique réactive |
| RTL | Register Transfer Level - niveau transfert de registres |
| SoC | System on Chip - système sur puce |
| STA | Static Timing Analysis - analyse de timing statique |
| TSV | Through-Silicon Via - via traversant le silicium |
| UVM | Universal Verification Methodology |

### A.2 Établissements de Formation de Référence

| Établissement | Spécialités | Localisation |
|---------------|-------------|--------------|
| Grenoble INP - Phelma | Process, Conception, Matériaux | Grenoble |
| INSA Lyon | Microélectronique, Matériaux | Lyon |
| Polytechnique | Physique, Architecture | Saclay |
| CentraleSupélec | Systèmes, Électronique | Saclay |
| Télécom Paris | Conception, Systèmes | Saclay |
| ENSEIRB-MATMECA | Électronique, Conception | Bordeaux |
| ENSEEIHT | Électronique, Automatique | Toulouse |
| ISAE-SUPAERO | Systèmes embarqués | Toulouse |
| ENS Paris-Saclay | Recherche fondamentale | Saclay |
| Université Grenoble Alpes | Physique, Matériaux | Grenoble |

### A.3 Certifications Professionnelles Existantes

| Certification | Domaine | Organisme |
|---------------|---------|-----------|
| Six Sigma Green/Black Belt | Qualité, Process | ASQ, IASSC |
| ISTQB | Test logiciel | ISTQB |
| IPC-A-610 | Assemblage électronique | IPC |
| Habilitations électriques | Sécurité | INRS |
| SEMI S2/S8 | Sécurité équipements | SEMI |

---

*Document de référence — Version 0.1*  
*Projet GenToGen2027 / TOGAFrance*  
*À compléter avec les fiches métiers détaillées restantes*
