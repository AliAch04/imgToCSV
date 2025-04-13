import cv2
import pandas as pd
import pytesseract

# Configuration de Tesseract (si nécessaire pour extraction de texte depuis l'image)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ACER\AppData\Local\Tesseract-OCR\tesseract.exe"

def process_image(image_path):
    """Fonction pour extraire du texte d'une image et le sauvegarder en CSV."""
    # Lire l'image
    image = cv2.imread(image_path)

    if image is None:
        print("Erreur : Impossible de lire l'image. Vérifiez le chemin.")
        return

    # Extraire le texte de l'image avec pytesseract
    text = pytesseract.image_to_string(image)
    
    # Transformer le texte extrait en données structurées
    lines = text.strip().split('\n')
    data = [line.split(';') for line in lines if ';' in line]

    # Valider les données extraites
    if len(data) < 2:
        print("Erreur : Les données extraites ne sont pas dans le bon format.")
        return

    # Extraire les en-têtes et les lignes
    columns = data[0]  # Première ligne comme en-têtes de colonnes
    rows = []
    for row in data[1:]:
        if len(row) == len(columns):
            rows.append(row)  # Ajouter uniquement les lignes valides
        else:
            print(f"Ligne ignorée (nombre de colonnes incorrect) : {row}")

    # Vérifier qu'il reste des lignes valides
    if not rows:
        print("Erreur : Aucune donnée valide extraite.")
        return

    # Créer un DataFrame avec les données valides
    df = pd.DataFrame(rows, columns=columns)

    # Sauvegarder en CSV
    output_csv_path = 'fichier_sortie_from_image.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Les données extraites de l'image ont été sauvegardées dans {output_csv_path}")
    """Fonction pour extraire du texte d'une image et le sauvegarder en CSV."""
    # Lire l'image
    image = cv2.imread(image_path)

    if image is None:
        print("Erreur : Impossible de lire l'image. Vérifiez le chemin.")
        return

    # Extraire le texte de l'image avec pytesseract
    text = pytesseract.image_to_string(image)
    
    # Transformer le texte extrait en données structurées
    lines = text.strip().split('\n')
    data = [line.split(';') for line in lines if ';' in line]

    # Valider et créer le DataFrame
    if len(data) < 2:
        print("Erreur : Les données extraites ne sont pas au bon format.")
        return

    columns = data[0]
    rows = data[1:]
    df = pd.DataFrame(rows, columns=columns)

    # Sauvegarder en CSV
    output_csv_path = 'fichier_sortie_from_image.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Les données extraites de l'image ont été sauvegardées dans {output_csv_path}")

def process_text_directly():
    """Fonction pour insérer du texte directement et le sauvegarder en CSV."""
    print("Entrez vos lignes de texte (séparées par ';'). Tapez 'FIN' pour terminer :")

    lines = []
    while True:
        line = input("> ")  # Lire une ligne à la fois
        if line.strip().upper() == "FIN":
            break
        lines.append(line)

    # Transformer les lignes en tableau
    data = [line.split(';') for line in lines if ';' in line]

    # Valider les données et créer le DataFrame
    if len(data) < 2:
        print("Erreur : Les données saisies ne sont pas au bon format.")
        return

    columns = data[0]
    rows = data[1:]
    df = pd.DataFrame(rows, columns=columns)

    # Sauvegarder en CSV
    output_csv_path = 'fichier_sortie_from_text.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Les données saisies ont été sauvegardées dans {output_csv_path}")

# Interface utilisateur
print("Que voulez-vous faire ?")
print("1 : Charger un fichier image")
print("2 : Insérer du texte directement")
choice = input("Choix (1 ou 2) : ")

if choice == "1":
    image_path = input("Entrez le chemin de l'image : ")
    process_image(image_path)
elif choice == "2":
    process_text_directly()
else:
    print("Choix invalide. Veuillez relancer le programme.")
