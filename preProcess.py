import json
import time, datetime
import csv
##################################################
# data class to hold csv data
##################################################
class data():
    def __init__(self, classifier):
        self.examples = []
        self.attributes = []
        self.attr_types = []
        self.classifier = classifier
        self.class_index = None

class dataForAnalysis():
    def __init__(self):
        # so uglyyyyyyyy!!!! need to convert to arr 
        self.P1 = []
        self.P2 = []
        self.P3 = []
        self.P4 = []
        self.P5 = []
        self.P6 = []
        self.P7 = []
        self.P8 = []
        self.P9 = []

class fnirData():
    def __init__(self):
        # so uglyyyyyyyy!!!! need to convert to arr 
        self.G1 = []
        self.G2 = []
        self.G3 = []
        self.G4 = []
        self.G5 = []
        self.G6 = []
        self.G7 = []
        self.G8 = []
        self.G9 = []
        self.G10 = []
        self.G11 = []
        self.G12 = []
        self.G13 = []
        self.G14 = []
        self.G15 = []
        self.G16 = []
        self.G17 = []
        self.G18 = []

class channelData():
    def __init__(self):
        self.unixTime = None
        self.value = None
        self.label= None

class patternGroup():
    def __init__(self):
        self.start = None
        self.end = None
        self.label = None

##################################################
# read data from text
##################################################
def read_data(dataset, datafile,fdata):
    #"Opening input file"
    file_name = datafile
	#"Reading input file"
    doc = open(file_name).read()
	#"Read by line"
    rowsplit_data=doc.splitlines()
    print('The time of data: ',rowsplit_data[0])
    newtime, duration = readFnirsTime(rowsplit_data[0])
    addDatetoTime(newtime,'2018-12-04',duration)
    print('standard time:', newtime)
    print('duration:', duration)
    print('The num of total rows: ',len(rowsplit_data))

	#"read data "
    dataset.examples = [rows.split() for rows in rowsplit_data[2:]]
    print('The length of attributes: ',len(dataset.examples[0]))

    #list attributes
    for rows in dataset.examples:
        try:
            fdata.G1.append(rows[0]) 
            fdata.G2.append(rows[1]) 
            fdata.G3.append(rows[2]) 
            fdata.G4.append(rows[3]) 
            fdata.G5.append(rows[4]) 
            fdata.G6.append(rows[5]) 
            fdata.G7.append(rows[6]) 
            fdata.G8.append(rows[7]) 
            fdata.G9.append(rows[8])
            fdata.G10.append(rows[9]) 
            fdata.G11.append(rows[10]) 
            fdata.G12.append(rows[11]) 
            fdata.G13.append(rows[12]) 
            fdata.G14.append(rows[13]) 
            fdata.G15.append(rows[14]) 
            fdata.G16.append(rows[15]) 
            fdata.G17.append(rows[16]) 
            fdata.G18.append(rows[17])  
        except:
            continue

    #PORT = [rows[1] for rows in dataset.examples]
    print("the length of every group",len(fdata.G1),len(fdata.G2),len(fdata.G3),len(fdata.G4),
    len(fdata.G5),len(fdata.G6),len(fdata.G7),len(fdata.G8),len(fdata.G9),len(fdata.G10),
    len(fdata.G11),len(fdata.G12),len(fdata.G13),len(fdata.G14),len(fdata.G15),len(fdata.G16),
    len(fdata.G17),len(fdata.G18))
    return fdata

##################################################
# read data from json
##################################################
def read_jsonData(datafile):
    #"Opening input file"
    file_name = datafile
	#"Reading input file"
    doc = open(file_name,encoding='utf-8')
	#"Read by json"
    stbData =  json.load(doc)
    patternGroups = getPatternGroupTime(stbData)
    
    stStartTimeUnix = jsonToUnix(stbData['data'][0]['startTime'])
    print("sternburg start time ",stbData['data'][0]['startTime'],stStartTimeUnix)
    #newTime = newTime.replace('Z','')
    #newTime = cleanTimeData(stbData['data'][0]['startTime'])
    #print(rowsplit_data[0])
    #print('The num of total rows: ',len(rowsplit_data[0]))
    return stbData,patternGroups

##################################################
# get info from  json
##################################################  
def calculatePatternTime(start,end,jsonData,group):
    startTime = jsonData['data'][start]['startTime']
    endTime = jsonData['data'][end]['endTime']

    startTimeUnix = jsonToUnix(startTime)
    endTimeUnix = jsonToUnix(endTime)

    patternTime = patternGroup()
    patternTime.start = startTimeUnix
    patternTime.end = endTimeUnix
    patternTime.label = group
    # debug 
    #print('debug json info',patternTime.start,patternTime.end,patternTime.label)
    return patternTime
    

