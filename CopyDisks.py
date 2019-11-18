#import wmi
import os
import shutil
import datetime
today=str(datetime.date.today())
today=(today.replace('-', ''))
print(today)
c=wmi.WMI()
disk_name=[]
for f in c.Win32_LogicalDisk():
    #print(f) #listing all available opptions from WMI
    if f.Description=="Removable Disk": #skiping local disk's
    #a = [f.Caption] #galime i zodyna spausdinti dauigiau parametru
        disk_name.append(f.Caption)
        #disk_space.append

#suresti folderi kuris prasideda tam tikru string

#if any(x.startswith(today[:6]) for x in os.listdir('D://')):
#    print('found one ')

for dirpath, dirs, files in os.walk("D://"):
    if dirpath.endswith(today+'_1') or dirpath.endswith(today) or dirpath.endswith(today+'_2'):
        print(dirpath)
  #  if any(dirpath.endswith()):
       # print (dirpath)




#reikia suzinoti kiek failu ir koks ju dydis funkcija failams suskaiciuoti

#for d in disk_name:
#    print(os.listdir(disk_name[0]))


dest1=r"C:\Users\LaurynasZenevicius\Documents\Python\Test10-23_1"
#dest_1_size
dest2=r'C:\Users\LaurynasZenevicius\Documents\Python\Test_10-23_2'
#dest_2_size
dest3=r'C:\Users\LaurynasZenevicius\Documents\Python\Test_10-23_3'
#dest_3_size
dest_pack=[dest1,dest2,dest3]

#for d,dest in disk_name,dest_pack: