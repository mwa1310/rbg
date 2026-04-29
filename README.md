# 🖼️ rbg — Background Remover CLI

A simple and interactive command-line bot that automatically removes the background from any image using AI, powered by the [`rembg`](https://github.com/danielgatis/rembg) library.

---

## ✨ Features

- 🤖 Interactive CLI with a friendly bot interface
- 🧠 AI-powered background removal via `rembg`
- 🖼️ Automatic preview of the output image
- 🔁 Process multiple images in a single session
- 📁 Saves output as a transparent `.png` file in the current directory
- 🛡️ Robust error handling with clear, descriptive messages

---

## 📋 Requirements

- Python 3.7+
- [`rembg`](https://github.com/danielgatis/rembg)
- [`Pillow`](https://python-pillow.org/)

---

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/mwa1310/rbg.git
cd rbg
```

**2. Install the dependencies**

```bash
pip install rembg Pillow
```

> ⚠️ On first run, `rembg` will automatically download the AI model (~170 MB). An internet connection is required.

---

## 📦 Usage

Run the script from the directory containing your images:

```bash
python rgb.py
```

The bot will prompt you for the name of the image (including its extension):

```
Bonjour ! Je suis un bot qui supprime le fond de vos images.

Entrez le nom de votre image (avec son extension) :
> photo.jpg
...
⏳ Traitement en cours...
✅ Image sauvegardée : /your/path/photo2.png
```

The processed image is saved in the same directory with a `2` appended to the original filename (e.g., `photo2.png`), and opens automatically for preview.

You will then be asked whether you want to process another image:

```
Voulez-vous traiter une autre image ? (y/n) :
> n

Au revoir ! 👋
```

---

## 🛡️ Error Handling

The bot handles the following errors gracefully without crashing:

| Situation | Message |
|-----------|---------|
| File not found | `❌ Erreur : le fichier 'x' est introuvable dans le répertoire courant.` |
| Unsupported format | `❌ Erreur : format '.x' non supporté. Formats acceptés : ...` |
| Corrupted image | `❌ Erreur : impossible de lire 'x'. Le fichier est peut-être corrompu.` |
| Permission denied (read/write) | `❌ Erreur : accès refusé au fichier 'x'.` |
| Processing failure | `❌ Erreur lors du traitement de l'image : ...` |
| Preview unavailable | `⚠️ Impossible d'ouvrir la prévisualisation, mais l'image a bien été sauvegardée.` |
| Empty input | `❌ Erreur : aucun nom de fichier saisi.` |
| Invalid continue prompt | `⚠️ Réponse invalide. Tapez 'y' pour continuer ou 'n' pour quitter.` |

---

## 🖼️ Supported Formats

| Format | Extension |
|--------|-----------|
| JPEG | `.jpg`, `.jpeg` |
| PNG | `.png` |
| WebP | `.webp` |
| BMP | `.bmp` |
| TIFF | `.tiff` |

---

## 📁 Project Structure

```
RmBgBot/
│
├── rgb.py           # Main script
└── README.md        # Project documentation
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [rembg](https://github.com/danielgatis/rembg) by Daniel Gatis — for the background removal engine.
- [Pillow](https://python-pillow.org/) — for image processing.
