from pydub import AudioSegment
from pathlib import Path
import os
import pandas as pd
import datetime

# Plik z danymi:
file = '{}{}'.format(Path(__file__).parent,'''/Płytkast.xlsx''')

# Nazwy arkuszy:
workbook = pd.ExcelFile(file)
sheet_names = workbook.sheet_names

for sheet in sorted(sheet_names):
    odcinek= '{}_{}'.format(sheet,pd.read_excel(file, sheet_name=sheet).iloc[0, 1]).strip()
    
    ready = pd.read_excel(file, sheet_name=sheet).iloc[1,1]

    if pd.isnull(ready):
        folder_playlisty = '{}\\{}\\{}'.format(Path(__file__).parent,odcinek,'03_Playlista')
        pliki_do_scalenia=[i for i in list(os.walk(folder_playlisty))[0][2] if i.endswith('.mp3')]

        new_folder='{}\\{}\\04_Scalone'.format(Path(__file__).parent,odcinek)

        plik_scalony=None
       
        znaczniki_czasu=['00:00:00.000']   
        nazwy_plikow=[]     

        for i,j in enumerate(sorted(pliki_do_scalenia)):
            
            plik_do_dodania=AudioSegment.from_file('{}\\{}'.format(folder_playlisty,j))
            if plik_scalony:
                plik_scalony+=plik_do_dodania
            else:
                plik_scalony=plik_do_dodania
            
            czas=plik_scalony.duration_seconds+82800
            czas=datetime.datetime.fromtimestamp(czas)
            czas=czas.strftime('%H:%M:%S.%f')[:-3]          #00:00:00.000 Introduction
            znaczniki_czasu.append(czas)
            nazwy_plikow.append(j.rsplit('.mp3')[0])

        
        znc='\n'.join('{} {}'.format(i,j) for i,j in zip(znaczniki_czasu[:-1],nazwy_plikow))
        # print(znc)

        # znc=''.join(i for i in znc  if ord(i)<255)

        #open text file
        text_file = open('{}\\{}.chapters.txt'.format(new_folder,odcinek), "w",encoding="utf-8")
        
        #write string to file
        text_file.write(znc)
        
        #close file
        text_file.close()

        nowa_nazwa='{}\\{}.mp3'.format(new_folder,odcinek)

        # utwórz plik

        plik_scalony.export(nowa_nazwa, format="mp3",bitrate='320k')

        # dodaj znaczniki

        os.system('''mp3chaps -r "{}"'''.format(nowa_nazwa))
        os.system('''mp3chaps -i "{}"'''.format(nowa_nazwa))

        # usun plik znaczników

        # os. remove('{}\\{}.chapters.txt'.format(new_folder,odcinek))
        print(odcinek,':podcast został scalony z muzyką')
    
    else:
        print(odcinek,':gotowe')

'''
sound1 = AudioSegment.from_file("/path/to/sound.wav", format="wav")
sound2 = AudioSegment.from_file("/path/to/another_sound.wav", format="wav")

# sound1 6 dB louder
louder = sound1 + 6


# sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
combined = sound1 + sound2

# simple export
file_handle = combined.export("/path/to/output.mp3", format="mp3")
'''

def r():
    pass