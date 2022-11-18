import random

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = []

    if opt == '001':

        type = 'conceptual'

        alt_list = [{
            'choice': '$E=\\frac{\hbar^2k^2}{2m}$',
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': '$E=\infty$',
            'consideration': 'Alternativa errada',
            'point': 0.0
            })

        alt_list.append({
            'choice': '$E = \\frac{mk^2}{2}$',
            'consideration': 'Alternativa errada',
            'point': 0.0
            })

        alt_list.append({
            'choice': '$E=\hbar k$',
            'consideration': 'Alternativa errada',
            'point': 0.0
            })

        alt_list.append({
            'choice': '$E = \\frac{mk^2}{2}$',
            'consideration': 'Alternativa errada',
            'point': 0.0
            })

        text = r"""Determine a energia E da partícula que possui a função de onda $\Psi(x,t)=Ae^{i(kx-\omega t)}$"""

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
