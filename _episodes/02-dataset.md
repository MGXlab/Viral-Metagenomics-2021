---
title: "The dataset"
teaching: 0
exercises: 0
questions:
- "Where does the dataset come from."
- "What format is the sequencing data."
objectives:
- "Collect basic statistics about the dataset."
- "Run python scripts."
keypoints:
- "FASTA format does not contain sequencing quality information."
- "Next Generation Sequencing data is made of short sequences."
---
In this exercise you will analyze viral metagenomes derived from twelve human gut samples in ([Reyes et al Nature 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2919852/)). In this study, shotgun sequencing was carried out in the [454 platform](https://en.wikipedia.org/wiki/454_Life_Sciences) to produce unpaired (also called _single-end_) reads.

Raw sequencing data is usually stored in FASTQ format, which contains the sequence itself and the quality of each base. Check out [this video](https://www.youtube.com/watch?v=sdxVDy0lSAE) to get more insight into the sequencing process and FASTQ format. To make things faster, the data you are going to analyze today is in FASTA format, which does not contain the quality information. In the FASTA format we call _header_, _identifier_ or just _name_ to the line that precedes the nucleotide or aminoacid sequence. It always start with the `>` symbol and should be unique for each sequence.

Let's get started by downloading and unzipping the file file with the sequencing data in a directory called `0_Raw-data`.

~~~
# create the directory and move to it
$ mkdir 0_Raw-data
$ cd 0_Raw-data

# download and unzip
$ wget https://tbb.bio.uu.nl/dutilh/courses/CABBIO/Reyes_fasta.tgz
$ tar zxvf Reyes_fasta.tgz

# show the first 10 lines of a FASTA file
$ head -n 10 F1M.fna
~~~
{: .bash}

We have prepared a python script for you to get basic statistics about the sequencing data, such as the number of reads per sample, or their maximum and minimum length. Run the script as indicated below. **Which are the samples with the maximum and minimum number of sequences? In overall, which are the mean, maximum and minimum lengths of the sequences?**

~~~
$ python3 fasta_statistics.py -i 0_Raw-data
~~~

Next step is to put together all these short sequences to reconstruct larger genomic fragments in a process called **assembly**. More specifically, we will be doing a **cross-assembly**.

{% include links.md %}
