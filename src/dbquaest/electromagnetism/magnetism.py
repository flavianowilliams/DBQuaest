import random

def question(qpoint, opt):

    if opt == 'CEMAG001':

        type = 'conceptual'

        text = r"""A ﬁgura abaixo mostra a trajetória de uma partícula eletricamente carregada. $\\vec{{v}}$ representa a velocidade atravessando um campo magnético $\\vec{{B}}$. Determine a sua trajetória devido a ação da força magnética atuando sobre ela.
        
        \begin{center}
            \begin{minipage}[c]{0.5\linewidth}
                \begin{tikzpicture}[scale=0.5,transform shape, font=\Large]

                    \tkzInit[xmin=-3,xmax=3,ymin=-3,ymax=3]
                %	\tkzGrid[color=gray!20]
                    \tkzClip[space=1.0]

                    \tkzDefPoints{0/0/O,4/0/P}

                    \foreach \x in {-2.5,-1.5,...,2.5}{
                        \foreach \y in {-2.5,-1.5,...,2.5}{
                        \tkzDefPoint(\x,\y){B}
                        \tkzText(B){x}
                }
                }

                \draw[->, line width=1pt, color=red] (0,0) --++ (0,1.5) node [above] {$\vec{v}$};

                    \node[circle, radius=0.25, ball color=gray!50] (n1) at (0,0) {+};

                    \tkzText[above right=0.25cm](B){$\vec{B}$}

                \end{tikzpicture}
            \end{minipage}
        \end{center}

        """

        figure = ''

        unit = ''

        alt_list = [{'choice': 'Paralelo ao papel e circular no sentido anti-horário.', 'point': qpoint}]
        alt_list.append({'choice': 'Paralelo ao papel e circular no sentido horário.', 'point': 0.5*qpoint})
        alt_list.append({'choice': 'Paralelo ao papel e da direita para a esquerda.', 'point': 0.0})
        alt_list.append({'choice': 'Paralelo ao papel e da esquerda para a direita.', 'point': 0.0})
        alt_list.append({'choice': 'Paralelo ao papel e na vertical.', 'point': 0.0})

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}        

    return context
