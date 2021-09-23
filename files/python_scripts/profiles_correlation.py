#!/usr/bin/env python3

import argparse, os, time
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)


if __name__ == "__main__":

    ### Help section, accession with -h when the script is executed ###
    parser = argparse.ArgumentParser(description="Reads a file with the corrected profiles for several samples, "
                                                 " and calculates the correlation between the mapping references based on the "
                                                 "reads aligned. As output it gives the file 'scaffolds_corr_90.txt' with the "
                                                 "references that correlate >= 0.9 with the reference given by the user. First column "
                                                 "is the name of the reference and second column is the Spearman's correlation.")

    parser.add_argument("-p", "--profiles",
                        help="'profiles_depth_length_corrected.txt' file.",
                        type=str,
                        required=True)

    parser.add_argument("-s", "--scaffold_name",
                        help="Name for the ubiquitous scaffold to calculate the correlation with the rest.",
                        type=str,
                        required=True)

    parser.add_argument("-o", "--out_dir",
                        help="Output directory to place 'scaffolds_corr_90.txt' with the highly correlating scaffolds.",
                        type=str,
                        required=True)



    args = parser.parse_args()


    # read profiles
    df = pd.read_csv(args.profiles, index_col=0)

    # calculate correlation with the scaffold provided by the user
    corr = df.corrwith(df.loc[args.scaffold_name], axis=1)
    corr

    # get the ones with corr > 0.9. Write them to file with their corr values
    scaffolds_corr_out = f"{args.out_dir}/scaffolds_corr_90.txt"
    corr[corr>=0.9].to_csv(scaffolds_corr_out, header=False, sep="\t")
