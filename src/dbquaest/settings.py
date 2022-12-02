import os
from pathlib import Path
from dbquaest.electromagnetism import magnetism, electrodynamics, electrostatic, induced_magnetic_field, electromagnetic_induction
from dbquaest.quantum_physics import particle_wave_duality, uncertainty_principle, schrodinger_equation, potential_well, tunneling, bohrs_model
from dbquaest.waves import mhs, waves
from dbquaest.fluids import hydrostatic, hydrodynamics
from dbquaest.thermodynamics import zero_law
from dbquaest.mechanics import newtons_law, conservation_of_energy, particle_system, conservation_of_momentum
from dbquaest.relativity import special_relativity

# set base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# define modules

MODULES = [
    hydrostatic,
    hydrodynamics,
    newtons_law,
    conservation_of_energy,
    conservation_of_momentum,
    particle_system,
    zero_law,
    mhs,
    waves,
    electrostatic,
    electrodynamics,
    magnetism,
    induced_magnetic_field,
    electromagnetic_induction,
    particle_wave_duality,
    uncertainty_principle,
    bohrs_model,
    schrodinger_equation,
    potential_well,
    tunneling,
    special_relativity
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
