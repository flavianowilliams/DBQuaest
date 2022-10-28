import random

def question(qpoint, opt):

    if opt == 'CEELE001':

        type = 'conceptual'

        text = r"""Considere a figura abaixo onde as linhas trajeçadas representam superfícies equipotenciais Se colocarmos um elétron próximo a carga Q, quais trechos possíveis o elétron poderá se deslocar?
        
        \begin{center}
            \begin{minipage}[c]{0.5\linewidth}
                \begin{tikzpicture}[scale=0.5,transform shape, font=\Large]

                \tkzInit[xmin=-4,xmax=4,ymin=-4,ymax=4]
                \tkzClip[space=0.5]

                \tkzDefPoints{0/0/O,4/0/P}

                \foreach \x in {0.5,1.25,2.25,3,4}{
                    \tkzDrawCircle[R,dashed,color=gray!50](O,\x)
                }

                \foreach \y in {0,1,...,11}{
                    \tkzDefPointsBy[rotation= center O angle 30*\y](O,P){P1,P2}
                \draw[->, line width=1.0pt] (O) -- (P2);}

                \tkzDefPoints{3/0/a,4/0/b,0/4/c,0/3/d}

                \tkzDrawPoints[color=red,fill=red,size=0.3cm](a,b,c,d)

                \tkzDrawPoints(O)
                \tkzLabelPoints[above right,font=\Large](a,b,c,d)

                \node[circle, radius=0.25, ball color=gray!50] (n1) at (0,0) {Q};

                \end{tikzpicture}
            \end{minipage}
        \end{center}
        
        """

        figure = ''

        alt_list = [{'choice': r'$b\rightarrow a$ ou $c\rightarrow d$', 'unit': '', 'point': qpoint}]
        alt_list.append({'choice': r'$a\rightarrow b$ ou $d\rightarrow c$', 'unit': '', 'point': 0.0})
        alt_list.append({'choice': r'$b\rightarrow c$ ou $a\rightarrow d$', 'unit': '', 'point': 0.0})
        alt_list.append({'choice': r'$c\rightarrow b$ ou $d\rightarrow a$', 'unit': '', 'point': 0.0})
        alt_list.append({'choice': r'$b\rightarrow a\rightarrow d\rightarrow c$ ou $c\rightarrow d\rightarrow a\rightarrow b$', 'unit': '', 'point': 0.0})

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'alternative': alternative_list}

    else:

        context = {}

    return context
