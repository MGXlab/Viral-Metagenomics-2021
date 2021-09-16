---
title: Setup
---

## Install Conda
We will use `conda` to handle the dependencies for the workshop. **Please be sure you install it before the workshop**. More info [here](https://docs.conda.io/en/latest/miniconda.html).

After installing conda, follow steps below to download the dependencies file `workshop_env.yaml` and create a working environment with it.

~~~
# download the dependencies file
$ wget https://raw.githubusercontent.com/MGXlab/Viral-Metagenomics-2021/gh-pages/files/workshop_env.yaml

# create the environment
$ conda create -n viral_workshop -f workshop_env.yaml

# activate the environment
$ conda activate viral_workshop

# test the installation
$ spades.py -h
~~~



{% include links.md %}
