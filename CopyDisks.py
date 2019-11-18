import wmi
import distutils
import os
import multiprocessing
import shutil
import datetime
today=str(datetime.date.today())
today=(today.replace('-', ''))
c=wmi.WMI()
disk_name=[]
for f in c.Win32_LogicalDisk():
    #print(f) #listing all available opptions from WMI
    if f.Description=="Removable Disk": #skiping local disk's
        disk_name.append(f.Caption)
print(disk_name)

paths=[]
for disk in disk_name: #cycking thru all external  drives
    for dirpath, dirs, files in os.walk(disk):
        if dirpath.endswith(today+'_1') or dirpath.endswith(today) or dirpath.endswith(today+'_2'):
            paths.append(dirpath)
print(paths)



dest1=r"C:\Users\LaurynasZenevicius\Documents\Python\Test10-23_1"
#dest_1_size
dest2=r'C:\Users\LaurynasZenevicius\Documents\Python\Test_10-23_2'
#dest_2_size
dest3=r"C:\Users\LaurynasZenevicius\Documents\Python\Test_10-23_3"
#dest_3_size
dest_pack=[dest1,dest2,dest3]
new_dest=[]
#creating folder of the day in all locations


for dest in dest_pack:
    path=os.path.join(dest, today)
    new_dest.append(path)
    try:
        os.makedirs(path,exist_ok=True)
    except FileExistsError:
        # directory already exists
        pass


print(new_dest)
print(paths)



#for path in paths:
#    print(path)
#https: // stackoverflow.com / questions / 39307400 / adding - multiple - directories -as-destination - when - copying - files - in -python


def copy_folder(from_, to_):

    from distutils.dir_util import copy_tree
    distutils.dir_util._path_created = {}
    distutils.dir_util.copy_tree(from_, to_)
    copy_tree(from_, to_)

for i in paths:
    for x in  new_dest:
        copy_folder(i,x)

#testing area
print('test area')
#count files in folder and space
for i in paths:
    number_files = len(list)
    print(i, number_files)
    print('num of files in:', i, (len([name for name in os.listdir(i) if  os.path.isfile(os.path.join(i, name))])))
    def get_size(start_path =i):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
             # skip if it is symbolic link
                #if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
                return total_size

    print(i,get_size(), 'bytes')


#total_size = 0
#for i in paths:
#    start_path = i  # To get size of current directory
#    for path, dirs, files in os.walk(start_path):
#        for f in dirs:
#            fp = os.path.join(path, f)
#            total_size += os.path.getsize(fp)
#        print("Directory size: " +i+' '+ str(total_size))
#testing area

#count files in folder and space