import os

def install(package_name, print_output):
    install = os.popen('pak install -y ' + package_name).read()
    if print_output == True:
        print(install)
    else:
        print('Installation canceled')

def remove(package_name, print_output):
    remove = os.popen('pak uninstall -y ' + package_name).read()
    if print_output == True:
        print(remove)
    else:
        print('Installation canceled')
