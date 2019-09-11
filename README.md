# ArpDetector

A very simple detector of ARP spoofing attacks for Mac OS X.

  * Detects attacks by spotting MAC addresses assigned to several IP addresses on LAN.
  * Runs in the background using ```launchd```.
  * Sends OS X notifications when an ARP attack is suspected.
  * Runs on Python.

Note that the supplied property list runs the script every 30 min. Therefore, if an attack is carried out in the meantime, it will not be detected. If you wish to run it at smaller intervals, you can modify the plist manually.
 
## Installation

```
git clone git@github.com:almayor/ArpDetector.git
cd ArpDetector
make install
```
The installation script

  * hard-links the property list to ```~/Library/LaunchAgents/```
  * creates a directory ```~/bin``` if it doesn't already exist
  * hard-links the python script to that directory
  * loads and starts the process with ```launchctl```

To uninstall run

```
cd ArpDetector
make uninstall
```