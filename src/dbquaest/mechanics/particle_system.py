import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    g = cte('gravity')
    g_value = g['value']

    cte_list = [
        f"{g['symbol']}={g['value']} {g['unit']}"
    ]

    formula_list = [
        '$x_{cm}=\frac{1}{M}\sum m_ix_i$',
        '$y_{cm}=\frac{1}{M}\sum m_iy_i$',
        '$z_{cm}=\frac{1}{M}\sum m_iz_i$',
        '$p_{cm}=\frac{1}{M}\sum p_i$',
        '$p=mv$',
        '$\vec{F}_{res}=M\vec{a}_{cm}$'
        ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (0.5, 3, '\\unit{\kilo\gram}') # min, max, unidade
        p2 = (4, 8, '\\unit{\kilo\gram}') # min, max, unidade
        p3 = (5, 10, '\\unit{\kilo\gram}') # min, max, unidade
        p4 = (10, 25, '\\unit{\centi\metre}') # min, max, unidade
        p5 = (26, 75, '\\unit{\centi\metre}') # min, max, unidade
        p6 = (76, 100, '\\unit{\centi\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)
        value_4 = random_vars(p4, ntest)
        value_5 = random_vars(p5, ntest)
        value_6 = random_vars(p6, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um conjunto é formado por três blocos de massa $m_1=\\num{{{value_1[i0]}}}$ {p1[2]},$m_2=\\num{{{value_2[i0]}}}$ {p2[2]} e $m_3=\\num{{{value_3[i0]}}}$ {p3[2]}. Determine a coordenada x do centro de massa do conjunto.
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=10,ymin=0,ymax=5]
                    \\tkzClip[space=1.75]
                    \\tkzDrawX[right,label={{x}}]
                    \\tkzDefPoints{{1/0/A, 3/5/B}}
                    \\tkzText[below=0.25](A){{0}}
                    \\tkzDefRectangle[fill=gray!25](A,B)\\tkzGetPoints{{C}}{{D}}
                    \\tkzDrawPolygon(A, C, B, D)
                    \draw (D) to[dim arrow={{label=\\num{{{value_4[i0]}}} {p4[2]}}}] (B);
                    \\tkzDefPoints{{3/0/A, 6/5/B}}
                    \\tkzDefRectangle[fill=gray!50](A,B)\\tkzGetPoints{{C}}{{D}}
                    \\tkzDrawPolygon(A, C, B, D)
                    \draw (D) to[dim arrow={{label=\\num{{{value_5[i0]}}} {p5[2]}}}] (B);
                    \\tkzDefPoints{{6/0/A, 10/5/B}}
                    \\tkzDefRectangle[fill=gray!75](A,B)\\tkzGetPoints{{C}}{{D}}
                    \\tkzDrawPolygon(A, C, B, D)
                    \draw (D) to[dim arrow={{label=\\num{{{value_6[i0]}}} {p6[2]}}}] (B);
                    \\tkzDefPoints{{1.5/2.5/m1, 4/2.5/m2, 7.5/2.5/m3}}
                    \\tkzText[right](m1){{$m_1$}}
                    \\tkzText[right](m2){{$m_2$}}
                    \\tkzText[right](m3){{$m_3$}}
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': (value_1[i0]*value_4[i0]+value_2[i0]*(2*value_4[i0]+value_5[i0])+value_3[i0]*(2*value_4[i0]+2*value_5[i0]+value_6[i0]))/(2*(value_1[i0]+value_2[i0]+value_3[i0])),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': (value_1[i0]*value_4[i0]+value_2[i0]*(value_4[i0]+value_5[i0])+value_3[i0]*(value_4[i0]+value_5[i0]+value_6[i0]))/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.5
            })

        alt_list.append({
            'choice': (value_1[i0]*value_4[i0]+value_2[i0]*value_5[i0]+value_3[i0]*value_6[i0])/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.25
            })

        alt_list.append({
            'choice': (value_1[i0]*value_4[i0]+value_2[i0]*(2*value_4[i0]+value_5[i0])+value_3[i0]*(2*value_4[i0]+2*value_5[i0]+value_6[i0]))/((value_1[i0]+value_2[i0]+value_3[i0])),
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_4[i0]+value_5[i0]+value_6[i0])/3,
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_4[i0]+value_5[i0]+value_6[i0])/2,
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_4[i0]/2,
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_5[i0]/2,
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_6[i0]/2,
            'consideration': 'Errou em calcular o centro de massa',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\centi\metre}'

        for i in range(ntest):
            if i not in [i0]:
                val = (value_1[i]*value_4[i]+value_2[i]*(2*value_4[i]+value_5[i])+value_3[i]*(2*value_4[i]+2*value_5[i]+value_6[i]))/(2*(value_1[i]+value_2[i]+value_3[i]))
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
        p1 = (0.5, 3, '\\unit{\kilo\gram}') # min, max, unidade
        p2 = (4, 8, '\\unit{\kilo\gram}') # min, max, unidade
        p3 = (5, 10, '\\unit{\kilo\gram}') # min, max, unidade
        p4 = (0.1, 0.8, '') # min, max, unidade
        p5 = (10, 500, '\\unit{\\newton}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)
        value_4 = random_vars(p4, ntest)
        value_5 = random_vars(p5, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um conjunto é formado por três blocos de massa $m_1=\\num{{{value_1[i0]}}}$ {p1[2]},$m_2=\\num{{{value_2[i0]}}}$ {p2[2]} e $m_3=\\num{{{value_3[i0]}}}$ {p3[2]}. O coeficiente de atrito entre os blocos e o chão é igual a \\num{{{value_4[i0]}}}. Aplica-se uma força equivalente a \\num{{{value_5[i0]}}} {p5[2]} no bloco menor, assim como mostra a figura abaixo. Determine a intensidade da força RESULTANTE que atua no bloco menor.
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=10,ymin=0,ymax=5]
                    \\tkzClip[space=1.75]
                    \\tkzDrawX[right,label={{x}}]
                    \\tkzDefPoints{{1/0/A, 3/5/B}}
                    \\tkzDefRectangle[fill=gray!25](A,B)\\tkzGetPoints{{C}}{{D}}
                    \\tkzDrawPolygon(A, C, B, D)
                    \\tkzDefPoints{{3/0/A, 6/5/B}}
                    \\tkzDefRectangle[fill=gray!50](A,B)\\tkzGetPoints{{C}}{{D}}
                    \\tkzDrawPolygon(A, C, B, D)
                    \\tkzDefPoints{{6/0/A, 10/5/B}}
                    \\tkzDefRectangle[fill=gray!75](A,B)\\tkzGetPoints{{C}}{{D}}
                    \\tkzDrawPolygon(A, C, B, D)
                    \\tkzDefPoints{{1.5/2.5/m1, 4/2.5/m2, 7.5/2.5/m3}}
                    \\tkzText[right](m1){{$m_1$}}
                    \\tkzText[right](m2){{$m_2$}}
                    \\tkzText[right](m3){{$m_3$}}
                    \\tkzDefPoint(0,2.5){{v1}}
                    \draw[->, line width=2pt] (v1) --++ (1,0) node [left, at start] {{$\\vec{{F}}$}};
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': (value_5[i0]-value_4[i0]*g_value*(value_1[i0]+value_2[i0]+value_3[i0]))*value_1[i0]/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': (value_5[i0]-value_4[i0]*g_value*(value_1[i0]))*value_1[i0]/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Considerou a normal apenas do bloco menor, e não a do conjunto',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_5[i0]-value_4[i0]*g_value*(value_1[i0]+value_2[i0]+value_3[i0])),
            'consideration': 'Não considerou a reação atuando no bloco',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_5[i0]-value_4[i0]*(value_1[i0]+value_2[i0]+value_3[i0]))*value_1[i0]/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Considerou a massa do bloco ao invés da força normal no cálculo da força de atrito',
            'point': 0.5
            })

        alt_list.append({
            'choice': (value_5[i0]-value_4[i0]*g_value*(value_1[i0]+value_2[i0]+value_3[i0]))*(value_1[i0]+value_2[i0]+value_3[i0])/value_1[i0],
            'consideration': 'Errou no cálculo da força resultante',
            'point': 0.5
            })

        alt_list.append({
            'choice': (value_5[i0]-value_4[i0]*g_value*(value_1[i0]+value_2[i0]+value_3[i0]))*value_2[i0]/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Errou no cálculo da força resultante',
            'point': 0.5
            })

        alt_list.append({
            'choice': (value_5[i0]-value_4[i0]*g_value*(value_1[i0]+value_2[i0]+value_3[i0]))*value_3[i0]/(value_1[i0]+value_2[i0]+value_3[i0]),
            'consideration': 'Errou no cálculo da força resultante',
            'point': 0.5
            })

        figure = ''

        unit = '\\unit{\\newton}'

        for i in range(ntest):
            if i not in [i0]:
                val = (value_5[i]-value_4[i]*g_value*(value_1[i]+value_2[i]+value_3[i]))*value_1[i]/(value_1[i]+value_2[i]+value_3[i])
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

    elif opt == '003':

        type = 'objective'

        # generating input values list
        p1 = (1, 9, '\\unit{\kilo\gram}') # min, max, unidade
        p2 = (10, 50, '\\unit{\kilo\gram}') # min, max, unidade
        p3 = (1, 9, '\\unit{\metre}') # min, max, unidade
        p4 = (10, 50, '\\unit{\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)
        value_4 = random_vars(p4, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Calcule o centro de massa do conjunto abaixo.
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                	\\tikzstyle{{s1}}=[circle, radius=0.1, ball color=gray!50];
	                \\tkzInit[xmin=0,xmax=10,ymin=0,ymax=0]
	                \\tkzGrid[color=gray!20]
	                \\tkzClip[space=2]
	                \\tkzDefPoints{{1/0/m1,8/0/m2}}
	                \\tkzDrawX[label=x,right]
	                \draw[s1] (m1) circle [radius=0.1cm] node [above] {{\\num{{{value_1[i0]}}}{p1[2]}}};
	                \draw[s1] (m2) circle [radius=0.2cm] node [above] {{\\num{{{value_2[i0]}}}{p2[2]}}};
                    \\tkzText[below=0.5](m1){{\\num{{{value_3[i0]}}}{p3[2]}}}
                    \\tkzText[below=0.5](m2){{\\num{{{value_4[i0]}}}{p4[2]}}}
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': (value_1[i0]*value_3[i0]+value_2[i0]*value_4[i0])/(value_1[i0]+value_2[i0]),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': (value_1[i0]*value_3[i0]+value_2[i0]*value_4[i0])/value_2[i0],
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_1[i0]*value_3[i0]+value_2[i0]*value_4[i0])/value_1[i0],
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_3[i0]+value_4[i0],
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        alt_list.append({
            'choice': value_1[i0]+value_2[i0],
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_1[i0]*value_3[i0]+value_2[i0]*value_4[i0]),
            'consideration': 'Não dividiu a expressão pela massa total.',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_1[i0]*value_4[i0]+value_2[i0]*value_3[i0])/(value_1[i0]+value_2[i0]),
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_1[i0]*value_2[i0]+value_3[i0]*value_4[i0])/(value_1[i0]+value_2[i0]),
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        alt_list.append({
            'choice': (value_1[i0]*value_2[i0]+value_3[i0]*value_4[i0])/(value_1[i0]+value_2[i0]),
            'consideration': 'Errou em definir a expressão do centro de massa.',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\metre}'

        for i in range(ntest):
            if i not in [i0]:
                val = (value_1[i]*value_3[i]+value_2[i]*value_4[i])/(value_1[i]+value_2[i])
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

    elif opt == '004':

        type = 'conceptual'

        text = f"""Um dublê cai do alto de um prédio em cima de um colchão inflável sem ter algum hematoma. No entanto, sem o colchão os danos ao seu corpo seriam bem maiores. Isso acontece porque"""

        alt_list = [{'choice': 'O colchão aumenta o tempo de ação da força normal sobre o dublê.','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': 'O momento linear do dublê é menor quando ele chega ao colchão.','consideration': 'Nos casos com e sem colchão, o momento linear do dublê é o mesmo quando ele chega ao chão.','point': 0.0})
        alt_list.append({'choice': 'O colchão reduz a energia cinética do dublê.','consideration': 'A energia cinética do dublê não muda quando chega ao chão nos casos com e sem colchão.','point': 0.0})
        alt_list.append({'choice': 'O colchão reduz o impulso atuando sobre o dublê.','consideration': 'O impulso sobre o dublê não muda quando chega ao chão nos casos com e sem colchão.','point': 0.0})
        alt_list.append({'choice': 'O colchão reduz o peso do dublê.','consideration': 'O peso do dublê não muda quando chega ao chão nos casos com e sem colchão.','point': 0.0})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == '005':

        type = 'conceptual'

        text = f"""Um patinador segurando uma caixa encontra-se na origem de um sistema de coordenadas. Considere que a massa do patinador é muito maior que a caixa. Em um momento de raiva, o patinador decide jogar a caixa como mostra a figura. Determine a localização do centro de massa antes da caixa chegar ao chão."""

        alt_list = [{'choice': 'Na origem','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': 'À esquerda do patinador.','consideration': 'O estado de movimento do centro de massa não altera na ausência de forças externas.','point': 0.0})
        alt_list.append({'choice': 'À direita do patinador.','consideration': 'O estado de movimento do centro de massa não altera na ausência de forças externas.','point': 0.0})
        alt_list.append({'choice': 'A sua localização muda com o tempo.','consideration': 'O estado de movimento do centro de massa não altera na ausência de forças externas.','point': 0.0})
        alt_list.append({'choice': 'É necessário conhecer a massa do patinador e da caixa.','consideration': 'A variação do estado de movimento do centro de massa obedece à lei da conservação do momento, portanto a massa dos participante é diretamente irrelevante neste caso.','point': 0.0})

        figure = 'mechanics_particle_system_005'

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
