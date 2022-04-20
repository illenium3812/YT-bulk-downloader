# YT-bulk-downloader
YouTube bulk video download and for training of your Machine learning model. All the time clipped videos will be saved in clipped folder

## Installation
```
pip3 install -r requirements.txt
```

There are some bugs in the pytube lib raises RegexMatchErrors , so to fix them make these changes to cipher.py of the the package:

Changing the regex in **function_patterns** in cipher.py to:
```
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'
```

Changing **line 288** to:
```
nfunc=re.escape(function_match.group(1))),
```

cipher.py is present in lib folder of site-packages, incase you cant find it use this code to the get the address of site-packages:
```
from distutils.sysconfig import get_python_lib
print(get_python_lib())
```

## How to use

cd the project folder run this command: python YT-bulk-download.py **"Your Label you want to extract videos"**

### Example:
```
python YT-bulk-download.py "welding"
```
![image](https://user-images.githubusercontent.com/41062288/164191410-13d96496-703e-4422-8242-c2f22b8681cc.png)


