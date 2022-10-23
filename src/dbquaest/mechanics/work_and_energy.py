from random import seed, random
from unittest import result

def question(opt):

    error = list()
#    seed(1)

    if opt == 'MWE001':

        p1 = [1.0, 10.0] # min, max
        p2 = [1.0, 10.0] # min, max
        value_1 = p1[0]+(p1[1]-p1[0])*random()
        value_2 = p2[0]+(p2[1]-p2[0])*random()
        result = 0.5*value_1*value_2**2

        text = ('Considere uma partícula de massa {:7.2f} kg e velocidade {:7.2f} m/s. Determine a sua energia cinética.'.format(value_1, value_2))

        for i in range(9):
            value_1 = p1[0]+(p1[1]-p1[0])*random()
            value_2 = p2[0]+(p2[1]-p2[0])*random()
            error.append(value_1*value_2**2)

        context = {'text': text, 'result': result, 'error': error}

    elif opt == 'MWE002':

        p1 = [-10, 10.0] # min, max
        value_1 = p1[0]+(p1[1]-p1[0])*random()
        result = value_1

        text = ('Durante sua trajetória uma partícula realizou um trabalho de {:7.2f}. Qual foi a variação da sua energia cinética?'.format(value_1))

        for i in range(9):
            value_1 = p1[0]+(p1[1]-p1[0])*random()
            error.append(value_1)

        context = {'text': text, 'result': result, 'error': error}


    else:
        return print('There is no question')

    return context

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
