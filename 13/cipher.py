import string
lkey=string.ascii_lowercase
ukey=string.ascii_uppercase
rotation=int(input("enter how many rotations :"))
text=input("enter your text:")
decrypt=''
for i in range(0,len(text)):
  if(text[i] in lkey):
    char=lkey.index(text[i])
    c=(char+13)%26
    decrypt+=lkey[c]
  elif(text[i] in ukey):
    char=ukey.index(text[i])
    c=(char+13)%26
    decrypt+=ukey[c]
  elif (text[i]=='_'):
    decrypt+='_'
  else:
    decrypt+=text[i]
print(decrypt)
