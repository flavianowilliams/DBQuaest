import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte
from math import atan, cos, sin, tan, pi

def question(qpoint, opt, ntest):

    # constants

    g = cte('gravity')
    g_value = g['value']

    cte_list = [
        f"{g['symbol']}={g['value']} {g['unit']}"
        ]

    formula_list = [
        '$\vec{F}=m\vec{a}$'
    ]

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (0.2, 0.8, '') # min, max, unidade

        value_1 = random_vars(p1, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um bloco, está em repouso, apoiado sobre um plano inclinado como mostra a figura abaixo. O coeficiente de atrito estático entre o bloco e o plano é igual a \\num{{{value_1[i0]:7.2f}}} {p1[2]}. Determine a inclinação máxima que podemos aplicar ao plano sem que o bloco desça para baixo.

        \\begin{{center}}
            \\begin{{minipage}}[c]{{0.5\\linewidth}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=8,ymin=0,ymax=8]
                    \\tkzClip[space=1]

                    \\tkzDefPoints{{0/0/A,8/0/B,8/8/C}}

                    \\tkzDrawPolygon(A,B,C)

                    \\tkzDefPoints{{3/5/a,4/6/b,4/4/c,5/5/d}}

                    \\tkzDrawPolygon(b,a,c,d)
                    \\tkzFillPolygon[color=gray](b,a,c,d)

                    \\tkzDefPoints{{4/5/D}}

                    \draw[->,line width=1.5pt,color=red] (D) --++ (0,-3) node [below] {{\Huge $\\vec{{P}}$}};

                    \\tkzMarkAngle(B,A,C)
                    \\tkzLabelAngle[pos=1.5](B,A,C){{\Huge $\\theta$}}
                \end{{tikzpicture}}
            \end{{minipage}}
        \end{{center}}

        """

        alt_list = [{
            'choice': atan(value_1[i0])*180/pi,
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': atan(value_1[i0]),
            'consideration': 'Errou em converter a unidade radiano para graus',
            'point': 0.75
            })

        alt_list.append({
            'choice': atan(value_1[i0])*pi/180,
            'consideration': 'Errou em converter a unidade radiano para graus',
            'point': 0.75
            })

        figure = ''

        unit = '\\unit{\celsius}'

        for i in range(ntest):
            if i not in [i0]:
                val = atan(value_1[i])*180/pi
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
        p1 = (0.5, 60, '\\unit{\kilo\gram}') # min, max, unidade
        p2 = (20, 70, 'graus') # min, max, unidade
        p3 = (20, 70, 'graus') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Na figura abaixo podemos observar um bloco de massa M=\\num{{{value_1[i0]:7.2f}}} {p1[2]}, pendurado por dois fios de massas desprezíveis. Supondo $\\theta_1=\\num{{{value_2[i0]:7.2f}}}$ {p2[2]} e $\\theta_2=\\num{{{value_3[i0]:7.2f}}}$ {p3[2]}, determine a máxima tensão aplicada nos dois fios.

        \\begin{{center}}
            \\begin{{minipage}}[c]{{0.5\\linewidth}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
					\\tkzInit[xmin=-4,xmax=4,ymin=-8,ymax=0]
					%\\tkzGrid[color=gray!20]
					%\\tkzClip[space=1]
					
					\\tkzDefPoints{{0/-4/O,-4/0/A,4/0/B,0/-6/C}}
					
					%parede
					\\fill [pattern = north west lines] ($(B)+(0,0.25)$) rectangle (A);
					\draw (A) -- (B);
					
					\\tkzMarkAngle(O,A,B)
					\\tkzLabelAngle[pos=1.5](O,A,B){{\huge $\\theta_1$}}
					
					\\tkzMarkAngle(A,B,O)
					\\tkzLabelAngle[pos=1.5](A,B,O){{\huge $\\theta_2$}}
					
					\draw (O) -- (A) node [below left, midway] {{1}};
					\draw (O) -- (B) node [below right, midway] {{2}};
					
					\\tkzDefPoints{{-1/-6/a,1/-6/b,-1/-8/c,1/-8/d,0/-7/e}}
					
					\\tkzDrawCircle[R,fill=gray](O,0.25mm)
					
					\\tkzText(O){{M}}
					
                \end{{tikzpicture}}
            \end{{minipage}}
        \end{{center}}

        """

        var_1 = value_2[i0]*pi/180
        var_2 = value_3[i0]*pi/180
        func_1 = value_1[i0]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list = [{
            'choice': max(func_1,func_2),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        var_1 = value_2[i0]
        var_2 = value_3[i0]
        func_1 = value_1[i0]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list.append({
            'choice': atan(value_1[i0]),
            'consideration': 'Errou em converter a unidade graus para radiano',
            'point': 0.75
            })

        var_1 = value_2[i0]*180/pi
        var_2 = value_3[i0]*180/pi
        func_1 = value_1[i0]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list.append({
            'choice': max(func_1,func_2),
            'consideration': 'Errou em converter a unidade radiano para graus',
            'point': 0.75
            })

        var_1 = value_2[i0]*pi/180
        var_2 = value_3[i0]*pi/180
        func_1 = value_1[i0]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list.append({
            'choice': min(func_1,func_2),
            'consideration': 'Definiu a mínima tensão ao invés da máxima',
            'point': 0.5
            })

        var_1 = value_2[i0]*pi/180
        var_2 = value_3[i0]*pi/180
        func_1 = value_1[i0]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list.append({
            'choice': max(func_1,func_2*cos(var_1)),
            'consideration': 'Errou em definir uma das tensões',
            'point': 0.5
            })

        var_1 = value_2[i0]*pi/180
        var_2 = value_3[i0]*pi/180
        func_1 = value_1[i0]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list.append({
            'choice': max(func_1,func_2/cos(var_2)),
            'consideration': 'Errou em definir uma das tensões',
            'point': 0.5
            })

        var_1 = value_2[i0]*pi/180
        var_2 = value_3[i0]*pi/180
        func_1 = value_1[i0]/(cos(var_2)*tan(var_1)+sin(var_2))
        func_2 = float(func_1)*cos(var_2)/cos(var_1)

        alt_list.append({
            'choice': max(func_1,func_2),
            'consideration': 'Considerou a massa do bloco ao invés do peso',
            'point': 0.5
            })

        figure = ''

        unit = '\\unit{\\newton}'

        for i in range(ntest):
            if i not in [i0]:
                var_1 = value_2[i]*pi/180
                var_2 = value_3[i]*pi/180
                func_1 = value_1[i]*g_value/(cos(var_2)*tan(var_1)+sin(var_2))
                func_2 = float(func_1)*cos(var_2)/cos(var_1)
                val = max(func_1, func_2)
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
