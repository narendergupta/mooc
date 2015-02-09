import sys
import csv


def main(argv):
  train_count = -1
  if(len(argv)>0):
    train_count = int(argv[0])
  fhandle = open('data/data1.csv', 'r')
  freader = csv.reader(fhandle, delimiter=',')
  for i in range(train_count):
    print(next(freader))
  return None


if  __name__ == '__main__':
  main(sys.argv[1:])

