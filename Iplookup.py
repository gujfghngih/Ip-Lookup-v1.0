# -*- coding: utf-8 -*-
 def iplook():
    from clear import clear
    from start import virus
    import os
def draw():
    os.system("clear")
    print('''
    \033
\033[91m             ,----------------,              ,---------,
\033[91m        ,-----------------------,          ,"        ,"|
\033[91m      ,"                      ,"|        ,"        ,"  |
\033[91m     +-----------------------+  |      ,"        ,"    |
\033[91m     |  .-----------------.  |  |     +---------+      |
\033[91m     |  |                 |  |  |     | -==----'|      |
\033[91m     |  |\033[93m  I LOVE DOS!\033[91m    |  |  |     |         |      |
\033[91m     |  |\033[93m   IP Lookup\033[91m     |  |  |/----|`---=    |      |
\033[91m     |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
\033[91m     |  |                 |  |  |  // |(((( [33]|    ,"
\033[91m     |  `-----------------'  |," .;'| |((((     |  ,"
\033[91m     +-----------------------+  ;;  | |         |,"     \033[91m-π¬π»π¬πΉπ΅π¨π³ π«π¬π΄πΆπ΅-
\033[91m        /_)______________(_/  //'   | +---------+
\033[91m   ___________________________/___  `,
\033[91m  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
\033[91m / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
\033[91m/_==__==========__==_ooo__ooo=_/'   /___________,"
\033[91m`-----------------------------'
    ''')
    print("\n")
def menu():
    print("\n")
    print("\033[92m===================================================================================================")
    print("\033[93m                 }--{+} π°π· π³πΆπΆπ²πΌπ· π©π π¬π»π¬πΉπ΅π¨π³ π«π¬π΄πΆπ΅ {+}--{")
    print("                                     \033[93m[1] Start lookup  ")
    print("                                                                  \033[93m[99] exit")
    print("\033[92m===================================================================================================")
    print("\n")
def menu2():
    print("\n")
    print("\033[92m=============================================================================================")
    print("\033[92m===========\033[93mCoded by }--{+} π©π π¬π»π¬πΉπ΅π¨π³ π«π¬π΄πΆπ΅ {+}--{ \033[92m=============")
    print("                                      ")
    print("            \033[93m[1] Target IP           \033[93m[2] My IP   ")
    print("                                      ")
    print("            \033[93m[3] Whois lookup      \033[93m[4] Port Scan ")
    print("                                      ")
    print("                 \033[93m[5] Reverse ip lookup         ")
    print("\033[92m=============================================================================================")
    print("\n")
draw()
menu()
option1 = input("β  Eternal Demon β  || β  I-Anonymous-I β : ~# ")
if option1 == 1:
    os.system("clear")
    draw()
    menu2()
    option = input("β  Eternal Demon β  || β  I-Anonymous-I β : ~# ")
    if option == 1:
        ip = raw_input("What Your Target IP : ")
        url = "https://ipapi.co/"
        response = urllib2.urlopen(url + ip + "/json")
        data = response.read()
        values = json.loads(data)
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("\r")
        print("\033[91m IP              :  " + values['ip'])
        print("\033[91m City            :  " + values['city'])
        print("\033[91m Region          :  " + values['region'])
        print("\033[91m Region Code     :  " + values['region_code'])
        print("\033[91m Country         :  " + values['country_name'])
        print("\033[91m Country Capital :  " + values['country_capital'])
        print("\033[91m Country Area    :  " + str(values['country_area']))
        print("\033[91m Location        :  " + str(values['latitude'])+ " " + str(values['longitude']))
        print("\033[91m Continent       :  " + values['continent_code'])
        print("\033[91m Time Zone       :  " + values['timezone'])
        print("\033[91m Currency        :  " + values['currency'])
        print("\033[91m Calling Code    :  " + values['country_calling_code'])
        print("\033[91m Organisation    :  " + values['org'])
        print("\033[91m ASN             :  " + values['asn'])
        print ("\r")
        raw_input("Press Enter To Exit ..")
    elif option == 2:
        url = "https://ipapi.co/"
        url2 = "http://ipinfo.io/"
        response = urllib2.urlopen(url + "json")
        response2 = urllib2.urlopen(url2 + "json")
        data = response.read()
        data2 = response2.read()
        values = json.loads(data)
        values2 = json.loads(data2)
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("\r")
        print("\033[91m Public IP       :  " + values['ip'])
        print("\033[91m Private IP      :  " + values2['ip'])
        print("\033[91m City            :  " + values['city'])
        print("\033[91m Region          :  " + values['region'])
        print("\033[91m Region Code     :  " + values['region_code'])
        print("\033[91m Country         :  " + values['country_name'])
        print("\033[91m Country Capital :  " + values['country_capital'])
        print("\033[91m Country Area    :  " + str(values['country_area']))
        print("\033[91m Location        :  " + str(values['latitude'])+ " " + str(values['longitude']))
        print("\033[91m Continent       :  " + values['continent_code'])
        print("\033[91m Time Zone       :  " + values['timezone'])
        print("\033[91m Currency        :  " + values['currency'])
        print("\033[91m Calling Code    :  " + values['country_calling_code'])
        print("\033[91m Organisation    :  " + values['org'])
        print("\033[91m ASN             :  " + values['asn'])
        print ("\r")
        raw_input("Press Enter To Exit ..")
    elif option == 3:
        d3 = raw_input('Enter IP Or Domain : ')
        os.system("clear")
        os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
        print("")
        quit()
    elif option == 4:
        d3 = raw_input('Enter IP Or Domain : ')
        os.system("clear")
        os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
        print("")
        quit()
    elif option == 5:
        d3 = raw_input('Enter IP Or Domain : ')
        os.system("clear")
        os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
        os.system("clear")
        os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
        print("")
        print("\033[91m\033[1mFile Saved On : ")
        os.system("clear")
        print("File : index.html?q=" +d3)
        print("\033[0m")
          quit()
    elif option1 == '99':
        clear()
        virus()
