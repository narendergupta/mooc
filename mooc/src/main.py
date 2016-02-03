from datamodel import DataModel

import argparse
import sys


def main(args):
    dm = DataModel(args.data_file)
    dm.read_data(to_read_count=args.data_rows_to_read,
            normalize_data=True)
    dm.write_data('../data/data_norm.csv')


if  __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_file", required=True,
            help="Path of CSV data file")
    parser.add_argument("--data_rows_to_read", type=int, default=10,
            help="Number of data rows to be read, default is complete data")
    args = parser.parse_args()
    main(args)

