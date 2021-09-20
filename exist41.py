str = input()
import pathlib
file = pathlib.Path(str)
if file.exists():
    print('file exist')
else:
    print('file not exist')