def getPatternGroupTime(jsonData):
    groupArr =[]
    groupArr.append(calculatePatternTime(0,20,jsonData,2))
    groupArr.append(calculatePatternTime(21,22,jsonData,1))
    groupArr.append(calculatePatternTime(23,44,jsonData,3))
    groupArr.append(calculatePatternTime(45,73,jsonData,4))
    groupArr.append(calculatePatternTime(74,98,jsonData,5))
    groupArr.append(calculatePatternTime(99,118,jsonData,6))
    groupArr.append(calculatePatternTime(119,126,jsonData,7))
    groupArr.append(calculatePatternTime(127,152,jsonData,8))
    # debug 
    print('debug gropArr info',groupArr[0].start,groupArr[0].end,groupArr[0].label)
    return groupArr

def getKeyDownTime(jsonData):
    arr = []
    wholeData = jsonData['data']
    for data in wholeData:
        curData = jsonToUnix(data['endTime'])
        arr.append(curData)
        #print('debug keydown data ',curData)
    return arr




##################################################
# standard  time
##################################################
def jsonToUnix(time):
    newTime = cleanTimeData(time)
    unixTime = timeStandards(newTime)
    return unixTime

def cleanTimeData(time):
    newTime = time.replace('T',' ')
    newTime = newTime.replace('Z','')
    return newTime

def timeStandards(preTime):
    timeArray = time.strptime(preTime, "%Y-%m-%d %H:%M:%S.%f")
    timeStamp = int(time.mktime(timeArray))
    #print('Json timeStamp: ',timeStamp,preTime)
    return timeStamp
    
##################################################
# read fnirs timeData  7.8125hz 10000/78125=
##################################################
def readFnirsTime(time):
    #newtime = time[6:18]
    parts = time.split("\"")
    newtime = parts[1]
    parts = time.split(" + ")
    duration = parts[1]
    duration = duration.replace('s','')
    duration = float(duration)
    return newtime, duration 

def addDatetoTime(preTime,data,duration):
    timeStr = data+" "+preTime
    timeArray = time.strptime(timeStr,"%Y-%m-%d %H:%M:%S.%f")
    timeStamp = int(time.mktime(timeArray))
    #print('Fnirs start time texas: ',timeStamp,timeStr)
    timeStamp = timeStamp + 6*60*60 # texas time from Greenich
    #print('Fnirs start time timeStamp: ',timeStamp,datetime.datetime.fromtimestamp(timeStamp))
    timeStamp = timeStamp + duration
    print('sternmburg start（Fnirs） time timeStamp: ',timeStamp,datetime.datetime.fromtimestamp(timeStamp))
    return timeStamp

##################################################
# calculate time stamp
##################################################
def addTimetoPerfdata(perData,initTime,index,label):
    index = index+1
    base = float(1/7.8125)
    container = channelData()
    container.unixTime = initTime + index * base
    container.value = perData
    container.label = label
    # print('debug addtime ',perData,container.unixTime,index)
    return container

def transferRawToTimeseries(startUnixTime,fdata,patternGroup):
    tsArr = fnirData()
    # print('debug raw data',fdata.G1,seconds_perline,startUnixTime)
    len_fdata = len(fdata.G1)
    for i in range(0,len_fdata):
        unixTime = addTimetoPerfdata(fdata.G1[i],startUnixTime,i,0).unixTime
        labelFlag,labelIndex = classifyFdata(patternGroup,unixTime)
        if(labelFlag):
            tsArr.G1.append(addTimetoPerfdata(fdata.G1[i],startUnixTime,i,labelIndex))
            tsArr.G2.append(addTimetoPerfdata(fdata.G2[i],startUnixTime,i,labelIndex))
            tsArr.G3.append(addTimetoPerfdata(fdata.G3[i],startUnixTime,i,labelIndex))
            tsArr.G4.append(addTimetoPerfdata(fdata.G4[i],startUnixTime,i,labelIndex))
            tsArr.G5.append(addTimetoPerfdata(fdata.G5[i],startUnixTime,i,labelIndex))
            tsArr.G6.append(addTimetoPerfdata(fdata.G6[i],startUnixTime,i,labelIndex))
            tsArr.G7.append(addTimetoPerfdata(fdata.G7[i],startUnixTime,i,labelIndex))
            tsArr.G8.append(addTimetoPerfdata(fdata.G8[i],startUnixTime,i,labelIndex))
            tsArr.G9.append(addTimetoPerfdata(fdata.G9[i],startUnixTime,i,labelIndex))
            tsArr.G10.append(addTimetoPerfdata(fdata.G10[i],startUnixTime,i,labelIndex))
            tsArr.G11.append(addTimetoPerfdata(fdata.G11[i],startUnixTime,i,labelIndex))
            tsArr.G12.append(addTimetoPerfdata(fdata.G12[i],startUnixTime,i,labelIndex))
            tsArr.G13.append(addTimetoPerfdata(fdata.G13[i],startUnixTime,i,labelIndex))
            tsArr.G14.append(addTimetoPerfdata(fdata.G14[i],startUnixTime,i,labelIndex))
            tsArr.G15.append(addTimetoPerfdata(fdata.G15[i],startUnixTime,i,labelIndex))
            tsArr.G16.append(addTimetoPerfdata(fdata.G16[i],startUnixTime,i,labelIndex))
            tsArr.G17.append(addTimetoPerfdata(fdata.G17[i],startUnixTime,i,labelIndex))
            tsArr.G18.append(addTimetoPerfdata(fdata.G18[i],startUnixTime,i,labelIndex))

    return tsArr
    
