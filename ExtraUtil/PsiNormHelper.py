# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:25:20 2018

@author: Cheese
"""

"""
item1 = resultNameToDict()
item2 = funcTempToJSON()
item3 = funcDictToJSON()
"""




def settings(debug):
    return True


def checkGuiInput(userInput, inputType):
    import re
    if inputType == "str":
        if re.match("^[0-9a-zA-Z\-\_\(\)ığĞüÜşŞİöÖçÇ ]+$", userInput):
            return True
        else:
            return False
        
    if inputType == "flo":
        try:
            userInput = float(userInput)
            return True
        except:
            return False
    
    if inputType == "int":
        try:
            userInput = int(userInput)
            return True
        except:
            return False

def criticalError(errorTitle, errorMessage, shouldIBeep):
    """
    errorTitle = Title of the popup, string, if None, prints a console message instead.
    errorMessage = string
    shouldIbeep = Should it make a beep sound, boolean
    """
    
    if shouldIBeep:
        import winsound
        try:
            winsound.Beep(440, 50)
        except:
            pass
    
    if errorTitle:
        guiSimplePopup(errorTitle, errorMessage)
        
    else:
        print(errorMessage)

def stroopFixer():
    result_list = []
    for i in range(15):
        result_list.append(i)
        
    mean_list = [10.09, result_list[1]-999, result_list[2]-999,
                 11.63, result_list[4]-999, result_list[5]-999,
                 15.93, result_list[7]-999, result_list[8]-999,
                 24.87, result_list[10]-999, result_list[11]-999,
                 35.96, result_list[13]-999, result_list[14]-999]

    sd_list = [3.71, 1, 1,
               5.41, 1, 1,
               4.06, 1, 1,
               10.94, 1, 1,
               16.23, 1, 1]
    new_mean_list = []
    new_sd_list = []
    
    for i in [0, 3, 6, 9, 12]:
        new_mean_list.append(mean_list[i])
        for a in range(2):
            new_mean_list.append(None)
        
        new_sd_list.append(sd_list[i])
        for a in range(2):
            new_sd_list.append(None)
    
    print("mean_list = ")    
    print(new_mean_list)
    
    print("sd_list = ")
    print(new_sd_list)
    
#stroopFixer()

def resultNameToDict():
    """
    Removes empty space and escapes from result names
    """
    result_name = ["\nSayı dizisi toplam: ", "\nSayı dizisi ileri: ", "\nSayı dizisi geri: "]    
           
    
    for i in range(len(result_name)):
        print("\"" + str(i) + "\": \"" + result_name[i].strip() + " \",")

def funcTempToJSON():
    """
#    testMmtDataDict = testMmtDataDict.json
#    testMocaDataDict = testMocaDataDict.json
#    test3msDataDict = test3msDataDict.json
#    testGisdDataDict = testGisdDataDict.json
#    testEcrDataDict = testEcrDataDict.json
#    testSbstDataDict = testSbstDataDict.json
#    testRkftDataDict = testRkftDataDict.json
#    testTmDataDict = testTmDataDict.json
#    testStroopDataDict = testStroopDataDict.json
#    testWisconsinDataDict = testWisconsinDataDict.json
#    testVvtDataDict = testVvtDataDict.json
#    testCct1DataDict = testCct1DataDict.json
#    testCct2DataDict = testCct2DataDict.json
    testWechslerDataDict = testWechslerDataDict.json
    testWechslerSayiDataDict = testWechslerSayiDataDict.json
#    testVfDataDict = testVfDataDict.json
#    testSfDataDict = testSfDataDict.json
#    testCdDataDict = testCdDataDict.json
#    testSdotDataDict = testSdotDataDict.json
#    testMonthsDataDict = testMonthsDataDict.json
#    testVaNVCDataDict = testVaNVCDataDict.json
#    testBNTDataDict = testBNTDataDict.json
    """
    
    tempdataDict = {
    "testName": "Wechsler zeka testi - Sadece Sayılar",
	
    "paraNum": 3,
	
    "0": "Sayı dizisi toplam: ",
    "1": "Sayı dizisi ileri: ",
    "2": "Sayı dizisi geri: ",
            
    "zScoreLegend": {"all":"more"},
	
	"testType": "cutOff",
	
	"cutOffList": [
		{
			"sex": "Male",
			"eduLow": 0,
			"eduHigh": 4,
			"ageLow": 0,
			"ageHigh": 200,
			"0": {
				"parameterNormExists": True,
				"cutOffGroupCutoffList": [17, 19],
				"cutOffGroupNameList": ["Eşik altı değer", "Sınır değer", "Normal"]
				}
			},
		{
			"sex": "Male",
			"eduLow": 5,
			"eduHigh": 200,
			"ageLow": 0,
			"ageHigh": 200,
			"0": {
				"parameterNormExists": True,
				"cutOffGroupCutoffList": [21, 23],
				"cutOffGroupNameList": ["Eşik altı değer", "Sınır değer", "Normal"]
				}
			}
		],
	
    "normList": []
}
    
    jsonDumper('testWechslerSayiDataDict.json', tempdataDict)
    
    
def dictMaker(paraNum, sex, eduLow, eduHigh, ageLow, ageHigh, mean_list, sd_list):
    
    JSONable ={
            "sex": sex,
            "eduLow": eduLow,
            "eduHigh": eduHigh,
            "ageLow": ageLow,
            "ageHigh": ageHigh            
            }
    
    for i in range(paraNum):
        JSONable[str(i)] =  [mean_list[i], sd_list[i]]
        
        
    return JSONable
    
def jsonLoader(jsonFileName):
    import json
    with open(jsonFileName, 'r', encoding="utf8") as fp:
        mainDict = json.load(fp)

    return mainDict


def jsonDumper(jsonName, dataDict):
    #jsonName= 'test3msDataDict.json'
    import json
    with open(jsonName, 'w', encoding='utf8') as fp:
        json.dump(dataDict, fp, sort_keys=False, indent=4, ensure_ascii=False)
        

def funcDictToJSON(JSONToLoad):
    z = 0.00000001 #Equivalent of 0
    
    f = "Female"
    m = "Male"        
    
    paraNum = jsonLoader(JSONToLoad)["paraNum"]
    
    """

   """

    sex = m
    eduLow = 13
    eduHigh = 100
    ageLow = 65
    ageHigh = 200
    
    mean_list = [19.35, 39.65]
    sd_list = [2.50, 5.24]
    
    doubleTrouble = True #If both male and female norms are same, iterate twice
    
    if doubleTrouble:
        for sex in [f, m]:
            toAppend = dictMaker(paraNum, sex, eduLow, eduHigh, ageLow, ageHigh, mean_list, sd_list)
            
            for key, entry in toAppend.items():
                print(key, entry)
            
            loadedJSON = jsonLoader(JSONToLoad)
            
            normList = loadedJSON["normList"]
            
            normList.append(toAppend)
            
            loadedJSON["normList"] = normList
            
            jsonDumper(JSONToLoad, loadedJSON)
    else:
        toAppend = dictMaker(paraNum, sex, eduLow, eduHigh, ageLow, ageHigh, mean_list, sd_list)
            
        for key, entry in toAppend.items():
            print(key, entry)
        
        loadedJSON = jsonLoader(JSONToLoad)
        
        normList = loadedJSON["normList"]
        
        normList.append(toAppend)
        
        loadedJSON["normList"] = normList
        
        jsonDumper(JSONToLoad, loadedJSON)
        


#resultNameToDict()
#funcTempToJSON()

funcDictToJSON('testBentonFaceDataDict.json')
