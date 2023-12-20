import subprocess
import optparse 
import re

def get_user_input():
    parse_opject=optparse.OptionParser() #argümanları inceler
    parse_opject.add_option("-i","--interface",dest="interface",help="arayüz değiştirilecek!")# ağ adı birimi belirleme 
    parse_opject.add_option("-m","--mac",dest="mac_address",help="yeni mac adresi")# yeni mac adrsini belirtir

    return parse_opject.parse_args()  #kodları ayırır ve kullanılabilecek biçime getirir 

def change_mac_address(user_interface,user_mac_address): # belirtilen ağ arabiriminin mac adresini değiştirme
    subprocess.call(["ifconfig",user_interface,"down"])#belirtilen ağ birimini geçici olarak devre dışı bırakmaya yarar 
    subprocess.call(["ifconfig", user_interface,"hw","ether",user_mac_address])#kullanıcı tarafından sağlanan yeni mac adresi ile değiştiriyor
    subprocess.call(["ifconfig",user_interface,"up"])#değişen mac adresini arabirimi tekrardan aktif etmek için kullanılır 

def control_new_mac(interface):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None    
    
print("MyMacChanger başladı!")
(user_input,arguments) = get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Başarı!")
else:
    print("Hata!")    