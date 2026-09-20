from template import template_render
from ui import ask_name , database , pip_or_uv , docker
from fs import create_folder
from commands import inital

name = ask_name()
is_created=create_folder(name=name)
while not is_created:
    name = ask_name()
    is_created = create_folder(name=name)
db_name = database(['mongoDB' ,'mysql', 'sqlite' , 'postgresql'])
print(db_name)

pov = pip_or_uv()
print(pov)
docker = docker() 
print(docker)
if docker:
    template_render({'db_name' : db_name})
