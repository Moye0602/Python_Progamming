import shutil
path=__file__.split('/')
path=('/').join(path[:-1])
source_path =path+'stuff'+'.py'
destination_path = path+'stuff'+'_dup.py'
shutil.copy(source_path, destination_path)
print('backup of ','stuff', 'complete')
