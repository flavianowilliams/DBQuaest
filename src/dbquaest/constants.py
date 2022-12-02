def cte(input):

    constants_list = [
        {'type': 'gravity', 'symbol': r'g', 'value': 10.0, 'unit': '$m/s^2$'},
        {'type': 'gravity 2', 'symbol': r'g', 'value': 9.8, 'unit': '$m/s^2$'},
        {'type': 'water density', 'symbol': '$\rho_{H_2O}$', 'value': 1000.0, 'unit': '$kg/m^3$'},
        {'type': 'Planck constant (eV)', 'symbol': 'h', 'value': 4.14e-15, 'unit': '$eV\cdot s$'},
        {'type': 'Planck constant', 'symbol': 'h', 'value': 6.63e-34, 'unit': '$kg\cdot m^2/s$'},
        {'type': 'reduced Planck constant (eV)', 'symbol': '$\hbar$', 'value': 6.58e-16, 'unit': '$eV\cdot s$'},
        {'type': 'speed of light', 'symbol': 'c', 'value': 3.0e8, 'unit': 'm/s'},
        {'type': 'permeability', 'symbol': '$\mu_0$', 'value': 1.26e-6, 'unit': '$N/A^2$'},
        {'type': 'electron mass (eV)', 'symbol': '$m_e$', 'value': 0.511, 'unit': '$MeV/c^2$'},
        {'type': 'proton charge', 'symbol': '$e$', 'value': 1.6e-19, 'unit': '$C$'},
        ]

    value = list(filter(lambda u: u['type'] == input, constants_list))

    return value[0]
