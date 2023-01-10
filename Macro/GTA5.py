from os import *
import os
import subprocess
from lib.search_folder import *

class GTA5():
    def CoupeCo():
        choose_file = File.choose_file()
        #Nom de régle possible
        name_1 = "Grand Theft Auto V"
        name_2 = "GTA5.exe"
        name_3 = "Rockstar Games Launcher"
        #Name_1
        subprocess.run(["netsh", "firewall", "add", "rule" + name_1, "dir=in", "action=block", "program=" + choose_file])
        subprocess.run(["netsh", "firewall", "add", "rule" + name_1, "dir=out", "action=block", "program=" + choose_file])
        #Name_2
        subprocess.run(["netsh", "firewall", "add", "rule" + name_2, "dir=in", "action=block", "program=" + choose_file])
        subprocess.run(["netsh", "firewall", "add", "rule" + name_2, "dir=out", "action=block", "program=" + choose_file])
        #Name_3
        subprocess.run(["netsh", "firewall", "add", "rule" + name_3, "dir=in", "action=block", "program=" + choose_file])
        subprocess.run(["netsh", "firewall", "add", "rule" + name_3, "dir=out", "action=block", "program=" + choose_file])
    def ReCo():
        test = 1
        print(test)