import random

def question(qpoint, opt):

    if opt == 'CEMAG001':

        type = 'conceptual'

        text = f"""A ﬁgura abaixo mostra a trajetória de uma partícula carregada $\\vec{{v}}$ representa a velocidade atravessando um campo magnético $\\vec{{B}}$. Determine a sua trajetória devido a ação da força magnética atuando sobre ela."""

        figure = 'CEMAG001'

        alt_list = [{'choice': 'Paralelo ao papel e circular no sentido anti-horário.', 'unit': '', 'point': qpoint}]
        alt_list.append({'choice': 'Paralelo ao papel e circular no sentido horário.', 'unit': '', 'point': 0.5*qpoint})
        alt_list.append({'choice': 'Paralelo ao papel e da direita para a esquerda.', 'unit': '', 'point': 0.0})
        alt_list.append({'choice': 'Paralelo ao papel e da esquerda para a direita.', 'unit': '', 'point': 0.0})
        alt_list.append({'choice': 'Paralelo ao papel e na vertical.', 'unit': '', 'point': 0.0})

        indx = random.sample(range(0,5),5)

        alternative_list = [alt_list[u] for u in indx]

        context = {'type': type, 'text': text, 'figure': figure, 'alternative': alternative_list}

    else:

        context = {}        

    return context
