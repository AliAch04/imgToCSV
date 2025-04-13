import cv2
import pandas as pd

def process_image(image_path):
    """Fonction pour traiter l'image et extraire les données en CSV."""
    # Charger l'image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Erreur : L'image n'a pas pu être chargée. Vérifiez le chemin.")
        return

    # (Pour l'instant, simulation : remplacer par votre traitement d'image/text réel)
    text_data = [
        "Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin",
        "Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US",
        "Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US",
    ]

    # Convertir le texte en DataFrame pandas
    data = [line.split(';') for line in text_data]
    columns = data[0]
    rows = data[1:]
    df = pd.DataFrame(rows, columns=columns)

    # Sauvegarder en CSV
    output_csv_path = 'fichier_sortie.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Les données ont été extraites et sauvegardées dans {output_csv_path}")

def process_text_directly(input_text):
    """Fonction pour traiter un texte directement inséré par l'utilisateur."""
    # Séparer le texte par lignes
    lines = input_text.strip().split('\n')
    data = [line.split(';') for line in lines]
    columns = data[0]
    rows = data[1:]
    df = pd.DataFrame(rows, columns=columns)

    # Sauvegarder en CSV
    output_csv_path = 'fichier_sortie_direct_text.csv'
    df.to_csv(output_csv_path, index=False)

    print(f"Les données insérées ont été sauvegardées dans {output_csv_path}")

# Interface utilisateur
print("Que voulez-vous faire ?")
print("1 : Charger un fichier image")
print("2 : Insérer le contenu texte directement")
choice = input("Choix (1 ou 2) : ")

if choice == "1":
    image_path = input("Entrez le chemin de l'image : ")
    process_image(image_path)
elif choice == "2":
    print("Insérez votre texte (les lignes séparées par des sauts de ligne, les colonnes séparées par ';') :")
    input_text = input("Texte : ")
    process_text_directly(input_text)
else:
    print("Choix invalide. Veuillez relancer le programme.")
