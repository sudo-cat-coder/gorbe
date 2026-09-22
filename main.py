from re import U

from template import docker_template ,fastapi_project , database_template
from ui import ask_name , database , pip_or_uv , docker , wanrning , user_perfrence_for_database , framework
from fs import create_folder
from commands import uv_inital , venv , install_package_pip , django_start , git_init

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
    install_package_pip(['cowsay' , 'requests'] , path=is_created['path'])
    if framework_name == 'Django':
        django_start(name=name)
    if framework_name == 'FastAPI':
        fastapi_project(name=name , pov='pip' ,path=PIP_PATH)
        database_template(content={'db_name' : db_name} , path=PIP_PATH , name=name , pov='pip')
    if docker :

        content = {**user_perfrence_for_database(db_name) , 'db_name' : db_name}
        docker_template(content , path=PIP_PATH ,framework_name=framework_name)
    git_init(path=PIP_PATH)


if pov == 'uv':
    uv_inital(path=is_created['path'] , name=name , packages=[framework_name])
    if framework_name == 'Django':
        django_start(name=name)
    if framework_name == 'FastAPI':
        fastapi_project(name=name , pov='uv')
        database_template({'db_name' : db_name},path=UV_PATH , pov='uv',name=name)
    if docker:

        content = {**user_perfrence_for_database(db_name) , 'db_name' : db_name}
        docker_template(content , path=UV_PATH ,framework_name=framework_name)

    git_init(path=UV_PATH)




if pov == 'uv':
    wanrning(path=UV_PATH)
if pov == 'pip':
    wanrning(path=PIP_PATH)
