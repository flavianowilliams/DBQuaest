def cte(input):

    constants_list = [
        {'type': 'gravity', 'symbol': r'g', 'value': 10.0, 'unit': '$m/s^2$'},
        {'type': 'gravity 2', 'symbol': r'g', 'value': 9.8, 'unit': '$m/s^2$'},
        {'type': 'water density', 'symbol': '$\rho_{H_2O}$', 'value': 1000.0, 'unit': '$kg/m^3$'},
        {'type': 'Planck constant (eV)', 'symbol': 'h', 'value': 4.1357e-15, 'unit': '$eV\cdot s$'},
        {'type': 'Planck constant', 'symbol': 'h', 'value': 6.62607015e-34, 'unit': '$kg\cdot m^2/s$'},
        {'type': 'speed of light', 'symbol': 'c', 'value': 300.0e8, 'unit': 'm/s'},
        ]

    value = list(filter(lambda u: u['type'] == input, constants_list))

    return value[0]
