import os, json
rootdir = os.getcwd()
 
for subdir, dirs, files in os.walk(rootdir):
    """
    Change the name to whatever you want to mass change in the 'if file =="Name.json" to what each json file is named in its directory.
    You can also just completely remove this if statement and it will try to perfom all operations.
    The way this works is it goes into each folder and then open each Json that you attempt to open if it exists, if it does exist then it opens the json, reads it, and then overwrites it with whatever changes you made
 
    copy and paste this print statement to after this comment block to see what all the directory names are
    print('Subdir: {}\t Dirs: {}\tFiles{}'.format(subdir,dirs,files))
    """ 
    
    if 'Boomerang' in subdir:
        #print('Doing stuff to Boomerang Monkeys only')
        for file in files:
            try:
                if file == 'AttackModel_Attack_.json':
                    to_read_from = open(os.path.join(subdir, file),'r')
                    to_write=json.load(to_read_from)
                    to_read_from.close()
 
                    to_write['range']= 99.0
                    to_write['attackThroughWalls'] = True
                    to_write['weapons'][0]['projectile']['pierce'] = 1000
                    to_write['weapons'][0]['projectile']['display'] = '98010195051b16341bab67a674472835'
                    to_write['weapons'][0]['rateFrames'] = 0
                    with open(os.path.join(subdir, file),'w') as t:
                        json.dump(to_write,t,indent=4)
                    t.close()
 
                elif file == 'AttackModel_OrbitAttack_.json':
                    to_read_from = open(os.path.join(subdir, file),'r')
                    to_write=json.load(to_read_from)
                    to_read_from.close()
 
                    to_write['weapons'][0]['rateFrames'] = 0
                    to_write['weapons'][0]['animation'] = 0
                    with open(os.path.join(subdir, file),'w') as t:
                        json.dump(to_write,t,indent=4)
                    t.close()
 
                elif file =='OrbitModel_.json':
                    to_read_from = open(os.path.join(subdir, file),'r')
                    to_write=json.load(to_read_from)
                    to_read_from.close()
 
                    to_write['projectile']['display'] = '98010195051b16341bab67a674472835'
                    to_write['projectile']["hasDamageModifiers"] = True
                    to_write['projectile']["radius"] = 9
                    to_write['projectile']["scale"] = 1.5
                    with open(os.path.join(subdir, file),'w') as t:
                        json.dump(to_write,t,indent=4)
                    t.close()
            except Exception as e:
                print(e)