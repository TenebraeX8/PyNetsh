# PyNetsh.Interface
This library provides functions for the computers interfaces
```
from PyNetsh.Interface import *
```

## Functions
* enableInterface(strInterface, setEnabled=True):\
    enables or disables specified interface\
    __strInterface:__ a string with the profile's name\
    __setEnabled:__ _[Optional]_ if true, sets the interface administrative state enabled\
    __returns__ nothing

* getInterfacesJSON():\
    reads the current status of the interfaces on the computer\
    __returns__ a JSON-string containing the interfaces

* getInterfacesList():\
    reads the current status of the interfaces on the computer\
    __returns__ a list of strings containing the interfaces

### Httpstunnel

* httpstunnel_configScript():\
    gets the configuration script of the Httpstunnel\
    __returns__ a string

### IPv4

* IPv4_configScript():\
    gets the configuration script of the IPv4\
    __returns__ a string

### IPv6    

* IPv6_configScript():\
    gets the configuration script of the IPv6\
    __returns__ a string    

### IPv6to4

* IPv6to4_configScript():\
    gets the configuration script of the IPv6to4\
    __returns__ a string

### Isatap

* isatap_configScript():\
    gets the configuration script of the isatap\
    __returns__ a string

### Portproxy

* portproxy_configScript():\
    gets the configuration script of the portproxy\
    __returns__ a string

### TCP

* tcp_configScript():\
    gets the configuration script of the tcp protocol\
    __returns__ a string

### Teredo

* Teredo_configScript():\
    gets the configuration script of the Teredo Client\
    __returns__ a string

* Teredo_showState():\
    reads the state of the Teredo-Client\
    __returns__ a JSON-string containing the state of the Teredo Client