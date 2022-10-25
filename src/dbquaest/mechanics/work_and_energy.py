import random
#from random import random as rnd

def question(qpoint, opt):

#    seed(1)

    if opt == 'MWE001':

        p1 = [1.0, 10.0, 'kg'] # min, max
        p2 = [1.0, 10.0, 'm/s'] # min, max
        value_1 = p1[0]+(p1[1]-p1[0])*random.random()
        value_2 = p2[0]+(p2[1]-p2[0])*random.random()
        alt_list = [{'value': 0.5*value_1*value_2**2, 'unit': 'J', 'point': qpoint}]

        text = (
            'Considere uma partícula de massa {:7.2f} {} e velocidade {:7.2f} {}. Determine a sua energia cinética.'.format(value_1, p1[2], value_2, p2[2])
            )

        figure = 'MWE001'

        for i in range(9):
            value_1 = p1[0]+(p1[1]-p1[0])*random.random()
            value_2 = p2[0]+(p2[1]-p2[0])*random.random()
            alt_list.append({'value': value_1*value_2**2, 'unit': 'J', 'point': 0.0})

    elif opt == 'MWE002':

        p1 = [-10.0, 10.0, 'J'] # min, max
        value_1 = p1[0]+(p1[1]-p1[0])*random.random()
        alt_list = [{'value': value_1, 'unit': 'J', 'point': qpoint}]

        text = (
            'Durante sua trajetória uma partícula realizou um trabalho de {:7.2f} {}. Qual foi a variação da sua energia cinética?'.format(value_1, p1[2])
            )

        figure = ''

        for i in range(9):
            value_1 = p1[0]+(p1[1]-p1[0])*random.random()
            alt_list.append({'value': value_1, 'unit': 'J', 'point': 0.0})

    else:
        
        text = ''

        alt_list = [{'value': None, 'unit': None, 'point': None}]

    indx = random.sample(range(0,10),10)

    alternative_list = [alt_list[u] for u in indx]

#    alternative = sorted(alternative, key=lambda u: u['value'])

    context = {'text': text, 'figure': figure, 'alternative': alternative_list}

    return context

#def gen_random(nlist):
#
#    indx = list()
#
#    for i in range(10):
#        number = random.randrange(0,9,1)
#        if (number in indx) == False:
#            indx.append(number)
#
#    return indx

#class Quest():
#
#    def __init__(self, opt):
#        self.opt = opt
#
#    def setQuestion(self):
#
#        error = list()
#        seed(1)
#
#        if self.opt == 'MWE001':
#            p1 = [1.0, 10.0] # min, max
#            p2 = [1.0, 10.0] # min, max
#            value_1 = p1[0]+(p1[1]-p1[0])*random()
#            value_2 = p2[0]+(p2[1]-p2[0])*random()
#            result = 0.5*value_1*value_2**2
#            text = ('Considere uma partícula de massa {:7.2f} kg e velocidade {:7.2f} m/s. Determine a sua energia cinética.'.format(value_1, value_2))
#            for i in range(9):
#                value_1 = p1[0]+(p1[1]-p1[0])*random()
#                value_2 = p2[0]+(p2[1]-p2[0])*random()
#                error.append(value_1*value_2**2)
#            context = {'text': text, 'result': result, 'error': error}
#        else:
#            return print('There is no question')
#
#        return context
