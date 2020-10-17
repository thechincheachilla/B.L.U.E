import requests 
import xml.etree.ElementTree as ET 
  
def loadRSS(): 
  
    # url of rss feed 
    url = 'https://www.govinfo.gov/rss/bills.xml'
  
    # creating HTTP response object from given url 
    resp = requests.get(url) 
  
    # saving the xml file 
    with open('topnewsfeed.xml', 'wb') as f: 
        f.write(resp.content) 