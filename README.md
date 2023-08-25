# Artificial Data Plug and Play

Get up and running with experimenting on artificial NHS data!

> **This material is maintained by the [NHS England Data Science team](mailto:datascience@nhs.net)**.
>
> See our other work here: [NHS England Analytical Services](https://github.com/NHSDigital/data-analytics-services).

To contact us raise an issue on Github or via [email](mailto:datascience@nhs.net) and we will respond promptly.


## What is artificial data?
Artificial data sets provide users with large volumes of data that share some of the characteristics of real data while protecting patient confidentiality. They are designed to model the structure of real data but are completely artificial – they do not contain any actual patient records. We are piloting this new service with a limited number of artificial data sets.

You can find out more about the pilot on the [NHS website](https://digital.nhs.uk/services/artificial-data).

## What is this repo for?
This repo contains some example code for getting started with using artificial data with minimal setup. 

It was creating using the [rap-package-template](https://github.com/NHSDigital/rap-package-template/tree/main) which provides a neat way to create new repositories for Reproducible Analytical Pipelines.

### What does the repo contain?
The repo contains the following files and directories:
```
|- sql                  # Code for interacting with SQL
|- src                  # Source code for data ingestion, cleaning, processing, etc
|- templates            # Templates for excel reporting
|- tests                # Test modules
|- pyproject.toml       # Configuration
|- plug_and_play.ipynb  # Plug and play notebook
|- requirements.txt     # Python dependencies to be installed via pip
|- ...                  # Additional repo files (e.g. .gitignore)
```

**Note:** because this repo was created from the [rap-package-template](https://github.com/NHSDigital/rap-package-template/tree/main) there are a number of files / folders that persist from that template. 
These have been left in the repo so that you can fork the repo and adapt to your own needs! 

For the plug and play tutorial, the main file you'll be interacting with is [plug_and_play.ipynb](./plug_and_play.ipynb). See below for instructions on how to get set up to run the tutorial. 


## How do I get started?

If you are setting up the tutorial in an environment which is provisioned out of the box (such as Google Colab or GitHub Codespaces), see *Quick start*.
More detailed instructions can be found in *Full setup*.

### Quick start
The easiest way to run the tutorial is in an environment which is provisioned out of the box.
Clicking one of the buttons below will open the repo in the respective environment with all the dependencies setup so you can just get coding!

<a href="https://github.com/codespaces/new?template_repository=NHSDigital/artificial-data-plug-and-play" target="_parent"><img src="https://github.com/codespaces/badge.svg" width="200" alt="Open In Codespaces"/></a>
<a href="https://colab.research.google.com/github/NHSDigital/artificial-data-plug-and-play/blob/main/plug_and_play.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" width="150" alt="Open In Colab"/></a>


### Full setup
Prerequisites:
- A bash terminal (although similar instructions will work in PowerShell)
- Python >= 3.10
- An IDE or text editor (such as VS Code or PyCharm)

Open a terminal and execute the following
1. Navigate to a directory you want to create the tutorial repo in (using `cd DESTINATION_DIRECTORY`)
1. Clone the repo using `git clone https://github.com/NHSDigital/artificial-data-plug-and-play.git`
1. Open the repo in the terminal using `cd artificial-data-plug-and-play` and create a virtual environment via `python -m venv .venv` (note you don't have to do this in a virtual environment, but it is recommended)
1. Activate the environment and install the requirements `. .venv/bin/activate && pip install -r requirements.txt`
1. (Optional) Install jupyter via `pip install jupyter`. This will allow you to use jupyter notebooks thoough the classic web interface.
1. Open the tutorial
    - Using jupyter if you installed it using the command above `jupyter notebook plug_and_play.ipynb`
    - Alternatively, you can open the notebook in your IDE of choice (for example using [VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks))

You should now be ready to run the plug and play!

## See also
Here are some other related projects that are worth checking out:
1. [Reproducible Analytical Pipeline example](https://github.com/NHSDigital/RAP_example_pipeline_python/tree/main)  which uses artificial HES data to create a simple stats publication
1. [Codebase to generate artificial data](https://github.com/NHSDigital/artificial-data-generator) written for Databricks using Python / PySpark