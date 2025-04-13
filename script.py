import cv2
import pandas as pd

# Charger l'image
image_path = "C:/Users/ACER/Pictures/Screenshots/cars.png"  # Remplacez par le chemin de votre image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Afficher l'image (facultatif)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Segmenter l'image pour extraire le texte (cela dépend de votre image)
# Par exemple, vous pouvez découper des zones spécifiques ou améliorer la lisibilité
# Si vous avez un texte "propre", alors cette étape peut être limitée.

# Si vous avez déjà des données structurées, vous pouvez les convertir en CSV
text_data = [
    "Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin",
    "Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US",
    "Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US",
    "Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US",
    "AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US",
    "Ford Torino;17.0;8;302.0;140.0;3449.;10.5;70;US",
    "Ford Galaxie 500;15.0;8;429.0;198.0;4341.;10.0;70;US",
    "Chevrolet Impala;14.0;8;454.0;220.0;4354.;9.0;70;US",
    "Plymouth Fury iii;14.0;8;440.0;215.0;4312.;8.5;70;US",
    "Pontiac Catalina;14.0;8;455.0;225.0;4425.;10.0;70;US",
    "AMC Ambassador DPL;15.0;8;390.0;190.0;3850.;8.5;70;US",
    "Citroen DS-21 Pallas;0;4;133.0;115.0;3090.;17.5;70;Europe",
    "Chevrolet Chevelle Concours (sw);0;8;350.0;165.0;4142.;11.5;70;US,"
    "Ford Torino (sw);0;8;351.0;153.0;4034.;11.0;70;US",
    "Plymouth Satellite (sw);0;8;383.0;175.0;4166.;10.5;70;US",
]

# Convertir le texte en structure tabulaire
data = [line.split(';') for line in text_data]
columns = data[0]  # En-têtes de colonnes
rows = data[1:]    # Données
# Vérifiez et nettoyez les lignes
rows = [row for row in rows if len(row) == len(columns)]

# Créer un DataFrame avec les données propres
df = pd.DataFrame(rows, columns=columns)

# Sauvegarder les données en fichier CSV
output_csv_path = 'fichier_sortie_opencv.csv'
df.to_csv(output_csv_path, index=False)

print(f"Données sauvegardées dans {output_csv_path}")
