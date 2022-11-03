import random

def question(qpoint, opt):

    if opt == 'CQUPH001':

        type = 'conceptual'

        alt_list = [{
            'choice': '$\Delta x=(p/m)\Delta t$',
            'point': qpoint
            }]

        alt_list.append({
            'choice': '$\Delta x = 0$',
            'point': 0.0
            })

        alt_list.append({
            'choice': '$\Delta x=\Delta t$',
            'point': 0.0
            })

        alt_list.append({
            'choice': '$\Delta x=(m/p)\Delta t$',
            'point': 0.0
            })

        alt_list.append({
            'choice': '$\Delta x=\Delta p$',
            'point': 0.0
            })

        text = r"""Do princípio da incerteza de Heisenberg, para uma partícula com energia $E=p^2/2m$ mostre que $\Delta x\Delta p\approx \hbar$ resulta em $\Delta E\Delta t\approx \hbar$ se..."""

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
