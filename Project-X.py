import time
import os
from termcolor import colored
import os.path
import tarfile
import subprocess
def main():
    while(True):
        os.system("clear && reset")
        print colored("Welcome to Project X After Installing and Updating your system it will turn into a hacking tool", "red", attrs=['bold'])        
        print colored('Made By Darkwar', 'blue', attrs=['bold'])
        print colored("[1] Installing System","green", attrs=['bold'])
        print colored("[2] Running ssh", "cyan", attrs=['bold'])
        print colored("[3] Installing apps", "yellow", attrs=['bold'])
        print colored("[4] Update System", "blue", attrs=['bold'])
        print colored("[5] Back Up sources.list", "green", attrs=['bold'])
        print colored("{6} Install MsfConsole please use 2 then this", "green", attrs=['bold'])
        print("{7} install tor and access the tor browser")
        print("{8} Installs Everything")
        print colored("[0] Exit", "red", attrs=['dark'])
        bot = raw_input("Enter Option: ")

        if bot == "1":
           
            os.system("sudo apt install -y apache2-bin hexchat hping3 macchanger virtualbox  xterm net-tools wireshark python3 python python-minimal python3-pip python-pip  zenmap aircrack-ng openssh-server hydra-gtk hydra libatk-adaptor:i386 libgail-common:i386 build-essential libreadline-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev libyaml-dev curl zlib1g-dev gawk bison libffi-dev libgdbm-dev libncurses5-dev libtool sqlite3 libgmp-dev gnupg2 dirmngr nmap ruby-bundler ruby-nokogiri build-essential patch ruby-dev zlib1g-dev liblzma-dev httrack virtualenv acccheck 6tunnel 4g8 anytun apt-cacher apache2-utils apt-cacher-ng git squid3 parallel snapd sqlmap apt-cacher-ng adb apktool lua5.1 lua5.2 lua50 braa sslsplit sslstrip edb-debugger android-sdk arduino ncrack cewl chntpw cmospwd crunch maskprocessor httptunnel binwalk p0f guymager bbqsql  openvas-manager cryptcat postgresql postgresql-contrib ettercap-graphical hashcat pixiewps mdk3 lighttpd isc-dhcp-server hostapd build-essential autoconf libtool pkg-config python-opengl python-pil python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev python-pip xdotool bleachbit libcanberra-gtk-module libcanberra-gtk-module:i386 kdenlive kazam python3-cairo python3-xlib default-jre mercurial python3-cairo p0f cpanminus apt-file lksctp-tools nginx-full mkchromecast ttyrec python-opster bluetooth bluez bluez-tools rfkill blueman gimp kismet dhcpcd5 openjdk-8-jdk-headless adb imagemagick sysvbanner lolcat gnustep-gui-runtime figlet gr-gsm nodejs abiword brasero k3b libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libdvd-pkg ubuntu-restricted-extras q4wine tshark")
           
            os.system("snap install john-the-ripper && snap install imagemagick")
            os.system("snap install null")
            os.system("sudo gem install bundler")
            os.system("git clone https://github.com/commixproject/commix.git")
            os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb")
            os.system("wget http://git.osmocom.org/gr-gsm/plain/apps/grgsm_livemon.grc && grcc -d . grgsm_livemon.grc && mv grgsm_livemon.py grgsm_livemon")
            os.system("wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip")
            os.system("git clone https://github.com/elceef/dnstwist.git")
            os.system("sudo add-apt-repository ppa:ozmartian/apps")
            os.system("sudo apt install qml-module-qtmultimedia vidcutter")
            os.system("sudo add-apt-repository ppa:ondrej/nginx")
            os.system("sudo add-apt-repository ppa:openshot.developers/ppa && sudo apt-get update && sudo apt-get install openshot-qt")
            os.system("git clone https://github.com/boxug/trape.git")
            os.system("git clone https://github.com/fwaeytens/dnsenum.git")
    	    os.system("sudo gem install nokogiri")
            os.system("pip3 install scrapy && pip install scrapy && pip install telepot && pip3 install telepot dnspython3 aiohttp httplib2 socksipy-branch requests url bs4")   
            os.system("git clone https://github.com/bettercap/bettercap.git")
            os.system("git clone https://github.com/v3n0m-scanner/v3n0m-scanner.git")
            os.system("git clone https://github.com/Rajkumrdusad/Tool-X.git")
            os.system("wget https://github.com/aanarchyy/bully/archive/master.zip && unzip master.zip && sudo rm -fr master.zip")
            os.system("cd bully-master/src && make && sudo make install")
            os.system("git clone https://github.com/lightos/credmap.git")
            os.system("git clone https://github.com/MetaChar/Mercury.git")
            os.system("git clone https://github.com/mIcHyAmRaNe/okadminfinder3.git")
            os.system("git clone https://github.com/M4sc3r4n0/Evil-Droid.git")
            os.system("sudo npm install -g combolist-generator")
            os.system("git clone https://github.com/RomaniukVadim/hack_scripts.git && git clone https://github.com/adnane-X-tebbaa/Katana.git && git clone https://github.com/scorpion3013/checkolotl.git && git clone https://github.com/scorpion3013/SimpleCheck.git")
            os.system("clear && reset")
            
        elif bot == "2":
            os.system("sudo systemctl start ssh")
	    os.system("sudo ufw allow ssh")
	    os.system("sudo iptables -P FORWARD ACCEPT")
            os.system("sudo iptables -P OUTPUT ACCEPT")
            os.system("sudo iptables -P INPUT ACCEPT")
            os.system("sudo systemctl enable postgresql && sudo systemctl start postgresql")
            os.system("sudo /etc/init.d/nessusd start")
            time.sleep(1)
    

        elif bot == "3":
            os.system("sudo snap install discord")
            os.system("sudo snap install telegram-desktop")
            os.system("sudo snap refresh core --beta")
            time.sleep(1)

        elif bot == "4":
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("sudo apt autoremove")
     
        elif bot == "5":
            print("Welcome To Backup")
            print colored("***Note NEED BACKUP FIRST BEFOR RESTORING***", "red", attrs=['bold'])
            print colored("{1} Backup", "green", attrs=['bold'])
            print colored ("{2} Restore", "blue", attrs=['bold'])
            rb = raw_input("Enter Option: ")
            if rb == "1":
                if not os.path.exists("/etc/apt/backup"):
                    os.system("sudo mkdir /etc/apt/backup")
                    os.system("sudo cp /etc/apt/sources.list -r /etc/apt/backup/sources.list")

            elif rb == "2":
                os.system("sudo mv /etc/apt/backup/sources.list /etc/apt/sources.list")
                os.system("sudo rm -fr /etc/apt/backup") 
       
        elif bot == "6":
            os.system("clear")
            os.system("sudo ./msfinstall")
            os.system("clear")
            os.system("sudo ufw allow 4444")
            print("Please port Forward Port 4444")
            print("To Run Msfconsole type msfconsole")    
       
        elif bot == "7":
            os.system("sudo add-apt-repository ppa:micahflee/ppa && sudo apt update && sudo apt install torbrowser-launcher && sudo apt install tor")
            time.sleep(3)
            print("run sudo netstat -plnt | fgrep 9050")
            time.sleep(3)
            
        elif bot == "8":
            os.system("sudo apt install -y apache2-bin hexchat hping3 macchanger virtualbox  xterm net-tools wireshark python3 python python-minimal python3-pip python-pip  zenmap aircrack-ng openssh-server hydra-gtk hydra libatk-adaptor:i386 libgail-common:i386 build-essential libreadline-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev libyaml-dev curl zlib1g-dev gawk bison libffi-dev libgdbm-dev libncurses5-dev libtool sqlite3 libgmp-dev gnupg2 dirmngr nmap ruby-bundler ruby-nokogiri build-essential patch ruby-dev zlib1g-dev liblzma-dev httrack virtualenv acccheck 6tunnel 4g8 anytun apt-cacher apache2-utils apt-cacher-ng git squid3 parallel snapd sqlmap apt-cacher-ng adb apktool lua5.1 lua5.2 lua50 braa sslsplit sslstrip edb-debugger android-sdk arduino ncrack cewl chntpw cmospwd crunch maskprocessor httptunnel binwalk p0f guymager bbqsql  openvas-manager cryptcat postgresql postgresql-contrib ettercap-graphical hashcat pixiewps mdk3 lighttpd isc-dhcp-server hostapd build-essential autoconf libtool pkg-config python-opengl python-pil python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev python-pip xdotool bleachbit libcanberra-gtk-module libcanberra-gtk-module:i386 kdenlive kazam python3-cairo python3-xlib default-jre mercurial python3-cairo p0f cpanminus apt-file lksctp-tools nginx-full mkchromecast ttyrec python-opster bluetooth bluez bluez-tools rfkill blueman gimp kismet dhcpcd5 openjdk-8-jdk-headless adb imagemagick sysvbanner lolcat gnustep-gui-runtime figlet gr-gsm nodejs abiword brasero k3b libdvdnav4 libdvdread4 gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly libdvd-pkg ubuntu-restricted-extras q4wine tshark")
            os.system("snap install john-the-ripper && snap install imagemagick")
            os.system("snap install null")
            os.system("sudo gem install bundler")
            os.system("git clone https://github.com/commixproject/commix.git")
            os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && sudo apt install ./google-chrome-stable_current_amd64.deb")
            os.system("wget http://git.osmocom.org/gr-gsm/plain/apps/grgsm_livemon.grc && grcc -d . grgsm_livemon.grc && mv grgsm_livemon.py grgsm_livemon")
            os.system("wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip")
            os.system("git clone https://github.com/elceef/dnstwist.git")
            os.system("sudo add-apt-repository ppa:ozmartian/apps")
            os.system("sudo apt install qml-module-qtmultimedia vidcutter")
            os.system("sudo add-apt-repository ppa:ondrej/nginx")
            os.system("sudo add-apt-repository ppa:openshot.developers/ppa && sudo apt-get update && sudo apt-get install openshot-qt")
            os.system("git clone https://github.com/boxug/trape.git")
            os.system("git clone https://github.com/fwaeytens/dnsenum.git")
    	    os.system("sudo gem install nokogiri")
            os.system("pip3 install scrapy && pip install scrapy && pip install telepot && pip3 install telepot dnspython3 aiohttp httplib2 socksipy-branch requests url bs4")   
            os.system("git clone https://github.com/bettercap/bettercap.git")
            os.system("git clone https://github.com/v3n0m-scanner/v3n0m-scanner.git")
            os.system("git clone https://github.com/Rajkumrdusad/Tool-X.git")
            os.system("wget https://github.com/aanarchyy/bully/archive/master.zip && unzip master.zip && sudo rm -fr master.zip")
            os.system("cd bully-master/src && make && sudo make install")
            os.system("git clone https://github.com/lightos/credmap.git")
            os.system("git clone https://github.com/MetaChar/Mercury.git")
            os.system("git clone https://github.com/mIcHyAmRaNe/okadminfinder3.git")
            os.system("git clone https://github.com/M4sc3r4n0/Evil-Droid.git")
            os.system("sudo npm install -g combolist-generator")
            os.system("git clone https://github.com/RomaniukVadim/hack_scripts.git && git clone https://github.com/adnane-X-tebbaa/Katana.git && git clone https://github.com/scorpion3013/checkolotl.git && git clone https://github.com/scorpion3013/SimpleCheck.git")
            os.system("sudo systemctl start ssh")
	    os.system("sudo ufw allow ssh")
	    os.system("sudo iptables -P FORWARD ACCEPT")
            os.system("sudo iptables -P OUTPUT ACCEPT")
            os.system("sudo iptables -P INPUT ACCEPT")
            os.system("sudo systemctl enable postgresql && sudo systemctl start postgresql")
            os.system("sudo /etc/init.d/nessusd start")
            time.sleep(1)
            os.system("sudo snap install discord")
            os.system("sudo snap install telegram-desktop")
            os.system("sudo snap refresh core --beta")
            time.sleep(1)
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("sudo apt autoremove")
            os.system("clear && reset")
        elif bot == "0" or "exit":
            os.system("clear && reset")
            break
            
main()

exit("Thx For Useing Project-X\nCome Back Soon")



""" 
#sudo netstat -plnt | fgrep 9050


archlinux - install the tools


#burb suite - https://portswigger.net/burp/releases/download?product=community&version=2.1.07&type=linux&componentid=100

More Hacking Tools:

#bionic - https://packages.ubuntu.com/bionic/net/

#echo /etc/sysctl.conf net.ipv4.tcp_challenge_ack_limit = 999999999
"""
