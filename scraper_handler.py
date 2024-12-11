# This script reads product names and URLs from a text file, scrapes reviews for each product
# from Best Buy's website, and saves the reviews in organized text files within a "reviews" folder.

import requests
from bs4 import BeautifulSoup
import os

class ScraperHandler:
    def __init__(self, input_file):
        # Initializes the scraper with the input file and sets up the output folder
        self.input_file = input_file
        self.output_folder = "reviews"
        os.makedirs(self.output_folder, exist_ok=True)

    def fetch_reviews(self, url, output_file, product_name):
        # Headers to mimic a browser and avoid blocks
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.bestbuy.com/"
        }

        # Sends request to the URL
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")   # Parses page content
            reviews = soup.find_all("li", class_="review-item")     # Finds all review items

            # Opens output file
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(f"Product Reviews for {product_name}\n\n")
                # Loops through all reviews
                for i, review in enumerate(reviews, 1):
                    # Gets and cleans up review text
                    review_text = review.find("div", class_="ugc-review-body").get_text(strip=True)
                    clean_review = ' '.join(review_text.split())
                    file.write(f"Review {i}:\n{clean_review}\n{'-'*40}\n\n")
            print(f"Reviews saved to {output_file}")
        else:
            print(f"Failed to fetch page, status code: {response.status_code}")

    def process_urls(self):
        # Reads URLs and product names from input file
        current_product_name = None
        with open(self.input_file, "r") as file:
            for line in file:
                url = line.strip()
                # If line starts with "#", represents the product name
                if url.startswith("#"):
                    current_product_name = url.replace("#", "").strip()
                # If line is a URL, fetch reviews for that product
                elif url:
                    # Defines output file path inside the "reviews" folder
                    if current_product_name:
                        output_file = f"{self.output_folder}/{current_product_name.replace(' ', '_').lower()}_reviews.txt"
                    else:
                        output_file = f"{self.output_folder}/default_reviews.txt"  # In case no product name is provided
                    # Fetches reviews and saves to file
                    self.fetch_reviews(url, output_file, current_product_name)
