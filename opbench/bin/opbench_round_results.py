import argparse
import logging
import csv

import pandas as pd

from opbench.helper import round_up

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description="Round results from opbench_batch_fit to obtain gas costs"
)

parser.add_argument("input_file", help="Path to the input CSV file")
parser.add_argument(
    "-s",
    "--significant-figures",
    type=int,
    default=2,
    help="Number of significant figures. Default: 2",
)
parser.add_argument("-o", "--output", type=str, required=True, help="Output CSV file")


def format_int(i):
    return "{:_d}".format(i)


def main():
    args = parser.parse_args()

    df = pd.read_csv(args.input_file, keep_default_na=False)

    col_indices = [2 * i + 3 for i in range((len(df.columns) - 2) // 2)]

    col_labels = [df.columns[i] for i in col_indices]

    for label in col_labels:
        col = df[label].to_list()
        # new_col = col.apply(lambda x: format_int(round_up(x, args.significant_figures)))

        new_col = []
        for i in col:
            if isinstance(i, str):
                try:
                    i = eval(i)
                except:
                    new_col.append("")
                    continue

            if isinstance(i, int) or isinstance(i, float):
                new_col.append(format_int(round_up(i, args.significant_figures)))
            else:
                new_col.append("")

        df[label] = new_col

    df.to_csv(args.output, index=False, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)


if __name__ == "__main__":
    main()
