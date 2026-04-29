from rembg import remove
from PIL import Image
from pathlib import Path
import time

# Fonction pour imprimer le texte du bot lentment
def print_slowly(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)

# Definir le chemin des images d'entree et de sortie
input_path = Path.cwd()
output_path = Path.cwd()

# Definir la fonction pour retirer le bg d'une image quelconque et afficher le resultat
def removebg(input_img):
    image = Image.open(input_img)
    output = remove(image)
    input_name = input_img.stem + str(2)
    output_img = output_path.joinpath(input_name+".png")
    output.save(output_img)
    output = Image.open(output_img)
    output.show()

def bot():
    print_slowly("Enter the name of your image (with its extension): ")
    i = input(str())
    print_slowly("...")
    removebg(input_path.joinpath(i))

print_slowly("Hi! I am a bot that help you to remove the background of an image.")
print()
bot()

while True:
     print_slowly("continue ? (y/n)")
     choise = input()
     if choise.lower() == "y":
          bot()
     else:
        break