ten = input()
mssv = input()
list_ten = ten.split()
ten = list_ten[len(list_ten)-1] + '.'
ho = ''
for i in range(0, len(list_ten)-1):
    ho += list_ten[i]
mssv = mssv[3:]
email = ten + ho + mssv + '@gmail.uit.edu.vn'
print(email.lower())

