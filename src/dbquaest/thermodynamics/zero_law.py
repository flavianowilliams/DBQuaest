import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = [
        '$\frac{C}{5}=\frac{K-273}{5}=\frac{F-32}{9}$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (1.1, 10, 'vezes') # min, max, unidade
        p2 = (0.001, 0.1, '$m^3/s$') # min, max, unidade

        value_1 = random_vars(p1, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um viajante, ao desembarcar no aeroporto de Londres, observou que o valor da temperatura do ambiente na escala Fahrenheit é \\num{{{value_1[i0]:7.2f}}} {p1[2]}. Qual é o valor dessa temperatura?"""

        alt_list = [{
            'choice': 160/(5*value_1[i0]-9),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 160/(5-9*value_1[i0]),
            'consideration': 'Trocou o valor da temperatura de Celsius para Fahrenheit',
            'point': 0.0
            })

        alt_list.append({
            'choice': 273/(value_1[i0]-1),
            'consideration': 'Calculou a temperatura em Kelvin ao invés de Fahrenheit',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 288/(9*value_1[i0]-5),
            'consideration': 'Errou em definir a equação de conversão de temperatura',
            'point': 0.0
            })

        alt_list.append({
            'choice': 32/(value_1[i0]-1),
            'consideration': 'Errou em definir a equação de conversão de temperatura',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\celsius}'

        for i in range(ntest):
            if i not in [i0]:
                val = 160/(5*value_1[i]-9)
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

    else:

        context = {}

    return context
