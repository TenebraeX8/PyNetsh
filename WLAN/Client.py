import sys
import json
from __core import executeAndGetLines
from __core import executeNonQuery


#----------------------------------------------------------------------
#List Profiles

def listProfiles():
    out = executeAndGetLines("netsh wlan show profile")
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
#disconnect
def disconnect():
    executeNonQuery("netsh wlan disconnect")

#-----------------------------------------------------------------------
#connect
def connectTo(strProfile):
    executeNonQuery("netch wlan connect " + strProfile)
