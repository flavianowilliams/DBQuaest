import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte

def question(qpoint, opt, ntest):

    # constants

    cte_list = []

    formula_list = [
        '$E=\frac{n^2\pi^2\hbar^2}{2ma^2}\quad(n=1,2,\cdot)$',
        '$\lambda = \frac{32.97}{2n+1}a^2$'
    ]

    if opt == '001':

        type = 'conceptual'

        text = f"""Considere a molécula de Hexadieno
        	\\begin{{align*}}
		        C=C-C=C-C=C
	        \end{{align*}}
            Sabendo que o comprimento de ligação C-C é aproximadamente 1,4 \AA, e que o seu estado fundamental se encontra no nível n=3, determine o comprimento de onda da radiação máxima emitida pela molécula.

        """

        alt_list = [{'choice': '231','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': '194','consideration': 'Calculou o comprimento de onda do etileno','point': 0.5})
        alt_list.append({'choice': '207','consideration': 'Calculou o comprimento de onda do butadieno','point': 0.5})
        alt_list.append({'choice': '1616','consideration': 'Errou em definir a expressão do comprimento de onda máximo','point': 0.0})
        alt_list.append({'choice': '323','consideration': 'Errou em definir a expressão do comprimento de onda máximo','point': 0.0})

        figure = ''

        unit = '\\unit{\\nano\metre}'

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == '002':

        type = 'conceptual'

        text = f"""Duas moléculas de etileno podem se combinar para formar uma molécula de butadieno. Determine a energia de duas moléculas de etileno e uma de butadieno e verifique qual afirmação abaixo é verdadeira.

        """

        alt_list = [{'choice': 'Essa reação química forma uma molécula estável, pois a energia do butadieno é 18 vezes menor que duas moléculas de etileno.','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': 'Essa reação química forma uma molécula instável, pois a energia do butadieno é 18 vezes menor que duas moléculas de etileno.', 'consideration': 'Errou em afirmar que a estabilidade da formação não acontece com a diminuição da energia','point': 0.5})
        alt_list.append({'choice': 'Essa reação química forma uma molécula estável, pois a energia do butadieno é 18 vezes maior que duas moléculas de etileno.','consideration': 'Errou em afirmar que a estabilidade da formação somente acontece com o aumento da energia','point': 0.5})
        alt_list.append({'choice': 'Essa reação química forma uma molécula instável, pois a energia do butadieno é 18 vezes maior que duas moléculas de etileno.', 'consideration': 'Errou em calcular a diferença de energia de uma molécula de butadieno e duas de etileno','point': 0.0})
        alt_list.append({'choice': 'Essa reação química forma uma molécula estável, independente da energia do butadieno comparado à duas moléculas de etileno.','consideration': 'Errou em afirmar que a estabilidade da formação independe da diminuição da energia','point': 0.0})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == '003':

        type = 'conceptual'

        text = f"""Um elétron está livre para se movimentar ao longo de superfície na forma de um quadrado de lado L. Sabendo que pelo postulado de de Broglie $p_x = \hbar kx$ , $p_y = \hbar ky$ e que a função de onda deve ser nula nas extremidades do quadrado, determine a função de onda deste elétron."""

        alt_list = [{'choice': '$\psi(x,y)=c\sin k_x x\sin k_y y$','consideration': 'Alternativa correta','point': qpoint}]
        alt_list.append({'choice': '$\psi(x,y)=c\cos k_x x\cos k_y y$','consideration': 'Alternativa errada','point': 0.0})
        alt_list.append({'choice': '$\psi(x,y)=c\sin k_x x\cos k_y y$','consideration': 'Alternativa errada','point': 0.0})
        alt_list.append({'choice': '$\psi(x,y)=c\cos k_x x\sin k_y y$','consideration': 'Alternativa errada','point': 0.0})
        alt_list.append({'choice': '$\psi(x,y)=c_1\sin k_x x+c_2sin k_y y$','consideration': 'Alternativa errada','point': 0.0})

        figure = ''

        unit = ''

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
