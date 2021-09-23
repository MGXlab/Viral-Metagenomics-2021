#!/usr/bin/env python3

import argparse, os, time
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
from glob import glob
from Bio import SeqIO


if __name__ == "__main__":

    ### Help section, accession with -h when the script is executed ###
    parser = argparse.ArgumentParser(description="Calculates summary statistics of the FASTA files "
                                                  "in the directory provided by the user, and prints "
                                                  "them to stdout.")
    parser.add_argument("-i", "--input_dir",
                        help="Directory with the FASTA files to be analyzed. "
                        "Accepted extensions are '.fna' and '.fasta'.",
                        type=str,
                        required=True)

    args = parser.parse_args()


    # list the FASTA files in the directory
    fasta_files = glob(f"{args.input_dir}/*.fna") + glob(f"{args.input_dir}/*.fasta")
    print(f"{len(fasta_files)} FASTA files in the directory.")
    print("Calculating statistics...")
    print()


    # define the names for the target statistics
    stats = ["#seqs", "mean_len", "max_len", "min_len", ">50kb", ">5kb", ">1kb", ">500b", ">200b", ">50b", "#Ns" ]

    # get base names of the samples using os.path.basename()
    samples = sorted([os.path.basename(fasta_file).split(".f")[0] for fasta_file in fasta_files])

    # create a nested dictionary: first level are the samples, second level are the stats
    # all the stats are initialized as 0 (zero)
    samples_stats = dict()
    for sample in samples:
        samples_stats[sample] = {stat:0 for stat in stats}


    # iterate fasta_files while filling the samples_stats dict
    for fasta_file in fasta_files:

        # get the sample name from the file
        sample = os.path.basename(fasta_file).split(".f")[0]

        # read the file with the parse() function. It requires format to be specified
        records = SeqIO.parse(fasta_file, "fasta")

        # 'records' object is of the class 'FastaIterator'. Convert it to list
        records_list = [record for record in records]

        # Append to the list 'lengths' the length of each sequence
        lengths = [len(record.seq) for record in records_list]

        # Compute mean length
        mean_length = np.mean(lengths)

        # Check the length of the sequences. Add +1 to the corresponding stat
        more_50k = sum(i > 50000 for i in lengths)
        more_5k  = sum(i > 5000 for i in lengths)
        more_1k  = sum(i > 1000 for i in lengths)
        more_500 = sum(i > 500 for i in lengths)
        more_200 = sum(i > 200 for i in lengths)
        more_50  = sum(i > 50 for i in lengths)

        # count the number of Ns
        Ns = 0
        for record in records_list:
            Ns += record.seq.count("N")

        # store statistics in the samples_stats dictionary
        samples_stats[sample]["#seqs"] = len(records_list)
        samples_stats[sample]["mean_len"] = "{:.2f}".format(mean_length)
        samples_stats[sample]["max_len"] = max(lengths)
        samples_stats[sample]["min_len"] = min(lengths)
        samples_stats[sample][">50kb"] = more_50k
        samples_stats[sample][">5kb"]  = more_5k
        samples_stats[sample][">1kb"]  = more_1k
        samples_stats[sample][">500b"] = more_500
        samples_stats[sample][">200b"] = more_200
        samples_stats[sample][">50b"]  = more_50
        samples_stats[sample]["#Ns"]   = Ns



    df = pd.DataFrame(samples_stats)
    df = df.reindex(stats)
    print(df)
