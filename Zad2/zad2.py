#Tworzenie  nowych  plików  w  zadanym  katalogu  (parametr  wywołania skryptu), 
#według listy umieszczonej  w  pliku  (drugi  parametr  wywołania  skryptu).  
#Nowe  pliki  mają  być  zerowej  wielkości (puste). 
#Jeżeli jakiś plik już istnieje, to nie powinien zostać zniszczony.
import sys
import os

if(len(sys.argv))!=3:
    print('Niepoprawna ilość algumentów')
    quit()

path1 = sys.argv[1]
path2 = sys.argv[2]

if os.path.isdir(path1)==False or os.path.isfile(path2)==False:
    print('Nie ma takiego/takich folderu/folderów')
    quit()

fileToRead = open(path2)
filesNames = fileToRead.read().split()
fileToRead.close()

for name in filesNames:
  f = open(path1+"\\"+name, "a")
  f.close()


