import os 
import re 
def search(file,pattern=r'\d{3}-\d{3}-\d{4}'):
    f=open(file,'r')
    text=f.read()
    if re.search(pattern,file):
        return re.search(pattern,file)
    else: 
        return ' '
results=[] 
for folder,sun_folders,files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files: 
        full_path=folder+'\\'+f
        results.append(search(full_path))
for r in results: 
  #  if r!='': 
        print(r)
         
