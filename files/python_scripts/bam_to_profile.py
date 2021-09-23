#!/usr/bin/env python3

import argparse, os, pysam, time
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
from glob import glob
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == "__main__":

    ### Help section, accession with -h when the script is executed ###
    parser = argparse.ArgumentParser(description="Given a BAM file, obtains the abundance profile of its samples. "
                                                 "It prints the 15 most ubiquitous references and the number of reads aligning to them "
                                                 "directly to stdout, and draws a heatmap in 'top500_ubiquitous.png' with this information "
                                                 "for the top 500 references. Last, it writes to 'profiles_depth_length_corrected.txt' the "
                                                 "profiles corrected by depth of the sample and length of the reference.")
    parser.add_argument("-b", "--bam_file",
                        help="BAM file with the mapping information. IMPORTANT: it should not contain unmapped reads and needs to be sorted and indexed.",
                        type=str,
                        required=True)

    parser.add_argument("-o", "--out_dir",
                        help="Output directory to put the heatmap and the profiles corrected by depth and length.",
                        type=str,
                        required=True)



    args = parser.parse_args()

    bam = pysam.AlignmentFile(args.bam_file, "rb")

    contigs = {reference:length for reference, length in zip(bam.references, bam.lengths)}

    samples = sorted(list(set([read.qname.split(".")[0] for read in bam.fetch(until_eof=True)])))
    print(f"{len(samples)} samples detected in the BAM file {os.path.basename(args.bam_file)}")
    print(samples)
    print("Iterating alignments...")


    samples_contigs_counts = dict()
    for sample in samples:
        samples_contigs_counts[sample] = {contig:0 for contig in contigs}


    # fill dictionary
    bam = pysam.AlignmentFile(args.bam_file, "rb")
    for read in bam.fetch(until_eof=True):
        # get the sample id
        sample = read.qname.split(".")[0]

        # get contig id
        contig = bam.get_reference_name(read.tid)

        samples_contigs_counts[sample][contig] += 1


    # raw dataframe
    df_raw = pd.DataFrame(samples_contigs_counts)
    #print(df_raw.loc["NODE_2781_length_771_cov_305.255587"])

    # sort the contigs by ubiquity
    ubq = df_raw.astype(bool).sum(axis=1)
    df_raw.insert(0, "nsamples", ubq)
    df_raw = df_raw.sort_values(by=['nsamples'], ascending=False)


    # remove the nsamples before correcting by depth
    nsamples = df_raw["nsamples"]
    df_raw = df_raw.drop(columns="nsamples")
    # correct by depth of the sample
    df_depth = df_raw.div(df_raw.sum(axis=0), axis=1)
    df_depth.insert(0, "nsamples", nsamples)


    # correct by length of the contigs
    df_len = pd.DataFrame()
    for column in df_depth.columns:
        if column != "nsamples":
            df_len[column] = df_depth[column] / df_depth.index.map(contigs)

    out_file = f"{args.out_dir}/profiles_depth_length_corrected.txt"
    df_len.to_csv(out_file)

    print("Generating heatmap...")

    out_heatmap = f"{args.out_dir}/top500_ubiquitous.png"

    log2 = np.log2(df_raw + 1)
    fig, ax = plt.subplots(figsize=(11,12))

    sns.heatmap(log2[:500],
                cmap="plasma_r",
                yticklabels=False,
                ax = ax)

    ax.set_title('log2 mapped reads of the top 500 ubiquitous scaffolds')
    plt.xlabel("Samples")
    plt.ylabel("Scaffolds")

    plt.savefig(out_heatmap, facecolor='w', bbox_inches="tight")


    print("\n\nShowing reads aligned to the 15 most ubiquitous contigs:\n")
    df_raw.insert(0, "nsamples", nsamples)
    print(df_raw[:15])

print(df_raw[:10])
print(df_raw.sum(axis=0))
