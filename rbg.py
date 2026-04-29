from rembg import remove
from PIL import Image, UnidentifiedImageError
from pathlib import Path
import time

# Formats d'image supportés
SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}

# Fonction pour imprimer le texte du bot lentement
def print_slowly(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# Definir le chemin des images d'entree et de sortie
input_path = Path.cwd()
output_path = Path.cwd()

# Definir la fonction pour retirer le bg d'une image quelconque et afficher le resultat
def removebg(input_img):
    # Vérifier que le fichier existe
    if not input_img.exists():
        print_slowly(f"\n❌ Erreur : le fichier '{input_img.name}' est introuvable dans le répertoire courant.\n")
        return False

    # Vérifier que le format est supporté
    if input_img.suffix.lower() not in SUPPORTED_FORMATS:
        print_slowly(f"\n❌ Erreur : format '{input_img.suffix}' non supporté.")
        print_slowly(f"\n   Formats acceptés : {', '.join(SUPPORTED_FORMATS)}\n")
        return False

    # Ouvrir l'image
    try:
        image = Image.open(input_img)
    except UnidentifiedImageError:
        print_slowly(f"\n❌ Erreur : impossible de lire '{input_img.name}'. Le fichier est peut-être corrompu.\n")
        return False
    except PermissionError:
        print_slowly(f"\n❌ Erreur : accès refusé au fichier '{input_img.name}'.\n")
        return False

    # Supprimer le background
    print_slowly("\n⏳ Traitement en cours...")
    try:
        output = remove(image)
    except Exception as e:
        print_slowly(f"\n❌ Erreur lors du traitement de l'image : {e}\n")
        return False

    # Sauvegarder le résultat
    output_name = input_img.stem + "2.png"
    output_img = output_path / output_name
    try:
        output.save(output_img)
    except PermissionError:
        print_slowly(f"\n❌ Erreur : impossible de sauvegarder '{output_name}'. Vérifiez les permissions du dossier.\n")
        return False
    except OSError as e:
        print_slowly(f"\n❌ Erreur lors de la sauvegarde : {e}\n")
        return False

    print_slowly(f"\n✅ Image sauvegardée : {output_img}\n")

    # Afficher le résultat
    try:
        result = Image.open(output_img)
        result.show()
    except Exception:
        print_slowly("⚠️  Impossible d'ouvrir la prévisualisation, mais l'image a bien été sauvegardée.\n")

    return True

def bot():
    print_slowly("\nEntrez le nom de votre image (avec son extension) : ")
    i = input("> ").strip()

    # Vérifier que l'entrée n'est pas vide
    if not i:
        print_slowly("❌ Erreur : aucun nom de fichier saisi.\n")
        return

    print_slowly("...")
    removebg(input_path / i)

# --- Point d'entrée ---
print_slowly("Bonjour ! Je suis un bot qui supprime le fond de vos images.")
print()
bot()

while True:
    print_slowly("\nVoulez-vous traiter une autre image ? (y/n) : ")
    choice = input("> ").strip().lower()
    if choice == "y":
        bot()
    elif choice == "n":
        print_slowly("\nAu revoir ! 👋\n")
        break
    else:
        print_slowly("⚠️  Réponse invalide. Tapez 'y' pour continuer ou 'n' pour quitter.\n")