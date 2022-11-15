import random
from random import choice
from dbquaest.utils import random_vars

def question(qpoint, opt):

    if opt == 'OPWMHS001':

        type = 'objective'

        # generating input values list
        p1 = (200, 400, 'g') # min, max, unidade
        p2 = (20, 60, 'N/m') # min, max, unidade

        value_1 = random_vars(p1, 10)
        value_2 = random_vars(p2, 10)

        i0 = choice([i for i in range(10)])

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

        alt_list.append({
            'choice': value_2[i0]*(1.e-3)*10/value_1[i0],
            'consideration': 'Errou em definir a fórmula do período',
            'point': 0.0
            })

        text = f"""Um objeto de massa {value_1[i0]:7.2f} {p1[2]} executa um movimento harmônico simples preso à extremidade de uma mola, cuja constante elástica é de {value_2[i0]:7.2f} {p2[2]}. Qual deve ser o comprimento de um pêndulo simples para que ele oscile com um período igual ao do objeto preso à mola?"""

        figure = ''

        unit = 'm'

        for i in range(10):
            if i not in [i0]:
                alt_list.append({
                    'choice': value_1[i],
                    'consideration': 'Alternativa errada',
                    'point': 0.0
                    })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
