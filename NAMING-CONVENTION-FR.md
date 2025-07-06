# Convention de nommage – Programme2027

Pour garder le dépôt lisible, structuré et compréhensible par tous, nous appliquons les règles suivantes :

---

## 📁 Dossiers principaux

- `/programme/` → Un fichier par pilier, format `XX_TitreCourt.md`
  - Ex : `01_Constitution.md`, `07_Migrations.md`

- `/finance/` → Tous les fichiers liés au chiffrage, format `chiffrage_*.md`
  - Ex : `chiffrage_global.md`, `chiffrage_migrations.md`

- `/documentation/` → Méthodes, lexique, principes TOGAFrance
- `/adaptations/` → Forks par pays ou région (format : `/adaptations/NOMDU_PAYS`)
- `/examples/` → Modèles-type : `modele_diagnostic.md`, `exemple_plan_action.md`
- `/tools/` → Scripts et fichiers techniques

---

## 📄 Fichiers

- Toujours en **kebab-case ou snake_case** (pas d’espaces, pas d’accents)
  - Exemple : `lettre_aux_elus.md`, `plan_togaf_adm.md`

- Utiliser le préfixe selon le contenu :
  - `README.md`, `CONTRIBUTING.md`, `ROADMAP.md` → racine
  - `CHANGES.md` → suivi des modifications
  - `GLOSSAIRE.md`, `FAQ.md` → en `/documentation`

- Pour les versions traduites :
  - `README-FR.md`, `ROADMAP-FR.md`, `CONTRIBUTING-FR.md`

---

## 🧠 Raison

> Un dépôt lisible est un dépôt partageable.  
> Cette convention permet à tout citoyen ou développeur de naviguer sans se perdre.
