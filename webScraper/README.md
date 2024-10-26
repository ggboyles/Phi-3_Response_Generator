# Best Buy Product Review Web Scraper

## Project Description

This project is a web scraper designed to extract product reviews from Best Buy's website. The scraper reads product URLs and names from a text file, then saves each product’s reviews to a uniquely named text file in a ``reviews`` folder.

This project was developed for CS 325 (Software Engineering).

---

## Setup and Installation

1. **Clone this repository or download the ZIP file**

2. **Install Anaconda**

Anaconda is required to manage the environment for this project.

You can download Anaconda here if you do not have it installed.

[Anaconda Download Page](https://www.anaconda.com/products/distribution#download-section)

3. **Create and Activate the Conda Environment**

Create the environment using the `requirements.yaml` file:

```conda env create -f requirements.yaml```

Then, activate the environment:

```conda activate scraper_env```

## Instructions

1. **Edit ``productURLs.txt``**

- Use comments to specify the product names.

- Add URLs for each product on a new line.

**Note**: Be sure to scroll to the end of the product reviews on the main product page and hit "See All Customer Reviews" before copying your URL.

2. **Run the Script**

Run the script by using:

```python scraper.py```

3. **View Responses**

After completion, terminal will show for each URL

``"Responses saved to reviews/{product_name}_reviews.txt"``

You can find each ``.txt`` file in the ``reviews`` folder.
