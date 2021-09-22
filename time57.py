import time
def thuat_toan():
    for i in range(1, 11):
        print(i)
start_time = time.time()
thuat_toan()
end_time = time.time()
elapsed_time = end_time - start_time
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")