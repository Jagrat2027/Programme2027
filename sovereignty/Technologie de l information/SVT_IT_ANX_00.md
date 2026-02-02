# SVT_IT_ANX_00 — Analyse des Impacts et Structure des Annexes
## Document Préparatoire au Plan de Souveraineté IT 2027-2047

---

**Document de référence** : SVT_IT_00  
**Classification** : Public  
**Auteur** : Jeff / Jagrat  
**Date** : Janvier 2026  
**Version** : 0.1

---

## Objet du Document

Ce document réalise un tour d'horizon des impacts du plan de souveraineté IT et propose une structure d'annexes opérationnelles nécessaires à sa mise en œuvre.

---

## 1. Analyse des Impacts par Domaine

### 1.1 Capital Humain — Impacts Critiques

#### Constat de départ
- **Flux actuel** : ~3 000 diplômés/an en microélectronique (toutes spécialités)
- **Besoin cible** : 25 000-28 000 diplômés/an à horizon 2040
- **Gap** : Facteur x8 à x10 en 15 ans

#### Impacts identifiés

| Dimension | Impact | Urgence |
|-----------|--------|---------|
| **Formations inexistantes** | Conception fonderie, lithographie, packaging 3D, mémoires DRAM | Critique |
| **Profils hybrides manquants** | Physique des matériaux + conception, Hardware + IA, Process + automatisation | Élevée |
| **Reconversion industrielle** | 80 000 techniciens à former depuis autres secteurs (auto, aéro, chimie) | Élevée |
| **Fuite des cerveaux** | Compétition TSMC/Intel/Samsung qui recrutent en Europe à +50% salaires | Critique |
| **Encadrement doctoral** | Capacité actuelle insuffisante (500 thèses/an vs 1 500 nécessaires) | Moyenne |
| **Langues et mobilité** | Besoin d'anglais technique, stages internationaux obligatoires | Moyenne |

#### Métiers à créer ou renforcer massivement

| Catégorie | Métiers spécifiques | Volume estimé 2047 |
|-----------|--------------------|--------------------|
| Conception | Architectes SoC, designers RISC-V, vérification formelle | 15 000 |
| Fabrication | Ingénieurs process, techniciens salle blanche, métrologues | 60 000 |
| Packaging | Spécialistes 3D-IC, interconnexions avancées, test | 20 000 |
| Équipements | Ingénieurs lithographie, plasma, dépôt, gravure | 25 000 |
| Logiciel embarqué | Firmware, drivers, OS temps réel, cybersécurité | 40 000 |
| Support | Maintenance, qualité, supply chain, HSE | 40 000 |

---

### 1.2 Tissu Industriel — Impacts Structurels

#### Constat de départ
- Écosystème français concentré sur quelques acteurs (STMicro, Soitec, X-Fab)
- Quasi-absence d'équipementiers de rang mondial
- Supply chain fragmentée et dépendante

#### Chaîne de valeur à construire

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CHAÎNE DE VALEUR SEMICONDUCTEURS                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  AMONT                         CŒUR                           AVAL          │
│  ──────                        ────                           ────          │
│                                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────┐│
│  │  MATÉRIAUX   │───▶│ ÉQUIPEMENTS  │───▶│ FABRICATION  │───▶│ PACKAGING  ││
│  │              │    │              │    │              │    │    TEST    ││
│  │ • Silicium   │    │ • Litho      │    │ • Fonderie   │    │            ││
│  │ • Gaz purs   │    │ • Gravure    │    │ • IDM        │    │ • Assembly ││
│  │ • Chimie     │    │ • Dépôt      │    │ • OSAT       │    │ • Test     ││
│  │ • Substrats  │    │ • Métrologie │    │              │    │ • Burn-in  ││
│  └──────────────┘    └──────────────┘    └──────────────┘    └────────────┘│
│        │                    │                   │                   │       │
│        ▼                    ▼                   ▼                   ▼       │
│   [À CRÉER]            [À CRÉER]           [RENFORCER]        [À CRÉER]    │
│   5-10 PME/ETI         10-15 sociétés      STMicro, X-Fab     5-10 OSAT    │
│                                            + nouvelles fabs    français     │
│                                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CONCEPTION (FABLESS)                      INTÉGRATION SYSTÈMES             │
│  ────────────────────                      ─────────────────────             │
│  ┌──────────────────┐                      ┌──────────────────┐             │
│  │ • Design houses  │                      │ • OEM défense    │             │
│  │ • IP vendors     │                      │ • Industriels    │             │
│  │ • EDA tools      │                      │ • Télécom        │             │
│  └──────────────────┘                      └──────────────────┘             │
│        │                                          │                         │
│        ▼                                          ▼                         │
│   [À CRÉER]                                  [EXISTANT]                     │
│   20-30 fabless FR                           Thales, Safran,               │
│   + 5 éditeurs EDA                           Naval Group, etc.             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Industries à créer

