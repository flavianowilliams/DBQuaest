import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    h = cte('Planck constant (eV)')
    h_value = h['value']

    h2 = cte('Planck constant')
    h2_value = h2['value']

    c = cte('speed of light')
    c_value = c['value']

    cte_list = [
        f"{h['symbol']}={h['value']} {h['unit']}",
        f"{h2['symbol']}={h2['value']} {h2['unit']}",
        f"{c['symbol']}={c['value']} {c['unit']}"
    ]

    formula_list = [
        '$\lambda=\frac{h}{p}$',
        '$E=h\nu$',
        '$eV=h\nu-\phi$'
    ]

    if opt == '001':

        type = 'objective'

        p1 = (2.28, 2.28, 'eV') # Work function of Sodium
        p2 = (100, 540, 'nm')

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""A função trabalho do sódio é \\num{{{value_1[i0]:7.2f}}} {p1[2]}, determine a energia cinética dos elétrons que são emitidos desse material quando ele é bombardeado por radiação com comprimento de onda de \\num{{{value_2[i0]:7.2f}}} {p2[2]}."""

        alt_list = [{
            'choice': h_value*c_value/(value_2[i0]*1.e-9)-value_1[i0],
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': h_value*c_value/(value_2[i0])-value_1[i0],
            'consideration': 'Errou em converter a unidade nanometro para metro',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': h_value*c_value/(value_2[i0]*1.e-9)+value_1[i0],
            'consideration': 'Errou em definir a equação do efeito fotoelétrico',
            'point': 0.0
            })

        alt_list.append({
            'choice': h_value*c_value*(value_2[i0]*1.e-9)-value_1[i0],
            'consideration': 'Errou em definir a expressão da velocidade da luz',
            'point': 0.0
            })

        alt_list.append({
            'choice': h_value*(value_2[i0]*1.e-9)-value_1[i0],
            'consideration': 'Utilizou o comprimento de onda ao invés da frequência na equação do efeito fotoelétrico',
            'point': 0.0
            })

        alt_list.append({
            'choice': h_value*c_value/(value_2[i0]*1.e-9),
            'consideration': 'Não considerou a função trabalho na equação do efeito fotoelétrico',
            'point': 0.0
            })

        figure = ''

        unit = 'eV'

        for i in range(ntest):
            if i != i0:
                val = h_value*c_value/(value_2[i]*1.e-9)-value_1[i]
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

        p1 = [100, 200, '\\unit{\gram}']
        p2 = [80, 200, '\\unit[per-mode = symbol]{\kilo\metre\per\hour}']

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Calcule o comprimento de onda de uma bola de basebol que possui uma massa de \\num{{{value_1[i0]}}} {p1[2]} a uma velocidade de \\num{{{value_2[i0]}}} {p2[2]}. Seria possível observar os efeitos da física quântica nesse caso?"""

        alt_list = [{
            'choice': h2_value*1.e9/((value_1[i0]*1.0e-3)*(value_2[i0]/3.6)),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': h2_value/((value_1[i0]*1.0e-3)*(value_2[i0]/3.6)),
            'consideration': 'Errou em converter a unidade metro para nanometro',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': h2_value*1.e9/((value_1[i0])*(value_2[i0]/3.6)),
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': h2_value*1.e9/((value_1[i0]*1.0e-3)*(value_2[i0])),
            'consideration': 'Errou em converter a unidade km/h para m/s',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': h2_value*1.e9/(value_1[i0]*value_2[i0]),
            'consideration': 'Errou em converter as unidades km/h para m/s e grama para quilograma',
            'point': 0.5*qpoint
            })

        alt_list.append({
            'choice': h2_value*1.e9/((value_1[i0]*1.0e+3)*(value_2[i0]/3.6)),
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75
            })

        alt_list.append({
            'choice': h2_value*1.e9/((value_1[i0]*1.0e-3)*(value_2[i0]*3.6)),
            'consideration': 'Errou em converter a unidade km/h para m/s',
            'point': 0.75
            })

        alt_list.append({
            'choice': h2_value*1.e9/((value_1[i0]*1.0e+3)*(value_2[i0]*3.6)),
            'consideration': 'Errou em converter as unidades km/h para m/s e grama para quilograma',
            'point': 0.5
            })

        alt_list.append({
            'choice': h2_value*1.e9/((value_2[i0]/3.6)),
            'consideration': 'Não incluiu a massa na expressão de de Broglie',
            'point': 0.0
            })

        alt_list.append({
            'choice': h2_value*1.e9*((value_1[i0]*1.0e-3)*(value_2[i0]/3.6)),
            'consideration': 'Errou em definir a expressão de de Broglie',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\\nano\metre}'

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
