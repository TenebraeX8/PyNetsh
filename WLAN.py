import os
import sys
sys.path.append(os.path.dirname(__file__))
import json
from __core import executeAndGetLines
from __core import executeNonQuery
from __core import xmlToDict

#----------------------------------------------------------------------
#List Profiles

def listProfiles():
    '''
    returns a stringlist with the wlan-profiles saved on this computer
    '''
    out = executeAndGetLines("netsh wlan show profiles")
    OutStructure = __buildProfileStructure(out)
    print(OutStructure)
    return out

def __buildProfileStructure(lines):
    Heading = lines[0]
    lines = lines[1:]
    Structure = {}
    while len(lines) > 0:
        if lines[1].startswith("-----"):
            Structure[lines[0]] = []
            cnt = 2
            while cnt < len(lines) and not lines[cnt].startswith("-----") :
                Structure[lines[0]].append(lines[cnt])
                cnt+=1
            if cnt != len(lines):
                Structure[lines[0]] = Structure[lines[0]][:-1]
                cnt -=1
            lines = lines[cnt:]
    return json.dumps({Heading:Structure})

#----------------------------------------------------------------------
#profile config
def getProfileConfigurations():
    '''
    returns a list of JSON-encoded strings containing the advanced data of each profile on this computer
    '''
    executeNonQuery("netsh wlan export profile")
    files = os.listdir(".")
    files = [x for x in files if x.endswith(".xml")]
    profiles = []
    for f in files:
        try:
            Structure = xmlToDict("./" + f)
            profiles.append(json.dumps(Structure))
            os.remove("./" + f)
        except IOError:
            pass
    return profiles

def getProfileConfiguration(strProfile):
    '''
    returns a JSON-encoded string containing the advanced data of the specified Profile
    '''
    executeNonQuery("netsh wlan export profile " + strProfile)
    files = os.listdir(".")
    files = [x for x in files if x.endswith(".xml")]
    profiles = []
    for f in files:
        try:
            Structure = xmlToDict("./" + f)
            profiles.append(json.dumps(Structure))
            os.remove("./" + f)
        except IOError:
            pass
    return profiles[0]

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
    executeNonQuery("netch wlan connect " + strProfile)

#------------------------------------------------------------------------
#available profiles
def getAvilableNetworks():
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


def __getValuePairFromLine(strLine):
    splitter = strLine.split(":")
    if len(splitter) == 2:
        return splitter[0].strip(), splitter[1].strip()
    else: return None, None
