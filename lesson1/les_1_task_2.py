"""1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака."""
c1 = 5
c2 = 6
and_op = c1 & c2
or_op = c1 & c2
or_op = c1 | c2
xor_op = c1 ^ c2
left = c1 << 2
right = c1 >> 2

print(f'Производим побитовые логические операции над числами {c1} и {c2}')
print(f'Побитовое И: {and_op}, в битах: {bin(and_op)}')
print(f'Побитовое ИЛИ: {or_op}, в битах: {bin(or_op)}')
print(f'Побитовое Ислючающее ИЛИ: {xor_op}, в битах: {bin(xor_op)}')
print(f'Побитовый сдвиг влево 5<<2 = {left}')
print(f'Побитовый сдвиг вправо 5>>2 = {right}')