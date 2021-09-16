String = input()
count = {}
vowels = 'ueoai'
for i in String:
    if i == 'ueoai' in String:
        count[i] += 1
    else:
        count[i] = 1
print(count)
# i phải nằm trong String và có chứa những từ 'ueoai'