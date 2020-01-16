import time
import os
from termcolor import colored

#if os.geteuid() != 0:
  #  exit("You need root to run this script good bye")

def main():
    os.system("clear && reset")
    print colored("Welcome to Project X After Installing and Updating your system it will turn into a hacking tool", "red")

main()
if __name__ == '__main__':
    print colored('Made BY Darkwar', 'blue')
    print colored("[1] Installing System","green")
    print colored("[2] Running ssh", "red")
    print colored("[3] Installing apps", "yellow")
    print colored("[4] Update System", "blue")
    bot = raw_input("Enter Option: ")

if bot == "1":
    os.system("sudo apt install apache2-bin macchanger virtualbox  xterm net-tools wireshark python3 python python-minimal python3-pip python-pip  zenmap aircrack-ng openssh-server hydra-gtk hydra libatk-adaptor:i386 libgail-common:i386 build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev libyaml-dev curl zlib1g-dev gawk bison libffi-dev libgdbm-dev libncurses5-dev libtool sqlite3 libgmp-dev gnupg2 dirmngr nmap ruby-bundler ruby-nokogiri build-essential patch ruby-dev zlib1g-dev liblzma-dev httrack virtualenv acccheck 6tunnel 4g8 anytun apt-cacher apache2-utils apt-cacher-ng git squid3 parallel snapd sqlmap apt-cacher-ng adb apktool lua5.1 lua5.2 lua50 braa sslsplit sslstrip edb-debugger android-sdk arduino ncrack cewl chntpw cmospwd crunch maskprocessor httptunnel binwalk p0f guymager bbqsql  openvas-manager cryptcat postgresql postgresql-contrib")
    os.system("snap install john-the-ripper")
    os.system("git clone https://github.com/LionSec/katoolin.git")
    os.system("gem install bundler")
    os.system("git clone https://github.com/commixproject/commix.git")
    os.system("git clone https://github.com/haroonawanofficial/XSS-Finder.git")
    os.system("sudo apt-get install -y build-essential autoconf libtool pkg-config python-opengl python-pil python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev python-pip xdotool bleachbit")
    os.system("snap install null")
    os.system("sudo gem install nokogiri")
    os.system("sudo git clone https://github.com/rapid7/metasploit-framework.git")
    os.system("sudo chown -R `whoami` /home/darkwar/Desktop/metasploit-framework")
    os.system("pip3 install scrapy && pip install scrapy && pip install telepot && pip3 install telepot")
    time.sleep(2)
    os.system("cd /home/darkwar/Desktop/metasploit-framework && bundle install ")
    time.sleep(1)
    os.system("clear && reset")
    exit("Thanks for using Project-X")

if bot == "2":
    os.system("systemctl start ssh")
    os.system("sudo ufw allow ssh")
    os.system("sudo iptables -P FORWARD ACCEPT")
    os.system("sudo iptables -P OUTPUT ACCEPT")
    os.system("sudo iptables -P INPUT ACCEPT")
    

elif bot == "3":
    os.system("sudo snap install discord spotify")
    os.system("sudo snap install telegram-desktop")
    os.system("sudo snap refresh core --beta")

elif bot == "4":
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("sudo apt autoremove")
    











#burb suite - https://portswigger.net/burp/releases/download?product=community&version=2.1.07&type=linux&componentid=100

#bionic - https://packages.ubuntu.com/bionic/net/

#kali tools - https://linuxhint.com/install_kali_tools_ubuntu/
