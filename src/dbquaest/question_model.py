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
        p1 = (1, 10, '\\unit[per-mode = symbol]{\kilo\gram\metre\per\second}') # min, max, unidade
        p2 = (1, 10, '\\unit[per-mode = symbol]{\kilo\gram\metre\per\second}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Valor 1: \\num{{{value_1[i0]:7.2f}}} {p1[2]}. Valor 2: \\num{{{value_2[i0]:7.2f}}} {p2[2]}
        
        \\begin{{minipage}}[c]{{0.5\\linewidth}}
            \\begin{{center}}
                \\begin{{tikzpicture}}[scale=0.5,transform shape, font=\Large]
                    \\tkzInit[xmin=0,xmax=10,ymin=-3,ymax=3]
                    \\tkzClip[space=1.75]
                \end{{tikzpicture}}
            \end{{center}}
        \end{{minipage}}

        """

        alt_list = [{
            'choice': value_1[i0],
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': value_2[i0],
            'consideration': 'Trocou um pelo outro :(',
            'point': 0.0
            })

        figure = ''

        unit = '\\unit{\celsius}'

        for i in range(ntest):
            if i not in [i0]:
                val = value_1[i]
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
