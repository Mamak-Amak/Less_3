import os

path = {'my_project': [
    {'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}
]}

for key, value in path.items():
    if not os.path.exists((key)):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))

# import shutil
# import os
# from pathlib import Path
#
# dir_ = os.path.abspath(os.curdir)
#
#
#
# set = Path(f'{dir_}/my project/settings')
# mai = Path(f'{dir_}/my project/mainapp')
# adm = Path(f'{dir_}/my project/adminapp')
# aut = Path(f'{dir_}/my project/authapp')
#
#
# set.mkdir(parents=True, exist_ok=True)
# mai.mkdir(exist_ok=True)
# adm.mkdir(exist_ok=True)
# aut.mkdir(exist_ok=True)
#
#
# print(dir_)


# shutil.rmtree('my project')