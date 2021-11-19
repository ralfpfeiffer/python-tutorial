from pathlib import Path

#Absolute Path
# 'c:\Program Files\Microsoft
# '/usr/local/bin'

#Relative Path
p = Path()
path = Path('ecommerce')
path2 = Path('emails')
#path2.mkdir()
#path2.rmdir()

print(path.exists())
print(path2.exists())

for file in p.glob('*.py'):
    print(file)




