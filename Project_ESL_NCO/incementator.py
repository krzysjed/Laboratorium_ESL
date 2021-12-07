from myhdl import block, always_seq


@block
def inc(count, FCW, enable, clock, reset):

    """ Incrementer with enable.
    count -- output
    FCW -- Frequency Control Word
    enable -- control input
    clock -- clock input
    reset -- asynchronous reset input
    """

    @always_seq(clock.posedge, reset=reset)
    def seq():
        if enable:
            count.next = count + FCW
    return seq


