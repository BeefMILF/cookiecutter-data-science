# Cookiecutter Data Science for TDSP

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Cookiecutter homepage](http://drivendata.github.io/cookiecutter-data-science/)
#### [TDSP homepage](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/)

### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/maknotavailable/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.png)](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
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
```

### Installing development requirements
------------

    pip install -r requirements.txt

### More information on customizing the cookiecutter template
------------

    First steps:
    https://cookiecutter.readthedocs.io/en/latest/first_steps.html