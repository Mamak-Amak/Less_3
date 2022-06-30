from os import walk, path, listdir
import shutil

pr_name = 'my_project'

try:
    for root, dirs, files in walk(pr_name):
        if 'templates' in dirs and root != pr_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root,'templates', entry)),
                path.join(pr_name, 'templates', entry)

except FileExistsError:
    print("dfdfdfdf")





