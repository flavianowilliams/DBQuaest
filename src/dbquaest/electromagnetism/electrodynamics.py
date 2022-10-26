import random
from sys import ps2

def question(qpoint, opt):

#    seed(1)

    if opt == 'OEELD001':

        p1 = [1.0, 10.0, 'A'] # min, max
        value_1 = random.uniform(p1[0], p1[1])
        alt_list = [{'choice': value_1, 'unit': '', 'point': qpoint}]

        text = f"""Uma corrente elétrica de {value_1:7.2f} percorre um ﬁo de cobre. Sabendo-se que a carga de um elétron é igual a $1,6\times 10^{{-19}}\;C$, qual é o número de elétrons que atravessa, por minuto, a seção reta desse ﬁo?"""

        figure = ''

        for i in range(9):
            value_1 = random.uniform(p1[0], p1[1])
            alt_list.append({'choice': value_1, 'unit': '', 'point': 0.0})

    else:
        
        text = ''

        figure = ''

        alt_list = [{'choice': None, 'unit': None, 'point': None}]

    indx = random.sample(range(0,10),10)

    alternative_list = [alt_list[u] for u in indx]

#    alternative = sorted(alternative, key=lambda u: u['value'])

    context = {'text': text, 'figure': figure, 'alternative': alternative_list}

    return context

def c_question(qpoint, opt):

#    seed(1)

    if opt == 'xxxxx':

        text = f"""xxxx"""

        figure = ''

        p1 = [1.0, 10.0, 'kg'] # min, max
        p2 = [1.0, 10.0, 'm/s'] # min, max

        alt_list = [{'choice': 'Paralelo ao papel e da direita para a esquerda.', 'point': 0.0}]
        alt_list.append({'choice': 'Paralelo ao papel e da esquerda para a direita.', 'point': 0.0})
        alt_list.append({'choice': 'Paralelo ao papel e na vertical.', 'point': 0.0})
        alt_list.append({'choice': 'Paralelo ao papel e circular no sentido horário.', 'point': 0.5*qpoint})
        alt_list.append({'choice': 'Paralelo ao papel e circular no sentido anti-horário.', 'point': qpoint})

    else:
        
        text = ''

        figure = ''

        alt_list = [{'choice': None, 'point': None}]

    indx = random.sample(range(0,5),5)

    alternative_list = [alt_list[u] for u in indx]

#    alternative = sorted(alternative, key=lambda u: u['value'])

    context = {'text': text, 'figure': figure, 'alternative': alternative_list}

    return context
