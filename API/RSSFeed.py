import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd
  
def loadRSS(): 
  
    # url of rss feed 
    url = 'https://www.govinfo.gov/rss/bills.xml'
  
    # creating HTTP response object from given url 
    response = requests.get(url) 
  
    # saving the xml file 
    with open('newest_bills.xml', 'wb') as file: 
        file.write(response.content) 

def parseXML(xmlfile): 
  
    # get root element
    root = ET.parse(xmlfile).getroot()
  
    # create empty list for news items 
    bill_items = [] 
  
    # iterate items 
    for item in root.findall('./channel/item'): 
  
        # empty bills dictionary 
        bills = {} 
  
        # iterate child elements of item 
        for child in item: 
            bills[child.tag] = child.text.encode('utf8') 
    
  
        # append bill dictionary to news items list 
        bill_items.append(bills) 
      
    # return bill items list 
    return bill_items 

def savetoCSV(bill_items, filename): 
  
    # specifying the fields for csv file 
    fields = ['guid', 'title', 'pubDate', 'category', 'link', 'description'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(bill_items) 

def readCSV(csvfile):
    bills = pd.read_csv(csvfile)

def main(): 
    # load rss from web to update existing xml file 
    loadRSS() 
  
    # parse xml file 
    bill_items = parseXML('newest_bills.xml') 

    # store news items in a csv file 
    savetoCSV(bill_items, 'bill_items.csv')
main()

