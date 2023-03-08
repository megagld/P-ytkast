from pathlib import Path
import pandas as pd
import os
import urllib.request


# Plik z danymi:
file = '{}{}'.format(Path(__file__).parent,'''/Płytkast.xlsx''')

# Nazwy arkuszy:
workbook = pd.ExcelFile(file)
sheet_names = workbook.sheet_names

#podkatalogi 
katalogi=list(os.walk(Path(__file__).parent))[0][1]

for sheet in sorted(sheet_names):
    odcinek= '{}_{}'.format(sheet,pd.read_excel(file, sheet_name=sheet).iloc[0, 1]).strip()
    ready = pd.read_excel(file, sheet_name=sheet).iloc[1,1]
    mp3_url = pd.read_excel(file, sheet_name=sheet).iloc[1,3]

    if pd.isnull(ready):
        # jeśli jeszcze nie gotowy, to twórz katalog i pobierz dane
        try:
            os.mkdir('{}/{}'.format(Path(__file__).parent,odcinek))
            def_folder=['01_Podcast','02_Płyta','03_Playlista','04_Scalone']
            for i in def_folder:
                try:
                    os.mkdir('{}/{}\\{}'.format(Path(__file__).parent,odcinek,i))
                except:
                    pass
            print(odcinek,':zostały stworzone katalogi robocze')
        except:
            print(odcinek,':katalogi zostały stworzone wcześniej')
    
        # ściaga podcast
        # print(mp3_url)
        # print('{}\\{}\\{}\\{}'.format(Path(__file__).parent,odcinek,'01_Podcast',"podcast.mp3"))
        urllib.request.urlretrieve(mp3_url, '{}\\{}\\{}\\{}'.format(Path(__file__).parent,odcinek,'01_Podcast',"podcast.mp3"))
        print('podcast został pobrany')


    else:
        print(odcinek,':gotowe')

def r():
    pass