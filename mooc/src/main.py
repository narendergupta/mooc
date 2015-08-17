from datamodel import DataModel

import argparse
import sys


def main(args):
    dm = DataModel()
    dm.read_data(to_read_count=10, normalize_data=True)
    dm.write_data('../data/data_imp.csv')


if  __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--master_file", required=True)
    parser.add_argument("--output_f1_file")
    args = parser.parse_args()
    main(args)

