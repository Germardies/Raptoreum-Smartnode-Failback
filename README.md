RTM SmartnodeFailback v1.0 ©2024 by Raptoreum and Germardies
============================================================

Lightpaper
-----------
RTM SmartnodeFailback is a script that checks whether the process (raptoreumd) of your wallet/samrtnode is running.
If this process is not running, it is automatically restarted.

The use of this script is intended to prevent your Raptoreum Smartnode from receiving the Posed Banned status.

The script consists of 2 files:
1. install.py
2. smartnoderestart.py

The install.py sets up a service on your VPS server. This service automatically starts the smartnodesrestart.py file (even after the VPS is restarted).

The Smartnodes.py file checks at an interval specified by you (default = 15 minutes) whether the "raptoreumd" process is running on your VPS.
If it is not running, an attempt is made to start this service.

This process is documented in the file ~/smartnodecontroll.log.

A big thank you to the Discord user Badfish, who gave me this idea with a bash script.

Documentation & Instructions
----------------------------
Please note the sequence!
1. you must download both files and save them on your VPS.
2. Open the file with the command "nano smartnoderestart.py" and adjust at least the variable process_path in line 7. The correct path to your raptoreumd file must be entered here.
3. save and close the file
4. start the installation file with the command "python3 install.py".
Now the service process is created and started, which sets everything in motion.

You do not need to do anything else. The raptoreum.d process should now be running.
You can check this in two ways:
1. enter the command "htop" and look for the process raptoreumd
2. go to the directory of your wallet and check the status of your smartnode using "./raptoreum-cli smartnode status"
 
COPYRIGHT
---------
The MIT License (MIT)
Copyright (c) 2024 The Raptoreum developers (https://github.com/Raptor3um)
Copyright (c) 2024 Germardies (https://github.com/Germardies)