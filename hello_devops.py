#!/usr/bin/env python3

import platform # Standard Library for OS/hardware info
import sys # Provides access to pyhton interpreter details
import os # Operating system interface

def main():
 print(f"OS : {platform.system()} {platform.release()}")
# platform.system() returns 'Linux', 'Windows', or 'Darwin'

 print(f"Python : { sys.version.split()[0]}")
# Sys.version gives the full Python version string

 print(f"Working Dir : {os.getcwd()}")
# os.getcwd() returns the current working directory

try:
 print(f"User : {os.getlogin()}")
except OSError:
#os.getlogin() return the login name of the current user

 print(f"user : {os.environ.get('USER', 'unknown')}")
# fallback when running in non-interactive shells (CI/CD)

if __name__ == "__main__":

#This gueard ensures main() only runs when script is executed directly
#not when it is imported as a module

 main()
