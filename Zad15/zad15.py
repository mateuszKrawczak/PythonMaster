#Policzenie wszystkich plików w zadanym katalogu (parametr wywołania skryptu), 
#do których ustawione jest prawo dostępu do wykonania („execute”).
import sys
import os

if(len(sys.argv))!=2:
    print('Niepoprawna ilość algumentów')
    quit()

path = sys.argv[1]

if os.path.isdir(path)==False:
    print('Nie ma takiego folderu')
    quit()

files = os.listdir(path)
counter = 0
for file in files:
    if os.path.isfile(path+"\\"+file)==True:
        if os.access(path+"\\"+file, os.X_OK)==True:
            counter+=1

print('Liczba plików, do których ustawione jest prawo dostępu do wykonywania w zadanym katalogu wynosi: ',counter)