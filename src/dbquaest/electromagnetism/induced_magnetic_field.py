from math import cos, sin
import random

def question(qpoint, opt):

    if opt == 'OEIMF001':

        type = 'objective'

        p1 = [1.0e-6, 1.0e-5, 'C'] # min, max
        p2 = [0.1, 1.0, 'T'] # min, max
        p3 = [1.0e3, 5.0e3, 'm/s'] # min, max
        p4 = [0, 90, 'graus'] # min, max

        value_1 = random.uniform(p1[0], p1[1])
        value_2 = random.uniform(p2[0], p2[1])
        value_3 = random.uniform(p3[0], p3[1])
        value_4 = random.uniform(p4[0], p4[1])

        alt_list = [{'choice': value_1*value_2*value_3*sin(value_4*3.14/180), 'unit': ' N', 'point': qpoint}]
        alt_list.append({'choice': value_1*value_2*value_3*sin(value_4), 'unit': ' N', 'point': 0.75*qpoint})
        alt_list.append({'choice': value_1*value_2*value_3*cos(value_4*3.14/180), 'unit': ' N', 'point': 0.25*qpoint})
        alt_list.append({'choice': value_1*value_2*value_3*value_4, 'unit': ' N', 'point': 0.25*qpoint})

        text = f"""Uma partícula de carga {value_1:.2e} {p1[2]} é lançada em um campo magnético uniforme de {value_2:7.2f} {p2[2]} , com uma velocidade de {value_3:5.2f} {p3[2]}. Calcule o valor da força magnética atuando na carga se o ângulo entre a velocidade e o campo magnético for {value_4:7.2f} {p4[2]}."""

        figure = ''

        for i in range(6):
            value_1 = random.uniform(p1[0], p1[1])
            value_2 = random.uniform(p2[0], p2[1])
            value_3 = random.uniform(p3[0], p3[1])
            value_4 = random.uniform(p4[0], p4[1])
            alt_list.append({'choice': value_1*value_2*value_3*sin(value_4*3.14/180), 'unit': ' N', 'point': 0.0})

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'alternative': alternative_list}

    else:

        context = {}

    return context