| Maillon | Type d'entreprise | Nombre cible | Investissement |
|---------|-------------------|--------------|----------------|
| Matériaux | PME chimie électronique | 5-8 | 2 Md€ |
| Substrats | ETI silicium/SiC/GaN | 3-5 | 3 Md€ |
| Équipements lithographie | Champion national | 1-2 | 8 Md€ |
| Équipements process | ETI spécialisées | 10-15 | 5 Md€ |
| Métrologie/inspection | PME/ETI | 5-8 | 2 Md€ |
| Design fabless | Start-ups/scale-ups | 20-30 | 3 Md€ |
| EDA/CAO | Éditeurs logiciels | 3-5 | 1 Md€ |
| OSAT (packaging/test) | ETI | 5-10 | 4 Md€ |
| **Total** | | **~70 entreprises** | **28 Md€** |

---

### 1.3 Recherche et Innovation — Impacts Stratégiques

#### Constat de départ
- Excellence reconnue en R&D amont (CEA-Leti, CNRS, INRIA)
- Faiblesse chronique dans le passage à l'échelle industrielle ("valley of death")
- Écosystème de transfert technologique fragmenté

#### Impacts identifiés

| Dimension | Impact | Actions requises |
|-----------|--------|------------------|
| **Transfert techno** | Accélérer le passage TRL 4-6 vers TRL 7-9 | Pilotes industriels, démonstrateurs |
| **PI et brevets** | Protéger les innovations stratégiques | Stratégie brevets offensive, fonds défensif |
| **Ruptures techno** | Anticiper le post-silicium | Programmes graphène, quantique, photonique |
| **Coopération EU** | Mutualiser les efforts R&D | IPCEI, Horizon Europe, bilatéraux |
| **Brain drain** | Retenir les chercheurs | Passerelles public-privé, salaires compétitifs |

#### Feuille de route technologique simplifiée

| Horizon | Technologie | Objectif France/EU | TRL actuel → cible |
|---------|-------------|-------------------|-------------------|
| 2027-2030 | FDSOI 18nm | Production volume | TRL 9 (acquis) |
| 2030-2035 | FinFET 14/10nm | Production souveraine | TRL 6 → 9 |
| 2032-2038 | GAA 7/5nm | Codéveloppement EU | TRL 4 → 8 |
| 2035-2042 | CFET 3nm | Participation EU | TRL 3 → 7 |
| 2040-2047 | Post-silicium | Leadership niches | TRL 2 → 6 |

---

### 1.4 Impacts Territoriaux et Sociaux

#### Constat de départ
- Concentration historique sur le sillon alpin (Grenoble)
- Risque de déserts industriels dans autres régions
- Enjeux d'acceptabilité (eau, énergie, produits chimiques)

#### Cartographie des impacts territoriaux

