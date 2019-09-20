import os
import subprocess
import xml.etree.cElementTree as ET

def executeNonQuery(cmd):
    _ =subprocess.getoutput(cmd)

def execute(cmd):
    return __cleanLinebreaks(subprocess.check_output(cmd, shell=True).decode("utf-8"))

def executeAndGetLines(cmd):
    out = execute(cmd)
    strList = stripList(__cleanLinebreaks(out).split("\n"))
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

