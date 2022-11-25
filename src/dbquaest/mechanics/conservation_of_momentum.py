import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = [
        '$\vec{F}_{\text{res}}=\frac{d\vec{P}}{dt}$',
        '$\vec{J}=\Delta\vec{P}=\int^{t_f}_{t_i}\vec{F}_{\text{res}}dt$',
        '$\vec{p}=m\vec{v}$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (100, 500, '\\unit{\gram}') # min, max, unidade
        p2 = (1, 25, '\\unit[per-mode = symbol]{\metre\per\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Uma partícula, de massa \\num{{{value_1[i0]:7.2f}}} {p1[2]}, descreve um movimento circular uniforme com velocidade \\num{{{value_2[i0]:7.2f}}} {p2[2]}. Calcule o impulso que a força centrípeta exerce sobre a partícula durante um intervalo de tempo equivalente à metade do período desse movimento.
        
        """

        alt_list = [{
            'choice': 2*(value_1[i0]*1.e-3)*value_2[i0],
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': (value_1[i0]*1.e3)*value_2[i0],
            'consideration': 'Errou em definir a variação da quantidade de movimento e converter a unidade grama para quilograma',
            'point': 0.25
            })

        alt_list.append({
            'choice': (value_1[i0])*value_2[i0],
            'consideration': 'Errou em em definir a variação da quantidade de movimento e converter a unidade grama para quilograma',
            'point': 0.25
            })

        alt_list.append({
            'choice': 2*(value_1[i0]*1.e3)*value_2[i0],
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75
            })

        alt_list.append({
            'choice': 2*(value_1[i0])*value_2[i0],
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75
            })

        alt_list.append({
            'choice': 0.0,
            'consideration': 'Errou em definir a variação da quantidade de movimento',
            'point': 0.5
            })

        alt_list.append({
            'choice': (value_1[i0]*1.e-3)*value_2[i0],
            'consideration': 'Errou em definir a variação da quantidade de movimento',
            'point': 0.5
            })

        figure = ''

        unit = '\\unit{\\newton\\cdot\second}'

        for i in range(ntest):
            if i not in [i0]:
                val = 2*(value_1[i]*1.e-3)*value_2[i]
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

        type = 'objective'

        # generating input values list
        p1 = (500, 800, '\\unit{\kilo\gram}') # min, max, unidade
        p2 = (900, 2000, '\\unit{\kilo\gram}') # min, max, unidade
        p3 = (20, 70, '\\unit[per-mode = symbol]{\metre\per\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Considere um sistema constituído por um automóvel, de massa \\num{{{value_1[i0]}}} {p1[2]} e um caminhão de massa \\num{{{value_2[i0]}}} {p2[2]}. Determine o módulo da quantidade de movimento do centro de massa do sistema, considerando que o automóvel e o caminhão se movimentam na mesma direção a \\num{{{value_3[i0]}}} {p3[2]}, mas em sentidos opostos.
        
        """

        alt_list = [{
            'choice': abs(value_3[i0]*(value_1[i0]-value_2[i0])),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': abs(value_3[i0]*(value_1[i0]+value_2[i0])),
            'consideration': 'Errou em considerar que os automóveis estão em movimento no mesmo sentido',
            'point': 0.0
            })

        alt_list.append({
            'choice': abs((value_1[i0]+value_2[i0])),
            'consideration': 'Errou em definir o cálculo da quantidade de movimento do automóvel',
            'point': 0.0
            })

        alt_list.append({
            'choice': abs((value_1[i0]-value_2[i0])),
            'consideration': 'Errou em definir o cálculo da quantidade de movimento do automóvel',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\kilo\gram\cdot\metre\per\second}'

        for i in range(ntest):
            if i not in [i0]:
                val = abs(value_3[i]*(value_1[i]-value_2[i]))
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 0.00001:
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
