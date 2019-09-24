import os
import sys
sys.path.append(os.path.dirname(__file__))
import json
from __core import execute, executeAndGetLines, executeNonQuery
from __core import extractFirstElementfromDict
from __core import stripList, removeEmpty
from __core import isAdmin, NotAdminException

#----------------------------------------------------------------------
#List Interfaces

def getInterfacesJSON():
    '''
    returns a JSON-string with the interfaces-profiles and their current status
    '''
    output = executeAndGetLines("netsh interface show interface")
    return __buildProfileStructure(output)

def getInterfacesList():
    '''
    returns a list of strings with the names of the available interfaces    
    '''
    return __getInterfacesJSONToList(getInterfacesJSON())


def __buildProfileStructure(lines):
    outStructure = []
    if len(lines) > 1:
        Headings = __splitByBlanks(lines[0])
        lines = lines[1:]
        if lines[0].find("---------")>=0: lines = lines[1:]
        if len(lines) > 1:
            for line in lines:
                Data = __splitByBlanks(line)
                if len(Headings) == len(Data):
                    curStructure = {}
                    for x in range(len(Headings)):
                        curStructure[Headings[x]] = Data[x]
                    outStructure.append(curStructure)
    return json.dumps(outStructure)


def __getInterfacesJSONToList(getInterfacesOutput):
    curStructure = json.loads(getInterfacesOutput)
    interfaceList =[]            
    for elem in curStructure: 
        interfaceList.append(elem["Interface Name"])
    return interfaceList

#----------------------------------------------------------------------
#Enable Interfaces

def enableInterface(strInterface, setEnabled=True):
    '''
    enables or disables specified interface
    '''
    if not isAdmin(): raise NotAdminException()
    else : 
        strEnabled = "ENABLED" if setEnabled else "DISABLED"
        strCmd = 'netsh interface set interface name="' + strInterface + '" admin=' + strEnabled
        executeNonQuery(strCmd)


#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section IPv6to4
def IPv6to4_configScript():
    '''
    returns a string containing the configuration of the IPv6to4
    '''
    return __abstractConfigScript("6to4")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section Httpstunnel
def httpstunnel_configScript():
    '''
    returns a string containing the configuration of the Httpstunnel
    '''
    return __abstractConfigScript("httpstunnel")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section IPv4
def IPv4_configScript():
    '''
    returns a string containing the configuration of the IPv4
    '''
    return __abstractConfigScript("ipv4")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section IPv6
def IPv6_configScript():
    '''
    returns a string containing the configuration of the IPv6
    '''
    return __abstractConfigScript("ipv6")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section Portproxy
def portproxy_configScript():
    '''
    returns a string containing the configuration of the portproxy
    '''
    return __abstractConfigScript("portproxy")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section tcp
def tcp_configScript():
    '''
    returns a string containing the configuration of the tcp protocol
    '''
    return __abstractConfigScript("tcp")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section Isatap
def isatap_configScript():
    '''
    returns a string containing the configuration of the isatap
    '''
    return __abstractConfigScript("isatap")

#----------------------------------------------------------------------
#----------------------------------------------------------------------
#Section Teredo
def Teredo_showState():
    '''
    returns a JSON-string with the state of the Teredo Client
    '''
    output = executeAndGetLines("netsh interface teredo show state")
    outStructure = {}
    for line in output:
        key, value = __getValuePairFromLine(line)
        if key != None and value != None:
            outStructure[key] = value
    return json.dumps(outStructure)

def Teredo_configScript():
    '''
    returns a string containing the configuration of the Teredo Client
    '''
    return __abstractConfigScript("teredo")


#----------------------------------------------------------------------
#----------------------------------------------------------------------
def __abstractConfigScript(strModule):
    return execute("netsh interface " + strModule + " dump").strip()

#----------------------------------------------------------------------
def __splitByBlanks(strLine, blankCount = 3):
    blanks = ""
    for _ in range(blankCount): blanks += " "
    splitter = strLine.split(blanks)
    return removeEmpty(stripList(splitter))
    
#----------------------------------------------------------------------
def __getValuePairFromLine(strLine):
    splitter = strLine.split(":")
    if len(splitter) == 2:
        return splitter[0].strip(), splitter[1].strip()
    else: return None, None