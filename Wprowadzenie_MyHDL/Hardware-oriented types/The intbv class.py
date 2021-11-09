from myhdl import intbv

a = intbv(24)
print(len(a),a)

a = intbv(6, min=0, max=7)
print(len(a),a)

a = intbv(6, min=-3, max=7)
print(len(a),a)

a = intbv(6, min=-13, max=7)
print(len(a),a)
