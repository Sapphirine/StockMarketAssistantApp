import urllib2
import time
import datetime

stocksToPull = 'AAPL','GOOG','MSFT','AMZN','EBAY','TSLA'

def pullData(stock):
    try:
        print 'Currently pulling',stock
        print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
        fileLine = stock+'.txt'
        
        try:
            readExistingData = open(fileLine,'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]  #the second last line(the last line is emepty)
            lastUnix = mostRecentLine.split(',')[0]          
        except:
            lastUnix = 0    #if the file doesn't exist
            
        saveFile = open(fileLine,'a')
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')
        
        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine) == 6:
                    
                    if int(splitLine[0]) > int(lastUnix):
                        lineToWrite = eachLine+'\n'
                        saveFile.write(lineToWrite)
                        
        saveFile.close()
                        
        print 'Pulled',stock
        print 'sleeping...'
        time.sleep(1)
            
        
        
    except Exception,e:
        print 'main loop',str(e)
        

while True:
    for stock in stocksToPull:
        pullData(stock)
    time.sleep(10)

    



 
