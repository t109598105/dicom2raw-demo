import os

for i in os.listdir('.'):
    if not i == 'rename.py':
        os.rename(i, i+'.dcm')