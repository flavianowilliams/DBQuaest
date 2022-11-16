import random
from random import choice
from dbquaest.utils import random_vars
from math import pi

def question(qpoint, opt, ntest):

    g = Constants().g

    dens = 1000

    if opt == 'OPFHYS001':

        type = 'objective'

        # generating input values list
        p1 = (5, 95, '\%') # min, max, unidade
        p2 = (5, 15, 'cm') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Determine o empuxo sobre uma esfera de raio {value_2[i0]:7.2f} {p2[2]} que possui {value_1[i0]:7.2f} {p1[2]} do seu volume submerso."""

        alt_list = [{
            'choice': 4*pi*g*dens*(value_1[i0]*0.01)*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 4*pi*g*dens*(value_1[i0]*0.01)*(value_2[i0])**3/3,
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 4*pi*dens*(value_1[i0]*0.01)*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Não considerou a aceleração da gravidade',
            'point': 0.5*qpoint
            })

        alt_list.append({
            'choice': 4*pi*g*dens*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Considerou o volume total ao invés do volume submerso',
            'point': 0.25
            })

        alt_list.append({
            'choice': 4*pi*g*dens*(value_1[i0])*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Errou em definir o valor da porcentagem',
            'point': 0.25
            })

        alt_list.append({
            'choice': 4*pi*g*dens*(value_1[i0]*0.01)*(value_2[i0]*1.e-2)**2,
            'consideration': 'Considerou a área da superfície esférica ao invés do volume',
            'point': 0.25
            })

        figure = ''

        unit = 'N'

        for i in range(ntest):
            if i not in [i0]:
                val = 4*pi*g*dens*(value_1[i]*0.01)*(value_2[i]*1.e-2)**3/3
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

    elif opt == 'OPFHYS002':

        type = 'objective'

        # generating input values list
        p1 = (5, 20, 'L') # min, max, unidade
        p2 = (7000, 7000, '$kg/m^3$') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""O peso de um recipiente com água é igual ao peso do suporte e da esfera de ferro maciço (figura a). Quando a esfera suspensa é abaixada e mergulhada na água, a balança se inclina (figura b). Considere que o volume da bola é {value_1[i0]:7.2f} {p1[2]}, a densidade do ferro é {value_2[i0]:7.2f} {p2[2]} e a densidade da água é {dens} $kg/m^3$. Calcule a massa adicional que deve ser colocada no lado direito da balança a fim de equilibrá-la novamente, com a bola ainda suspensa e imersa na água."""

        alt_list = [{
            'choice': 2*dens*(value_1[i0]*1.e-3),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 2*dens*(value_1[i0]),
            'consideration': 'Errou em converter a unidade L para m3',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 2*dens*(value_1[i0]*1.e-3),
            'consideration': 'Não considerou a aceleração da gravidade',
            'point': 0.5*qpoint
            })

        alt_list.append({
            'choice': 2*value_2[i0]*(value_1[i0]*1.e-3),
            'consideration': 'Considerou a densidade do ferro ao invés da água',
            'point': 0.25
            })

        alt_list.append({
            'choice': dens*(value_1[i0]*1.e-3),
            'consideration': 'Errou em definir a fórmula do peso aparente',
            'point': 0.25
            })

        alt_list.append({
            'choice': 2*dens*(value_1[i0]*1.e-3)*g,
            'consideration': 'Calculo o peso adicional e não a massa',
            'point': 0.25
            })

        alt_list.append({
            'choice': dens*(value_1[i0]*1.e-3)*g,
            'consideration': 'Calculo o peso adicional e não a massa e errou em definir a fórmula do peso aparente',
            'point': 0.0
            })

        figure = ''

        unit = 'kg'

        for i in range(ntest):
            if i not in [i0]:
                val = 2*dens*(value_1[i]*1.e-3)
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

    else:

        context = {}

    return context

def constants():

    cte = [
        {'type': 'gravity', 'value': 10, 'unit': '$m/s^2$'}
    ]

    return cte

