import os
import ctypes
import subprocess
import xml.etree.cElementTree as ET

def executeNonQuery(cmd):
    _ =subprocess.getoutput(cmd)

def execute(cmd):
    binOut = subprocess.check_output(cmd, shell=True)
    strOut = ""
    try:
        strOut = binOut.decode("utf-8")
    except UnicodeDecodeError:
        strOut = binOut.decode("latin-1")
    return __cleanLinebreaks(strOut)

def executeAndGetLines(cmd):
    out = execute(cmd)
    strList = stripList(out.split("\n"))
    return removeEmpty(strList)

def removeEmpty(strList):
    return [x for x in strList if x != ""]

def stripList(strList):
    for idx, elem in enumerate(strList):
        strList[idx] = elem.strip()
    return strList

def __cleanLinebreaks(text):
    return text.replace("\r\n", "\n")

def xmlToDict(xmlFile):
    tree = ET.parse(xmlFile)
    treeRoot = tree.getroot()
    root = {}
    __rekXmlIterator(treeRoot, root)
    return root

def __rekXmlIterator(treeElement, inputStructure):
    for node in treeElement:
        tag = node.tag.split("}")[1]    
        if len(node) > 0:
            inputStructure[tag] = {}
            __rekXmlIterator(node, inputStructure[tag])
        else: inputStructure[tag] = node.text

def extractFirstElementfromDict(inputDict):
    return list(inputDict.keys())[0]

def isAdmin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

class NotAdminException(Exception):
    def __init__(self):
        super().__init__("The requested operation requires elevation (Run as administrator)")
