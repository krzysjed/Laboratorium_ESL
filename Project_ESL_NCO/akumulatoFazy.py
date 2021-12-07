from myhdl import block, always_seq,intbv


@block
def PA(acc, count, p_off, enable, clock, reset):
    """ Phase accumulation.
    acc -- wave samples index
    count --  incrementer output
    p_off -- phase offset
    enable -- control input
    clock -- clock input
    reset -- asynchronous reset input
    """

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            acc.next = intbv(count + p_off)[33:21]

    return seq


