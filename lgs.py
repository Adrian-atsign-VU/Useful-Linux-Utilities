# Run the command
#subprocess.run(['command'], shell = True)

import subprocess
import platform
exitenabled = 0
ostype = platform.system()
def close():
    print()
def invalidinput():
        print("\nInvalid input! Please restart the script.")

if ostype == 'Linux':

    print("Linux Gaming Setup Utility v0.1\n\n")

    #Install Steam ********************************************************************************************************
    response = input("Would you like to install steam?\n")

    if response == 'Y':
        print("Do you want to install the System Package or Flatpak?\n")
        response = input("")
        if response == 'Flatpak':
            subprocess.run(['sudo flatpak install steam'], shell = True)
            
            askforcustomproton = 1
        elif response == 'System Package':
            subprocess.run(['sudo apt install steam'], shell = True)
            askforcustomproton = 1
        else:
            invalidinput()

    elif response == 'N':
        askforcustomproton = 0
    else:
        askforcustomproton = 0

    if exitenabled == 0:
        if askforcustomproton == 1:
            print("Would you like to install the custom proton (GE Proton)?\n")
            response = input("")

            if response == 'Y':
                print("Are you using the Flatpak version of Steam?")
                response = input("")

                if response == 'Y':
                    subprocess.run(['wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton9-15/GE-Proton9-15.tar.gz'], shell = True)
                    subprocess.run(['tar -xf GE-Proton*.tar.gz -C ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/'], shell = True)

                elif response == 'N':
                    subprocess.run(['wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton9-15/GE-Proton9-15.tar.gz'], shell = True)
                    subprocess.run(['mkdir ~/.steam/root/compatibilitytools.d'], shell = True)
                    subprocess.run(['cd ~/Downloads'], shell = True)
                    subprocess.run(['tar -xf GE-Proton*.tar.gz -C ~/.steam/root/compatibilitytools.d/'], shell = True)
                    
                
                else:
                    invalidinput()

    print("You will most likely need to restart steam manually.\nPress enter to continue.\n")
    input()
else:
    print("This script is for Linux machines only, hence the name.")