| Pôle | Vocation | Emplois directs 2047 | Enjeux spécifiques |
|------|----------|---------------------|-------------------|
| **Grenoble-Crolles** | Fab avancée, R&D | 50 000 | Eau, foncier, transport |
| **Saclay-Paris** | R&D, design, IA | 30 000 | Coût de vie, logement |
| **Toulouse** | Spatial, embarqué, test | 20 000 | Diversification aéro |
| **Rennes-Lannion** | Télécom, cybersécurité | 15 000 | Attractivité talents |
| **Sophia Antipolis** | Design, logiciel | 15 000 | Concurrence internationale |
| **Tours-Bordeaux** | Power electronics, auto | 20 000 | Reconversion filières |
| **Bassins reconversion** | Techniciens, support | 50 000 | Formation, mobilité |

#### Impacts sociaux

| Dimension | Impact positif | Risque | Mitigation |
|-----------|---------------|--------|------------|
| Emploi | +200 000 emplois qualifiés | Pénurie main d'œuvre | Formation massive |
| Salaires | Hausse secteur tech | Inflation locale | Logement, transport |
| Reconversion | Opportunités nouveaux métiers | Inadéquation compétences | Accompagnement personnalisé |
| Environnement | Technologies propres | Consommation eau/énergie | Recyclage, ENR |

---

### 1.5 Impacts Juridiques et Réglementaires

#### Adaptations législatives nécessaires

| Domaine | Mesure | Véhicule législatif |
|---------|--------|---------------------|
| **Investissements étrangers** | Renforcement screening secteur semiconducteurs | Décret IEF |
| **Marchés publics** | Clause de souveraineté pour composants critiques | Code marchés publics |
| **Environnement** | Procédures accélérées pour fabs stratégiques | Loi industrie verte |
| **Formation** | Création diplômes nationaux microélectronique | Arrêtés ministériels |
| **Recherche** | Statut chercheur-entrepreneur facilité | Loi programmation recherche |
| **Fiscalité** | CIR renforcé semiconducteurs, zones franches | Loi de finances |

---

## 2. Structure des Annexes Proposées

### Vue d'ensemble

| Réf. | Titre | Pages estimées | Priorité |
|------|-------|----------------|----------|
| **SVT_IT_ANX_A** | Référentiel des Métiers et Compétences | 40-50 | P1 |
| **SVT_IT_ANX_B** | Plan de Formation et Cursus | 30-40 | P1 |
| **SVT_IT_ANX_C** | Cartographie Industrielle Cible | 35-45 | P1 |
| **SVT_IT_ANX_D** | Feuille de Route Technologique | 25-35 | P2 |
| **SVT_IT_ANX_E** | Schéma Territorial d'Implantation | 20-30 | P2 |
| **SVT_IT_ANX_F** | Cadre Juridique et Réglementaire | 20-25 | P2 |
| **SVT_IT_ANX_G** | Matrice des Risques Détaillée | 15-20 | P3 |
| **SVT_IT_ANX_H** | Plan de Financement Détaillé | 25-30 | P2 |
| **SVT_IT_ANX_I** | Benchmark International | 20-25 | P3 |
| **SVT_IT_ANX_J** | Indicateurs et Tableau de Bord | 15-20 | P2 |

---

### 2.1 SVT_IT_ANX_A — Référentiel des Métiers et Compétences

**Objectif** : Définir précisément les profils nécessaires, les compétences associées et les volumes par phase.

**Contenu prévu** :

1. **Nomenclature des métiers** (60+ fiches)
   - Famille : Conception / Fabrication / Équipements / Test / Support
   - Pour chaque métier : mission, compétences clés, formation requise, salaire indicatif

2. **Matrice compétences**
   - Compétences techniques (hard skills)
   - Compétences transverses (soft skills)
   - Niveaux de maîtrise (junior/confirmé/expert)

3. **Gap analysis**
   - Situation actuelle vs cible par métier
   - Identification des tensions critiques

4. **Pyramide des qualifications**
   - Répartition docteurs / ingénieurs / techniciens / opérateurs
   - Évolution par phase

**Exemple de fiche métier** :

