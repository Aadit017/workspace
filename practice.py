from colorama import Fore
f=open('prc.txt','w')
f.write("this is a test string :-)")
f.close()
import os 
print(Fore.GREEN+(os.getcwd()))
print(Fore.LIGHTCYAN_EX+' ')
print((os.listdir('C:\\Users\\GOD')))
print(Fore.WHITE+"")
import shutil 
a=open('prc_2.txt','w+')
a.write('this has to be moved ')
a.close()
#shutil.move('prc_2.txt','C:\\Users\\GOD')
#for folder,subfolder,files in os.walk('C:\\Users\\GOD'): 
   # print(f'cuurently {folder},{subfolder},{files}')
    
