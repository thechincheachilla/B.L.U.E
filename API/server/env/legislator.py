import pandas as pd
import csv

class Legislator:

    def parseLegislator(csvfile):
        return pd.read_csv(csvfile).T.to_dict()

    if __name__ == '__main__':
        main()
