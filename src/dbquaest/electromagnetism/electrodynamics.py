import random

def question(qpoint, opt, ntest):

    if opt == 'OEELD001':

        type = 'objective'

        p1 = [1.0, 10.0, 'A'] # min, max
        value_1 = random.uniform(p1[0], p1[1])
        alt_list = [{'choice': value_1*60/1.6e-19, 'point': qpoint}]
        alt_list.append({'choice': value_1/1.6e-19, 'point': 0.75*qpoint})
        alt_list.append({'choice': value_1*60*1.6e-19, 'point': 0.50*qpoint})
        alt_list.append({'choice': value_1*1.6e-19, 'point': 0.50*qpoint})

        text = f"""Uma corrente elétrica de {value_1:7.2f} {p1[2]} percorre um ﬁo de cobre. Sabendo-se que a carga de um elétron é igual a $1,6\\times 10^{{-19}}\;C$, qual é o número de elétrons que atravessa, por minuto, a seção reta desse ﬁo?"""

        figure = ''

        unit = ''

        for i in range(6):
            value_1 = random.uniform(p1[0], p1[1])*1.e+19
            alt_list.append({'choice': value_1, 'point': 0.0})

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == 'OEELD002':

        type = 'objective'

        p1 = [1.0, 5.0, 'A'] # min, max
        value_1 = random.uniform(p1[0], p1[1])
        alt_list = [{'choice': 120*value_1, 'point': qpoint}]
        alt_list.append({'choice': 120*value_1**2, 'point': 0.0})
        alt_list.append({'choice': 120/value_1, 'point': 0.0})
        alt_list.append({'choice': value_1/120, 'point': 0.0})

        text = f"""Uma diferença de potencial de 120 V é aplicada a uma bomba d’água. Sabe-se que em funcionamento, o motor da bomba é percorrido por uma corrente de {value_1:7.2f} {p1[2]}. Qual é a potência desenvolvida nesse motor?"""

        figure = ''

        unit = 'W'

        error = [0, 36000] # min, max
        for i in range(6):
            value_1 = random.uniform(error[0], error[1])
            alt_list.append({'choice': value_1, 'point': 0.0})

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
