from pathlib import Path
import os

# Plik z danymi:
folder= '{}'.format(Path(__file__).parent)

mx=0
mx_path=''
for i,j,k in os.walk(folder):
    for l in k:
        
    print(k)

def r():
    pass        