---
title: Setup
---


> ## Operating System
> - This course has been tested on **Ubuntu 20.04** and everything should run smoothly in any other Linux distribution and **MacOSX**.
> - It has not been tested on **Windows**. Moreover, if this is your OS we won't be able to help you with the command line, so be sure to be fluent with it.
>
{: .callout}


> ## How to follow this course
> - Along the lessons you will find specific questions about the data and discussion blocks. We recommend you to create a separate document and write your answers there.
> - For the analysis, we recommend you to create a directory, ie. `viral_metagenomics_course`, and work from there. Each of the steps will have its own directory within the main one. At the end you should end up with a structure similar to the one below.
~~~
# create the directory and move to it
$ mkdir viral_metagenomics_course
$ cd viral_metagenomics_course
...
# after the course it will be similar to this:
viral_metagenomics_course
├── 0_raw-data
├── 1_cross-assembly
├── 2_mapping
├── 3_profiles
├── 4_re-assembly
├── python_scripts
└── my_answers.docx
~~~
>
{: .keypoints}



## Install Conda
We will use `conda` to handle software dependencies. If you don't have it installed, get the **Latest Miniconda Intaller** from [here](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links). Installing it should be as straightforward as opening a terminal session and running code below, but it might vary depending on your system setup. Ask the instructors if you have any doubt about it. During installation, you will be asked “Do you wish the installer to initialize Anaconda3 by running conda init?” Type “yes”. More on installing [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) (Linux) and [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) (MacOSX).

~~~
# Linux
$ bash Miniconda3-latest-Linux-x86_64.sh

# MacOSX
$ bash Miniconda3-latest-MacOSX-x86_64.sh
~~~

#### Create environment
After installing conda, follow steps below to download the dependencies file `workshop_env.yaml` and create a working environment with it.

~~~
# download the dependencies file
$ wget https://raw.githubusercontent.com/MGXlab/Viral-Metagenomics-2021/gh-pages/files/workshop_env.yaml

# create the environment
$ conda env create --name metaviral_workshop -f workshop_env.yaml

# activate the environment
$ conda activate metaviral_workshop

# test the installation
$ spades.py -h
~~~

## Download Python scripts
We will be using some python scripts as well. You can keep them in their folder or move them to other locations, just be aware of the relative path to input and output files. Run `python <script> -h` on any of these scripts (replace `<script>`) to see the help message.

~~~
# download the scripts folder
$ wget https://github.com/MGXlab/Viral-Metagenomics-2021/raw/gh-pages/files/python_scripts.zip

# unzip it
$ unzip python_scripts.zip
~~~


{% include links.md %}
