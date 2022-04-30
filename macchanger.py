print("*************************I AM NOT RESPONSIBLE FOR ANY ILLEGAL USE*************************")

import os
from getmac import get_mac_address as gmc
if not "SUDO_UID" in os.environ.keys():
    exit("RUN THE SCRIPT AS ROOT")
try:
 def Macchanger():
   user_interface = str(input("[Enter The Desired Network Interface]: "))
   print(f"[Your MAC Address Is]: {gmc()}")
   desired_mac = input("[Enter The MAC Address You Want To Spoof]: ")
   while desired_mac == "":
       desired_mac = str(input("[Enter The MAC Address You Want To Spoof]: "))
   os.system(f"ifconfig {user_interface} down")
   os.system(f"ifconfig {user_interface} hw ether {desired_mac}")
   os.system(f"ifconfig {user_interface} up")
   print(f"[Your MAC Was Successfully Changed To]: {desired_mac}")
 Macchanger()
 option = ""
 while option != "yes" or option != "no" or option != "Yes" or option != "No":
   option = input("[Do You Want To Change Your MAC Again]: ")
   if option == "Yes" or option == "yes" or option == "YES":
    Macchanger()
   elif option == "No" or option == "no" or option == "NO":
    exit("\nThanks For Using M0dCh4ng3r")
   elif option == "exit" or option == "quit":
       exit("\nThanks For Using M0dCh4ng3r")
   else:
    print("Invalid Command!")
except KeyboardInterrupt:
    exit("\nThanks For Using M0dCh4ng3r")
