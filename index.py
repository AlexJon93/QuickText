from sys import argv
from csv_reader import csv_reader
from messenger import body_former

def main(fileloc):
        mem_list = csv_reader.csv_parse(open(fileloc))
        for item in mem_list:
                print(item)

if __name__ == "__main__":
        main(argv[1])