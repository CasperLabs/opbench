import argparse
import logging
import csv

import pandas as pd

from math import log, ceil, floor, isnan
logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(
    description="Round results from opbench_batch_fit to obtain gas costs"
)

parser.add_argument("input_file", help="Path to the input CSV file")
parser.add_argument("-s", "--significant-figures", type=int, default=2, help="Number of significant figures. Default: 2")
parser.add_argument("-o", "--output", type=str, required=True, help="Output CSV file")

def round_up(f, n):
    assert(n > 0)
    assert(not isnan(f))

    if abs(f) > 1:

        sign = 1 if f >= 0 else -1
        f_ = abs(f)

        n_digits = floor(log(f_, 10))
        exponent = max(n_digits - n + 1, 0)
        # print(n_digits, exponent)

        f_ = f_ / 10**exponent

        if f >= 0:
            f_ = ceil(f_)
        else:
            f_ = floor(f_)

        f_ = f_ * 10**exponent
        f_ = f_ * sign

    elif 0 <= abs(f) <= 1:
        f_ = 0

    return f_

def format_int(i):
    return "{:_d}".format(i)

def main():
    args = parser.parse_args()

    df = pd.read_csv(args.input_file, keep_default_na=False)

    col_indices = [2*i+3 for i in range((len(df.columns)-2)//2)]

    col_labels = [df.columns[i] for i in col_indices]

    # print(round_up(3.2, 1)) # Should give 4
    # print(round_up(684, 2)) # Should give 690

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

    df.to_csv(args.output, index=False, quotechar="\"", quoting=csv.QUOTE_NONNUMERIC)


if __name__ == "__main__":
    main()

