import os


# check if  that name dose exist return false 
def chack_name(name):
    cwd = os.getcwd()
    if str(name) in os.listdir(cwd):
        return False
    return True


# create_folder 
def create_folder(name):
    if chack_name(name):
        os.mkdir(f'{os.getcwd()}/{name}')
        if str(name) in os.listdir():
            raise RuntimeError( 'folder created')
        raise RuntimeError('i dont know just we have error')
    raise RuntimeError('folder dose exist')
