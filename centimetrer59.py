h_feet = int(input())
h_inch = int(input())
h_inch += h_feet * 12
h_cm = round(h_inch * 2.54, 1)
print('your height: %d cm.' % h_cm)