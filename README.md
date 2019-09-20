# PyNetsh
A simple library for the most important functions of the Windows netshell. Backend, the Windows command line is called to execute these commands. This library is intended to mask out all the commands used to do simple stuff like disconnecting from a Wifi. It also parses the information output into JSON-encoded strings for better postprocessing.\
\
If you did not work with json yet, please dont try to use methods like ```.find()```. Just use the python standard library json (```import json``` ) and convert it into a dictionary with ```json.loads()```

## Usage
It was important to me to write this library without using any other dependencies than the python standard libraries. 
1. Clone the repo (or copy the content of the files)
2. In your python-script write
   ```
   from PyNetsh import *
   ```
   Note: If you dont clone the repo, just import the files you copied.

3. Now you can use the functions (and modules) of the library

Read the README of the specific library you want to use for more informations.
