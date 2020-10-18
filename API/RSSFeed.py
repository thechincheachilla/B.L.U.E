import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd



def loadXML(url, filename, final_filename, singleOr100):
    # url of rss feed 
    response = requests.get(url) 
  
    # saving the xml file 
    with open(filename, 'wb') as file: 
        file.write(response.content) 
    if singleOr100 == '100':
        parseXML(filename, final_filename)
    elif singleOr100 == 'single':
        parseXMLSponsor(filename)



def parseXML(xmlfile, final_filename): 
  
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
    savetoCSV(bill_items, final_filename)

def parseXMLSponsor(xmlfile):
    root = ET.parse(xmlfile).getroot()

    bill_info = []

    for item in root.findall('billStatus/bill'):
        
        info = {'summaries' : [], 'sponsors' : [], 'cosponsors' : []}

        for child in item:
            print(child.tag)
            if child.tag == 'summaries':
                for item in root.findall('billStatus/bill/summaries/billSummaries/item'):
                    if child.tag == 'text':
                        info[child.tag].append(child.text.encode('utf8'))
            elif child.tag == 'sponsors' or child.tag == 'cosponsors':
                for item in root.findall('billStatus/bill/sponsors/item'):
                    if child.tag == 'fullName':
                        info[child.tag].append(child.text.encode('utf8'))

        bill_info.append(info)
    # list of dictionaries where the keys are the tags and values are lists
    return bill_info


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
    df = pd.read_csv(csvfile)
    df['guid'] = df.apply(lambda x : x['guid'][11:-3], axis=1)
    return df['guid'].tolist()

def extractSponsors(csv):
	bills = {}
    for guid in csv:
        guid = csv[0]
        url = 'https://www.govinfo.gov/bulkdata/BILLSTATUS/116/hr/BILLSTATUS-116' + guid + '.xml'
        bills[guid] = loadXML(url, "bill_sponsors.xml", "sponsor_names.csv", "single")
        return bills




'''
mapToBill takes in a dictionary (with bills as keys and sponsors as values)
and reverses the key mapping pair so that we can get a dictionary of sponsors
mapped to what they sponsored
'''
def mapToBill(bills):
    legislators = {}
    
    for bill, sponsors in bills.items():
    	#check sponsors for each bill
    	for sponsor in sponsors:
            if sponsor not in legislators:
                legislators[sponsor] = [bill]
            else:
                legislators[sponsor].append(bill)

    return legislators


def main(): 
	# load rss from web to update existing xml file 
    loadXML('https://www.govinfo.gov/rss/bills.xml', "newest_bills.xml", "bill_items.csv", "100") 
    # parse xml file 
    # bill_items = parseXML('newest_bills.xml') 
    # store news items in a csv file 
    # savetoCSV(bill_items, 'bill_items.csv')
    print(readCSV("bill_items.csv"))
    datas = extractSponsors(readCSV("bill_items.csv"))
    for data in datas:
        print(data)
 


if __name__ == '__main__':
    main()

