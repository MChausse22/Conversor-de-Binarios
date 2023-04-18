
print('\nNome do projeto: Conversor de números reais para binário')
print('\nIntegrantes do grupo:\n- Ryan do Nascimento Maciel\n- Matheus Chaussê Xavier')

n = float(input("\nDado de entrada: "))

def bin_real(num, bits):
    exp = -1
    n = num
    inf = ''
    sup = ''

    for i in range(1, bits + 1):  # monta o binario inferior
        if n - 2 ** exp > 0:
            n = n - 2 ** exp
            inf += '1'
        else:
            inf += '0'
        exp -= 1
    dec_inf = 0
    for i in range(len(inf)):  # conversão bin_inf para decimal
        if inf[i] == '1':
            dec_inf += 2 ** -(i + 1)
    j = len(inf) - 1
    while inf[j] == '1' and j >= 0:  # soma 1 no binario inferior
        sup = '0' + sup
        j -= 1
    sup = '1' + sup  # digito somado
    j -= 1
    while j >= 0:  # termina a soma repetindo os digitos inalterados
        sup = inf[j] + sup
        j -= 1
    dec_sup = 0
    if len(sup) == bits:  # checar se o limite superior não é 1
        for i in range(len(sup)):  # conversão bin_sup para decimal
            if sup[i] == '1':
                dec_sup += 2 ** -(i + 1)
    else:
        dec_sup = 1.0

    num_abs_i = abs(num - dec_inf) / num
    num_abs_s = abs(num - dec_sup) / num
    
    print('Com', bits, 'bits')
    print('Aproximação a menor:', '0.' + inf, '->', dec_inf, 'com erro =', f'{num_abs_i:.4%}')
    print('Aproximação a maior:', '0.' + sup, '->', dec_sup, 'com erro =', f'{num_abs_s:.4%}')

print('\nResultados\n')
for bits in range(5, 17):
    bin_real(n, bits)
    print()


