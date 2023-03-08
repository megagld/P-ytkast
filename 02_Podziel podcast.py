from calendar import c
from pathlib import Path
from re import S
import pandas as pd
import os
from pydub import AudioSegment

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def rep_char(i):
    to_rep='\/:*?"<>|'
    for j in to_rep:
        i=i.replace(j,'')
    i=''.join(j for j in i if ord(j)>31)    
    return i.rstrip('.').rstrip(' ')

# Plik z danymi:
file = '{}{}'.format(Path(__file__).parent,'''/Płytkast.xlsx''')

# Nazwy arkuszy:
workbook = pd.ExcelFile(file)
sheet_names = workbook.sheet_names

#podkatalogi 
katalogi=list(os.walk(Path(__file__).parent))[0][1]

for sheet in sorted(sheet_names):
    odcinek= '{}_{}'.format(sheet,pd.read_excel(file, sheet_name=sheet).iloc[0, 1]).strip()

    playlist_folder=list(os.walk('{}\\{}\\03_Playlista'.format(Path(__file__).parent,odcinek)))
    ready = pd.read_excel(file, sheet_name=sheet).iloc[1,1]

    # jeśli katalog '03_Playlista' nie ma pliku "Wstęp" i jeśli nie jest oznaczony jako "gotowy" to:
    if pd.isnull(ready) and '00 Wstęp_podcast.mp3' not in playlist_folder:
        try:
            # pobierz dane (czasy) do podziału podcastu
            data = pd.read_excel(file, sheet_name=sheet, header=None, usecols='B',skiprows = 3)
            
            # pobranie pliku audio podcastu
            plik_podcast = '{}\\{}\\{}'.format(Path(__file__).parent,odcinek,'01_Podcast\\podcast.mp3')
            sound_file = AudioSegment.from_file(plik_podcast)

            # ustalenie momentów cięcia
            cuts=[i[0].split(' ')[0] for  i in data.values.tolist()]
            cuts=[0]+[get_sec(i) for i in cuts]+[sound_file.duration_seconds]

            # ustalenie nazw części
            titles=['Wstęp']+ [' '.join(i[0].split(' ')[1:]) for  i in data.values.tolist()]

            # utworzenie listy z częściam
            parts=[]
            for i in range(len(cuts)-1):
                parts.append((i,titles[i],cuts[i:i+2]))

            # tworzenie podzielonych plików audio

            silent=AudioSegment.silent(duration=2000)

            for i,j,k in parts:
                x,y=k
                if i>1:x-=2   #zakładka 2s dla ciętych słów
                new_file = silent+sound_file[1000*x : 1000*y]+silent
                nazwa='{}\\{}\\03_Playlista\\{:02d}_podcast_{}.mp3'.format(Path(__file__).parent,odcinek,i,rep_char(j))


                new_file.export(nazwa, format="mp3",bitrate='192k')
        except:
            None
            print(odcinek,':podcast został podzielony')
        else:
            print(odcinek,':gotowe')
def r():
    pass