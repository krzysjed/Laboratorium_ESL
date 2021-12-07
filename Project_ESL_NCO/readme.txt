Oscylator sterowany numerycznie (NCO)
Projekt ralizuję funkcję oscylatora sterowanego numerycznie NCO w języku MyHDL. 
Genuruje on dwie 8-bitowe fale nośne: sinus i cosinus na podstawie zaalokowanej w pamięci tablicy z próbkami ćwiartki sinusa.
Oscylator ma sterowaną częstotliwość i przesunięcie fazowe, obie to 32-bitowe dane wejśćiowe:
FCW - Frequency control word - dana definująca częstotliwość na podstawie poniższego wzoru:
Częstotliwość fali = (FCW * częstotliwość zegara)/(2^32)
Poff - Phase offset - dana definiująca przesunięcie fazowe na podstawie poniższego wzoru:
Przesunięcie fazowe = (Poff * 2 * pi)/(2^32)
Wyniki symulacji zostały przedstawione w pliku Przyklad Sin_Cos.png
