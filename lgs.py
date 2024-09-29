# Run the command
#result = subprocess.run(['command'], capture_output=True, text=True, check=True)

# Output the result
#print(result.stdout)

import subprocess
import platform
exitenabled = 0
ostype = platform.system()
def close():
    print()
def invalidinput():
        print("\nInvalid input! Please restart the script.")

if ostype == 'Linux':

    result = subprocess.run(['sudo apt install python3-full'], capture_output=True, text=True, check=True)
    print(result.stdout)

    print("Linux Gaming Setup Utility v0.1\n\n")

    #Install Steam ********************************************************************************************************
    response = input("Would you like to install steam?\n")

    if response == 'Y':
        print("Do you want to install the System Package or Flatpak?\n")
        response = input("")

        if response == 'Flatpak':
            result = subprocess.run(['sudo flatpak install steam'], capture_output=True, text=True, check=True)
            print(result.stdout)
            askforcustomproton = 1
        elif response == 'System Package':
            result = subprocess.run(['sudo apt install steam'], capture_output=True, text=True, check=True)
            print(result.stdout)
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
                    result = subprocess.run(['wget https://github.com/AbhishekGit-AWS/beanStalk/blob/master/index.php'], capture_output=True, text=True, check=True)
                    print(result.stdout)
                    result = subprocess.run(['mkdir ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/'], capture_output=True, text=True, check=True)
                    print(result.stdout)
                    result = subprocess.run(['tar -xf GE-Proton*.tar.gz -C ~/.var/app/com.valvesoftware.Steam/data/Steam/compatibilitytools.d/'], capture_output=True, text=True, check=True)

                elif response == 'N':
                    result = subprocess.run(['wget https://github.com/AbhishekGit-AWS/beanStalk/blob/master/index.php'], capture_output=True, text=True, check=True)
                    print(result.stdout)
                    result = subprocess.run(['mkdir ~/.steam/root/compatibilitytools.d'], capture_output=True, text=True, check=True)
                    print(result.stdout)
                    result = subprocess.run(['cd ~/Downloads'], capture_output=True, text=True, check=True)
                    print(result.stdout)
                    result = subprocess.run(['tar -xf GE-Proton*.tar.gz -C ~/.steam/root/compatibilitytools.d/'], capture_output=True, text=True, check=True)
                    print(result.stdout)
                
                else:
                    invalidinput()

    print("You will most likely need to restart steam manually.\nPress enter to continue.\n")
    input()
else:
    print("This script is for Linux machines only, hence the name.")

