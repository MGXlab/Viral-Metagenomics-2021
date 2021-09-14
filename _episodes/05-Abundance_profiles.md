---
title: "Abundance profiles"
teaching: 0
exercises: 0
questions:
- ""
objectives:
- ""
keypoints:
- ""
---

To start off, we will run the python script `bam_to_profile.py` to get a counts table like the one showed in the previous section. It will print in the terminal the 15 most ubiquitous scaffolds, ie. the scaffolds that are present in more samples. **What does the column _nsamples_ mean?**

~~~
# create a directory to store output files
$ mkdir 3_profiles

# run the script
$ python scripts/bam_to_profile.py -b all_samples_cross_sorted.bam -o 3_profiles/
~~~

>## Discussion: Genome fragments
> There are several scaffolds present in 11 samples. Could they come from the same organism? In that case, think about reasons for the assembler not being able to reconstruct the complete genome but fragments of it.
{: .challenge}

The number of reads aligned to a scaffold reflects its abundance (ie. the abundance of the species) in the sample. The more present a species is in a sample, the more sequencing reads is going to obtain during the sequencing process. This abundance is directly related to the **depth of coverage**.

INCLUDE IMAGE HERE

However, note well the counts itself do not represent the **relative abundance** in the sample. To know this we need to normalize by the **total number of sequencing reads** in the sample and the **length of the scaffold** as follows:

![equation](<img src="http://www.sciweavers.org/tex2img.php?eq=Rel.abundance%20%3D%20%20%5Cfrac%7BMappedReads%7D%7BTotalReads%2AScaffoldLength%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="Rel.abundance =  \frac{MappedReads}{TotalReads*ScaffoldLength} " width="411" height="47" />)

Related to the discussion above, it is interesting to look at the abundance of the scaffolds in a sample because scaffolds coming from the same species should have the similar abundances (or depths of coverage, remember they are directly related). It this way, we can group scaffolds in **bins** representing a genome in a process called **binning**.

>## Discussion: Binning
> We just saw how relative abundance can be used to gather scaffolds into a bin. Can you think of other features used for binning?
{: .challenge}

In the next section we will use the abundances across all the samples to bin our scaffolds.

![Image]({{ page.root }}/fig/test_assembly.png)

{% include links.md %}
