from myhdl import Signal, ConcatSignal, intbv

M = 5
request_list = [Signal(bool()) for i in range(M)]  # signal
print(request_list)
request_vector = ConcatSignal(*reversed(request_list))  # signal to bit vector
print(request_vector)

grant_vector = Signal(intbv(5)[M:])  # bit vector
print(grant_vector)
grant_list = [grant_vector(i) for i in range(M)]  # bit vector to signal
print(grant_list)