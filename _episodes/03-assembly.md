---
title: "Assembly"
teaching: 0
exercises: 0
questions:
- ""
objectives:
- ""
keypoints:
- ""
---

*Sequence assembly* is the reconstruction of long contiguous genomic sequences (called *contigs* or *scaffolds*) from short sequencing reads. Before 2014 a common approach in metagenomics was to compare the short sequencing reads to the genomes of known organisms in the database (and some studies today still take this approach). However, recall that most of the sequences of a metavirome are unknown, meaning that they yield no hits when comparing them to the databases. Because of this we need of database-independent approaches to describe new viral sequences. As bioinformatics tools improved, sequence assembly enabled recovery of longer sequences of the metagenomic datasets. Having a longer sequence means having more information to classify it, so using metagenome assembly helps to characterize the microbiome.

In cross-assembly, **multiple datasets are combined and assembled together**, allowing the discovery of shared sequence elements between the assembled contigs. For this exercise we will use _de novo_ cross-assembly, where the sequences of all samples are assembled together. This implies that if a virus (or other sequence element) is present in several different samples, its sequencing reads from the different samples will be joined into one contig. We will look for viruses that are present in many people. To do that, we will map the reads back to the cross-assembly and obtain the abundance profiles of each contig across the samples. If we find a contig that aligns reads from all twelve samples, this would mean that all the samples share that viral sequence.

~~~
# first create the directory and move the file to it
$ mkdir 0_Raw-data
$ cp Reyes_fasta.tgz 0_Raw-data

# move to the directory and uncompress the file
$ tar zxvf Reyes_fasta.tgz
~~~
{: .bash}

We have prepared a python script for you to get basic statistics about the sequencing data, such as the number of reads per sample, or their maximum and minimum length. Run the script as indicated below. **Which are the samples with the maximum and minimum number of sequences? In overall, which are the mean, maximum and minimum lengths of the sequences?**

~~~
$ python3 fasta_statistics.py -i 0_Raw-data
~~~



Next step is to put together all these short sequences to reconstruct larger genomic fragments in a process called **assembly**. More specifically, we will be doing a **cross-assembly**.

{% include links.md %}
