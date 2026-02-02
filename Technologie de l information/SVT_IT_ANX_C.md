# SVT_IT_ANX_C — Cartographie Industrielle Cible
## Plan de Souveraineté IT 2027-2047

---

**Document de référence** : SVT_IT_00, SVT_IT_ANX_00, SVT_IT_ANX_A, SVT_IT_ANX_B  
**Classification** : Public  
**Auteur** : Jeff / Jagrat  
**Date** : Janvier 2026  
**Version** : 0.1

---

## Sommaire

1. [Analyse de la Chaîne de Valeur Actuelle](#1-chaîne-de-valeur-actuelle)
2. [Chaîne de Valeur Cible 2047](#2-chaîne-de-valeur-cible-2047)
3. [Cartographie des Entreprises à Créer](#3-entreprises-à-créer)
4. [Fiches Détaillées par Segment](#4-fiches-par-segment)
5. [Stratégie de Consolidation](#5-stratégie-de-consolidation)
6. [Écosystème de Soutien](#6-écosystème-de-soutien)
7. [Plan d'Action et Calendrier](#7-plan-daction)
8. [Budget et Financement](#8-budget-et-financement)

---

## 1. Analyse de la Chaîne de Valeur Actuelle

### 1.1 Vue d'Ensemble de l'Industrie Mondiale

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHAÎNE DE VALEUR MONDIALE SEMICONDUCTEURS                │
│                         (Parts de marché 2025)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONCEPTION        FABRICATION       ÉQUIPEMENTS      MATÉRIAUX            │
│  ───────────       ───────────       ───────────      ─────────            │
│                                                                             │
│  🇺🇸 USA 60%       🇹🇼 Taïwan 65%    🇳🇱 ASML 85%     🇯🇵 Japon 55%        │
│  (Apple, Nvidia,   (TSMC)           (litho EUV)      (chimie, gaz)        │
│   AMD, Qualcomm)                                                           │
│                    🇰🇷 Corée 18%     🇺🇸 USA 35%      🇩🇪 Allemagne 15%    │
│  🇨🇳 Chine 15%     (Samsung)        (Applied, Lam)   (Merck, BASF)        │
│  (HiSilicon,                                                               │
│   montée rapide)   🇺🇸 USA 10%      🇯🇵 Japon 30%    🇺🇸 USA 15%          │
│                    (Intel, GF)      (TEL, SCREEN)    (Entegris, CMC)      │
│  🇪🇺 Europe 8%                                                             │
│  (ARM UK, NXP,     🇨🇳 Chine 5%     🇰🇷 Corée 5%     🇨🇳 Chine 10%        │
│   Infineon)        (SMIC)                            (terres rares)        │
│                                                                             │
│  🇫🇷 FRANCE <1%    🇪🇺 Europe 2%    🇪🇺 Europe <5%   🇫🇷 FRANCE 3%        │
│  (quelques IP)     (STMicro,        (quelques PME)   (Air Liquide,        │
│                     X-Fab)                            Soitec)              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Acteurs Français Existants

#### Fabrication (IDM et Fonderie)

| Entreprise | CA 2024 | Effectifs FR | Activité | Nœud techno | Forces | Faiblesses |
|------------|---------|--------------|----------|-------------|--------|------------|
| **STMicroelectronics** | 17 Md$ | 11 000 | IDM | 28nm (18nm FDSOI) | Leader européen, R&D forte | Pas de nœuds avancés |
| **X-Fab** | 800 M$ | 800 | Fonderie spécialisée | 180nm-60nm | Niches (auto, médical) | Taille limitée |
| **Altis Semiconductor** | 150 M€ | 400 | Fonderie mature | 250nm+ | Composants discrets | Technologie ancienne |

#### Matériaux et Substrats

| Entreprise | CA 2024 | Effectifs FR | Activité | Position mondiale |
|------------|---------|--------------|----------|-------------------|
| **Soitec** | 1,1 Md€ | 2 000 | Substrats SOI | #1 mondial SOI |
| **Air Liquide Electronics** | 2 Md€ | 1 500 | Gaz ultra-purs | #2 mondial gaz électronique |
| **Kem One** | 400 M€ | 300 | Chimie fine | Position de niche |

#### Conception (Fabless et IP)

| Entreprise | CA 2024 | Effectifs FR | Activité | Spécialité |
|------------|---------|--------------|----------|------------|
| **Kalray** | 30 M€ | 200 | Processeurs | MPPA (calcul massif) |
| **GreenWaves Technologies** | 15 M€ | 80 | Processeurs IA | GAP (edge AI) |
| **Music not Noise** | 5 M€ | 30 | Processeurs audio | DSP basse conso |
| **Music IC** | 10 M€ | 40 | Circuits audio | Amplis, convertisseurs |
| **Tiempo Secure** | 8 M€ | 50 | IP sécurité | Circuits asynchrones |
| **Dolphin Design** | 20 M€ | 100 | IP basse conso | Ultra-low power |

#### Équipements et Services

| Entreprise | CA 2024 | Effectifs FR | Activité | Position |
|------------|---------|--------------|----------|----------|
| **RECIF Technologies** | 25 M€ | 80 | Manipulation wafers | Niche mondiale |
| **SET** | 40 M€ | 150 | Équipements packaging | Leader flip-chip |
| **Screen Semiconductor FR** | 50 M€ | 100 | Maintenance, support | Filiale japonaise |
| **Pfeiffer Vacuum FR** | 80 M€ | 200 | Pompes à vide | Filiale allemande |

#### Test et Services

| Entreprise | CA 2024 | Effectifs FR | Activité |
|------------|---------|--------------|----------|
| **Presto Engineering** | 60 M€ | 200 | Test, caractérisation |
| **e-Xstream (Hexagon)** | 30 M€ | 100 | Simulation |
| **Serma Technologies** | 100 M€ | 500 | Analyse, fiabilité |

### 1.3 Diagnostic : Forces et Faiblesses

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ANALYSE SWOT INDUSTRIE FRANÇAISE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FORCES                                    FAIBLESSES                       │
│  ───────                                   ──────────                       │
│  ✓ STMicro : champion européen             ✗ Aucune fonderie avancée (<14nm)│
│  ✓ Soitec : leader mondial substrats SOI   ✗ Absence quasi-totale équipements│
│  ✓ Air Liquide : excellence gaz            ✗ Pas de capacité mémoires       │
│  ✓ CEA-Leti : R&D de classe mondiale       ✗ Écosystème fabless embryonnaire│
│  ✓ Compétences FDSOI                       ✗ Dépendance critique ASML      │
│  ✓ Talents (mais en fuite)                 ✗ Manque d'intégration verticale │
│                                                                             │
│  OPPORTUNITÉS                              MENACES                          │
│  ────────────                              ───────                          │
│  ○ Chips Act européen (43 Md€)             ● Domination asiatique croissante│
│  ○ Relocalisation post-COVID               ● Guerre commerciale US-Chine    │
│  ○ Électrification (auto, énergie)         ● Course aux subventions mondiale│
│  ○ IA : explosion de la demande            ● Pénurie talents mondiale       │
│  ○ Souveraineté : prise de conscience      ● Retard technologique cumulatif │
│  ○ RISC-V : opportunité architecturale     ● Coûts des fabs exponentiels    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.4 Gaps Critiques par Segment

| Segment | Situation actuelle | Gap vs leaders | Urgence |
|---------|-------------------|----------------|---------|
| Fonderie avancée (<14nm) | Néant | Total | **Critique** |
| Mémoires (DRAM, HBM) | Néant | Total | **Critique** |
| Équipements lithographie | Néant | Total | **Critique** |
| Équipements gravure/dépôt | Quelques PME | Majeur | Élevée |
| Packaging avancé (2.5D/3D) | Embryonnaire | Important | Élevée |
| Conception fabless | Quelques start-ups | Important | Élevée |
| EDA / Outils CAO | Néant | Total | Moyenne |
| Métrologie avancée | Partiel | Modéré | Moyenne |
| Substrats | Soitec (SOI) | Limité | Faible |
| Gaz et chimie | Air Liquide | Limité | Faible |

---

## 2. Chaîne de Valeur Cible 2047

### 2.1 Vision Stratégique

**Objectif** : Construire une chaîne de valeur souveraine couvrant 70% des besoins critiques (défense, infrastructure, santé) avec un écosystème compétitif à l'export sur les niches d'excellence.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHAÎNE DE VALEUR FRANCE/EUROPE 2047                      │
│                         (Objectifs de parts mondiales)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│         AMONT                    CŒUR                       AVAL            │
│                                                                             │
│  ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐     │
│  │   MATÉRIAUX     │      │   FABRICATION   │      │   PACKAGING     │     │
│  │                 │      │                 │      │                 │     │
│  │ Substrats  15%  │─────▶│ Fonderie   10%  │─────▶│ OSAT        8%  │     │
│  │ Gaz/Chimie 20%  │      │ IDM        15%  │      │ Avancé     12%  │     │
│  │ Précurseurs 10% │      │ Mémoires    3%  │      │                 │     │
│  └─────────────────┘      └─────────────────┘      └─────────────────┘     │
│           │                        │                        │               │
│           │               ┌────────┴────────┐               │               │
│           │               ▼                 ▼               │               │
│           │      ┌─────────────┐   ┌─────────────┐         │               │
│           │      │ ÉQUIPEMENTS │   │ CONCEPTION  │         │               │
│           │      │             │   │             │         │               │
│           │      │ Litho    5% │   │ Fabless 8%  │         │               │
│           │      │ Process 15% │   │ IP      10% │         │               │
│           │      │ Test    10% │   │ EDA      5% │         │               │
│           │      └─────────────┘   └─────────────┘         │               │
│           │                                                 │               │
│           └─────────────────────┬───────────────────────────┘               │
│                                 ▼                                           │
│                    ┌─────────────────────────┐                              │
│                    │     INTÉGRATION         │                              │
│                    │                         │                              │
│                    │  Systèmes défense  90%  │                              │
│                    │  Infra critique    70%  │                              │
│                    │  Automobile        40%  │                              │
│                    │  Grand public      20%  │                              │
│                    └─────────────────────────┘                              │
│                                                                             │
│  LÉGENDE : % = Part de marché mondial visée pour la France/Europe          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Positionnement Stratégique par Segment

| Segment | Stratégie | Ambition 2047 | Justification |
|---------|-----------|---------------|---------------|
| **Fonderie avancée** | Partenariat EU | 10% mondial (avec DE, NL) | Coûts prohibitifs seul |
| **Fonderie mature** | Expansion nationale | 15% mondial | Marché auto, industriel |
| **Mémoires** | Niche (HBM, spécialisées) | 3% mondial | Trop tard pour DRAM volume |
| **Équipements litho** | Partenariat + niches | 5% mondial | ASML incontournable |
| **Équipements process** | Champion national | 15% mondial | Créneau accessible |
| **Packaging avancé** | Leadership européen | 12% mondial | Croissance forte, window |
| **Conception fabless** | Écosystème dense | 8% mondial | Faible capex, forte valeur |
| **IP et EDA** | Niches spécialisées | 5-10% mondial | Différenciation |
| **Matériaux** | Consolidation leadership | 15-20% mondial | Acquis à défendre |

### 2.3 Dimensionnement de l'Écosystème Cible

| Catégorie | 2026 | 2032 | 2039 | 2047 |
|-----------|------|------|------|------|
| Grands groupes (>1 Md€ CA) | 3 | 5 | 7 | 10 |
| ETI (100 M€ - 1 Md€) | 15 | 35 | 60 | 80 |
| PME significatives (10-100 M€) | 40 | 100 | 180 | 250 |
| Start-ups (<10 M€) | 80 | 200 | 350 | 400 |
| **Total entreprises** | **138** | **340** | **597** | **740** |
| **Emplois directs** | **50 000** | **90 000** | **150 000** | **200 000** |
| **CA total filière** | **25 Md€** | **50 Md€** | **90 Md€** | **130 Md€** |

---

## 3. Cartographie des Entreprises à Créer

### 3.1 Vue Synthétique

| Segment | Entreprises existantes | À créer | À renforcer | Investissement total |
|---------|----------------------|---------|-------------|---------------------|
| Fonderie/IDM | 3 | 2 (fabs) | 3 | 55 Md€ |
| Mémoires | 0 | 1 (fab spécialisée) | — | 12 Md€ |
| Équipements lithographie | 0 | 2 | — | 10 Md€ |
| Équipements process | 5 | 12 | 5 | 8 Md€ |
| Équipements métrologie/test | 3 | 6 | 3 | 4 Md€ |
| Packaging/OSAT | 2 | 8 | 2 | 6 Md€ |
| Conception fabless | 10 | 25 | 10 | 4 Md€ |
| IP/EDA | 3 | 5 | 3 | 2 Md€ |
| Matériaux/Chimie | 8 | 6 | 8 | 5 Md€ |
| Services (test, design) | 10 | 10 | 10 | 2 Md€ |
| **TOTAL** | **44** | **~75** | **~44** | **108 Md€** |

### 3.2 Matrice de Création par Phase

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              CALENDRIER DE CRÉATION/RENFORCEMENT DES ENTREPRISES            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1 (2027-2032)           PHASE 2 (2032-2039)      PHASE 3 (2039-2047)│
│  ──────────────────           ──────────────────       ─────────────────── │
│                                                                             │
│  FONDERIE                     FONDERIE                  FONDERIE            │
│  • Extension STMicro Crolles  • Fab EU 7nm (FR/DE/NL)  • Fab EU 3nm        │
│  • Fab FR 14nm (projet)       • Extension capacités     • Consolidation     │
│                                                                             │
│  ÉQUIPEMENTS                  ÉQUIPEMENTS               ÉQUIPEMENTS         │
│  • Création Litho FR #1       • Création Litho FR #2   • Maturité champions │
│  • 5 PME process              • 7 ETI process          • Export mondial     │
│  • 3 PME métrologie           • 3 ETI métrologie                            │
│                                                                             │
│  PACKAGING                    PACKAGING                 PACKAGING           │
│  • 3 start-ups packaging      • 5 ETI packaging        • Leaders européens  │
│  • Extension SET              • Fab packaging 3D                            │
│                                                                             │
│  CONCEPTION                   CONCEPTION                CONCEPTION          │
│  • 10 start-ups fabless       • 15 scale-ups           • 5+ licornes        │
│  • Accélérateur RISC-V        • Champions RISC-V       • Export IP          │
│  • 2 éditeurs EDA             • 3 éditeurs EDA                              │
│                                                                             │
│  MATÉRIAUX                    MATÉRIAUX                 MATÉRIAUX           │
│  • 3 PME chimie               • 3 ETI consolidées      • Leadership mondial │
│  • Extension Soitec           • Nouveaux substrats                          │
│                                                                             │
│  Budget phase : 35 Md€        Budget phase : 45 Md€    Budget phase : 28 Md€│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Fiches Détaillées par Segment

### 4.1 Segment Fonderie et IDM

---

#### PROJ-FAB-01 : Extension et Modernisation STMicroelectronics Crolles

**Type** : Renforcement acteur existant

**Situation actuelle**
- Site de Crolles : 300mm, technologie FDSOI 28nm/18nm
- Capacité : ~15 000 wafers/mois
- Effectifs : 5 000 personnes

**Projet**
- Extension capacité : +20 000 wafers/mois
- Nouveau bâtiment salle blanche : 25 000 m²
- Migration vers FDSOI 10nm
- Ligne pilote pour nœuds avancés

**Investissement** : 7,5 Md€ (2027-2035)

**Financement**
| Source | Part | Montant |
|--------|------|---------|
| STMicroelectronics | 40% | 3,0 Md€ |
| État français | 25% | 1,9 Md€ |
| Union Européenne (Chips Act) | 25% | 1,9 Md€ |
| Région AURA | 10% | 0,7 Md€ |

**Emplois créés** : +3 000 directs, +6 000 indirects

**Calendrier**
| Phase | Période | Contenu |
|-------|---------|---------|
| 1 | 2027-2029 | Construction nouveau bâtiment |
| 2 | 2029-2031 | Installation équipements |
| 3 | 2031-2033 | Montée en charge production |
| 4 | 2033-2035 | Pleine capacité |

---

#### PROJ-FAB-02 : Fab France 14nm — Nouvelle Fonderie Souveraine

**Type** : Création nouvelle entreprise

**Concept**
Créer une fonderie française/européenne capable de produire des puces en technologie 14nm FinFET, couvrant les besoins souverains (défense, infrastructure critique).

**Caractéristiques techniques**
| Paramètre | Spécification |
|-----------|---------------|
| Technologie | 14nm FinFET |
| Taille wafer | 300mm |
| Capacité cible | 40 000 wafers/mois |
| Surface salle blanche | 35 000 m² |
| Surface totale site | 50 hectares |

**Localisation proposée** : Nouvelle implantation (Nord ou Est France) ou extension Saclay

**Critères de choix site**
- Disponibilité foncière (50+ ha)
- Accès eau (500 000 m³/an)
- Électricité (200 MW, bas carbone)
- Bassin d'emploi technique
- Accessibilité (autoroute, TGV, aéroport)

**Investissement** : 18 Md€ (2028-2038)

**Structure juridique proposée**
- Joint-venture européenne
- Actionnariat : France 40%, Allemagne 30%, Pays-Bas 20%, Autres EU 10%
- Gouvernance paritaire avec golden share française pour décisions stratégiques

**Partenariats technologiques**
- Intel (licence technologie FinFET)
- ASML (équipements lithographie)
- Lam Research / Applied Materials (équipements process)
- CEA-Leti (R&D, qualification process)

**Emplois** : 5 000 directs + 10 000 indirects

**Calendrier**
| Phase | Période | Contenu | Budget |
|-------|---------|---------|--------|
| Études | 2027-2028 | Faisabilité, site, partenariats | 200 M€ |
| Construction | 2029-2033 | Bâtiments, infrastructure | 6 Md€ |
| Équipement | 2032-2036 | Installation, qualification | 10 Md€ |
| Ramp-up | 2036-2038 | Montée en volume | 1,8 Md€ |

---

#### PROJ-FAB-03 : Fab Européenne 7nm/5nm (Participation Française)

**Type** : Projet européen avec participation française

**Concept**
Participation française au projet européen de fonderie avancée sub-10nm, en partenariat avec l'Allemagne (Intel Magdeburg) et les Pays-Bas.

**Rôle France**
- Co-investissement (20% du projet)
- Fourniture équipements français
- Participation R&D (CEA-Leti)
- Clients garantis (défense, espace)

**Investissement France** : 8 Md€ sur 2030-2042

**Retombées**
- Accès garanti à capacité de production avancée
- Montée en compétences des équipes françaises
- Commandes pour équipementiers français

---

#### PROJ-FAB-04 : Fab Mémoires Spécialisées (HBM/eMRAM)

**Type** : Création nouvelle entreprise

**Concept**
Créer une capacité de production de mémoires spécialisées haute performance (HBM pour l'IA, eMRAM pour embarqué), segment à forte croissance et moindre intensité capitalistique que la DRAM standard.

**Positionnement**
- Ne pas concurrencer Samsung/SK Hynix sur DRAM standard
- Cibler les mémoires différenciées : HBM, MRAM, ReRAM
- Applications : IA, automobile, aérospatial, défense

**Partenariats**
- STMicroelectronics (intégration)
- CEA-Leti (R&D mémoires émergentes)
- Clients captifs (constructeurs IA européens)

**Investissement** : 12 Md€ (2032-2045)

**Emplois** : 2 500 directs

---

### 4.2 Segment Équipements

---

#### PROJ-EQP-01 : Champion National Lithographie — "LithoFrance"

**Type** : Création nouvelle entreprise

**Contexte**
ASML détient un monopole mondial sur la lithographie EUV. La dépendance est totale et représente un risque stratégique majeur. L'objectif n'est pas de concurrencer ASML sur l'EUV mais de :
1. Développer des alternatives DUV avancées
2. Maîtriser les technologies de lithographie pour les générations futures
3. Créer une capacité de maintenance souveraine

**Positionnement stratégique**
| Technologie | Leader actuel | Stratégie France |
|-------------|---------------|------------------|
| EUV | ASML (monopole) | Partenariat, pas de concurrence directe |
| DUV immersion | ASML, Nikon, Canon | Développement alternatif |
| NIL (nanoimprint) | Canon, EV Group | Opportunité de leadership |
| Lithographie directe (e-beam) | Niche | Potentiel souverain |

**Business model**
- Phase 1 (2027-2032) : Services de maintenance et retrofit
- Phase 2 (2032-2038) : Équipements DUV mid-range
- Phase 3 (2038-2047) : Technologies alternatives (NIL, multi-beam)

**Structure**
- Création ex nihilo avec essaimage CEA-Leti
- Partenariat avec acteurs optiques français (Thales, Safran)
- Licences technologiques (ASML pour maintenance, universités)

**Équipe fondatrice cible**
- 20 experts lithographie (CEA-Leti, ex-ASML, ex-Nikon)
- 10 ingénieurs optique (Thales, Safran)
- 5 managers industriels expérimentés

**Investissement** : 6 Md€ (2027-2042)

| Phase | Période | Investissement | Objectif |
|-------|---------|----------------|----------|
| Amorçage | 2027-2029 | 200 M€ | Équipe, R&D, prototypes |
| Développement | 2029-2035 | 2 Md€ | Premier équipement commercial |
| Industrialisation | 2035-2042 | 3,8 Md€ | Gamme complète, export |

**Emplois cibles** : 2 000 (2035), 4 000 (2045)

**CA cible** : 500 M€ (2035), 2 Md€ (2045)

---

#### PROJ-EQP-02 : ETI Gravure Plasma — "PlasmaFab"

**Type** : Création nouvelle entreprise

**Concept**
Créer un équipementier français spécialisé dans les équipements de gravure plasma, segment clé où Applied Materials et Lam Research dominent.

**Positionnement**
- Gravure plasma pour nœuds matures (28nm et au-dessus)
- Équipements spécialisés (matériaux III-V, SiC)
- Prix compétitif (-20% vs leaders américains)

**Avantages compétitifs visés**
- Proximité clients européens (STMicro, Infineon, NXP)
- Support et maintenance en français
- Customisation pour applications spécifiques

**Structure**
- Start-up deep tech avec spin-off CEA-Leti
- Partenariat avec industriel français (Air Liquide, Pfeiffer)

**Investissement** : 800 M€ (2028-2038)

**Emplois cibles** : 500 (2035), 1 200 (2045)

**CA cible** : 100 M€ (2035), 400 M€ (2045)

---

#### PROJ-EQP-03 : ETI Dépôt Couches Minces — "DepotTech"

**Type** : Création nouvelle entreprise

**Concept**
Équipementier spécialisé dans les équipements de dépôt de couches minces (CVD, PVD, ALD) pour la microélectronique.

**Segments cibles**
- ALD (Atomic Layer Deposition) pour nœuds avancés
- CVD spécialisé (diélectriques low-k, métaux)
- PVD pour interconnexions

**Investissement** : 600 M€ (2029-2040)

**Emplois cibles** : 400 (2035), 900 (2045)

---

#### PROJ-EQP-04 : Cluster PME Équipements Process

**Type** : Création et consolidation de PME

**Concept**
Faire émerger un écosystème de 10-15 PME spécialisées sur des niches d'équipements process, puis les consolider en ETI.

**Niches ciblées**

| Niche | PME à créer | Investissement unitaire | Marché mondial |
|-------|-------------|------------------------|----------------|
| Nettoyage wafers | 2 | 50 M€ | 3 Md€ |
| CMP (polissage) | 2 | 60 M€ | 4 Md€ |
| Recuit rapide (RTP) | 1 | 40 M€ | 1,5 Md€ |
| Implantation ionique | 1 | 80 M€ | 2 Md€ |
| Épitaxie | 2 | 70 M€ | 2 Md€ |
| Manipulation wafers | 1 (RECIF) | 30 M€ | 1 Md€ |
| Automation fab | 2 | 40 M€ | 3 Md€ |

**Mécanisme de soutien**
- Incubateur dédié "FabEquip Accelerator"
- Tickets d'amorçage : 2-5 M€ par projet
- Accompagnement technique : accès CEA-Leti
- Clients pilotes : STMicro, futures fabs

**Investissement total** : 1,5 Md€ (2027-2040)

**Emplois cibles** : 3 000 (cumulé 2045)

---

#### PROJ-EQP-05 : ETI Métrologie Semiconducteurs — "MetroSemi"

**Type** : Création par consolidation

**Concept**
Créer un champion français de la métrologie semiconducteurs par consolidation de PME existantes et création de nouvelles activités.

**Périmètre**
- Métrologie dimensionnelle (CD-SEM, scatterométrie)
- Métrologie de films (ellipsométrie, XRR)
- Inspection de défauts
- Métrologie électrique

**Cibles d'acquisition/partenariat**
- PME françaises existantes
- Activités métrologie de groupes diversifiés
- Start-ups deep tech

**Investissement** : 500 M€ (2028-2038)

**Emplois cibles** : 800 (2040)

---

#### PROJ-EQP-06 : ETI Équipements de Test — "TestFrance"

**Type** : Création nouvelle entreprise

**Concept**
Développer des équipements de test (ATE) pour semiconducteurs, marché dominé par Teradyne et Advantest.

**Positionnement**
- Test pour applications spécifiques (auto, aéro, défense)
- Test de puces françaises/européennes
- Intégration avec design houses françaises

**Investissement** : 400 M€ (2030-2042)

**Emplois cibles** : 600 (2042)

---

### 4.3 Segment Packaging et OSAT

---

#### PROJ-PKG-01 : Champion Packaging Avancé — "PackFrance 3D"

**Type** : Création nouvelle entreprise

**Contexte**
Le packaging avancé (2.5D, 3D, chiplets) est le segment à plus forte croissance. La France a une opportunité de prendre des positions avant que le marché ne se consolide.

**Technologies cibles**
| Technologie | Applications | Maturité | Position visée |
|-------------|--------------|----------|----------------|
| Fan-out WLP | Mobile, IoT | Mature | Fast follower |
| 2.5D (interposer) | HPC, IA | Croissance | Leader européen |
| 3D stacking | Mémoires HBM | Émergent | Pioneer |
| Chiplets | Processeurs | Émergent | Co-leader |
| Hybrid bonding | Tout | Futur | R&D avancée |

**Structure**
- Joint-venture : STMicro (30%) + SET (20%) + Investisseurs (30%) + État (20%)
- Site : Extension site SET (Alpes) + nouveau site (Toulouse)

**Capacité cible**
- 2035 : 10 000 wafers équivalents/mois
- 2045 : 50 000 wafers équivalents/mois

**Investissement** : 4 Md€ (2028-2042)

**Emplois cibles** : 3 000 (2042)

---

#### PROJ-PKG-02 : Réseau OSAT France

**Type** : Création de plusieurs entreprises

**Concept**
Créer 5-8 entreprises OSAT (Outsourced Semiconductor Assembly and Test) pour couvrir les besoins de packaging et test externalisés.

**Spécialisations**
| Entreprise | Spécialité | Localisation | Investissement |
|------------|------------|--------------|----------------|
| OSAT-Auto | Packaging automobile (AEC-Q) | Toulouse | 300 M€ |
| OSAT-Défense | Packaging haute fiabilité | Région parisienne | 250 M€ |
| OSAT-RF | Packaging RF et hyperfréquences | Sophia-Antipolis | 200 M€ |
| OSAT-Power | Packaging puissance (SiC, GaN) | Tours | 300 M€ |
| OSAT-Médical | Packaging implantables | Lyon | 150 M€ |

**Investissement total** : 1,5 Md€

**Emplois cibles** : 2 500 (cumulé)

---

### 4.4 Segment Conception (Fabless et IP)

---

#### PROJ-DES-01 : Écosystème Fabless RISC-V

**Type** : Programme d'accélération

**Contexte**
RISC-V est une opportunité historique de s'affranchir des architectures propriétaires (ARM, x86). La France doit créer un écosystème de conception autour de RISC-V.

**Composantes du programme**

| Composante | Description | Budget |
|------------|-------------|--------|
| Incubateur RISC-V | Accompagnement start-ups | 100 M€ |
| Fonds d'investissement | Tickets 1-20 M€ | 500 M€ |
| Plateforme de conception | Outils EDA mutualisés | 50 M€ |
| Programme de R&D | Cœurs souverains | 300 M€ |
| Certification | Processus de qualification | 50 M€ |

**Cibles de création**
- 15 start-ups fabless RISC-V (2027-2035)
- 5 scale-ups (>50 M€ CA) à horizon 2040
- 2 licornes potentielles à horizon 2045

**Domaines d'application prioritaires**
1. Processeurs edge AI / IoT
2. Processeurs sécurisés (défense, paiement)
3. Accélérateurs spécialisés (signal, crypto)
4. Processeurs automobiles (ADAS)
5. Processeurs pour le spatial

**Investissement total** : 1 Md€ (2027-2040)

**Emplois cibles** : 3 000 ingénieurs conception (2040)

---

#### PROJ-DES-02 : Renforcement Kalray — Champion National Processeurs

**Type** : Renforcement acteur existant

**Situation actuelle**
Kalray est la seule entreprise française à concevoir des processeurs haute performance (MPPA). Position fragile mais technologie différenciante.

**Plan de développement**
| Phase | Période | Objectif | Financement |
|-------|---------|----------|-------------|
| Survie | 2027-2029 | Atteindre rentabilité | 100 M€ |
| Croissance | 2029-2035 | Déploiement data centers | 200 M€ |
| Leadership | 2035-2040 | Champion européen | 300 M€ |

**Marchés cibles**
- Data centers (accélération IA)
- Automobile (ADAS niveau 4-5)
- Défense (systèmes embarqués critiques)

**Investissement public** : 300 M€ (subventions + participations)

**Emplois cibles** : 1 500 (2040)

---

#### PROJ-DES-03 : Éditeurs EDA Souverains

**Type** : Création et acquisition

**Contexte**
Les outils de conception (EDA) sont dominés par Synopsys, Cadence et Siemens. Dépendance totale et risque d'embargo.

**Stratégie**
1. Développer des outils open source (participation communauté mondiale)
2. Créer des éditeurs sur des niches spécifiques
3. Acquérir des start-ups EDA prometteuses

**Niches ciblées**
| Niche | Potentiel | Investissement |
|-------|-----------|----------------|
| Vérification formelle | Élevé | 80 M€ |
| Synthèse analogique | Moyen | 60 M€ |
| Place & route spécialisé | Moyen | 70 M€ |
| Simulation thermique 3D | Élevé | 50 M€ |
| IA pour EDA | Très élevé | 100 M€ |

**Investissement total** : 400 M€

**Emplois cibles** : 800 (2040)

---

#### PROJ-DES-04 : Consolidation IP Françaises

**Type** : Consolidation

**Acteurs existants**
- Dolphin Design (ultra-low power)
- Tiempo Secure (sécurité)
- Music IC / Music not Noise (audio)

**Objectif**
Créer un groupe IP français de taille critique pouvant rivaliser avec ARM, Imagination, CEVA.

**Scénario de consolidation**
- Holding "FranceIP" regroupant les acteurs
- Investissement en R&D mutualisé
- Force commerciale commune internationale

**Investissement** : 300 M€ (acquisitions + développement)

**CA cible groupe** : 500 M€ (2040)

---

### 4.5 Segment Matériaux et Chimie

---

#### PROJ-MAT-01 : Extension Soitec — Leadership Substrats

**Type** : Renforcement acteur existant

**Situation**
Soitec est n°1 mondial des substrats SOI. Position à défendre et étendre.

**Plan de développement**
| Axe | Investissement | Objectif |
|-----|---------------|----------|
| Extension capacité SOI | 1 Md€ | +50% capacité |
| Substrats SiC | 500 M€ | #3 mondial |
| Substrats GaN | 300 M€ | Position de leader |
| R&D substrats avancés | 200 M€ | Génération future |

**Investissement total** : 2 Md€ (2027-2037)

**Emplois supplémentaires** : +2 000

---

#### PROJ-MAT-02 : Cluster Chimie Électronique

**Type** : Création PME/ETI

**Concept**
Développer un écosystème de fournisseurs français de produits chimiques pour la microélectronique.

**Segments**
| Segment | PME à créer | Investissement | Leaders actuels |
|---------|-------------|----------------|-----------------|
| Résines photosensibles | 2 | 150 M€ | JSR, TOK, Shin-Etsu |
| Précurseurs ALD/CVD | 2 | 100 M€ | Entegris, Versum |
| Slurries CMP | 1 | 80 M€ | CMC, Fujimi |
| Solvants ultra-purs | 1 | 60 M€ | BASF, Honeywell |
| Acides/bases ultra-purs | 1 | 50 M€ | BASF, KMG |

**Partenariats**
- Air Liquide (distribution, purification)
- Arkema (chimie de spécialité)
- Solvay (matériaux avancés)

**Investissement total** : 500 M€

**Emplois cibles** : 1 500 (2040)

---

#### PROJ-MAT-03 : Sécurisation Terres Rares et Matériaux Critiques

**Type** : Programme stratégique

**Contexte**
La Chine contrôle 60% de la production mondiale de terres rares, essentielles pour certains composants.

**Actions**
| Action | Budget | Objectif |
|--------|--------|----------|
| Stocks stratégiques | 500 M€ | 2 ans de consommation |
| Recyclage électronique | 200 M€ | 20% des besoins |
| Diversification sources | 100 M€ | Accords avec Australie, Canada |
| Substitution matériaux | 150 M€ | R&D alternatives |

**Investissement total** : 950 M€

---

## 5. Stratégie de Consolidation

### 5.1 Vision de l'Écosystème Consolidé 2047

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ÉCOSYSTÈME FRANÇAIS SEMICONDUCTEURS 2047                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CHAMPIONS NATIONAUX (>1 Md€ CA)                                           │
│  ────────────────────────────────                                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │ STMicro     │ │ Soitec      │ │ LithoFrance │ │ PackFrance  │          │
│  │ (IDM)       │ │ (Substrats) │ │ (Équipements│ │ (Packaging) │          │
│  │ 25 Md€      │ │ 5 Md€       │ │  litho)     │ │ 3 Md€       │          │
│  │             │ │             │ │ 2 Md€       │ │             │          │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘          │
│                                                                             │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐          │
│  │ Air Liquide │ │ FranceIP    │ │ ProcessEquip│ │ Kalray      │          │
│  │ Electronics │ │ (IP/Design) │ │ (Équipements│ │ (Processeurs│          │
│  │ 4 Md€       │ │ 1 Md€       │ │  process)   │ │  HPC)       │          │
│  │             │ │             │ │ 2 Md€       │ │ 1 Md€       │          │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘          │
│                                                                             │
│  ETI SPÉCIALISÉES (100 M€ - 1 Md€ CA) : 80 entreprises                    │
│  ─────────────────────────────────────────────────────                     │
│  • 15 équipementiers process    • 10 sociétés de test                     │
│  • 8 OSAT/packaging             • 12 design houses                         │
│  • 10 fournisseurs matériaux    • 25 services/ingénierie                  │
│                                                                             │
│  PME ET START-UPS (<100 M€ CA) : 650 entreprises                          │
│  ───────────────────────────────────────────────                           │
│  • 150 en conception/IP         • 200 en services                          │
│  • 100 en équipements/outillage • 200 fournisseurs spécialisés            │
│                                                                             │
│  TOTAL : 740 entreprises | 200 000 emplois | 130 Md€ CA                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Mouvements de Consolidation Anticipés

| Période | Mouvement | Acteurs | Objectif |
|---------|-----------|---------|----------|
| 2028-2030 | Fusion IP | Dolphin + Tiempo + autres | Créer FranceIP |
| 2030-2033 | Consolidation équipements | PME process | Créer 3-4 ETI |
| 2032-2035 | Consolidation packaging | Start-ups + SET | Créer PackFrance |
| 2035-2038 | Consolidation OSAT | 5 OSAT régionaux | Créer réseau national |
| 2038-2042 | Consolidation design | Scale-ups RISC-V | Créer champions fabless |

### 5.3 Rôle de l'État dans la Consolidation

**Principes**
1. Faciliter sans forcer (incitations, pas de dirigisme)
2. Préserver la concurrence interne saine
3. Créer des champions capables d'exporter
4. Protéger contre les prédateurs étrangers (screening IDE)

**Outils**
| Outil | Usage |
|-------|-------|
| BPI France | Financement fusions, bridge loans |
| Fonds souverain | Prises de participation stratégiques |
| Screening IDE | Blocage acquisitions sensibles |
| Commande publique | Création de marchés captifs |
| Fiscalité | Incitations aux fusions franco-françaises |

---

## 6. Écosystème de Soutien

### 6.1 Infrastructure de Financement

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARCHITECTURE DE FINANCEMENT SEMICONDUCTEURS              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                         ┌─────────────────────┐                             │
│                         │  FONDS SOUVERAIN    │                             │
│                         │  SEMICONDUCTEURS    │                             │
│                         │  (10 Md€)           │                             │
│                         └──────────┬──────────┘                             │
│                                    │                                        │
│         ┌──────────────────────────┼──────────────────────────┐            │
│         ▼                          ▼                          ▼            │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐      │
│  │ FONDS AMORÇAGE  │     │ FONDS CROISSANCE│     │ FONDS STRATÉGIQUE│     │
│  │ (500 M€)        │     │ (2 Md€)         │     │ (5 Md€)          │     │
│  │                 │     │                 │     │                  │      │
│  │ Tickets:        │     │ Tickets:        │     │ Tickets:         │      │
│  │ 0,5 - 5 M€      │     │ 5 - 50 M€       │     │ 50 - 500 M€      │      │
│  │                 │     │                 │     │                  │      │
│  │ Cibles:         │     │ Cibles:         │     │ Cibles:          │      │
│  │ Start-ups       │     │ Scale-ups       │     │ Champions, Fabs  │      │
│  │ Spin-offs       │     │ ETI             │     │ Consolidation    │      │
│  └─────────────────┘     └─────────────────┘     └─────────────────┘      │
│         │                          │                          │            │
│         └──────────────────────────┼──────────────────────────┘            │
│                                    ▼                                        │
│                    ┌─────────────────────────┐                              │
│                    │   CO-INVESTISSEURS      │                              │
│                    │                         │                              │
│                    │ • BPI France            │                              │
│                    │ • CDC                   │                              │
│                    │ • Fonds privés (Tikehau,│                              │
│                    │   Eurazeo, Ardian...)   │                              │
│                    │ • Family offices        │                              │
│                    │ • Fonds européens (EIF) │                              │
│                    └─────────────────────────┘                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Infrastructure de R&D et Innovation

| Structure | Mission | Budget annuel |
|-----------|---------|---------------|
| **CEA-Leti** | R&D process et intégration | 400 M€ |
| **CEA-List** | R&D systèmes et logiciel | 150 M€ |
| **CNRS (labos)** | Recherche fondamentale | 100 M€ |
| **IRT Nanoelec** | Transfert technologique | 80 M€ |
| **Pôles de compétitivité** | Animation écosystème | 30 M€ |

### 6.3 Infrastructure d'Accompagnement

| Structure | Mission | Capacité |
|-----------|---------|----------|
| **Incubateur FabTech** | Accompagnement start-ups équipements | 30 start-ups/an |
| **Accélérateur RISC-V** | Programme dédié conception | 15 start-ups/an |
| **Station F - Vertical Semi** | Incubation généraliste | 50 start-ups |
| **Technocentres régionaux** | Accompagnement local | 100 projets/an |

### 6.4 Commande Publique Stratégique

**Principe** : Utiliser la commande publique pour créer des marchés captifs et soutenir l'écosystème.

| Secteur | Volume annuel | Part française cible |
|---------|---------------|---------------------|
| Défense | 2 Md€ | 80% |
| Spatial | 500 M€ | 70% |
| Santé publique | 300 M€ | 60% |
| Administration | 400 M€ | 50% |
| Énergie (EDF, etc.) | 600 M€ | 60% |
| Transport (SNCF, etc.) | 400 M€ | 50% |
| **Total mobilisable** | **4,2 Md€** | **~60%** |

---

## 7. Plan d'Action et Calendrier

### 7.1 Phase 1 : Fondations (2027-2032)

| Année | Actions clés | Budget |
|-------|--------------|--------|
| **2027** | Création Fonds Souverain Semi, Lancement incubateurs, Études de faisabilité fabs | 3 Md€ |
| **2028** | Création LithoFrance, 5 premières start-ups équipements, Extension STMicro (lancement) | 5 Md€ |
| **2029** | Création PlasmaFab et DepotTech, 10 start-ups fabless RISC-V, Décision site Fab 14nm | 6 Md€ |
| **2030** | Lancement construction Fab 14nm, Création PackFrance, Consolidation IP (FranceIP) | 8 Md€ |
| **2031** | Premier équipement LithoFrance, 5 OSAT régionaux lancés, Extension Soitec complète | 7 Md€ |
| **2032** | Fab 14nm : fin construction, Écosystème fabless : 25 entreprises, Cluster chimie opérationnel | 6 Md€ |

**Budget Phase 1** : 35 Md€

### 7.2 Phase 2 : Industrialisation (2032-2039)

| Année | Actions clés | Budget |
|-------|--------------|--------|
| **2033** | Fab 14nm : installation équipements, LithoFrance : gamme commerciale, Consolidation équipementiers | 7 Md€ |
| **2034** | Fab 14nm : qualification, PackFrance : capacité x3, Champions fabless émergents | 6 Md€ |
| **2035** | Fab 14nm : production volume, Participation Fab EU 7nm, Export équipements | 7 Md€ |
| **2036** | Extension capacités toutes fabs, 3 licornes fabless, Réseau OSAT complet | 6 Md€ |
| **2037** | Fab mémoires spécialisées (lancement), Consolidation ETI, Leadership packaging EU | 7 Md€ |
| **2038** | Maturité écosystème équipements, Export mondial, Préparation phase 3 | 6 Md€ |
| **2039** | Bilan phase 2, Ajustements stratégiques, Lancement projets phase 3 | 6 Md€ |

**Budget Phase 2** : 45 Md€

### 7.3 Phase 3 : Leadership (2039-2047)

| Période | Actions clés | Budget |
|---------|--------------|--------|
| **2039-2042** | Participation Fab EU 3nm, Technologies post-silicium, Champions mondiaux (3-5) | 15 Md€ |
| **2042-2045** | Consolidation leadership, Export massif, Nouvelles générations | 8 Md€ |
| **2045-2047** | Maturité écosystème, Ajustements, Préparation cycle suivant | 5 Md€ |

**Budget Phase 3** : 28 Md€

### 7.4 Jalons Clés

```
2027        2030        2033        2036        2040        2045        2047
  │           │           │           │           │           │           │
  ▼           ▼           ▼           ▼           ▼           ▼           ▼
┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
│Fonds│    │Fab  │    │Fab  │    │Fab  │    │Fab  │    │Fab  │    │Éco- │
│Souv.│    │14nm │    │14nm │    │14nm │    │EU   │    │EU   │    │syst.│
│créé │    │const│    │qual.│    │vol. │    │7nm  │    │3nm  │    │matur│
└─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
     │           │           │           │           │           │
     ▼           ▼           ▼           ▼           ▼           ▼
  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
  │Litho│    │Pack │    │Litho│    │3     │    │5     │    │Lead.│
  │FR   │    │FR   │    │FR   │    │licor-│    │champ.│    │mond.│
  │créé │    │créé │    │comm.│    │nes   │    │mond. │    │niches│
  └─────┘    └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
```

---

## 8. Budget et Financement

### 8.1 Budget Total par Segment

| Segment | Phase 1 | Phase 2 | Phase 3 | Total |
|---------|---------|---------|---------|-------|
| Fonderie/IDM | 15 Md€ | 25 Md€ | 15 Md€ | 55 Md€ |
| Mémoires | 2 Md€ | 5 Md€ | 5 Md€ | 12 Md€ |
| Équipements (tous) | 8 Md€ | 10 Md€ | 4 Md€ | 22 Md€ |
| Packaging/OSAT | 3 Md€ | 3 Md€ | — | 6 Md€ |
| Conception/IP/EDA | 4 Md€ | 2 Md€ | — | 6 Md€ |
| Matériaux/Chimie | 3 Md€ | — | 2 Md€ | 5 Md€ |
| Fonds/Écosystème | — | — | 2 Md€ | 2 Md€ |
| **TOTAL** | **35 Md€** | **45 Md€** | **28 Md€** | **108 Md€** |

### 8.2 Sources de Financement

| Source | Part | Montant | Mécanisme |
|--------|------|---------|-----------|
| Entreprises (fonds propres) | 35% | 38 Md€ | Investissements directs |
| État français | 25% | 27 Md€ | Subventions, prêts, participations |
| Union Européenne | 20% | 22 Md€ | Chips Act, IPCEI, Horizon Europe |
| Investisseurs privés | 12% | 13 Md€ | VC, PE, fonds souverains étrangers |
| Régions | 5% | 5 Md€ | Aides à l'implantation |
| Banques (dette) | 3% | 3 Md€ | Prêts garantis |
| **TOTAL** | **100%** | **108 Md€** | |

### 8.3 Retour sur Investissement

**Indicateurs économiques 2047**

| Indicateur | Valeur |
|------------|--------|
| CA filière française | 130 Md€ |
| Emplois directs | 200 000 |
| Emplois indirects | 400 000 |
| Exportations | 60 Md€ |
| Balance commerciale semi | +20 Md€ (vs -15 Md€ en 2025) |
| Recettes fiscales générées | 25 Md€/an |
| PIB additionnel | 80 Md€/an |

**ROI pour l'État**
- Investissement public : 27 Md€ sur 20 ans
- Recettes fiscales cumulées : 300 Md€ (20 ans)
- **ROI : x11**

---

## Annexes

### A.1 Liste des 75 Entreprises à Créer

| Réf. | Nom projet | Segment | Type | Investissement | Emplois 2045 |
|------|------------|---------|------|----------------|--------------|
| FAB-01 | Extension STMicro | Fonderie | Renforcement | 7,5 Md€ | 3 000 |
| FAB-02 | Fab France 14nm | Fonderie | Création | 18 Md€ | 5 000 |
| FAB-03 | Fab EU 7nm (part FR) | Fonderie | Participation | 8 Md€ | 1 000 |
| FAB-04 | Fab Mémoires | Mémoires | Création | 12 Md€ | 2 500 |
| EQP-01 | LithoFrance | Équipements | Création | 6 Md€ | 4 000 |
| EQP-02 | PlasmaFab | Équipements | Création | 800 M€ | 1 200 |
| EQP-03 | DepotTech | Équipements | Création | 600 M€ | 900 |
| EQP-04a-j | 10 PME process | Équipements | Création | 1,5 Md€ | 3 000 |
| EQP-05 | MetroSemi | Équipements | Consolidation | 500 M€ | 800 |
| EQP-06 | TestFrance | Équipements | Création | 400 M€ | 600 |
| PKG-01 | PackFrance 3D | Packaging | Création | 4 Md€ | 3 000 |
| PKG-02a-e | 5 OSAT | Packaging | Création | 1,5 Md€ | 2 500 |
| DES-01a-o | 15 start-ups RISC-V | Conception | Création | 500 M€ | 2 000 |
| DES-02 | Renforcement Kalray | Conception | Renforcement | 300 M€ | 1 500 |
| DES-03a-e | 5 éditeurs EDA | Conception | Création | 400 M€ | 800 |
| DES-04 | FranceIP | Conception | Consolidation | 300 M€ | 1 000 |
| MAT-01 | Extension Soitec | Matériaux | Renforcement | 2 Md€ | 2 000 |
| MAT-02a-g | 7 PME chimie | Matériaux | Création | 500 M€ | 1 500 |
| MAT-03 | Stocks stratégiques | Matériaux | Programme | 950 M€ | — |
| ... | (autres projets) | ... | ... | ... | ... |

### A.2 Cartographie Géographique Cible

| Région | Vocation | Entreprises 2047 | Emplois 2047 |
|--------|----------|------------------|--------------|
| Auvergne-Rhône-Alpes | Fabrication, R&D, Équipements | 200 | 70 000 |
| Île-de-France | Conception, R&D, Siège | 180 | 45 000 |
| Occitanie | Packaging, Test, Spatial | 120 | 35 000 |
| Bretagne | Télécom, Cybersécurité | 80 | 20 000 |
| Nouvelle-Aquitaine | Power, Automobile | 60 | 15 000 |
| Provence-Alpes-Côte d'Azur | Design, Photonique | 50 | 10 000 |
| Autres régions | Divers | 50 | 5 000 |
| **TOTAL** | | **740** | **200 000** |

### A.3 Partenariats Internationaux Clés

| Partenaire | Domaine | Type de partenariat | Priorité |
|------------|---------|---------------------|----------|
| Intel | Technologie FinFET | Licence + JV | Critique |
| ASML | Équipements litho | Maintenance + R&D | Critique |
| TSMC | Accès capacité | Accord commercial | Élevée |
| Samsung | Mémoires | Licence technologique | Élevée |
| Applied Materials | Équipements process | Partenariat technologique | Élevée |
| IMEC (Belgique) | R&D | Consortium | Élevée |
| Fraunhofer (Allemagne) | R&D | Bilatéral | Moyenne |
| IIT (Inde) | Talents, design | Formation, JV | Moyenne |

---

*Document de référence — Version 0.1*  
*Projet GenToGen2027 / TOGAFrance*
