BITS_IN_BYTE = 8
BYTES_IN_KB = 1024
BYTES_IN_MB = BYTES_IN_KB * 1024
BYTES_IN_GB = BYTES_IN_MB * 1024
BYTES_IN_TB = BYTES_IN_GB * 1024

bits = float(input("Enter the number of bits: "))
bytes = bits / BITS_IN_BYTE
megabytes = bytes / BYTES_IN_MB
gigabytes = bytes / BYTES_IN_GB
terabytes = bytes / BYTES_IN_TB

print(f"{bits} Bits is equal to:")
print(f"{megabytes} Megabytes (MB)")
print(f"{gigabytes} Gigabytes (GB)")
print(f"{terabytes} Terabytes (TB)")
