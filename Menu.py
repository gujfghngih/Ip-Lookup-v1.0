# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console
from pyfiglet import figlet_format
from termcolor import colored
from time import sleep 
from instainfo import instainfo
from iplook import iplook
from clear import clear
from numscan import numscan
from ketik import ketik
from ip import ip
from cipher import cyb

cyan = ("\033[1m\033[36m")
mawar = ("\033[31;1m")
white = ("\033[37m")
console = Console()
def virus():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = colored('''
…………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄
…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄
………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄
……..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█
…..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█
…..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
…▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌
…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█
…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█                                \033[93m_________________
..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█                              \033[93m|               |
..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█                              \033[93m|TOOL IN PROCESS|
.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█                              \033[93m|_______________|
.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██
..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██
..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█                               \033[93m1 [Ip Lookup]
..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█
….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█
……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█
………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█
………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀
………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░
…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█
………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█
…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█
…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌
……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█
……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█
………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█
………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█
………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█
………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█
………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█
………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█
……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀
………………………..▀▀██▓▓▓▓██▀
     ''' , 'red')
   for N, line in enumerate( x.split( "\n" ) ):
        print(line)
        sleep( 0.05 )
option = input('† Eternal Demon † || † I-Anonymous-I †: ~#  ')

 if option == '1':
        iplookup()
virus()
