from myhdl import block, always, instance, Signal, \
    ResetSignal, modbv, delay, StopSimulation
from incementator import inc
from akumulatoFazy import PA
from genFali import wave
#  Autorzy: Piotr Prusak, Krzysztof Jędrejasz

@block
def testbench():

    count = Signal(modbv(0)[32:])
    FCW = Signal(modbv(1000000)[32:])
    Poff = Signal(modbv(100)[32:])
    Acc = Signal(modbv(0)[11:])

    enable = Signal(bool(1))
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, isasync=True)

    sin = Signal(modbv(0)[8:])
    cos = Signal(modbv(0)[8:])

    inc_1 = inc(count, FCW, enable, clock, reset)
    pa_1 = PA(Acc, count, Poff, enable, clock, reset)
    wave_1 = wave(Acc, sin, cos, enable, clock, reset)
    HALF_PERIOD = delay(10)

    @always(HALF_PERIOD)
    def clockGen():
        clock.next = not clock

    @instance
    def stimulus():
        for i in range(10000):
            yield clock.negedge
        reset.next = 1
        for i in range(100):
            yield clock.negedge
        reset.next = 0
        for i in range(1000):
            yield clock.negedge
        enable.next = 0
        for i in range(1000):
            yield clock.negedge
        raise StopSimulation
    return clockGen, stimulus, inc_1, pa_1, wave_1


tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()
