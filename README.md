# Phi-3 Response Generator

## Project Description

This project uses the Phi-3-mini model to generate responses from a user-inputted text file of prompts. 

This project was developed for CS 325 (Software Engineering). 

---

## Setup and Installation

1. **Clone this Repository or Download the ZIP file**
<br>

2. **Install Anaconda**

Anaconda is required to manage the environment for this project.

You can download Anaconda here if you do not have it installed.

[Anaconda Download Page](https://www.anaconda.com/products/distribution#download-section)
<br>

3. **Download and Install Ollama**

Ollama is required to run the Phi-3-mini model locally.

You can download the Ollama app here if you do not have it installed.

[Ollama Download Page](https://ollama.com/download)
<br>

4. **Create and Activate the Conda Environment**

Create the environment using the `requirements.yaml` file:

```conda env create -f requirements.yaml```

Then, activate the environment:

```conda activate phi3_env```
<br>

5. **Install Ollama in the Conda Environment**

Install Ollama within the environment:

```pip install ollama```
<br>

6. **Pull Phi-3 Model**

Locally download the Phi-3-mini model:

```ollama pull phi3```

You can make sure it is installed with this:

```ollama list```


## Instructions

1. **Edit Prompts**

Modify the prompts within `prompts.txt` if desired. Be sure to keep them on separate lines.

2. **Run the Script**

Run the script by using:

```python run_model.py```

If this does not work, you can try using the full path to Python in the environment:

```/opt/anaconda3/envs/phi3_env/bin/python run_model.py```

3. **View Responses**

After completion, terminal will show

``"Responses saved to responses.txt"``

