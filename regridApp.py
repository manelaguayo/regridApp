import sys
import ac
import acsys 

#Aplicació al sidebar d'apps

def acMain(ac_version):
    appWindow = ac.newApp("regridApp")
    ac.setSize(appWindow, 200, 200)
    return "regridApp"

