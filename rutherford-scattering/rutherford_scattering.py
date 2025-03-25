def rutherford_scattering_formula(foil_atomic_conc:float,foil_thickness:float,num_alpha:int,foil_atomic_num:int,alpha_particle_energy:float,theta:float,elementary_charge:float=1.6021e-19,e_0:float=8.8524e-12):
    constant = num_alpha * foil_atomic_conc * foil_thickness * (foil_atomic_num**2) * (elementary_charge**4)
    denom_factor_1 = (8 * np.pi * e_0 * alpha_particle_energy)**2
    denom_factor_2 = np.sin(theta/2)**4

    return constant / (denom_factor_1 * denom_factor_2)


if __name__ == "__main__":
    pass
    import numpy as np

