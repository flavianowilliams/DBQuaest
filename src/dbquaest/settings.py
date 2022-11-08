from pathlib import Path
from dbquaest.electromagnetism import magnetism, electrodynamics, electrostatic, induced_magnetic_field
from dbquaest.quantum_physics import particle_wave_duality, uncertainty_principle, schrodinger_equation

# set base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# define modules

MODULES = [
    electrostatic,
    electrodynamics,
    magnetism,
    induced_magnetic_field,
    particle_wave_duality,
    uncertainty_principle,
    schrodinger_equation
    ]