##################################################
# assign fnirsData to pattern groups
##################################################
def classifyFdata(Pgroup,currentTime):
    for group in Pgroup: # could be improved
        if(currentTime <= float(group.end) and currentTime >= float(group.start)):
            print('debug classfy method ',currentTime,group.label)
            return True,group.label    
    return False ,group.label    



def writeCVS(data):
    out = open('P3.csv','a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    lenData = len(data.G1)

    for i in range(0,lenData):
        currentData = []
        # print("debug write cvs ",data.G1[i].label,data.G1[i].unixTime,
        # data.G1[i].value,data.G2[i].value,data.G3[i].value,data.G4[i].value,data.G5[i].value,
        # data.G6[i].value,data.G7[i].value,data.G8[i].value,data.G9[i].value,data.G10[i].value,
        # data.G11[i].value,data.G12[i].value,data.G13[i].value,data.G14[i].value,data.G5[i].value,
        # data.G16[i].value,data.G17[i].value,data.G18[i].value)
        currentData.append(data.G1[i].label)
        currentData.append(data.G1[i].unixTime)
        currentData.append(data.G1[i].value)
        currentData.append(data.G2[i].value)
        currentData.append(data.G3[i].value)
        currentData.append(data.G4[i].value)
        currentData.append(data.G5[i].value)
        currentData.append(data.G6[i].value)
        currentData.append(data.G7[i].value)
        currentData.append(data.G8[i].value)
        currentData.append(data.G9[i].value)
        currentData.append(data.G10[i].value)
        currentData.append(data.G11[i].value)
        currentData.append(data.G12[i].value)
        currentData.append(data.G13[i].value)
        currentData.append(data.G14[i].value)
        currentData.append(data.G15[i].value)
        currentData.append(data.G16[i].value)
        currentData.append(data.G17[i].value)
        currentData.append(data.G18[i].value)
        csv_write.writerow(currentData)
    print ("write over")


def writeKewdownData(data):
    out = open('P8_keydown.csv','a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    csv_write.writerow(data)
    print ("write key over")



def main():
    fdata = fnirData() 
    fdata = read_data(data,'./data/P3_NIRS-2018-11-28_002_oxyhb_T1to9961_C1to18.txt',fdata)
    jsonData,patternGroup = read_jsonData('./jsondata/1204_sam_8.json')
    startTime = cleanTimeData(jsonData['data'][0]['startTime'])
    startTime = timeStandards(startTime)

    # wriring final dataste to cvs 
    # processedFdata = transferRawToTimeseries(startTime,fdata,patternGroup)
    # print("debug final dataset", len(processedFdata.G1),processedFdata.G1[100].label)
    # writeCVS(processedFdata)

    # wrting keydown data
    keydownData = getKeyDownTime(jsonData)
    writeKewdownData(keydownData)
    
    # debugggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
    # print(processedFdata.G18[17].unixTime,processedFdata.G18[17].value,processedFdata.G18[17].label)
    # print(processedFdata.G17[17].unixTime,processedFdata.G17[17].value)
    # print(processedFdata.G16[17].unixTime,processedFdata.G16[17].value)
    # print(processedFdata.G15[17].unixTime,processedFdata.G15[17].value)
    # print(processedFdata.G14[17].unixTime,processedFdata.G14[17].value)
    # print(processedFdata.G13[17].unixTime,processedFdata.G13[17].value)
    # print(processedFdata.G12[17].unixTime,processedFdata.G12[17].value)
    # print(processedFdata.G11[17].unixTime,processedFdata.G11[17].value)
    # print(processedFdata.G10[17].unixTime,processedFdata.G10[17].value)
    # print(processedFdata.G9[17].unixTime,processedFdata.G9[17].value)
    # print(processedFdata.G8[17].unixTime,processedFdata.G8[17].value)
    # print(processedFdata.G7[17].unixTime,processedFdata.G7[17].value)
    
    


if __name__ == "__main__":
	main()