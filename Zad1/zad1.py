#Zmiana  nazw  wszystkich  plików  w  zadanym  katalogu  (parametr  wywołania  skryptu),  
#do  których mamy ustawione prawo zapisu, przez dopisanie dodatkowego członu .old. 
#Wcześniej należy skasować wszystkie pliki, które już mają takie rozszerzenie
import sys
import os

path = sys.argv[1]
if os.path.isdir(path)==True:
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path+"\\"+file)==True:
            if (".old" in file)==True:
                os.remove(path+"\\"+file)
            else :
                os.rename(path+"\\"+file, path+"\\"+file+".old")
 
