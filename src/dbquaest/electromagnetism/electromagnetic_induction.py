import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = [
        '$\frac{d\Phi}{dt}=-\varepsilon$',
        '$\Phi=\int \vec{B}\cdot \hat{n}dA$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (5, 50, '\\unit{\centi\metre}') # min, max, unidade
        p2 = (0.2, 1.0, '\\unit{\ohm}') # min, max, unidade
        p3 = (7, 9, '\\unit{\second}') # min, max, unidade
        p4 = (10, 20, '\\unit{\second}') # min, max, unidade
        p5 = (1, 5, '\\unit{\tesla}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)
        value_4 = random_vars(p4, ntest)
        value_5 = random_vars(p5, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""O gráfico mostra a dependência com o tempo de um campo magnético espacialmente uniforme que atravessa perpendicularmente a área de uma espira quadrada de \\num{{{value_1[i0]:7.2f}}} {p1[2]} de lado. Sabe-se que a resistência elétrica do fio, do qual é formada a espira, é \\num{{{value_2[i0]:7.2f}}} {p2[2]}. Calcule a corrente elétrica induzida na espira entre os instantes \\num{{{value_3[i0]:7.2f}}} {p3[2]} e \\num{{{value_4[i0]:7.2f}}} {p4[2]}.
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=10,ymin=0,ymax=5]
                    \\tkzClip[space=1.75]
                    \\tkzDrawX[right,label={{t(s)}}]
                    \\tkzDrawY[above,label={{B(T)}}]
                    \\tkzFct[domain=0:3, color=red, line width=1.5pt]{{x}}
                    \\tkzDefPointByFct[ref=A](3)
                    \\tkzPointShowCoord(A)
                    \\tkzFct[domain=3:7, color=red, line width=1.5pt]{{3}}
                    \\tkzDefPointByFct[ref=B](7)
                    \\tkzPointShowCoord(B)
                    \\tkzFct[domain=7:10, color=red, line width=1.5pt]{{10-x}}
                    \\tkzDefPointByFct[ref=C](7)
                    \\tkzPointShowCoord(C)
                    \\tkzDefPoints{{3/0/D,7/0/E,0/3/F,10/0/G}}
                    \\tkzText[below, color=black](D){{3,0}}
                    \\tkzText[below, color=black](E){{{value_3[i0]}}}
                    \\tkzText[below, color=black](G){{{value_4[i0]}}}
                    \\tkzText[left, color=black](F){{{value_5[i0]}}}
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': -1.e3*(0-value_5[i0])*(value_1[i0]*1e-2)**2/((value_4[i0]-value_3[i0])*value_2[i0]),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': -1.e3*(0-value_5[i0])*(value_1[i0])**2/((value_4[i0]-value_3[i0])*value_2[i0]),
            'consideration': 'Errou em converter a unidade centímetro em metro',
            'point': 0.75
            })

        alt_list.append({
            'choice': -(0-value_5[i0])*(value_1[i0]*1e-2)**2/((value_4[i0]-value_3[i0])*value_2[i0]),
            'consideration': 'Errou em converter a unidade ampére para miliampére',
            'point': 0.75
            })

        alt_list.append({
            'choice': -(0-value_5[i0])*(value_1[i0])**2/((value_4[i0]-value_3[i0])*value_2[i0]),
            'consideration': 'Errou em converter a unidade ampére para miliampére e centímetro para metro',
            'point': 0.5
            })

        alt_list.append({
            'choice': 0.0,
            'consideration': 'Errou em definir a lei de Faraday',
            'point': 0.0
            })

        alt_list.append({
            'choice': 1.e3*(0-value_5[i0])*(value_1[i0]*1e-2)**2/((value_4[i0]-value_3[i0])*value_2[i0]),
            'consideration': 'Errou em definir o sentido da corrente elétrica segundo a lei da Faraday-Lenz',
            'point': 0.5
            })

        alt_list.append({
            'choice': -1.e3*(0-value_5[i0])*(value_1[i0]*1e-2)**2/((value_3[i0]-3)*value_2[i0]),
            'consideration': 'Errou em calcular a variação do fluxo magnético',
            'point': 0.5
            })

        alt_list.append({
            'choice': -1.e3*(0-value_5[i0])*(value_1[i0]*1e-2)**2*value_2[i0]/((value_4[i0]-value_3[i0])),
            'consideration': 'Errou em definir a lei da Ohm',
            'point': 0.5
            })

        alt_list.append({
            'choice': -1.e3*(0-value_5[i0])*(value_1[i0]*1e-2)**2/((value_3[i0]-0)*value_2[i0]),
            'consideration': 'Errou em calcular a variação do fluxo magnético',
            'point': 0.5
            })

        figure = ''

        unit = '\\unit{\m\\ampere}'

        for i in range(ntest):
            if i not in [i0]:
                val = -1.e3*(0-value_5[i])*(value_1[i]*1e-2)**2/((value_4[i]-value_3[i])*value_2[i])
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
        p1 = (5, 50, '\\unit{\centi\metre}') # min, max, unidade
        p2 = (1, 50, '\\unit{\\tesla}') # min, max, unidade
        p3 = (0.1, 0.9, '\\unit[per-mode = symbol]{\metre\per\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""As extremidades de uma barra metálica de comprimento \\num{{{value_1[i0]:7.2f}}} {p1[2]} estão sendo deslizadas ao longo de um fio em forma de U como mostra a figura abaixo. Todo o conjunto está inserido em um campo magnético uniforme $\\vec{{B}}$, cuja intensidade é de \\num{{{value_2[i0]:7.2f}}} {p2[2]}. Sabendo que a velocidade da barra é de \\num{{{value_3[i0]:7.2f}}} {p3[2]}, determine a f.e.m. induzida na espira.
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=11,ymin=0,ymax=7]
                    \\tkzClip[space=1.75]
                    \\tkzDefPoints{{1/1/A1, 9.5/1/A2, 1/5/A3, 9.5/5/A4}}
                    \draw[color=brown!50, line width=1.5pt] (A1) -- (A2);
                    \draw[color=brown!50, line width=1.5pt] (A3) -- (A4);
                    \draw[color=brown!50, line width=1.5pt] (A1) -- (A3);
                    \\tkzDefPoints{{4/1/A5, 4/5/A6}}
                    \draw[color=gray, line width=2.5pt] (A5) -- (A6);
                    \\tkzDefPoints{{2/1/v1, 2.5/5/v2, 1/3/v3, 4/3/v4}}
                    \draw[->, color=red, line width=1.5pt] (v1) --++ (1,0) node [below, midway] {{i}};
                    \draw[->, color=red, line width=1.5pt] (v2) --++ (-1,0) node [above, midway] {{i}};
                    \draw[->, color=red, line width=1.5pt] (v3) --++ (0,-1) node [left, midway] {{i}};
                    \draw[->, color=black, line width=3pt] (v4) --++ (1,0) node [right] {{\Huge$\\vec{{v}}$}};
                    \\tkzDefPoints{{9/1.5/t1}}
                    \\tkzText[above right](t1){{\Huge $\\vec{{B}}$}}
                    \\foreach \l in {{0, 1.5, ..., 11}}{{
                        \\foreach \h in {{0, 1.5, ..., 7}}{{
                            \\tkzDefPoint(\l,\h){{p}}
                            \\tkzText(p){{x}}
                        }}
                    }}
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': -(value_1[i0]*1.e-2)*value_2[i0]*value_3[i0],
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': -(value_1[i0])*value_2[i0]*value_3[i0],
            'consideration': 'Errou em converter a unidade centímetro em metro',
            'point': 0.75
            })

        alt_list.append({
            'choice': -(value_1[i0]*1.e2)*value_2[i0]*value_3[i0],
            'consideration': 'Errou em converter a unidade centímetro em metro',
            'point': 0.75
            })

        alt_list.append({
            'choice': -(value_1[i0]*1.e-2)*value_2[i0]/value_3[i0],
            'consideration': 'Errou em definir a expressão da taxa de variação do fluxo magnético',
            'point': 0.0
            })

        alt_list.append({
            'choice': -(value_1[i0]*1.e-2)*value_3[i0]/value_2[i0],
            'consideration': 'Errou em definir a expressão da taxa de variação do fluxo magnético',
            'point': 0.0
            })

        alt_list.append({
            'choice': -value_3[i0]*value_2[i0]/(value_1[i0]*1.e-2),
            'consideration': 'Errou em definir a expressão da taxa de variação do fluxo magnético',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_1[i0]*1.e-2)*value_2[i0]*value_3[i0],
            'consideration': 'Errou em definir o sentido da f.e.m. segundo a lei da Faraday-Lenz',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\\volt}'

        for i in range(ntest):
            if i not in [i0]:
                val = (value_1[i]*1.e-2)*value_2[i]*value_3[i]
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
