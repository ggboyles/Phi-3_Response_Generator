# Product Review Analyzer

## Project Description

This project combines a web scraper and a phi3 response generator to analyze reviews from Best Buy's website, which are saved to text files and visualized on aa graph.

This project was developed for CS 325 (Software Engineering).

---

## Setup and Installation

1. **Clone this repository or download the ZIP file**

2. **Install Anaconda**

Anaconda is required to manage the environment for this project.

You can download Anaconda here if you do not have it installed.

[Anaconda Download Page](https://www.anaconda.com/products/dis

3. **Download and Install Ollama**

Ollama is required to run the Phi-3-mini model locally.

You can download the Ollama app here if you do not have it installed.

[Ollama Download Page](https://ollama.com/download)

4. **Create and Activate the Conda Environment**

Create the environment using the `requirements.yaml` file:

```conda env create -f requirements.yaml```

Then, activate the environment:

```conda activate phi3_env```

5. **Install Ollama in the Conda Environment**

Install Ollama within the environment:

```pip install ollama```

6. **Pull Phi-3 Model**

Locally download the Phi-3-mini model:

```ollama pull phi3```

You can make sure it is installed with this:

```ollama list```

## Instructions

1. **Edit ``productURLs.txt`` if desired**

- Use comments to specify the product names.

- Add URLs for each product on a new line.

**Note**: Be sure to scroll to the end of the product reviews on the main product page and hit "See All Customer Reviews" before copying your URL.

2. **Run the Script**

Run the script by using:

```python project3_main.py```

**Note**: Make sure the Ollama application is running in the background before running the script.

3. **View Responses and Graph**

You can find each ``.txt`` file in the ``sentiments`` folder. The graph will be saved as ``sentiment_graph.png``