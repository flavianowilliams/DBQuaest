import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = [
        '$A_1v_1=A_2v_2$',
        '$p_1+\rho gh_1+\frac{\rho v^2_1}{2}=p_2+\rho gh_2+\frac{\rho v^2_2}{2}$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (100, 500, '\\unit{\square\centi\metre}') # min, max, unidade
        p2 = (0.001, 0.1, '\\unit[per-mode = symbol]{\cubic\metre\per\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Em um cano que possui uma área de seção reta de \\num{{{value_1[i0]:7.2f}}} {p1[2]} atravessa água com uma vazão de \\num{{{value_2[i0]:7.2f}}} {p2[2]}. Qual é a velocidade de escoamento da água nesse cano?"""

        alt_list = [{
            'choice': value_2[i0]/(value_1[i0]*1.e-4),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': value_2[i0]/(value_1[i0]*1.e-2),
            'consideration': 'Errou em converter a unidade cm2 para m2',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': value_2[i0]/(value_1[i0]),
            'consideration': 'Errou em converter a unidade cm2 para m2',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': value_1[i0]/(value_2[i0]*1.e-4),
            'consideration': 'Errou em definir a fórmula da vazão',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]*(value_2[i0]*1.e-4),
            'consideration': 'Errou em definir a fórmula da vazão',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]/(value_2[i0]*1.e-2),
            'consideration': 'Errou em definir a fórmula da vazão e em converter a unidade cm2 para m2',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]/(value_2[i0]),
            'consideration': 'Errou em definir a fórmula da vazão e em converter a unidade cm2 para m2',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]*(value_2[i0]*1.e-2),
            'consideration': 'Errou em definir a fórmula da vazão e em converter a unidade cm2 para m2',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]*(value_2[i0]),
            'consideration': 'Errou em definir a fórmula da vazão e em converter a unidade cm2 para m2',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit[per-mode = symbol]{\metre\per\second}'

        for i in range(ntest):
            if i not in [i0]:
                val = value_2[i]/(value_1[i]*1.e-4)
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
