from template import template_render
from ui import ask_name , database , pip_or_uv , docker , wanrning
from fs import create_folder
from commands import inital , venv , install_package_pip

name = ask_name()
is_created=create_folder(name=name)
while not is_created['state']:
    name = ask_name()
    is_created = create_folder(name=name)
if is_created['state']:
    print(is_created['path'])
db_name = database(['mongoDB' ,'mysql', 'sqlite' , 'postgresql'])
print(db_name)

pov = pip_or_uv()
if pov == 'pip':
    venv(path=is_created['path'])
    install_package_pip('cowsay' , path=is_created['path'])
docker = docker() 
print(docker)
if docker:
    template_render({'db_name' : db_name} , path= is_created['path'])

wanrning(path=is_created['path'])
