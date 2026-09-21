from template import docker_template
from ui import ask_name , database , pip_or_uv , docker , wanrning , user_perfrence_for_database , framework
from fs import create_folder
from commands import uv_inital , venv , install_package_pip , django_start

name = ask_name()
is_created=create_folder(name=name)
while not is_created['state']:
    name = ask_name()
    is_created = create_folder(name=name)

UV_PATH = f'{is_created['path']}/{name}'
PIP_PATH = f'{is_created['path']}'
framework_name = framework()

db_name = database(['mysql', 'sqlite' , 'postgresql' ])

pov = pip_or_uv()
docker = docker()
if pov == 'pip':
    venv(path=is_created['path'])
    install_package_pip('cowsay' , path=is_created['path'])
    if docker :

        content = {**user_perfrence_for_database(db_name) , 'db_name' : db_name}
        docker_template(content , path=PIP_PATH)


if pov == 'uv':
    uv_inital(path=is_created['path'] , name=name , package=framework_name)
    if framework_name == 'Django':
        django_start(name=name)
    if docker:

        content = {**user_perfrence_for_database(db_name) , 'db_name' : db_name}
        docker_template(content , path=UV_PATH)




if pov == 'uv':
    wanrning(path=UV_PATH)
if pov == 'pip':
    wanrning(path=PIP_PATH)
