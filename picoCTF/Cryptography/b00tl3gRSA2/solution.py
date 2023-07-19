import Crypto.Util.number
from Crypto.Util.number import *


c= 62546374379902027683509644678750945257944737199427591953831141632792896166821415554927590055503401938160836636235961339033000526130512278651823958749101242973506545187444372556157647678409103411039379621250913979212679644452826404034035362554006840915531158240549209033901661632829506787666549599189622247129
n= 105416223329273082006960187688075693872597403695320466786816133526818758130459118799831681394921559906741424858372157667750321402561133715822161056107642839226192488771439952858090908816189511235830154152412060975553814970980770823763893030337009203221497844487932411392312410529785580842684968138518709744353
e= 37466775867201090974382770828972139972449323653433932478833455883549587761612283964851600694751177119912843267559739819566172336693112099159949303140444697829856970440962503736439026546306700715614022990633445910325968413441746307954685503134417349184997678170835631735818942676431926523234282491617328558773


# if e is replaced with d meaning that e is now very large, then of course d will be very small
# so we can bruteforce d to obtain our message

for i in range(100000):
    message = pow(c , i , n)
    message = long_to_bytes(message)
    if(message.startswith(b"picoCTF{")):
        print(message)
