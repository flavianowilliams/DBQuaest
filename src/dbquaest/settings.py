import os
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

# environment variables

# Set environment variables

with open(f"{BASE_DIR}/src/dbquaest/.env", 'r') as file:
    txt = file.readlines()
    env_list = [item.replace('\n', '').split('=') for item in txt]

os.environ[env_list[0][0]] = env_list[0][1]
os.environ[env_list[1][0]] = env_list[1][1]

print(os.getenv('EMAIL'), os.getenv('PASSWORD'))
