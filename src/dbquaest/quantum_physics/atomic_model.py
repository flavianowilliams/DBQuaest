import random

def question(qpoint, opt):

    if opt == 'OQATM001':

        type = 'objective'

        p1 = [] #
        p2 = [] #
        p3 = [] #
        p4 = [] #

        var = random.uniform(p4[0], p4[0])

        alt_list = [{
            'choice': var,
            'point': qpoint
            }]

        text = f"""xxxxx"""

        figure = ''

        unit = 'eV'

        for i in range(9):
            error = random.uniform(p4[0], p4[0])
            alt_list.append({'choice': error, 'point': 0.0})

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
