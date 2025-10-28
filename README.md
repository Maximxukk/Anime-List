# 🎌 Anime Recommendation Randomizer

The **Anime Recommendation Randomizer** is a Python-based program that fetches data from the [MyAnimeList](https://myanimelist.net/) API (via [Jikan](https://jikan.moe/)) to generate **random anime recommendations** from the current **Top 100 Anime list**.  

Each recommendation includes the **title**, **synopsis**, and **official cover image**, giving users an easy way to discover new anime to watch — straight from the command line.

---

## 🧠 How It Works

The program connects to the Jikan API, retrieves a list of the top anime, and then randomly selects one (or multiple) entries to display.  
Each recommendation prints:

- 🎬 **Title** – The anime’s name  
- 📝 **Synopsis** – A short plot summary  
- 🖼️ **Image** – A link or automatically displayed cover art  

You can also modify the number of random recommendations shown or display multiple at once.

---

## 🧩 Features

- ✅ Fetches live anime data using the [Jikan API](https://jikan.moe/)  
- ✅ Displays title, description, and cover image  
- ✅ Supports multiple random recommendations  
- ✅ Simple, clean, and beginner-friendly Python code  
- ✅ Easily expandable to GUI or web-based applications  

---

## ⚙️ Requirements

Make sure you have Python 3 installed, then install the dependencies:

```bash
pip install requests Pillow

python anime_randomizer.py

🎲 Random Anime Recommendation 🎲

Title: Shingeki no Kyojin Season 3 Part 2
Synopsis: Seeking to restore humanity's diminishing hope, the Survey Corps embark on a mission...
Image: https://cdn.myanimelist.net/images/anime/1517/100633.jpg
--------------------------------------------------------------------------------
