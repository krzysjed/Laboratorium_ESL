from myhdl import intbv
from myhdl import bin
a = intbv(12, min=0, max=16)
print(bin(a))

b = a.signed()
print(b)


print(bin(b, width=4))

data_bus = intbv(44)[8:]
print(data_bus)

real = data_bus[8:4].signed()
imag = data_bus[4:].signed()
print(real, imag)