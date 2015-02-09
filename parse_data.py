import sys
from datamodel import DataModel


def main(argv):
  train_count = -1
  if(len(argv)>0):
    train_count = int(argv[0])
  dm = DataModel()
  lines = dm.get_data(train_count)
  print(lines[-1])


if  __name__ == '__main__':
  main(sys.argv[1:])

