# PyNetsh.WLAN
This library provides functions for the computers wifi
```
from PyNetsh.WLAN import *
```

## Functions
* addProfile(strPath):\
    adds a profile to the saved configurations. Configuration has to be an exported .xml file\
    __strPath:__ the path to the config-file (*.xml)\
    __returns__ nothing

* connectTo(strProfile)\
  tries to establish a WLAN-Connection to the specified Profile\
    __strProfile:__ a string with the profile's name\
    __returns__ nothing

* deleteProfile(strProfile):
    This function permanently deletes a profile
    __strProfile:__ a string with the profile's name\
    __returns__ nothing

* disconnect()\
    shuts down the WLAN-Connection\
    __returns__ nothing

* exportProfile(strProfile, strPath, clearKey=True)\
    exports a profile to a xml-file\
    __strProfile:__ a string with the profile's name\
    __strPath:__ the path to the folder to which the file will be saved\
    __clearKey:__ _[Optional]_ if true, sets the "key=clear" property\
    __returns__ nothing

* getAvilableNetworksJSON()\
    Scans for available networks\
    __returns__ a list of JSON-encoded strings 

* getAvilableNetworksList()\
    Scans for available networks\
    __returns__ a list of strings containing the names

* getDriverReport():\
    gets all the information available for installed drivers\
    __returns__ a string containing the informations

* getProfileConfiguration(strProfile) \
    Reads the configuration of the specified Profile\
    __strProfile:__ a string with the profile's name\
    __returns__ a JSON-encoded string

* getProfileConfigurations() \
    Reads the configurations of all wifis saved on the computer\
    __returns__ a list of JSON-encoded strings     
    
* getProfilesJSON() \
  Reads the names of the saved profiles on this computer\
    __returns__ a JSON-string containing the profiles

* getProfilesList() \
  Reads the names of the saved profiles on this computer\
    __returns__ a list of strings containing the profiles

* setConnectionMode(strProfile, setToAuto=True)\
    updates the connection mode of the specified profile\
    __strProfile:__ a string with the profile's name\
    __setToAuto:__ _[Optional]_ if true, sets the profiles connection mode to auto. Else to manual\
    __returns__ nothing