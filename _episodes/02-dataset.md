---
title: "The dataset"
teaching: 0
exercises: 0
questions:
- "Where does the dataset come from"
- "What format is the sequencing data"
objectives:
- "Collect basic statistics about the dataset"
- "Run python scripts"
keypoints:
- ""
---
In this exercise you will analyze viral metagenomes derived from twelve human gut samples in ([Reyes et al Nature 2010](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2919852/)). In this study, shotgun sequencing was carried out in the [454 platform](https://en.wikipedia.org/wiki/454_Life_Sciences) to produce unpaired (also called _single-end_) reads.

Raw sequencing data is usually stored in FASTQ format, which contains the sequence itself and the quality of each base. Check out [this video](https://www.youtube.com/watch?v=sdxVDy0lSAE) to get more insight into the sequencing process and FASTQ format. To make things faster, the data you are going to analyze today is in FASTA format, which does not contain the quality information.

~~~
$ ls
~~~
{: .bash}

{% include links.md %}
