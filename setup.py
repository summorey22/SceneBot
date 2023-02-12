import os

try:
    os.system('conda env create -f environment.yml')
    os.system('conda activate scdt')
except Exception as e:
    print(e)