```
┌────────────────────────────────────────────────────────────────┐
│ MÉTIER : Ingénieur Process Lithographie                        │
├────────────────────────────────────────────────────────────────┤
│ Famille    : Fabrication                                       │
│ Niveau     : Bac+5 / Ingénieur                                │
│ Expérience : 3-5 ans                                          │
├────────────────────────────────────────────────────────────────┤
│ MISSION                                                        │
│ Développer et optimiser les procédés de photolithographie      │
│ pour les nœuds technologiques avancés (14nm et au-delà)       │
├────────────────────────────────────────────────────────────────┤
│ COMPÉTENCES CLÉS                                               │
│ • Physique des semi-conducteurs                               │
│ • Optique et photochimie                                      │
│ • Métrologie dimensionnelle                                   │
│ • Statistiques et DOE (Design of Experiments)                 │
│ • Anglais technique courant                                   │
├────────────────────────────────────────────────────────────────┤
│ FORMATION TYPE                                                 │
│ • École d'ingénieur (Phelma, INSA, Centrale) + spé micro      │
│ • Master physique des matériaux                               │
│ • Thèse industrielle (bonus)                                  │
├────────────────────────────────────────────────────────────────┤
│ VOLUME CIBLE 2047 : 3 500     │ SALAIRE : 45-75 K€            │
│ TENSION ACTUELLE : CRITIQUE   │ ÉVOLUTION : Chef de projet    │
└────────────────────────────────────────────────────────────────┘
```

---

### 2.2 SVT_IT_ANX_B — Plan de Formation et Cursus

**Objectif** : Définir les cursus à créer, adapter ou renforcer pour atteindre les volumes de formation requis.

**Contenu prévu** :

1. **Diagnostic de l'offre actuelle**
   - Cartographie des formations existantes
   - Capacités et taux de remplissage
   - Adéquation avec besoins industriels

2. **Nouveaux cursus à créer**

| Niveau | Intitulé | Établissements cibles | Capacité/an |
|--------|----------|----------------------|-------------|
| Bac+2 | BTS Microélectronique et Salle Blanche | 20 IUT | 2 000 |
| Bac+3 | BUT Fabrication Semiconducteurs | 15 IUT | 1 500 |
| Bac+3 | Licence Pro Packaging Électronique | 10 universités | 800 |
| Bac+5 | Master Conception Circuits Intégrés | 8 universités | 1 000 |
| Bac+5 | Diplôme ingénieur spé Fonderie | 5 écoles | 500 |
| Bac+8 | Doctorat industriel Microélectronique | National | 500 |

3. **Réforme des cursus existants**
   - Renforcement modules semiconducteurs dans écoles généralistes
   - Stages obligatoires en industrie (6 mois minimum)
   - Certifications professionnelles reconnues

4. **Formation continue et reconversion**
   - Programmes courts (3-6 mois) pour reconversion
   - VAE adaptée aux métiers de la microélectronique
   - Partenariats Pôle Emploi / OPCO

5. **Attractivité internationale**
   - Programmes en anglais
   - Bourses talents étrangers
   - Passerelles visa-emploi

---

### 2.3 SVT_IT_ANX_C — Cartographie Industrielle Cible

**Objectif** : Définir précisément l'écosystème industriel à construire, maillon par maillon.

**Contenu prévu** :

1. **Analyse de la chaîne de valeur actuelle**
   - Acteurs existants par segment
   - Parts de marché et positionnement
   - Forces et faiblesses

2. **Chaîne de valeur cible 2047**

| Segment | Acteurs actuels FR | Acteurs cibles 2047 | Gap |
|---------|-------------------|--------------------|----|
| Silicium | Soitec (substrats) | Soitec x2 + 2 nouveaux | +2 |
| Chimie électronique | Air Liquide (partiel) | 5 PME spécialisées | +4 |
| Équipements litho | Néant | 1-2 champions | +2 |
| Équipements process | Quelques PME | 10-15 ETI | +10 |
| Fonderie | STMicro, X-Fab | +2 fabs avancées | +2 |
| Design fabless | Quelques start-ups | 20-30 scale-ups | +25 |
| OSAT | Néant significatif | 5-10 ETI | +8 |

3. **Fiches entreprises à créer**
   - Business model type
   - Investissement requis
   - Partenaires potentiels
   - Timeline de création

