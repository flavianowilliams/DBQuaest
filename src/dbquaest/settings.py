from pathlib import Path
from dbquaest.electromagnetism import magnetism, electrodynamics, electrostatic, induced_magnetic_field
from dbquaest.quantum_physics import particle_wave_duality, uncertainty_principle, schrodinger_equation
from dbquaest.waves import mhs
from dbquaest.fluids import hydrostatic, hydrodynamics

# set base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# define modules

MODULES = [
    hydrostatic,
    hydrodynamics,
    mhs,
    electrostatic,
    electrodynamics,
    magnetism,
    induced_magnetic_field,
    particle_wave_duality,
    uncertainty_principle,
    schrodinger_equation
    ]

# define database directory

DB_DIR = '/home/flaviano/Dropbox/IFPR/ensino/atividades/'