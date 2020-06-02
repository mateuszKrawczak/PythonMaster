#Przesuwanie  wszystkich  plików  z  ustawionym  prawem  wykonywania  z  jednego  katalogu  do  drugiego.   
#Pozostałe   pliki   w   katalogu   nie   powinny   być   ruszane.   
#Nazwy   katalogów,   źródłowego i docelowego, zadawane jako parametry skryptu. 
import sys
import os
import shutil

if(len(sys.argv))!=3:
    print('Niepoprawna ilość algumentów')
    quit()

path1 = sys.argv[1]
path2 = sys.argv[2]

if os.path.isdir(path1)==False or os.path.isdir(path2)==False:
    print('Nie ma takiego/takich folderu/folderów')
    quit()

files = os.listdir(path1)
for file in files:
    if os.path.isfile(path1+"\\"+file)==True:
        if os.access(path1+"\\"+file, os.X_OK)==True:
            shutil.copy2(path1+"\\"+file, path2)
