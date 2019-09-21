import os
import sys
sys.path.append(os.path.dirname(__file__))
import json
from __core import execute
from __core import executeAndGetLines
from __core import executeNonQuery
from __core import xmlToDict
from __core import extractFirstElementfromDict

#----------------------------------------------------------------------
#List Profiles

def getProfilesJSON():
    '''
    returns a JSON-string with the wlan-profiles saved on this computer
    '''
    out = executeAndGetLines("netsh wlan show profiles")
    OutStructure = __buildProfileStructure(out)
    return OutStructure

def getProfilesList():
    '''
    returns a list of strings with the wlan-profiles saved on this computer    
    '''
    return __getProfilesJSONToList(getProfilesJSON())

def __buildProfileStructure(lines):
    Heading = lines[0]
    lines = lines[1:]
    Structure = {}
    while len(lines) > 0:
        if lines[1].startswith("-----"):
            Structure[lines[0]] = []
            cnt = 2
            while cnt < len(lines) and not lines[cnt].startswith("-----") :
                strLine = lines[cnt]
                if strLine.find(":") >= 0: _, strLine = __getValuePairFromLine(strLine)
                Structure[lines[0]].append(strLine)
                cnt+=1
            if cnt != len(lines):
                Structure[lines[0]] = Structure[lines[0]][:-1]
                cnt -=1
            lines = lines[cnt:]
    return json.dumps({Heading:Structure})

def __getProfilesJSONToList(getProfilesOutput):
    '''
    Converts the JSON Output of "getProfiles()" to a list
    '''
    getProfilesOutput = json.loads(getProfilesOutput)
    firstKey = extractFirstElementfromDict(getProfilesOutput)
    curStruct = getProfilesOutput[firstKey]
    profileList = []
    for key in curStruct:
        for elem in curStruct[key]:
            if elem != "<None>" and elem != "<Kein>":
                profileList.append(elem)
    return profileList


#----------------------------------------------------------------------
#profile config
def getProfileConfigurations():
    '''
    returns a list of JSON-encoded strings containing the advanced data of each profile on this computer
    '''
    return __abstr_getProfileConfig(profiles = getProfilesList())

def getProfileConfiguration(strProfile):
    '''
    returns a JSON-encoded string containing the advanced data of the specified Profile
    '''
    return __abstr_getProfileConfig(profiles=[strProfile])[0]

def __abstr_getProfileConfig(profiles):
    if not os.path.exists("./tmp/") : os.mkdir("./tmp/")
    for profile in profiles:
        exportProfile(profile, "./tmp/")    
    files = os.listdir("./tmp/")
    files = [x for x in files if x.endswith(".xml")]
    profiles = []
    for f in files:
        try:
            Structure = xmlToDict("./tmp/" + f)
            profiles.append(json.dumps(Structure))
            os.remove("./tmp/" + f)
        except IOError:
            pass
    os.rmdir("./tmp/")
    return profiles

#----------------------------------------------------------------------
#disconnect
def disconnect():
    '''
    shuts down the WLAN-Connection
    '''
    executeNonQuery("netsh wlan disconnect")

#-----------------------------------------------------------------------
#connect
def connectTo(strProfile):
    '''
    tries to establish a WLAN-Connection to the specified Profile
    '''
    executeNonQuery("netsh wlan connect " + strProfile)

#------------------------------------------------------------------------
#available profiles
def getAvilableNetworksJSON():
    '''
    returns an JSON-encoded list of Strings containing information of available Networks
    '''
    output = executeAndGetLines("netsh wlan show networks")
    Wifis = []
    output = output[1:]         #Skip interface name
    while output[0].find(":") < 0: output = output[1:]
    while len(output) >= 4:
        key, name = __getValuePairFromLine(output[0])
        if key != None:
            Structure = {key:{}}
            Structure[key]["name"] = name
            for x in range(1,4):
                attr, value = __getValuePairFromLine(output[x])
                Structure[key][attr] = value
            Wifis.append(json.dumps(Structure))
        output = output[4:]
    return Wifis

def getAvilableNetworksList():
    return __getAvailableNetworkJSONToList(getAvilableNetworksJSON())

def __getAvailableNetworkJSONToList(getProfilesOutput):
    ProfileList = []
    for jsonString in getProfilesOutput:
        ssid = json.loads(jsonString)    
        firstKey = extractFirstElementfromDict(ssid)
        ssid = ssid[firstKey]
        ProfileList.append(ssid["name"])
    return ProfileList

#------------------------------------------------------------------------
#Connection mode
def setConnectionMode(strProfile, setToAuto=True):
    '''
    updates the connection mode of the specified profile
    '''
    strMode = "auto" if setToAuto else "manual"
    strCmd = 'netsh wlan set profileparameter name="' + strProfile + '" connectionmode=' + strMode
    executeNonQuery(strCmd)

#------------------------------------------------------------------------
#profiles
def deleteProfile(strProfile):
    '''
    CAREFULL!!!! This function permanently deletes a profile
    '''
    strCmd = 'netsh wlan delete profile name="' + strProfile + '"'
    executeNonQuery(strCmd)

def exportProfile(strProfile, strPath, clearKey=True):
    '''
    exports a profile to a xml-file
    '''
    strKey = "key=clear " if clearKey else ""
    strCorrPath = os.path.normpath(strPath)
    strCmd = 'netsh wlan export profile name="' + strProfile + '" ' + strKey + 'folder="' + strCorrPath + '"'
    executeNonQuery(strCmd)

def addProfile(strPath):
    '''
    adds a profile to the saved configurations. Configuration has to be an exported .xml file
    '''
    strCorrPath = os.path.normpath(strPath)
    strCmd = 'netsh wlan add profile filename="' + strCorrPath + '"'
    executeNonQuery(strCmd)

#------------------------------------------------------------------------
#profiles
def getDriverReport():
    '''
    returns a string with all information available for drivers
    '''
    return execute("netsh wlan show drivers")


#------------------------------------------------------------------------
def __getValuePairFromLine(strLine):
    splitter = strLine.split(":")
    if len(splitter) == 2:
        return splitter[0].strip(), splitter[1].strip()
    else: return None, None