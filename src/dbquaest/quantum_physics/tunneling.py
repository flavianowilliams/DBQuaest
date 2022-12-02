import random
from random import choice
from dbquaest.utils import random_vars
from dbquaest.constants import cte
from math import log, sqrt, sinh

def question(qpoint, opt, ntest):

    # constants

    me = cte('electron mass (eV)')
    me_value = me['value']

    h = cte('reduced Planck constant (eV)')
    h_value = h['value']

    c = cte('speed of light')
    c_value = c['value']

    cte_list = [
        f"{me['symbol']}={me['value']} {me['unit']}",
        f"{h['symbol']}={h['value']} {h['unit']}",
        f"{c['symbol']}={c['value']} {c['unit']}",
    ]

    formula_list = []

    if opt == '001':

        type = 'objective'

        # generating input values list
        p1 = (0.5, 20, '\\unit{\electronvolt}') # min, max, unidade
        p2 = (21, 50, '\\unit{\electronvolt}') # min, max, unidade
        p3 = (0.05, 0.9, '') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Um elétron com energia cinética de \\num{{{value_1[i0]}}} {p1[2]} incide em um potencial degrau de {{{value_2[i0]}}} {p2[2]}. Determine o alcance que ele irá penetrar na região energeticamente proibida quando a sua probabilidade for {{{value_3[i0]}}} vezes o seu valor ao incidir no degrau de potencial.
        
        """

        kappa = sqrt(2*(me_value*1.e6)*((value_2[i0]-value_1[i0])))/(h_value*c_value)
        kappa_err1 = sqrt(2*(me_value)*((value_2[i0]-value_1[i0])))/(h_value*c_value)
        kappa_err2 = sqrt(2*(me_value*1.e6)*((value_2[i0]-value_1[i0])))/(h_value)
        kappa_err3 = sqrt(2*(me_value*1.e6)*((value_2[i0])))/(h_value*c_value)
        kappa_err4 = sqrt(2*(me_value*1.e6)*((value_1[i0])))/(h_value*c_value)

        alt_list = [{
            'choice': (-log(value_3[i0])/(2*kappa))*1.e9,
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 0,
            'consideration': 'Errou em considerar a probabilidade de penetração na região energeticamente proibida',
            'point': 0.0
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa)),
            'consideration': 'Errou em converter a unidade metro para nanometro',
            'point': 0.75
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err1))*1.e9,
            'consideration': 'Errou em converter a unidade megaelétron-volt para elétron-volt',
            'point': 0.75
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err1)),
            'consideration': 'Errou em converter a unidade megaelétron-volt para elétron-volt e metro para nanometro',
            'point': 0.5
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err2))*1.e9,
            'consideration': 'Errou em considerar a velocidade da luz na expressão no fator de penetração',
            'point': 0.5
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err2)),
            'consideration': 'Errou em considerar a velocidade da luz na expressão no fator de penetração e em converter a unidade metro para nanometro',
            'point': 0.25
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err3))*1.e9,
            'consideration': 'Errou em definir a expressão do fator de penetração',
            'point': 0.5
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err4))*1.e9,
            'consideration': 'Errou em definir a expressão do fator de penetração',
            'point': 0.5
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err3)),
            'consideration': 'Errou em definir a expressão do fator de penetração e em converter a unidade metro para nanometro',
            'point': 0.25
            })

        alt_list.append({
            'choice': (-log(value_3[i0])/(2*kappa_err4)),
            'consideration': 'Errou em definir a expressão do fator de penetração e em converter a unidade metro para nanometro',
            'point': 0.25
            })

        figure = ''

        unit = '\\unit{\\nano\metre}'

        for i in range(ntest):
            if i not in [i0]:
                kappa = sqrt(2*(me_value*1.e6)*((value_2[i]-value_1[i])))/(h_value*c_value)
                val = (-log(value_3[i])/(2*kappa))*1.e9
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 0.0001:
                    alt_list.append({
                        'choice': val,
                        'consideration': 'Alternativa errada',
                        'point': 0.0
                        })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    elif opt == '002':

        type = 'objective'

        # generating input values list
        p1 = (0.1, 0.3, '\\unit{\\nano\metre}') # min, max, unidade
        p2 = (5, 10, '\\unit{\electronvolt}') # min, max, unidade
        p3 = (1, 4, '\\unit{\\volt}') # min, max, unidade

        value_1 = random_vars(p1, ntest)
        value_2 = random_vars(p2, ntest)
        value_3 = random_vars(p3, ntest)

        i0 = choice([i for i in range(10)])

        text = f"""Em um dispositivo semicondutor, uma camada de óxido forma uma barreira com \\num{{{value_1[i0]}}} {p1[2]} de largura e {{{value_2[i0]}}} {p2[2]} de altura. Elétrons chegam a barreira depois de serem acelerados por uma tensão de {{{value_3[i0]}}} {p3[2]}. Que fração de elétrons incidentes conseguem atravessar a barreira por tunelamento?
        
        """

        kappa = sqrt(2*(me_value*1.e6)*((value_2[i0]-value_3[i0])))/(h_value*c_value)
        kappa_err1 = sqrt(2*(me_value)*((value_2[i0]-value_3[i0])))/(h_value*c_value)
        kappa_err2 = sqrt(2*(me_value*1.e6)*((value_2[i0]-value_3[i0])))/(h_value)
        kappa_err3 = sqrt(2*(me_value*1.e6)*((value_2[i0])))/(h_value*c_value)
        kappa_err4 = sqrt(2*(me_value*1.e6)*((value_3[i0])))/(h_value*c_value)

        alt_list = [{
            'choice': 100/(1+(sinh((kappa*1.e-9)*value_1[i0])*value_2[i0])**2/(4*value_3[i0]*(value_2[i0]-value_3[i0]))),
            'consideration': 'Alternativa correta',
            'point': qpoint
            }]

        alt_list.append({
            'choice': 0,
            'consideration': 'Errou em considerar a probabilidade de penetração na região energeticamente proibida',
            'point': 0.0
            })

        alt_list.append({
            'choice': 1/(1+(sinh((kappa*1.e-9)*value_1[i0])*value_2[i0])**2/(4*value_3[i0]*(value_2[i0]-value_3[i0]))),
            'consideration': 'Errou em calcular o valor em porcentagem',
            'point': 0.75
            })

        alt_list.append({
            'choice': 100/(1+(sinh((kappa_err1*1.e-9)*value_1[i0])*value_2[i0])**2/(4*value_3[i0]*(value_2[i0]-value_3[i0]))),
            'consideration': 'Errou em converter a unidade megaelétron-volt para elétron-volt',
            'point': 0.75
            })

        alt_list.append({
            'choice': 100/(1+(sinh((kappa_err3*1.e-9)*value_1[i0])*value_2[i0])**2/(4*value_3[i0]*(value_2[i0]-value_3[i0]))),
            'consideration': 'Errou em definir a expressão do fator de penetração',
            'point': 0.5
            })

        alt_list.append({
            'choice': 100/(1+(sinh((kappa_err4*1.e-9)*value_1[i0])*value_2[i0])**2/(4*value_3[i0]*(value_2[i0]-value_3[i0]))),
            'consideration': 'Errou em definir a expressão do fator de penetração',
            'point': 0.5
            })

        figure = ''

        unit = '\\unit{\percent}'

        for i in range(ntest):
            if i not in [i0]:
                kappa = sqrt(2*(me_value*1.e6)*((value_2[i]-value_3[i])))/(h_value*c_value)
                val = 100/(1+(sinh((kappa*1.e-9)*value_1[i])*value_2[i])**2/(4*value_3[i]*(value_2[i]-value_3[i])))
                minx_list = [abs(val-item['choice']) for item in alt_list]
                if min(minx_list) >= 0.001:
                    alt_list.append({
                        'choice': val,
                        'consideration': 'Alternativa errada',
                        'point': 0.0
                        })

        indx = random.sample(range(0,10),10)

        alternative_list = [alt_list[u] for u in indx]

        context = {'constants': cte_list, 'formulas': formula_list, 'type': type, 'text': text, 'figure': figure, 'unit': unit, 'alternative': alternative_list}

    else:

        context = {}

    return context
