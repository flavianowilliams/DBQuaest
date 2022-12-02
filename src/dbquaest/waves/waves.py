import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = []

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (1.2, 2.5, '\\unit{\metre}') # min, max, unidade
        p2 = (10, 20, '\\unit{\centi\metre}') # min, max, unidade
        p3 = (5, 60, '\\unit{\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um menino de \\num{{{value_1[i0]}}} {p1[2]} de altura produz uma sombra de \\num{{{value_2[i0]}}} {p2[2]}. No mesmo instante, um prédio próximo ao menino produz uma sombra de \\num{{{value_3[i0]}}} {p3[2]}. Qual é a altura do prédio?"""

        alt_list = [{
            'choice': value_3[i0]*value_1[i0]/(value_2[i0]*1.e-2),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': value_3[i0]*value_1[i0]/(value_2[i0]*1.e2),
            'consideration': 'Errou em converter a unidade centímetro para metro.',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': value_3[i0]*value_1[i0]/value_2[i0],
            'consideration': 'Errou em converter a unidade centímetro para metro.',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': (value_2[i0]*1.e-2)*value_1[i0]/value_3[i0],
            'consideration': 'Errou em definir a expressão da semelhança de triângulo.',
            'point': 0.0*qpoint
            })

        alt_list.append({
            'choice': value_3[i0]*(value_2[i0]*1.e-2)/value_1[i0],
            'consideration': 'Errou em definir a expressão da semelhança de triângulo.',
            'point': 0.0*qpoint
            })

        alt_list.append({
            'choice': value_2[i0]*value_1[i0]/value_3[i0],
            'consideration': 'Errou em definir a expressão da semelhança de triângulo e em converter a unidade centímetro para metro.',
            'point': 0.0*qpoint
            })

        alt_list.append({
            'choice': value_3[i0]*value_2[i0]/value_1[i0],
            'consideration': 'Errou em definir a expressão da semelhança de triângulo e em converter a unidade centímetro para metro.',
            'point': 0.0*qpoint
            })

        figure = ''

        unit = '\\unit{\metre}'

        for i in range(ntest):
            if i not in [i0]:
                val = (value_3[i]*value_1[i]/value_2[i])*1.e-2
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

        type = 'conceptual'

        text = f"""Uma pessoa pressiona a tecla de um piano que corresponde a nota Lá (440 Hz). Podemos dizer que
        \\begin{{enumerate}}
            \item [I] O comprimento de onda desse som no ar é 77 cm;
            \item [II] A frequência desse som ao atingir a orelha de um mergulhador próximo ao piano é menor que 440 Hz;
            \item [III] Sabendo que a velocidade do som na água é 1450 m/s, o comprimento de onda desse som na água será 3,3 m.
        \end{{enumerate}}
        Podemos dizer que são verdadeiras as afirmações...

        """

        alt_list = [{'choice': 'I e III','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': 'I e II','consideration': 'A frequência não altera quando o som atravessa um meio para o outro','point': 0.50*qpoint})
        alt_list.append({'choice': 'II e III','consideration': 'A frequência não altera quando o som atravessa um meio para o outro','point': 0.50*qpoint})
        alt_list.append({'choice': 'Todas estão corretas','consideration': 'A frequência não altera quando o som atravessa um meio para o outro','point': 0.75*qpoint})
        alt_list.append({'choice': 'Todas estão erradas','consideration': 'O comprimento de onda do som no ar está correto e a frequência não altera quando o som atravessa um meio para o outro','point': 0.25*qpoint})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == '003':

        type = 'conceptual'

        text = f"""Podemos dizer que a imagem formada no espelho abaixo é"""

        alt_list = [{'choice': 'Virtual e o espelho é convexo','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': 'Real e o espelho é côncavo','consideration': 'Alternativa errada','point': 0.0*qpoint})
        alt_list.append({'choice': 'Real e o espelho é convexo','consideration': 'Alternativa errada','point': 0.0*qpoint})
        alt_list.append({'choice': 'Virtual e o espelho é côncavo','consideration': 'Alternativa errada','point': 0.0*qpoint})
        alt_list.append({'choice': 'Virtual e o espelho é plano','consideration': 'Alternativa errada','point': 0.0*qpoint})

        figure = 'waves_waves_003'

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
