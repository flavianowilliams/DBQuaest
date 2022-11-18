def cte(input):

    constants_list = [
        {'type': 'gravity', 'symbol': r'g', 'value': 10.0, 'unit': r'$m/s^2$'},
        {'type': 'gravity 2', 'symbol': r'g', 'value': 9.8, 'unit': r'$m/s^2$'},
        {'type': 'water density', 'symbol': '$\rho_{H2O}$', 'value': 1000.0, 'unit': '$kg/m^3$'},
        {'type': 'Planck constant (eV)', 'symbol': 'h', 'value': 4.1357e-15, 'unit': f'$eV*s$'},
        {'type': 'Planck constant', 'symbol': 'h', 'value': 6.62607015e-34, 'unit': '$kg*m^2/s$'},
        {'type': 'speed of light', 'symbol': 'c', 'value': 299792458, 'unit': r'm/s'},
        ]

    value = list(filter(lambda u: u['type'] == input, constants_list))

    value = value[0]

    return value
