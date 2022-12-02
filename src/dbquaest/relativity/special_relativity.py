import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte
from math import sqrt

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = []

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (0.1, 0.99, 'c') # min, max, unidade
        p2 = (1, 5, '\\unit[per-mode = symbol]{\micro\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Uma partícula é produzida a uma certa altitude da atmosfera terrestre a uma velocidade igual a \\num{{{value_1[i0]}}} {p1[2]} decaindo em seguida em outras subpartículas depois de \\num{{{value_2[i0]}}} {p2[2]}. Determine o tempo que essa partícula duraria em um laboratório a uma velocidade muito menor que c antes do seu decaimento radioativo."""

        alt_list = [{
            'choice': value_2[i0]*sqrt(1-value_1[i0]**2),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': value_2[i0]/sqrt(1-value_1[i0]**2),
            'consideration': 'Errou em definir a dilatação do tempo.',
            'point': 0.25
            })

        alt_list.append({
            'choice': value_2[i0]/sqrt(1-value_1[i0]),
            'consideration': 'Errou em calcular o fator de Lorentz.',
            'point': 0.25
            })

        alt_list.append({
            'choice': value_2[i0]*sqrt(1-value_1[i0]),
            'consideration': 'Errou em calcular o fator de Lorentz.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_2[i0]/(1-value_1[i0]**2),
            'consideration': 'Errou em calcular o fator de Lorentz.',
            'point': 0.25
            })

        alt_list.append({
            'choice': value_2[i0]/value_1[i0],
            'consideration': 'Errou em calcular o fator de Lorentz.',
            'point': 0.25
            })

        figure = ''

        unit = '\\unit{\micro\second}'

        for i in range(ntest):
            if i not in [i0]:
                val = value_1[i]
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 0.01:
                    alt_list.append({
                    'choice': val,
                    'consideration': 'Alternativa errada',
                    'point': 0.0
                    })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == '002':

        type = 'conceptual'

        text = f"""Um astronauta numa futura estação espacial nota uma nave aproximando-se a 40\% da velocidade da luz. Em sentido oposto e numa trajetória paralela, ele observa um meteoróide indo de encontro à nave a 80\% da velocidade da luz. Com que velocidade os tripulantes da nave observam o meteoróide?"""

        alt_list = [{'choice': 'Abaixo de c.','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': 'Acima de 1,2c.','consideration': 'A velocidade do meteoróide não pode ser maior que c.','point': 0.0})
        alt_list.append({'choice': 'Exatamente igual a 1,2c.','consideration': 'A velocidade do meteoróide não pode ser maior que c.','point': 0.0})
        alt_list.append({'choice': 'Acima de c','consideration': 'A velocidade do meteoróide não pode ser maior que c.','point': 0.0})
        alt_list.append({'choice': 'Exatamente igual a c.','consideration': 'Nenhum objeto com massa diferente de zero pode assumir a velocidade igual a c.','point': 0.0})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
