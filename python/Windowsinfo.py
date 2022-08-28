
import platform
import datetime
import os
import sys
from winreg import *


def get_os_info():
    os_info = {}

    os_info['os'] = platform.system() + ' ' + platform.release()

    if os_info['os'].startswith('Windows'):
        os_info['os'] += ' ' + platform.version()

    return os_info


def get_windows_installation_date():
    key = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    installDate = QueryValueEx(key, "InstallDate")[0]

    date = datetime.datetime.fromtimestamp(int(installDate)).strftime('%Y-%m-%d %H:%M:%S')

    return date


def get_windows_version():
    key = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    version = QueryValueEx(key, "ProductName")[0]

    return version


def get_windows_build():
    key = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")

    build = QueryValueEx(key, "BuildLabEx")[0]

    return build



def get_windows_username():
    username = os.getlogin()

    return username


def get_windows_computer_name():
    computer_name = os.environ['COMPUTERNAME']

    return computer_name


def get_windows_domain():
    domain = os.environ['USERDOMAIN']

    return domain


def get_windows_loggedinuser():
    loggedinuser = os.environ['USERNAME']

    return loggedinuser


def main():
    print('OS: ' + get_os_info()['os'])
    print('Windows Version: ' + get_windows_version())
    print('Windows Build: ' + get_windows_build())
    print('Windows Username: ' + get_windows_username())
    print('Windows Computer Name: ' + get_windows_computer_name())
    print('Windows Domain: ' + get_windows_domain())
    print('Windows Logged In User: ' + get_windows_loggedinuser())

     #print(getattr(sys, "frozen", False))  # True if the program is running as a bundle (pyinstaller)

     #print(sys._MEIPASS)  # The directory where the bundled app is running from (pyinstaller)

     #print(sys.executable)  # The path to the executable binary that started this program (pyinstaller)

     #print(sys.argv[0])  # The path to the script that started this program (pyinstaller)

     #print(os.path.dirname(os.path.abspath(__file__)))  # The directory of the script that started this program (pyinstaller)

     #print(os.path.dirname(sys.executable))  # The directory of the executable binary that started this program (pyinstaller)

     #print(os.path.dirname(sys.argv[0]))  # The directory of the script that started this program (pyinstaller)


if __name__ == '__main__':
    main()