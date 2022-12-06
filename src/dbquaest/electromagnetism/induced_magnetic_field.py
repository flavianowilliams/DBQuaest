import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte
from math import cos, sin, atan, pi, sqrt

def question(qpoint, opt, ntest):

    # constants

    mu0 = cte('permeability')
    mu0_value = mu0['value']

    cte_list = [
        f"{mu0['symbol']}={mu0['value']} {mu0['unit']}"
    ]

    formula_list = [
        '$B=\frac{\mu_0 i}{2\pi r}$',
        '$d\vec{B}=\frac{\mu_0}{4\pi}\frac{id\vec{s}\times \vec{r}}{r^2}$',
        '$\oint_c \vec{B}\cdot d\vec{r}=\mu_0 i$',
        '$\vec{B}=\frac{\mu_0}{2\pi}\frac{\vec{\mu}}{z^3}$',
        '$B=\mu_0ni$',
        '$B=\frac{\mu_0Ni}{2\pi r}$'
    ]

    if opt == '001':

        type = 'objective'

        p1 = [1.0e-6, 1.0e-5, 'C'] # min, max
        p2 = [0.1, 1.0, 'T'] # min, max
        p3 = [1.0e2, 1.0e3, 'm/s'] # min, max
        p4 = [0, 90, 'graus'] # min, max

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)
        value_4 = random_vars(p4, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Uma partícula de carga \\num{{{value_1[i0]:.2e}}} {p1[2]} é lançada em um campo magnético uniforme de \num{{{value_2[i0]:7.2f}}} {p2[2]} , com uma velocidade de \num{{{value_3:5.2f}}} {p3[2]}. Calcule o valor da força magnética atuando na carga se o ângulo entre a velocidade e o campo magnético for \num{{{value_4:7.2f}}} {p4[2]}."""

        alt_list = [{
            'choice': value_1[i0]*value_2[i0]*value_3[i0]*sin(value_4[i0]*3.14/180),
            'consideration': 'Alternativa correta',
            'point': qpoint
             }]

        alt_list.append({
            'choice': value_1[i0]*value_2[i0]*value_3[i0]*sin(value_4[i0]),
            'consideration': 'Errou em converter a unidade graus para radianos',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': value_1[i0]*value_2[i0]*value_3[i0]*cos(value_4[i0]*3.14/180),
            'consideration': 'Errou em definir a expressão da força magnética',
            'point': 0.25*qpoint
            })

        alt_list.append({
            'choice': value_1[i0]*value_2[i0]*value_3[i0]*value_4[i0],
            'consideration': 'Errou em definir a expressão da força magnética',
            'point': 0.25*qpoint
            })

        figure = ''

        unit = 'N'

        for i in range(ntest):
            if i not in [i0]:
                val = value_1[i]*value_2[i]*value_3[i]*sin(value_4[i]*3.14/180)
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
        p1 = (10, 50, '\\unit{\\ampere}') # min, max, unidade
        p2 = (0.1, 1, '\\unit{\metre}') # min, max, unidade
        p3 = (0.1, 1, '\\unit{\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""A figura abaixo mostra a seção reta de dois fios retilíneos muito longos, ambos percorridos por uma corrente de \\num{{{value_1[i0]:7.2f}}} {p1[2]} orientada para fora do papel. A distância entre os fios é $d_1=\\num{{{value_2[i0]:7.2f}}}$ {p2[2]} e a distância entre o ponto P, equidistante dos dois fios, e o ponto médio do segmento de reta que liga os fios é $d_2=\\num{{{value_3[i0]:7.2f}}}$ {p3[2]}. Determine o módulo do campo magnético total produzido no ponto P.

        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=10,ymin=-3,ymax=3]
                    \\tkzClip[space=1.75]
                    \\tkzDefPoints{{0/-3/A,0/3/B,0/0/O,10/0/P}}
                    \draw[dashed] (A) -- (B) node [left=0.5, midway]{{\Huge $d_1$}};
                    \draw[dashed] (O) -- (P) node [above=0.5, midway]{{\Huge $d_2$}};
                    \\tkzDrawCircle[R, fill=gray!50](A,0.5)
                    \\tkzDrawCircle[R, fill=gray!50](B,0.5)
                    \\tkzDrawCircle[R, fill=gray!50](P,0.5)
                    \\tkzText[left=0.5](A){{\Huge $i_1$}}
                    \\tkzText[left=0.5](B){{\Huge $i_2$}}
                    \\tkzText[above=0.75](P){{\Huge P}}
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        r_value = 0.5*sqrt(value_2[i0]**2+4*value_3[i0]**2)
        r_err1 = sqrt(value_2[i0]**2+value_3[i0]**2)
        theta_value = 2*atan(value_3[i0]/r_value)
        theta_err1 = atan(value_3[i0]/r_value)

        alt_list = [{
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_value)))/(2*pi*r_value),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_value)))/(2*pi*r_value),
            'consideration': 'Errou em converter a unidade Tesla para microtesla',
            'point': 0.75
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1-cos(theta_value)))/(2*pi*r_value),
            'consideration': 'Errou em definir o vetor resultante',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_value)))/(4*pi*r_value),
            'consideration': 'Errou em definir a expressão do campo magnético do fio retilíneo',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]/(2*pi*r_value),
            'consideration': 'Errou em definir o vetor resultante',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2)/(2*pi*r_value),
            'consideration': 'Errou em definir o vetor resultante',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_err1)))/(2*pi*r_value),
            'consideration': 'Errou em definir o ângulo',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1-cos(theta_err1)))/(2*pi*r_value),
            'consideration': 'Errou em definir o ângulo e o módulo do vetor resultante',
            'point': 0.25
            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_err1)))/(4*pi*r_value),
            'consideration': 'Errou em definir o ângulo e a expressão do campo magnético',
            'point': 0.25
            })

#        alt_list.append({
#            'choice': mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_value)))/(2*pi*r_err1),
#            'consideration': 'Errou em definir a distância entre os fios e o ponto P',
#            'point': 0.5
#            })

        alt_list.append({
            'choice': 1.e6*mu0_value*value_1[i0]*sqrt(2*(1+cos(theta_err1)))/(2*pi*r_err1),
            'consideration': 'Errou em definir a distância entre os fios e o ponto P e o ângulo',
            'point': 0.25
            })

        figure = ''

        unit = '\\unit{\micro\\tesla}'

        for i in range(ntest):
            if i not in [i0]:
                val = 1.e6*mu0_value*value_1[i]*sqrt(2*(1+cos(theta_value)))/(2*pi*r_value)
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 1.e-2:
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
        p1 = (0.5, 2.5, '\\unit{\metre}') # min, max, unidade
        p2 = (10, 50, '\\unit{\\ampere}') # min, max, unidade
        p3 = (2, 10, '\\unit{\centi\metre}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Considere dois fios retilíneos de comprimento L=\\num{{{value_1[i0]:7.2f}}} {p1[2]}, ambos percorridos por uma corrente i de \\num{{{value_2[i0]:7.2f}}} {p2[2]}. A distância entre os fios é  $d=\\num{{{value_3[i0]:7.2f}}}$ {p3[2]}. Determine a força atuando em cada fio.

        \\begin{{center}}
            \\begin{{minipage}}[c]{{0.5\\linewidth}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=5,ymin=0,ymax=8]
                    \\tkzClip[space=1.25]
                    \\tkzDefPoints{{0/0/O, 5/0/A}}
                    \draw[fill=gray!50] (O) rectangle ++(0.3,8);
                    \draw[fill=gray!50] (A) rectangle ++(-0.3,8);
                    \\tkzDefPoints{{0/8/B, 5/8/C}}
                    \draw (A) to[dim arrow={{label=d}}] (O);
                    \draw (O) to[dim arrow={{label=L}}] (B);
                    \\tkzDefPoints{{0.75/3/D, 4.25/3/E}}
                    \draw[->, line width=1.5pt] (D) --++ (0,2) node [right, midway] {{\Huge i}};
                    \draw[->, line width=1.5pt] (E) --++ (0,2) node [left, midway] {{\Huge i}};
                \end{{tikzpicture}}
            \end{{minipage}}
        \end{{center}}

        """

        alt_list = [{
            'choice': 1.e3*mu0_value*value_1[i0]*value_2[i0]**2/(2*pi*(value_3[i0]*1.e-2)),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 1.e3*mu0_value*value_1[i0]*(value_3[i0]*1.e-2)**2/(2*pi*(value_2[i0])),
            'consideration': 'Errou em definir a força magnética atuando em um fio condutor',
            'point': 0.0
            })

        alt_list.append({
            'choice': 1.e3*mu0_value*value_1[i0]*value_2[i0]**2/(2*pi*value_3[i0]),
            'consideration': 'Errou em converter a unidade centímetro para metro',
            'point': 0.75
            })

        alt_list.append({
            'choice': mu0_value*value_1[i0]*value_2[i0]**2/(2*pi*(value_3[i0]*1.e-2)),
            'consideration': 'Errou em converter a unidade Newton para milinewton',
            'point': 0.75
            })

        alt_list.append({
            'choice': mu0_value*value_1[i0]*value_2[i0]**2/(2*pi*value_3[i0]),
            'consideration': 'Errou em converter a unidade Newton para milinewton e centímetro para metro',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e3*mu0_value*value_1[i0]*value_2[i0]/(2*pi*(value_3[i0]*1.e-2)),
            'consideration': 'Errou em definir a expressão da força magnética',
            'point': 0.5
            })

        alt_list.append({
            'choice': 1.e3*mu0_value*value_1[i0]*value_2[i0]**2*(2*pi*(value_3[i0]*1.e-2)),
            'consideration': 'Errou em definir a expressão do campo magnético do fio retilíneo',
            'point': 0.5
            })

        alt_list.append({
            'choice': mu0_value*value_1[i0]*value_2[i0]**2*(2*pi*(value_3[i0]*1.e-2)),
            'consideration': 'Errou em definir a expressão do campo magnético do fio retilíneo e em converter Newton para milinewton',
            'point': 0.25
            })

        alt_list.append({
            'choice': 1.e3*mu0_value*value_1[i0]*value_2[i0]**2*(2*pi*(value_3[i0])),
            'consideration': 'Errou em definir a expressão do campo magnético do fio retilíneo e em converter centímetro para metro',
            'point': 0.25
            })

        figure = ''

        unit = '\\unit{\m\\newton}'

        for i in range(ntest):
            if i not in [i0]:
                val = 1.e3*mu0_value*value_1[i]*value_2[i]**2/(2*pi*(value_3[i]*1.e-2))
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 1.e-2:
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

        text = f"""A figura mostra mostra os vetores velocidade de quatro elétrons nas vizinhanças de um fio percorrido por uma corrente i. As velocidades têm módulos iguais e a velocidade $\\vec{{v}}2$ aponta para dentro do papel. Os elétrons 1 e 2 estão à mesma distância do fio, e o mesmo acontece com os elétrons 3 e 4. Indique qual elétron não sofrerá ação de alguma força magnética atuando nele.
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tikzstyle{{s1}}=[circle, radius=0.1, ball color=gray!50];
                    \\tkzInit[xmin=0,xmax=10,ymin=-2,ymax=5]
                    \\tkzClip[space=0.25]
                    \\tkzDefPoints{{0/0/O, 3/-1/A}}
                    \draw[fill=gray!50] (O) rectangle ++(10,0.3);
                    \draw[->, line width=1.pt] (A) --++ (3,0) node[above, midway] {{i}};
                    \\tkzDefPoints{{2/3/v1, 4/3/v2, 6/3/v3, 8/3/v4}}
                    \draw[->, line width=1.pt] (v1) --++ (-2,0) node[above, midway] {{$\\vec{{v}}_1$}};
                    \draw[s1] (v1) circle [radius=0.3cm] node {{\huge -}};
                    \draw[->, line width=1.pt] (v2) --++ (0,-2) node[right, midway] {{$\\vec{{v}}_2$}};
                    \draw[s1] (v2) circle [radius=0.3cm] node {{\huge -}};
                    \draw[->, line width=1.pt] (v3) --++ (0,2) node[right, midway] {{$\\vec{{v}}_3$}};
                    \draw[s1] (v3) circle [radius=0.3cm] node {{\huge -}};
                    \draw[->, line width=1.pt] (v4) --++ (0,0) node[above=0.5] {{$\\vec{{v}}_4$}};
                    \draw[s1] (v4) circle [radius=0.3cm] node {{\huge $\\times$}};
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}
        
        """

        alt_list = [{'choice': '4.','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': '1.','consideration': 'A força magnética atuando no elétron será diferente de zero, pois a sua direção de propagação é perpendicular à direção do campo magnético induzido pela corrente i.','point': 0.0})
        alt_list.append({'choice': '2.','consideration': 'A força magnética atuando no elétron será diferente de zero, pois a sua direção de propagação é perpendicular à direção do campo magnético induzido pela corrente i.','point': 0.0})
        alt_list.append({'choice': '3.','consideration': 'A força magnética atuando no elétron será diferente de zero, pois a sua direção de propagação é perpendicular à direção do campo magnético induzido pela corrente i.','point': 0.0})
        alt_list.append({'choice': 'Todos sofrerão a ação de uma força magnética causada pelo fio.','consideration': 'O elétron número quatro não sofrerá ação de alguma força magnética, pois ele está se propagando na mesma direção do campo magnético induzido pela corrente i.','point': 0.0})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
