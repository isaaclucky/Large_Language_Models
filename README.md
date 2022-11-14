<h1 align="center">Prompt Engineering: In-context learning with GPT-3 and other Large Language Models 
</h1>
<div>
<a href="https://github.com/isaaclucky/Large_Language_Models/network/members"><img src="https://img.shields.io/github/forks/isaaclucky/Large_Language_Models" alt="Forks Badge"/></a>
<a href="https://github.com/isaaclucky/Large_Language_Models/pulls"><img src="https://img.shields.io/github/issues-pr/isaaclucky/Large_Language_Models" alt="Pull Requests Badge"/></a>
<a href="https://github.com/isaaclucky/Large_Language_Models/issues"><img src="https://img.shields.io/github/issues/isaaclucky/Large_Language_Models" alt="Issues Badge"/></a>
<a href="https://github.com/isaaclucky/Large_Language_Models/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/isaaclucky/Large_Language_Models?color=2b9348"></a>
<a href="https://github.com/isaaclucky/Large_Language_Models/blob/main/LICENSE"><img src="https://img.shields.io/github/license/isaaclucky/Large_Language_Models?color=2b9348" alt="License Badge"/></a>
</div>


</br>
<img src="images/100t.jpg" name="">


## Articles
- [Medium Article](https://medium.com/@Yishak_Tadele/large-language-models-prompt-engineering-2c42087937a0)

## Table of Contents

* [Prompt Engineering in Large Language Models](#Large_Language_Models)

  - [Introduction](##Introduction)
  - [Project Structure](#project-structure)
    * [data](#data)
    * [models](#models)
    * [notebooks](#notebooks)
    * [scripts](#scripts)
    * [sql](#sql)
    * [tests](#tests)
    * [logs](#logs)
    * [root folder](#root-folder)
  - [Installation guide](#installation-guide)

## Introduction

Large Language Models (LLM)s — are machine learning algorithms that can recognize, predict, and generate human languages on the basis of very large text-based data sets.

## Project Structure

### images:

- `images/` the folder where all snapshot for the project are stored.

### logs:

- `logs/` the folder where script logs are stored.

### mlruns:
- `mlruns/` the folder that contain auto generated mlflow runs.
### data:

 - `train_store.csv.dvc` the folder where the dataset versioned csv files are stored.

### .dvc:
- `.dvc/`: the folder where dvc is configured for data version control.

### .github:

- `.github/`: the folder where github actions and CML workflow is integrated.

### models:
- `models`: the folder where model pickle files are stored.

### notebooks:

- `data_preprocessing.ipynb`: a jupyter notebook for preprocessing the data.
- `data_exploration.ipynb`: a jupyter notebook for exploring the data.


###  scripts:

- `applications/`: folder where dashboard design are stored.
- `data_preprocessing.py`:  a python script for accessing information data from a pandas dataframe.
- `data_exploration.py`: a python script for plotting dataframes.
- `log_help.py`: a python script that creates python based logger.
### tests:

- `tests/`: the folder containing unit tests for the scripts.

### sql:

- `sql/`: the folder containing database table and mysql-python manipulator script.
### root folder

- `train.py`: holds cml report and model metrics.
- `results.txt`: contains cml pr reports.
- `requirements.txt`: a text file lsiting the projet's dependancies.
- `app.py`: main file for the streamlit application.
- `setup.py`: a configuration file for installing the scripts as a package.
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.
- `Dockerfile`: build users can create an automated build that executes several command-line instructions in a container.

## Installation guide

```bash
git clone https://github.com/isaaclucky/Large_Language_Models.git
cd Large_Language_Models
sudo python3 setup.py install
```
