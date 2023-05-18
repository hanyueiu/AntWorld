from PyQt5.QtGui import qRgba, qRgb
r, g, b, a = 200, 220, 250, 255

# YYH rgb进制转换
print("======内置函数=======")
print(bin(21))
print(oct(21))
print(hex(0o25))
print(hex(0b00010101))
print(int(0b00010101))

print(int(0o25))
print(int("0b00010101", base=2))
print('#%02x%02x%02x' % (r, g, b))

print("======PyQt5========")
print(bin(qRgba(r, g, b, a)))
print(qRgba(r, g, b, a) == int("%08s%08s%08s%08s" % (bin(a)[2:], bin(r)[2:], bin(g)[2:], bin(b)[2:]), base=2))
print(bin(qRgb(r, g, b)) == bin(qRgba(r, g, b, a)))
print(hex(qRgb(r, g, b)))

