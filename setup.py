print("*************************I AM NOT RESPONSIBLE FOR ANY ILLEGAL USE*************************")

import os
import time

if not 'SUDO_UID':
  exit("RUN THE SCRIPT AS ROOT")

print("Setting Up.......")
os.system("sudo chown root:root macchanger.py")
os.system("pip3 install getmac")
time.sleep(2)
print("Finishing Up.......")
os.system("sudo chmod 700 macchanger.py")
time.sleep(2)
print("Finished Setting Up!")
