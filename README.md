# 🖼️ RmBgBot — Background Remover CLI

A simple and interactive command-line bot that automatically removes the background from any image using AI, powered by the [`rembg`](https://github.com/danielgatis/rembg) library.

---

## ✨ Features

- 🤖 Interactive CLI with a friendly bot interface
- 🧠 AI-powered background removal via `rembg`
- 🖼️ Automatic preview of the output image
- 🔁 Process multiple images in a single session
- 📁 Saves output as a transparent `.png` file in the current directory

---

## 📋 Requirements

- Python 3.7+
- [`rembg`](https://github.com/danielgatis/rembg)
- [`Pillow`](https://python-pillow.org/)

---

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/RmBgBot.git
cd RmBgBot
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
python RmBgBot.py
```

The bot will prompt you for the name of the image (including its extension):

```
Hi! I am a bot that help you to remove the background of an image.
Enter the name of your image (with its extension): photo.jpg
...
```

The processed image will be saved in the same directory with a `2` appended to the original filename (e.g., `photo2.png`), and will open automatically for preview.

You will then be asked whether you want to process another image:

```
continue ? (y/n)
```

---

## 📁 Project Structure

```
RmBgBot/
│
├── RmBgBot.py       # Main script
└── README.md        # Project documentation
```

---

## 🖼️ Example

| Input | Output |
|-------|--------|
| `portrait.jpg` | `portrait2.png` (background removed, transparent) |

---

## ⚠️ Notes

- The input image must be located in the **same directory** as the script (or provide the full path).
- Output images are always saved in `.png` format to preserve transparency.
- Supported input formats: `.jpg`, `.jpeg`, `.png`, `.webp`, and most common image formats supported by Pillow.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [rembg](https://github.com/danielgatis/rembg) by Daniel Gatis — for the background removal engine.
- [Pillow](https://python-pillow.org/) — for image processing.
