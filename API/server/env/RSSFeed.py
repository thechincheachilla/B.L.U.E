import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import json


class RSSFeedMain:
    
    def loadXML(url, filename, final_filename, singleOr100):
        # url of rss feed 
        response = requests.get(url) 
    
        # saving the xml file 
        with open(filename, 'wb') as file: 
            file.write(response.content) 
        if singleOr100 == '100':
            return parseXML(filename, final_filename)
        elif singleOr100 == 'single':
            return parseXMLSponsor(filename)



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



        
        for item in root.findall('./bill'):

            info = {'summaries' : [], 'sponsors' : [], 'cosponsors' : [], 'titles' : []}
    
            for child in item:
                if child.tag == 'summaries':
                    for item in root.findall('./bill/summaries/billSummaries/item/text'):
                        info['summaries'].append(item.text)
                elif child.tag == 'sponsors':
                    for item in root.findall('./bill/sponsors/item/fullName'):
                        info['sponsors'].append(item.text)
                elif child.tag == 'cosponsors':
                    for item in root.findall('./bill/cosponsors/item/fullName'):
                        info['cosponsors'].append(item.text)     
                elif child.tag == 'titles':
                    for item in root.findall('./bill/titles/item/title'):
                        info['titles'].append(item.text)

            bill_info.append(info)
        
        # list of dictionaries where the keys are the tags and values are lists
        return bill_info


    def savetoCSV(bill_items, filename): 
    
        # specifying the fields for csv file 
        fields = ['guid', 'title', 'pubDate', 'category', 'link', 'description']
    
<<<<<<< Updated upstream
    for item in root.findall('./bill'):

        info = {'summaries' : [], 'sponsors' : [], 'cosponsors' : [], 'titles' : []}
        for child in item:
            if child.tag == 'summaries':
                for item in root.findall('./bill/summaries/billSummaries/item/text'):
                    info['summaries'].append(item.text)
            elif child.tag == 'sponsors':
                for item in root.findall('./bill/sponsors/item/fullName'):
                    info['sponsors'].append(item.text)
            elif child.tag == 'cosponsors':
                for item in root.findall('./bill/cosponsors/item/fullName'):
                    info['cosponsors'].append(item.text)     
            elif child.tag == 'titles':
                for item in root.findall('./bill/titles/item/title'):
                    info['titles'].append(item.text)

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
    df['guid'] = df.apply(lambda x : x['guid'][11:], axis=1)
    return df['guid'].tolist()


def extractSponsors(csv):
    # csv is list of guid
    bills = {}
    for guid in csv:
        if "is" in guid or "ih" in guid or "es" in guid or "eh" in guid or "rh" in guid:
            guid = guid[:-3]
        elif "rfs" in guid:
            guid = guid[:-4]

        for i in range(len(guid)):
            #print("guid: " + guid + ", i: " + str(i))
            if guid[i].isdigit():
                pre = guid[0:i]
                break

        #print("pre: " + str(pre) + ", post: " + str(guid))

        url = 'https://www.govinfo.gov/bulkdata/BILLSTATUS/116/' + pre + '/BILLSTATUS-116' + guid + '.xml'
        #print(url)
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

def convertToJson(data, extendData):
    billsDict = {}
    billsDict[data] = extendData
    with open('bills.txt', 'w') as outfile:
        json.dump(data, outfile)



def main(): 
	# load rss from web to update existing xml file 
    loadXML('https://www.govinfo.gov/rss/bills.xml', "newest_bills.xml", "bill_items.csv", "100") 
    # parse xml file 
    # bill_items = parseXML('newest_bills.xml') 
    # store news items in a csv file 
    #savetoCSV(bill_items, 'bill_items.csv')
    print(readCSV("bill_items.csv"))
    datas = extractSponsors(readCSV("bill_items.csv"))
    for data in datas:
        extendData = datas[data]
        #print("data: " + data)
        #print("value: ", datas[data])''
        #print("sponsors: ", datas[data][0])
        #print("sponsors: ", datas[data][1])
        #print("sponsors: ", datas[data][2])
        convertToJson(data, extendData)
 


if __name__ == '__main__':
    main()
=======
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
        df['guid'] = df.apply(lambda x : x['guid'][11:], axis=1)
        return df['guid'].tolist()


    def extractSponsors(csv):
        # csv is list of guid
        bills = {}
        for guid in csv:
            if "is" in guid or "ih" in guid or "es" in guid or "eh" in guid or "rh" in guid:
                guid = guid[:-3]
            elif "rfs" in guid:
                guid = guid[:-4]

            for i in range(len(guid)):
                #print("guid: " + guid + ", i: " + str(i))
                if guid[i].isdigit():
                    pre = guid[0:i]
                    break

            #print("pre: " + str(pre) + ", post: " + str(guid))

            url = 'https://www.govinfo.gov/bulkdata/BILLSTATUS/116/' + pre + '/BILLSTATUS-116' + guid + '.xml'
            #print(url)
            bills[guid] = loadXML(url, "bill_sponsors.xml", "sponsor_names.csv", "single")
            return bills




    '''
    mapToBill takes in a dictionary (with bills as keys and sponsors as values)
    and reverses the key mapping pair so that we can get a dictionary of sponsors
    mapped to what they sponsored
    '''
    def mapToBill(bills):
        legislators = {}
        
        for bill, lists in bills.items():
            # lists is a dictionary of lists
            combinedList = lists['sponsors']  + lists['cosponsors']
            for sponsor in combinedList: # for every name in 'sponsors' list
                words = sponsor.split()
                words = words[1:-1]
                words.append(words.pop(0)[:-1])
                newName = ' '.join(words)
                for legislator in legislators:
                    if newName not in legislators:
                        legislators[newName] = [bill]
                    else:
                        legislators[newName].append(bill)

        return legislators

    def convertToJson(data, extendData):
        billsDict = {}
        billsDict[data] = extendData
        with open('bills.txt', 'w') as outfile:
            json.dump(data, outfile)



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
            extendData = datas[data]
            #print("data: " + data)
            #print("value: ", datas[data])''
            #print("sponsors: ", datas[data][0])
            #print("sponsors: ", datas[data][1])
            #print("sponsors: ", datas[data][2])
            convertToJson(data, extendData)
    


    if __name__ == '__main__':
        main()
>>>>>>> Stashed changes

