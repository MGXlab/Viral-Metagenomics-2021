---
title: "Profiles correlation"
teaching: 0
exercises: 0
questions:
- ""
objectives:
- ""
keypoints:
- "Adding more samples with similar species diversity but different abundances increases the binning resolution."
---

From the previous section we know there are some scaffolds present in almost all samples, and that we can bin them looking at their abundances or depths in a sample. However, we can achieve a better binning resolution by taking all the samples into account.

Look at the table below, with the mean depth of coverage for each scaffold in each sample. Looking only at sample A, we would say that scaffolds 1,2,4,5 and 6 come from the same genome because they have the same depth. However, looking at Samples B and C we can see that there are indeed 3 bins: [2,5,6], [1,4] and [3,7]. Adding more samples to the binning step we can discern which scaffolds, with the same depth, come from the same species.

|            	| Sample A 	| Sample B 	| Sample C 	|
|:----------:	|:--------:	|:--------:	|:--------:	|
| Scaffold 1 	|    4x    	|    15x   	|    0x    	|
| Scaffold 2 	|    4x    	|    3x    	|    9x    	|
| Scaffold 3 	|    0x    	|    7x    	|    6x    	|
| Scaffold 4 	|    4x    	|    15x   	|    0x    	|
| Scaffold 5 	|    4x    	|    3x    	|    9x    	|
| Scaffold 6 	|    4x    	|    3x    	|    9x    	|
| Scaffold 7 	|    0x    	|    7x    	|    6x    	|

Now we are going to bin our scaffolds, but not all of them: we will focus on those that are present in most of the samples, and look for others with a similar abundance profile, ie. it pattern of abundance across the samples. For this, we will select one of the most ubiquitous contigs printed in the terminal in the previous section and the script `profiles_correlation.py` will calculate the correlation between its abundance profile  and the profiles of the rest of scaffolds. Those highly correlating with the scaffold you selected are likely to be part of the same bin.


However, note well the counts itself do not represent the **relative abundance** in the sample. To know this we need to normalize by the **total number of sequencing reads** in the sample and the **length of the scaffold** as follows:

![equation](https://latex.codecogs.com/gif.latex?Relative%20Abundance%20%3D%20%5Cfrac%7BMapped%20Reads%7D%7BTotalReads%20*%20Scaffold%20Length%7D)



{% include links.md %}
