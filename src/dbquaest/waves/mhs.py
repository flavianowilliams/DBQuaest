import random
from random import choice
from dbquaest.utils import random_vars
from math import sqrt

def question(qpoint, opt, ntest):

    if opt == 'OPWMHS001':

        type = 'objective'

        # generating input values list
        p1 = [100, 500, 'g'] # min, max, unidade
        p2 = [10, 100, 'N/m'] # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um objeto de massa {value_1[i0]:7.2f} {p1[2]} executa um movimento harmônico simples preso à extremidade de uma mola, cuja constante elástica é de {value_2[i0]:7.2f} {p2[2]}. Qual deve ser o comprimento de um pêndulo simples para que ele oscile com um período igual ao do objeto preso à mola?"""

        alt_list = [{
            'choice': value_1[i0]*(1.e-3)*10/value_2[i0],
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': value_1[i0]*10/value_2[i0],
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': value_1[i0]*(1.e-3)/value_2[i0],
            'consideration': 'Não considerou a aceleração da gravidade',
            'point': 0.5*qpoint
            })
#
        alt_list.append({
            'choice': value_2[i0]*(1.e-3)*10/value_1[i0],
            'consideration': 'Errou em definir a fórmula do período',
            'point': 0.10
            })

        alt_list.append({
            'choice': value_2[i0]*10/value_1[i0],
            'consideration': 'Errou em definir a fórmula do período e em converter grama para quilograma',
            'point': 0.05
            })

        figure = ''

        unit = 'm'

        for i in range(ntest):
            if i not in [i0]:
                val = value_1[i]*(1.e-3)*10/value_2[i]
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 0.01:
                    alt_list.append({
                        'choice': val,
                        'consideration': 'Alternativa errada',
                        'point': 0.0
                        })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == 'OPWMHS002':

        type = 'objective'

        # generating input values list
        p1 = [100, 500, 'g'] # min, max, unidade
        p2 = [20, 500, 'N/m'] # min, max, unidade
        p3 = [0.2, 2.0, 'J'] # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um bloco de massa {value_1[i0]:7.2f} {p1[2]} está executando um movimento harmônico simples sobre uma superfície horizontal sem atrito, preso a uma mola, também horizontal, cuja constante elástica é de {value_2[i0]:7.2f} {p2[2]}. Sabendo-se que a energia do bloco é de {value_3[i0]:7.2f} {p3[2]}, determine a amplitudo do movimento harmônico simples executado pelo bloco."""

        alt_list = [{
            'choice': sqrt(2*value_3[i0]/value_2[i0]),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': sqrt(value_2[i0]/(2*value_3[i0])),
            'consideration': 'Errou em definir a fórmula da energia do MHS',
            'point': 0.0
            })

        alt_list.append({
            'choice': 2*value_3[i0]/value_2[i0],
            'consideration': 'Errou em definir a fórmula da energia do MHS',
            'point': 0.0
            })

        figure = ''

        unit = 'm'

        for i in range(10):
            if i not in [i0]:
                alt_list.append({
                    'choice': sqrt(2*value_3[i]/value_2[i]),
                    'consideration': 'Alternativa errada',
                    'point': 0.0
                    })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == 'OPWMHS003':

        type = 'objective'

        # generating input values list
        p1 = [100, 500, 'g'] # min, max, unidade
        p2 = [20, 500, 'N/m'] # min, max, unidade
        p3 = [0.2, 2.0, 'J'] # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um bloco de massa {value_1[i0]:7.3f} {p1[2]} está executando um movimento harmônico simples sobre uma superfície horizontal sem atrito, preso a uma mola, também horizontal, cuja constante elástica é de {value_2[i0]:7.3f} {p2[2]}. Sabendo-se que a energia do bloco é de {value_3[i0]:7.3f} {p3[2]}, determine a máxima velocidade atingida pelo bloco."""

        alt_list = [{
            'choice': sqrt(2*value_3[i0]/(value_1[i0]*1.e-3)),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': sqrt(2*value_3[i0]/(value_1[i0])),
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': sqrt(2*value_3[i0]/(value_1[i0]*0.001)),
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': sqrt(2*value_1[i0]/(value_3[i0]*1.e-3)),
            'consideration': 'Errou em definir a fórmula da energia do MHS',
            'point': 0.0
            })

        alt_list.append({
            'choice': (2*value_3[i0]/(value_1[i0]*1.e-3)),
            'consideration': 'Errou em definir a fórmula da energia do MHS',
            'point': 0.0
            })

        alt_list.append({
            'choice': sqrt(value_3[i0]/(value_1[i0]*1.e-3)),
            'consideration': 'Errou em definir a fórmula da energia do MHS',
            'point': 0.0
            })

        figure = ''

        unit = 'm'

        for i in range(10):
            if i not in [i0]:
                alt_list.append({
                    'choice': sqrt(2*value_3[i]/(value_1[i]*1.e-3)),
                    'consideration': 'Alternativa errada',
                    'point': 0.0
                    })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
