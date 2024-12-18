import struct


byte_stream = struct.pack("iii", 10, 20, 30)
print(byte_stream)
print(struct.calcsize('i'))

a = struct.unpack('iii', byte_stream)
print(a)

company = b'johndoe'
day, month, year = 1, 2, 2024
awesome = True

steam = struct.pack("10s 3i ?", company, day, month, year, awesome)
print(steam)
c, d, m, y, a = struct.unpack("10s 3i ?", steam)
print(c)
print(d)
print(m)
print(y)
print(a)