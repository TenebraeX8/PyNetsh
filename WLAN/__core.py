import os
import subprocess

def executeNonQuery(cmd):
    os.system(cmd)

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