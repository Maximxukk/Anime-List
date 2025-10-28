# -----------------------------------------------------
# 🎌 Random Anime Recommendation Generator
# -----------------------------------------------------
# This program uses the Jikan API to fetch the top 100 anime
# and then randomly picks one to recommend to the user.
# It prints the title, synopsis, and image link (and can even
# open the image using Pillow).
# -----------------------------------------------------

import requests      # For connecting to the API and fetching data
import math          # For calculating pages if needed
import random        # For picking a random anime
from PIL import Image  # For displaying the anime cover image
from io import BytesIO  # For converting raw image bytes into an image object

# -----------------------------------------------------
# Function: get_top_anime()
# -----------------------------------------------------
# Fetches the top "limit" number of anime from the Jikan API.
# Handles pagination automatically (since Jikan returns up to 25 per page).
def get_top_anime(limit=100):
    anime_list = []            # This will store all the anime info
    page = 1                   # Page counter for pagination
    per_page = 25              # Max number of anime per page (Jikan API)
    total_pages = math.ceil(limit / per_page)  # Calculate how many pages we need

    while len(anime_list) < limit and page <= total_pages:
        # The API endpoint with dynamic page number
        url = f"https://api.jikan.moe/v4/top/anime?page={page}&limit={per_page}"

        # Send the GET request to the API
        response = requests.get(url)

        # If something goes wrong (like a 404 or 500 error)
        if response.status_code != 200:
            print(f"⚠️ Error fetching page {page}: {response.status_code}")
            break

        # Convert JSON data to a Python dictionary
        data = response.json()

        # Loop through each anime entry and extract useful info
        for anime in data['data']:
            title = anime['title']
            synopsis = anime['synopsis'] or "No description available."
            image = anime['images']['jpg']['image_url']

            # Append the anime as a dictionary into our list
            anime_list.append({
                "title": title,
                "synopsis": synopsis,
                "image": image
            })

        # Move to the next page
        page += 1

    # Return only up to the requested limit (e.g., 100)
    return anime_list[:limit]


# -----------------------------------------------------
# Function: show_image_from_url()
# -----------------------------------------------------
# Takes an image URL and displays it using Pillow (opens in default viewer)
def show_image_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
    except Exception as e:
        print(f"❌ Couldn't load image: {e}")


# -----------------------------------------------------
# Function: random_anime_generator()
# -----------------------------------------------------
# Picks a random anime from the list and shows it to the user.
def random_anime_generator(anime_list):
    # Keep running until the user types 'quit'
    while True:
        # Randomly select one anime from the list
        anime = random.choice(anime_list)

        # Print the anime info
        print("\n🎬 Your Random Anime Recommendation 🎬")
        print(f"Title: {anime['title']}")
        print(f"Synopsis: {anime['synopsis']}")
        print(f"Image: {anime['image']}")
        print("-" * 80)

        # Show image (optional)
        show_image_from_url(anime['image'])

        # Ask the user if they want another recommendation
        again = input("\nPress [Enter] for another or type 'quit' to exit: ").strip().lower()
        if again == "quit":
            print("👋 Goodbye! Happy watching!")
            break


# -----------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------
if __name__ == "__main__":
    print("Fetching anime data, please wait... 🎌")
    top_anime = get_top_anime(100)
    print(f"✅ Loaded {len(top_anime)} anime from MyAnimeList.\n")

    random_anime_generator(top_anime)
