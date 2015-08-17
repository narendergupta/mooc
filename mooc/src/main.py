from datamodel import DataModel

import argparse
import sys


def main(args):
    train_count = -1
    dm = DataModel()
    dm.read_data(to_read_count=10)
    print(dm.data)


if  __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--master_file", required=True)
    parser.add_argument("--output_f1_file")
    args = parser.parse_args()
    main(args)

