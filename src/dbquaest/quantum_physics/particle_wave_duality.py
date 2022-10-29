import random

def question(qpoint, opt):

    if opt == 'OQPWD001':

        type = 'objective'

        p1 = [2.28, 2.28, 'eV'] # Work function of Sodium
        p2 = [4.1357e-15, 4.1357e-15, 'eV*s'] # Planck constant
        p3 = [299792458, 299792458, 'm/s'] # speed of light
        p4 = [200, 540, 'nm']

        var = random.uniform(p4[0], p4[1])

        alt_list = [{
            'choice': p2[0]*p3[0]/(var*1.e-9)-p1[0],
            'unit': ' eV',
            'point': qpoint
            }]

        alt_list.append({
            'choice': p2[0]*p3[0]/var-p1[0],
            'unit': ' eV',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': p2[0]*var*1.e-9-p1[0],
            'unit': ' eV',
            'point': 0.25*qpoint
            })

        alt_list.append({
            'choice': p2[0]*p3[0]/(var*1.e-9)+p1[0],
            'unit': ' eV',
            'point': 0.25*qpoint
            })

        text = f"""A função trabalho do sódio é 2,28 eV, determine a energia cinética dos elétrons que são emitidos desse material quando ele é bombardeado por radiação com comprimento de onda de {var:7.2f} {p4[2]}."""

        figure = ''

        for i in range(6):
            error = random.uniform(p4[0], p4[1])
            alt_list.append({'choice': p2[0]*p3[0]/(error*1.e-9)-p1[0], 'unit': ' eV', 'point': 0.0})

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'alternative': alternative_list}

    elif opt == 'OQPWD002':

        type = 'objective'

        p1 = [6.62607015e-34, 6.62607015e-34, '$kg\cdot m^2/s$'] # Planck constant
        p2 = [100, 200, 'g']
        p3 = [80, 200, 'km/h']

        var_1 = random.uniform(p2[0], p2[1])
        var_2 = random.uniform(p3[0], p3[1])

        alt_list = [{
            'choice': 6.62607015e-34/((var_1*1.0e-3)*(var_2/3.6)),
            'unit': ' m',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 6.62607015e-34/((var_1)*(var_2/3.6)),
            'unit': ' m',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 6.62607015e-34/((var_1*1.0e-3)*(var_2)),
            'unit': ' eV',
            'point': 0.75*qpoint
            })

        alt_list.append({
            'choice': 6.62607015e-34/(var_1*var_2),
            'unit': ' eV',
            'point': 0.5*qpoint
            })

        alt_list.append({
            'choice': 6.62607015e-34/((var_1*1.0e+3)*(var_2/3.6)),
            'unit': ' m',
            'point': 0.75
            })

        alt_list.append({
            'choice': 6.62607015e-34/((var_1*1.0e-3)*(var_2*3.6)),
            'unit': ' m',
            'point': 0.75
            })

        alt_list.append({
            'choice': 6.62607015e-34/((var_1*1.0e+3)*(var_2*3.6)),
            'unit': ' m',
            'point': 0.5
            })

        alt_list.append({
            'choice': 6.62607015e-34/((var_2/3.6)),
            'unit': ' m',
            'point': 0.0
            })

        alt_list.append({
            'choice': 6.62607015e-34*((var_1*1.0e-3)*(var_2/3.6)),
            'unit': ' m',
            'point': 0.0
            })

        text = f"""Calcule o comprimento de onda de uma bola de basebol que possui uma massa de {var_1:7.2f} {p2[2]} a uma velocidade de {var_2:7.2f} {p3[2]}. Seria possível observar os efeitos da física quântica nesse caso?"""

        figure = ''

        error_1 = random.uniform(p2[0], p2[1])
        error_2 = random.uniform(p3[0], p3[1])
        alt_list.append({
            'choice': 6.62607015e-34/((error_1*1.0e-3)*(error_2/3.6)),
            'unit': ' m',
            'point': 0.0
            })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'alternative': alternative_list}

    else:

        context = {}

    return context