4. **Stratégie de consolidation**
   - Fusions-acquisitions souhaitables
   - Champions nationaux vs tissu PME/ETI
   - Articulation avec écosystème européen

---

### 2.4 SVT_IT_ANX_D — Feuille de Route Technologique

**Objectif** : Définir les jalons technologiques, les programmes R&D et l'articulation recherche-industrie.

**Contenu prévu** :

1. **Roadmap technologique détaillée**
   - Par nœud technologique (28nm → 3nm → post-silicium)
   - TRL et jalons de maturité
   - Dépendances critiques

2. **Programmes R&D structurants**

| Programme | Budget | Durée | Porteur | Partenaires |
|-----------|--------|-------|---------|-------------|
| RISC-V Souverain | 2 Md€ | 2027-2035 | CEA | STMicro, Thales, Kalray |
| Mémoires HBM | 3 Md€ | 2030-2040 | STMicro | CEA-Leti, IMEC |
| Litho DUV+ | 4 Md€ | 2028-2038 | Nouvel acteur | ASML (licence), Zeiss |
| Photonique intégrée | 2 Md€ | 2032-2045 | III-V Lab | Thales, Nokia |
| Calcul quantique | 3 Md€ | 2027-2047 | CEA | Pasqal, Alice&Bob, Quandela |

3. **Mécanismes de transfert technologique**
   - Lignes pilotes mutualisées
   - Plateformes de prototypage
   - Contrats de licence et spin-offs

---

### 2.5 SVT_IT_ANX_E — Schéma Territorial d'Implantation

**Objectif** : Définir la répartition géographique optimale des investissements.

**Contenu prévu** :

1. **Critères de localisation**
   - Disponibilité foncière et utilities (eau, énergie)
   - Bassin d'emploi et formation
   - Écosystème existant
   - Accessibilité et qualité de vie

2. **Carte des implantations cibles**
   - Fabs : Grenoble, Saclay, nouveau site (Nord/Est ?)
   - Campus formation : 5 sites principaux + maillage IUT
   - Centres R&D : articulation avec pôles existants

3. **Impact territorial par région**
   - Emplois créés
   - Investissements induits
   - Besoins infrastructure (logement, transport)

4. **Équilibre territorial**
   - Répartition équitable vs efficacité économique
   - Rôle des métropoles vs villes moyennes
   - Reconversion des territoires industriels

---

### 2.6 SVT_IT_ANX_F — Cadre Juridique et Réglementaire

**Objectif** : Identifier les adaptations législatives et réglementaires nécessaires.

**Contenu prévu** :

1. **Screening des investissements étrangers**
   - Extension du périmètre IEF aux semiconducteurs
   - Procédures d'autorisation accélérées pour investissements souverains

2. **Commande publique**
   - Clauses de préférence souveraineté
   - Critères extra-financiers (localisation, sécurité)

3. **Droit de l'environnement**
   - Procédures simplifiées pour projets d'intérêt national
   - Compensation carbone et eau

4. **Droit du travail et formation**
   - Création de nouveaux diplômes d'État
   - Cadre juridique des reconversions massives

5. **Fiscalité incitative**
   - CIR majoré semiconducteurs
   - Zones franches technologiques

---

### 2.7 SVT_IT_ANX_G — Matrice des Risques Détaillée

**Objectif** : Analyser exhaustivement les risques et définir les plans de contingence.

**Contenu prévu** :

1. **Matrice probabilité/impact**
   - 30-40 risques identifiés
   - Cotation et priorisation

2. **Fiches risques détaillées**
   - Description, causes, conséquences
   - Indicateurs d'alerte
   - Actions de mitigation
   - Plan de contingence

3. **Scénarios de crise**
   - Rupture Taiwan
   - Guerre commerciale élargie
   - Échec coordination européenne
   - Disruption technologique

---

### 2.8 SVT_IT_ANX_H — Plan de Financement Détaillé

**Objectif** : Détailler les sources et mécanismes de financement.

**Contenu prévu** :

