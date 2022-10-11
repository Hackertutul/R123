import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
        os.system('xdg-open https://www.facebook.com/Mr.Tutul.ok.Bro')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from tutul1 import main1
 
        main1()
 
 
 
elif bit == "32bit":
 
        from tutul1 import main1
 
 
        main1()
        
 