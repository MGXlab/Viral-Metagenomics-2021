import argparse, os, time, sys
from Bio import SeqIO


if __name__ == "__main__":

    ### Help section, accession with -h when the script is executed ###
    parser = argparse.ArgumentParser(description="Modifies the header line of the fasta files provided by Prodigal. "
                                                 "It only keeps the part of the header before the first space. "
                                                 "A new fasta file is created with the flag '_header'.")

    parser.add_argument("-i", "--input_file",
                        help="FASTA file to be modified.",
                        type=str,
                        required=True)

    args = parser.parse_args()


if __name__ == "__main__":

    if not args.input_file.endswith(".faa"):
        print("Is this a protein FASTA file? Make sure it is.")
        print("Exiting...")
        sys.exit()
    else:
        out_file = args.input_file.replace(".faa", "_headers.faa")

        records = SeqIO.parse(args.input_file, "fasta")
        to_write = list()
        for record in records:
            record.description = ""
            to_write.append(record)

        with open(out_file, "w") as fout:
            SeqIO.write(to_write, fout, "fasta")
