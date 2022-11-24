import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte
from math import pi

def question(qpoint, opt, ntest):

    # constants

    g = cte('gravity')
    g_value = g['value']

    dens = cte('water density')
    dens_value = dens['value']

    cte_list = [
        f"{g['symbol']}={g['value']} {g['unit']}",
        f"{dens['symbol']}={dens['value']} {dens['unit']}"
        ]

    formula_list = [
        '$p=\frac{F}{A}$',
        '$\rho=\frac{m}{V}$',
        '$p_2=p_1+\rho g h$',
        '$\frac{F_1}{A_1}=\frac{F_2}{A_2}$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (5, 95, '\%') # min, max, unidade
        p2 = (5, 15, '\\unit{\centi\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Determine o empuxo sobre uma esfera de raio \\num{{{value_2[i0]:7.2f}}} {p2[2]} que possui \\num{{{value_1[i0]:7.2f}}} {p1[2]} do seu volume submerso."""

        alt_list = [{
            'choice': 4*pi*g_value*dens_value*(value_1[i0]*0.01)*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 4*pi*g_value*dens_value*(value_1[i0]*0.01)*(value_2[i0])**3/3,
            'consideration': 'Errou em converter a unidade grama para quilograma',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 4*pi*dens_value*(value_1[i0]*0.01)*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Não considerou a aceleração da gravidade',
            'point': 0.5*qpoint
            })

        alt_list.append({
            'choice': 4*pi*g_value*dens_value*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Considerou o volume total ao invés do volume submerso',
            'point': 0.25
            })

        alt_list.append({
            'choice': 4*pi*g_value*dens_value*(value_1[i0])*(value_2[i0]*1.e-2)**3/3,
            'consideration': 'Errou em definir o valor da porcentagem',
            'point': 0.25
            })

        alt_list.append({
            'choice': 4*pi*g_value*dens_value*(value_1[i0]*0.01)*(value_2[i0]*1.e-2)**2,
            'consideration': 'Considerou a área da superfície esférica ao invés do volume',
            'point': 0.25
            })

        figure = ''

        unit = '\\unit{\\newton}'

        for i in range(ntest):
            if i not in [i0]:
                val = 4*pi*10*dens_value*(value_1[i]*0.01)*(value_2[i]*1.e-2)**3/3
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
        p1 = (5, 20, '\\unit{\litre}') # min, max, unidade
        p2 = (7000, 7000, '\\unit[per-mode = symbol]{\kilo\gram\per\cubic\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""O peso de um recipiente com água é igual ao peso do suporte e da esfera de ferro maciço (figura a). Quando a esfera suspensa é abaixada e mergulhada na água, a balança se inclina (figura b). Considere que o volume da bola é \\num{{{value_1[i0]:7.2f}}} {p1[2]}, a densidade do ferro é \\num{{{value_2[i0]:7.2f}}} {p2[2]} e a densidade da água é \\num{{{dens_value}}} {dens['unit']}. Calcule a massa adicional que deve ser colocada no lado direito da balança a fim de equilibrá-la novamente, com a bola ainda suspensa e imersa na água."""

        alt_list = [{
            'choice': 2*dens_value*(value_1[i0]*1.e-3),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 2*dens_value*(value_1[i0]),
            'consideration': 'Errou em converter a unidade L para m3',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 2*dens_value*(value_1[i0]*1.e-3),
            'consideration': 'Não considerou a aceleração da gravidade',
            'point': 0.5*qpoint
            })

        alt_list.append({
            'choice': 2*value_2[i0]*(value_1[i0]*1.e-3),
            'consideration': 'Considerou a densidade do ferro ao invés da água',
            'point': 0.25
            })

        alt_list.append({
            'choice': dens_value*(value_1[i0]*1.e-3),
            'consideration': 'Errou em definir a fórmula do peso aparente',
            'point': 0.25
            })

        alt_list.append({
            'choice': 2*dens_value*(value_1[i0]*1.e-3)*g_value,
            'consideration': 'Calculo o peso adicional e não a massa',
            'point': 0.25
            })

        alt_list.append({
            'choice': dens_value*(value_1[i0]*1.e-3)*g_value,
            'consideration': 'Calculo o peso adicional e não a massa e errou em definir a fórmula do peso aparente',
            'point': 0.0
            })

        figure = 'fluids_hydrostatic_002'

        unit = '\\unit{\kilo\gram}'

        for i in range(ntest):
            if i not in [i0]:
                val = 2*dens_value*(value_1[i]*1.e-3)
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
