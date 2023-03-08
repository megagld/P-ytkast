from pydub import AudioSegment
from pathlib import Path
import os
import pandas as pd
import regex as re

def zmien_na_mp3(numer,plik,folder_plyty,new_folder):
    file_from = '{}\\{}'.format(folder_plyty,plik+'.flac')
    plik=re.search('([a-zA-Z\d]*)([ \-_]*)(.*)',plik)[3]
    plik=rep_char(plik)
    file_to = '{}\\{:02d}_muzyka_{}.mp3'.format(new_folder,numer,plik)

    wav_audio = AudioSegment.from_file(file_from, format="flac")
    wav_audio.export(file_to, format="mp3",bitrate='320k')

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

for sheet in sorted(sheet_names):
    odcinek= '{}_{}'.format(sheet,pd.read_excel(file, sheet_name=sheet).iloc[0, 1]).strip()
    
    ready = pd.read_excel(file, sheet_name=sheet).iloc[1,1]

    if pd.isnull(ready):
        folder_plyty = '{}\\{}\\{}'.format(Path(__file__).parent,odcinek,'02_Płyta')
        pliki_flac=[i[:-5] for i in list(os.walk(folder_plyty))[0][2] if i.endswith('.flac')]

        new_folder='{}\\{}\\03_Playlista'.format(Path(__file__).parent,odcinek)

        for i,j in enumerate(sorted(pliki_flac)):
            zmien_na_mp3(i+1,j,folder_plyty,new_folder)
        print(odcinek,':płyta została przygotowana')
    else:
        print(odcinek,':gotowe')

def r():
    pass        