import random
import subprocess

if __name__ == '__main__':
    interface = 'eth0'
    new_mac = input("Enter your new MAC: ")

    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    try:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])

        f = open("macs.txt", "a")
        f.write("-> Assigned MAC: " + new_mac + '\n')
        f.close()

        print("-> Assigned MAC: " + new_mac)
    except Exception as error:
        print(error)
