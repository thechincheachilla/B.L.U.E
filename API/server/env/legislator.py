import pandas as pd
import csv

class Legislator:
    def parseLegislator(csvfile):
        return pd.read_csv(csvfile).T.to_json(); 

    if __name__ == '__main__':
        main()
