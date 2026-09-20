import os

def install_packeage(name):
    os.system(f'uv add {name}')
    os.system(f'uv pip install {name}')
    return

def inital(path : str , name:str):
    
    os.system(f'uv init {path}/{name}')
    return 'created'
