# PyNetsh.WLAN
This library provides functions for the computers wifi
```
from PyNetsh.WLAN import *
```

## Functions
* connectTo(strProfile)\
  tries to establish a WLAN-Connection to the specified Profile\
    __strProfile:__ a string with the profile's name\
    __returns__ nothing

* disconnect()\
  shuts down the WLAN-Connection\
    __returns__ nothing

* getAvilableNetworksJSON()\
    Scans for available networks\
    __returns__ a list of JSON-encoded strings 

* getAvilableNetworksList()\
    Scans for available networks\
    __returns__ a list of strings containing the names

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