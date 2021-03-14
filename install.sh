#!/bin/bash
clear
echo "
▀▀█▀▀ █▀▀█ █▀▀█ █   █▀▀ 
  █   █  █ █  █ █   ▀▀█ 
  ▀   ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀             

                                                ";

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/IP" ] ;
then
echo "[◉] A directory IP was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/IP"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/gujfghngih/IP.git /usr/share/doc/IP;
 echo "#!/bin/bash 
 python /usr/share/doc/IP/ip.py" '${1+"$@"}' > ip;
 chmod +x crips;
 sudo cp crips /usr/bin/;
 rm crips;


if [ -d "/usr/share/doc/IP" ] ;
then
echo "";
echo "[✔]Tool istalled with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔] ✔✔✔  All is done!! You can execute tool by typing ip  !     ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation faid![✘] ";
  exit
fi
