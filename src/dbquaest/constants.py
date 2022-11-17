def cte(input):

    constants_list = [
        {'type': 'gravity', 'symbol': r'g', 'value': 10.0, 'unit': r'$m/s^2$'},
        {'type': 'gravity 2', 'symbol': r'g', 'value': 9.8, 'unit': r'$m/s^2$'},
        {'type': 'water density', 'symbol': r'$\rho_{H2O}$', 'value': 1000.0, 'unit': r'$kg/m^3$'},
        ]

    value = list(filter(lambda u: u['type'] == input, constants_list))

    value = value[0]

    return value