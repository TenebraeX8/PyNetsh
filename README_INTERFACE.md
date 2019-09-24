# PyNetsh.Interface
This library provides functions for the computers interfaces
```
from PyNetsh.Interface import *
```

## Functions
* def enableInterface(strInterface, setEnabled=True):\
    enables or disables specified interface\
    __strInterface:__ a string with the profile's name\
    __setEnabled:__ _[Optional]_ if true, sets the interface administrative state enabled\
    __returns__ nothing

* getInterfacesJSON():\
    reads the current status of the interfaces on the computer\
    __returns__ a JSON-string containing the interfaces

* def getInterfacesList():\
    reads the current status of the interfaces on the computer\
    __returns__ a list of strings containing the interfaces

* def Teredo_showState():\
    reads the state of the Teredo-Client\
    __returns__ a JSON-string containing the state of the Teredo Client\


* def Teredo_configScript():\
    gets the configuration script of the Teredo Client\
    returns a string