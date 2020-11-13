import json, os
import random as r
from datetime import datetime
 
r.seed(datetime.now())
 
path_to_json = os.getcwd().replace('\\','/') + '/Jet/Towers'
path_to_replace = os.getcwd().replace('\\','/') + '/JetCompiled/Towers'
try:
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
except FileNotFoundError as e:
    print('Rerun BTD6 and then try again')
    a = input('Press enter to continue...')
    exit()
 
for file in json_files:
    this_file = path_to_json + '/' + file
    read_only = open(this_file,'r')
    json_to_overwrite = json.load(read_only)
    read_only.close()
    if r.randint(0,10) > 7:
        json_to_overwrite['isSubTower'] = True
        with open(this_file,'w') as updated_file:
            json.dump(json_to_overwrite,updated_file,indent=4)
            updated_file.close()
            os.replace(this_file, path_to_replace +'/'+ file)
    else:
        os.remove(this_file)