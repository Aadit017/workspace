import re 
text=input(" please enter the text :-)")
try: 
    phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    match=re.search(phone_pattern,text)
    print(match.group())
except: 
    print(" sorry :-(")