weight = float(input())
height = float(input())
BMI = weight / (height ** 2)
print("Chỉ số BMI của tôi: "+ str(round(BMI,1)))
if BMI < 18.5:
    print("hơi gầy")
elif BMI <= 24.9:
    print("bình thường")
elif  BMI <= 29.9:
    print(" tiền béo phì")
elif BMI <= 34.9:
    print("béo phì cấp dộ 1")
elif BMI <=  39.9:
    print("béo phì cấp độ 2")
else:
    print("béo phì cấp dộ 3")