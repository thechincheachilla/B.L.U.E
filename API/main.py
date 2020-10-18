# Author Dylan Jergens
# This program runs the search engine, taking user input

from search_engine import SearchEngine


def main():
    # from past 100 bills, extract information
    # get second rss stream that extracts info from bill's own xml
    # get a list of 


    # assuming the csv files are somewhere in here
    directory = "csv" #/API/*.csv
    engine = SearchEngine(directory)

    # returns a list of the file names, ranked by how relevant to the query they are
    ranking = engine.search(term)


if __name__ == '__main__':
    main()