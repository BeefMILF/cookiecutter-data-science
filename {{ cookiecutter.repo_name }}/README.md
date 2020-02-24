{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── assets             <- Version controlled assets, such as stopword lists. Training data should 
    │                         be stored in local data directory, outside of repository. 
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is <[Task]-[Short Description]>,
    │                         for example 'Data - Exploration'
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so code can be imported
    ├── code               <- Source code for use in this project.
    │   ├── __init__.py    <- Makes code a Python module
    │   │
    │   ├── main.py        <- Main file, later used for inference
    │   │
    │   ├── helper.py      <- Use case agnostic helper file, with common functions
    │   │   └── build_features.py
    │
    ├── tests              <- Source code for use in this project.
    │   └── test_main.py   <- Test for the main function
    └── tox.ini            <- tox file with settings for running tox; see https://tox.readthedocs.io/

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
