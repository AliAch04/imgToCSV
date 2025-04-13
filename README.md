# imgToCSV

Ce projet Python permet d'extraire du texte d'une image et de le convertir en fichier CSV structuré. Il est conçu pour répondre à divers besoins grâce à sa flexibilité :  
- **Option 1 :** Charger un fichier image pour extraire ses données.  
- **Option 2 :** Insérer manuellement du texte tabulaire directement via l'interface utilisateur.  

Le projet utilise trois bibliothèques principales :  
- `OpenCV` pour le traitement des images.  
- `pandas` pour la gestion des données tabulaires.  
- `pytesseract` pour la reconnaissance optique des caractères (OCR).  

Ce script est idéal pour transformer des images contenant des tableaux ou données textuelles en fichiers CSV réutilisables.

---

## Fonctionnalités

### 1. Extraction automatique depuis une image
- Le script traite une image (par exemple, une capture d'écran contenant un tableau de données) et extrait les données structurées.
- Les données extraites sont formatées en fichier CSV.

### 2. Saisie directe de texte structuré
- L'utilisateur peut choisir d'insérer manuellement plusieurs lignes de données au format tabulaire.
- Chaque ligne doit être saisie avec des colonnes séparées par `;`, et l'entrée se termine par le mot-clé `FIN`.

### 3. Validation et Nettoyage des Données
- Les lignes non conformes au format attendu sont automatiquement signalées et corrigées dans la mesure du possible.
- Les lignes invalides (par exemple, trop courtes ou mal formatées) sont ignorées.

---

## Installation et Configuration

### 1. Téléchargez ce dépôt
Cloner ce projet avec Git :  
```bash
git clone https://github.com/votre_nom_utilisateur/imgToCSV.git
cd imgToCSV

### 2. Configuration de Tesseract OCR
- Téléchargez et installez Tesseract OCR depuis ce lien : https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe

- Pendant l'installation, notez le chemin où Tesseract est installé (par exemple, C:\Program Files\Tesseract-OCR ou C:\Users\Nom_PC\AppData\Local\Tesseract-OCR). (Remplacez Nom_PC par le nom d'utilisateur de votre ordinateur.)

### 3. Installation des dépendances
- pip install opencv-python pandas

## Notes Importantes

### À propos des images
- Assurez-vous que votre image contient des données tabulaires structurées.

- Les séparateurs entre les colonnes doivent être des caractères comme ; ou ,.

- Les images floues ou de faible qualité peuvent entraîner des erreurs d'extraction.

### Validation des données
- Les lignes mal formatées ou contenant un nombre incorrect de colonnes sont ignorées.