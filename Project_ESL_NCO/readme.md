# Oscylator sterowany numerycznie (NCO)
Projekt ralizuję funkcję oscylatora sterowanego numerycznie NCO w języku MyHDL. 
Genuruje on dwie 8-bitowe fale nośne: sinus i cosinus na podstawie zaalokowanej w pamięci tablicy z próbkami ćwiartki sinusa.

Oscylator ma sterowaną częstotliwość i przesunięcie fazowe, obie to 32-bitowe dane wejśćiowe:

FCW - Frequency control word - dana definująca częstotliwość na podstawie poniższego wzoru:

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{fali}^{}=\frac{f_{clk}*FCW}{2^{32}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{fali}^{}=\frac{f_{clk}*FCW}{2^{32}}" title="f_{fali}^{}=\frac{f_{clk}*FCW}{2^{32}}" /></a>

Poff - Phase offset - dana definiująca przesunięcie fazowe na podstawie poniższego wzoru:

<a href="https://www.codecogs.com/eqnedit.php?latex=offset=\frac{2*\prod&space;*P_{off}}{2^{32}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?offset=\frac{2*\prod&space;*P_{off}}{2^{32}}" title="offset=\frac{2*\prod *P_{off}}{2^{32}}" /></a>

Wyniki symulacji zostały przedstawione poniżej:
![Symulacje](https://github.com/krzysjed/Laboratorium_ESL/blob/1a6936134bfd94e12c710d32c6bc9571c6b512f5/Project_ESL_NCO/Przyklad%20Sin_Cos.png)
Krzystając z powyższego wzoru dla użytego w symulacji zegara 50 Mhz wyznaczono częstotliwość na 11,6415 kHz co odpowiada okresowi 85,9	μs. 
Symulacja obrazuje również działanie sygnału reset oraz sygnału enable.
