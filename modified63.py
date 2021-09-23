import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime('email.py')))
print("created: %s" % time.ctime(os.path.getctime('email.py')))