1. **Budget détaillé par ligne**
   - Ventilation des 180-220 Md€
   - Échéancier annuel

2. **Sources de financement**
   - Budget État (PLF, PIA)
   - Fonds européens (IPCEI, Chips Act, NextGenEU)
   - BPI France et CDC
   - Investisseurs privés et PPP

3. **Véhicules financiers**
   - Agence nationale de financement
   - Fonds souverain dédié
   - Garanties publiques

4. **Retour sur investissement**
   - Recettes fiscales générées
   - Balance commerciale
   - Externalités positives

---

### 2.9 SVT_IT_ANX_I — Benchmark International

**Objectif** : Analyser les stratégies des autres pays pour en tirer des enseignements.

**Contenu prévu** :

1. **États-Unis** : CHIPS Act, stratégie Intel
2. **Chine** : Made in China 2025, SMIC, subventions massives
3. **Taïwan** : Modèle TSMC, écosystème intégré
4. **Corée du Sud** : Samsung/SK Hynix, soutien étatique
5. **Japon** : Renaissance semiconducteurs, Rapidus
6. **Europe** : Chips Act européen, IPCEI, coordination

**Enseignements clés** :
- Facteurs de succès
- Erreurs à éviter
- Applicabilité au contexte français

---

### 2.10 SVT_IT_ANX_J — Indicateurs et Tableau de Bord

**Objectif** : Définir les KPI de pilotage et le système de reporting.

**Contenu prévu** :

1. **Indicateurs stratégiques** (10-15)
   - Taux de souveraineté par segment
   - Emplois créés
   - Nœud technologique maîtrisé

2. **Indicateurs opérationnels** (30-50)
   - Par phase et par programme
   - Avancement physique et financier

3. **Tableau de bord type**
   - Fréquence de mise à jour
   - Circuits de reporting
   - Seuils d'alerte

---

## 3. Priorisation et Calendrier de Production

### Phase 1 : Annexes critiques (T1-T2 2027)

| Annexe | Livrable | Responsable suggéré |
|--------|----------|---------------------|
| ANX_A | Référentiel métiers V1 | DGEFP + Branches |
| ANX_B | Plan formation V1 | MESRI + Régions |
| ANX_C | Cartographie industrielle V1 | DGE + BPI |

### Phase 2 : Annexes structurantes (T3-T4 2027)

| Annexe | Livrable | Responsable suggéré |
|--------|----------|---------------------|
| ANX_D | Roadmap techno V1 | CEA + ANR |
| ANX_E | Schéma territorial V1 | ANCT + Régions |
| ANX_F | Cadre juridique V1 | SGG + Ministères |
| ANX_H | Plan financement V1 | DG Trésor + BPI |
| ANX_J | Tableau de bord V1 | SGPI |

### Phase 3 : Annexes complémentaires (2028)

| Annexe | Livrable | Responsable suggéré |
|--------|----------|---------------------|
| ANX_G | Matrice risques V1 | SGDSN + DGE |
| ANX_I | Benchmark V1 | DG Trésor + DGE |

---

## 4. Conclusion

L'ampleur du plan de souveraineté IT nécessite un corpus documentaire structuré et opérationnel. Les 10 annexes proposées couvrent l'ensemble des dimensions critiques :

- **Capital humain** (ANX_A, ANX_B) : Former 500 000 personnes
- **Industrie** (ANX_C) : Créer ~70 entreprises stratégiques
- **Technologie** (ANX_D) : Maîtriser le nœud 3nm
- **Territoire** (ANX_E) : Équilibrer concentration et diffusion
- **Cadre** (ANX_F, ANX_G, ANX_H) : Sécuriser l'exécution
- **Pilotage** (ANX_I, ANX_J) : Mesurer et ajuster

La priorité absolue porte sur les annexes A, B et C qui conditionnent la faisabilité même du plan : sans les hommes et les entreprises, aucune fab ne peut tourner.

---

*Document préparatoire — Version 0.1*  
*Projet GenToGen2027 / TOGAFrance*
