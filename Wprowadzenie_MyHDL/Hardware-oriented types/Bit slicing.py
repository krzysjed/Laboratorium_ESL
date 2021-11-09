from myhdl import intbv
from myhdl import bin

a = intbv(24)
print(bin(a))
'11000'

print(a[4:1])

print(intbv(4))

print(bin(a[4:1]))

a[4:1] = 0b001

print(bin(a))

print(intbv(18))

print(bin(a))
'11000'
print(bin(a[4:]))
'1000'
a[4:] = '0001'
print(bin(a))
'10001'
a[:] = 0b10101
print(bin(a))
'10101'
a = intbv(24)[5:]
print(a)