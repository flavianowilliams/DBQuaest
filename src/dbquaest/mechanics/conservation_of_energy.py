import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte
from math import sqrt

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = [
        '$E=K+U$',
        '$W=\Delta K$',
        '$K=\frac{mv^2}{2}$',
        '$\Delta U=-\int_c \vec{F}\cdot d\vec{s}$',
        '$U=mgy$',
        '$U=\frac{kx^2}{2}$',
        '$E=\frac{kx_m^2}{2}$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (1, 10, '\\unit{\joule}') # min, max, unidade
        p2 = (1, 10, '\\unit{\joule}') # min, max, unidade
        p3 = (1, 10, '\\unit{\joule}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Considere a situação apresentada na figura ao lado, na qual uma pessoa arremessa uma bola, verticalmente para baixo, do alto de um edifício. No ponto A, quando a pessoa solta a bola, a energia potencial (em relação ao solo) da bola é \\num{{{value_1[i0]:7.2f}}} {p1[2]} e sua energia cinética é \\num{{{value_2[i0]:7.2f}}} {p2[2]}. Suponha que, ao chegar a B, a energia cinética da bola seja de \\num{{{value_3[i0]:7.2f}}} {p3[2]}. Qual foi a perda da energia cinética da bola devido a resistência do ar ao se deslocar de A para B?"""

        alt_list = [{
            'choice': value_1[i0]+value_2[i0]-value_3[i0],
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': value_3[i0],
            'consideration': 'Considerou a energia cinética no ponto B ao invés do valor dissipado',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0],
            'consideration': 'Considerou a perda da energia potencial no ponto B ao invés do valor dissipado',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_2[i0],
            'consideration': 'Considerou a energia cinética no ponto A ao invés do valor dissipado',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]-value_2[i0]-value_3[i0],
            'consideration': 'Errou em definir a energia mecânica no ponto A',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_2[i0]-value_1[i0]-value_3[i0],
            'consideration': 'Errou em definir a energia mecânica no ponto A',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_2[i0]-value_3[i0],
            'consideration': 'Não considerou a energia potencial no ponto A',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]-value_3[i0],
            'consideration': 'Não considerou a energia cinética no ponto A',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]+value_2[i0],
            'consideration': 'Não considerou a dissipação da energia devido a resistência do ar',
            'point': 0.0
            })

        figure = 'mechanics_conservation_of_energy_001'

        unit = '\\unit{\joule}'

        for i in range(ntest):
            if i not in [i0]:
                val = value_1[i]+value_2[i]-value_3[i]
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
        p1 = (1, 100, '\\unit{\kilo\gram}') # min, max, unidade
        p2 = (5, 15, '\\unit{\metre}') # min, max, unidade
        p3 = (1, 4, '\\unit{\metre}') # min, max, unidade
        p4 = (5, 100, '\\unit{\\newton}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)
        value_4 = random_vars(p4, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Considere uma partícula de massa \\num{{{value_1[i0]:7.2f}}} {p1[2]} se movimentando na direção do eixo x. Ela percorre uma trajetória total de $x_2=\\num{{{value_2[i0]:7.2f}}}$ {p2[2]} mediante a ação de uma força $\\vec{{F}}$ como mostra a figura abaixo. À partir da origem a força aumenta continuamente até $x_1=\\num{{{value_3[i0]:7.2f}}}$ {p3[2]}, mantendo-se em seguida constante até o final do percurso. Sabendo que a força máxima $F_{{max}}$ que atua sobre ela equivale a \\num{{{value_4[i0]:7.2f}}} {p4[2]}, e que ela estava em repouso no início do movimento, determine a sua velocidade no final do percurso.

        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=10,ymin=0,ymax=6]
                    \\tkzClip[space=1.75]
                    \\tkzDrawX[right,label={{x(m)}}]
                    \\tkzDrawY[above,label={{F(N)}}]
            		\\tkzFct[domain=0:4,color=red,line width=1.5pt]{{x}}
                    \\tkzDefPointByFct[ref=A](4)
                    \\tkzPointShowCoord(A)
            		\\tkzFct[domain=4:10,color=red,line width=1.5pt]{{4}}
                    \\tkzDefPointByFct[ref=B](10)
                    \\tkzPointShowCoord(B)
                    \\tkzDefPoints{{4/0/x1, 10/0/x2, 0/4/F}}
                    \\tkzText[color=black, below](x1){{$x_1$}}
                    \\tkzText[color=black, below](x2){{$x_2$}}
                    \\tkzText[color=black, left](F){{$F_{{max}}$}}
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': sqrt((2*value_2[i0]-value_3[i0])*value_4[i0]/(value_1[i0])),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': sqrt(2*(2*value_2[i0]+value_3[i0])*value_4[i0]/(value_1[i0])),
            'consideration': 'Definiu errado a área do trabalho',
            'point': 0.5
            })

        alt_list.append({
            'choice': sqrt((value_3[i0])*value_4[i0]/(value_1[i0])),
            'consideration': 'Definiu errado a área do trabalho',
            'point': 0.5
            })

        alt_list.append({
            'choice': sqrt(2*(value_2[i0])*value_4[i0]/(value_1[i0])),
            'consideration': 'Definiu errado a área do trabalho',
            'point': 0.5
            })

        alt_list.append({
            'choice': (2*value_2[i0]-value_3[i0])*value_4[i0]/2,
            'consideration': 'Calculou apenas o trabalho, e não a velocidade',
            'point': 0.5
            })

        alt_list.append({
            'choice': ((2*value_2[i0]-value_3[i0])*value_4[i0]/(value_1[i0])),
            'consideration': 'Errou em calcular a velocidade',
            'point': 0.5
            })

        alt_list.append({
            'choice': sqrt((2*value_2[i0]-value_3[i0])*value_4[i0]/(2*value_1[i0])),
            'consideration': 'Errou em calcular a velocidade',
            'point': 0.5
            })

        figure = ''

        unit = '\\unit{\joule}'

        for i in range(ntest):
            if i not in [i0]:
                val = sqrt((2*value_2[i]-value_3[i])*value_4[i]/(value_1[i]))
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
