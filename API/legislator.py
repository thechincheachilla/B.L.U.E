import pandas as pd
import csv


def parseLegislator(csvfile):
    raw = pd.read_csv(csvfile)
    print(raw)

def main():
    parseLegislator("legislators-current.csv")
 

if __name__ == '__main__':
    main()
