import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    e = cte('proton charge')
    e_value = e['value']

    cte_list = [
        f"{e['symbol']}={e['value']} {e['unit']}"
    ]

    formula_list = []

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (0.25, 12, '\\unit[per-mode = symbol]{\\volt}') # min, max, unidade
        p2 = (0.1, 5, '\\unit[per-mode = symbol]{\\ampere}') # min, max, unidade
        p3 = (1, 60, '\\unit[per-mode = symbol]{\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""A unidade de energia comumente utilizada em física atômica é o elétron-Volt (eV). Um elétron-Volt pode representar a energia do estado fundamental do átomo de hidrogênio, que equivale a -13,6 eV. Isso torna conveniente expressar a energia dos elétrons no átomo em elétron-Volts ao invés de Joule. Determine o trabalho que uma bateria de \\num{{{value_1[i0]:7.2f}}} {p1[2]} realiza para produzir \\num{{{value_2[i0]:7.2f}}} {p2[2]} de corrente durante \\num{{{value_3[i0]:7.2f}}} {p3[2]}."""

        alt_list = [{
            'choice': value_1[i0]*value_2[i0]*value_3[i0]/e_value,
            'consideration': 'Alternativa correta.',
            'point': qpoint
            }]

        alt_list.append({
            'choice': -13.6,
            'consideration': 'Errou em definir o trabalho realizado pela bateria.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]*value_2[i0],
            'consideration': 'Errou em definir o trabalho realizado pela bateria e em converter a unidade Joule para elétron-Volt.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]*value_2[i0]/e_value,
            'consideration': 'Errou em definir o trabalho realizado pela bateria.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_2[i0],
            'consideration': 'Errou em definir o trabalho realizado pela bateria.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0],
            'consideration': 'Errou em definir o trabalho realizado pela bateria.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]*value_2[i0]*value_3[i0],
            'consideration': 'Errou em converter a unidade Joule para elétron-Volt.',
            'point': 0.75
            })

        figure = ''

        unit = '\\unit{\electronvolt}'

        for i in range(ntest):
            if i not in [i0]:
                val = value_1[i]*value_2[i]*value_3[i]/e_value
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

    elif opt == '001':

        type = 'conceptual'

        text = f"""Conceptual question"""

        alt_list = [{'choice': '','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': '','consideration': '','point': 0.0})
        alt_list.append({'choice': '','consideration': '','point': 0.0})
        alt_list.append({'choice': '','consideration': '','point': 0.0})
        alt_list.append({'choice': '','consideration': '','point': 0.0})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
