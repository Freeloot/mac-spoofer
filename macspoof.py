import random
import subprocess

global interface
global random_mac
interface = 'eth0'

def Main():

    random_mac = "%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    f = open("macs.txt", "a")
    f.write("-> Generated MAC: " + random_mac + '\n')
    f.close()
    print("-> Generated MAC: " + random_mac)

    print("[+] Changing MAC address for " + interface + " to " + random_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", random_mac])
    subprocess.call(["ifconfig", interface, "up"])

Main()
