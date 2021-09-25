import sys
print()
if sys.byteorder == 'little':
    print("little- endian platform.")
else:
    print("big- endian platform.")
print()