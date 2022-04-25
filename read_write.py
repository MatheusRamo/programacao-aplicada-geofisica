import numpy as np


def read_file(filename):
    array = np.array('d')
    with open(filename, "rb") as file:
        array = np.fromfile(file, np.float64)

    return array

def quadrature_and_phase(*files):
    E_real = read_file(files[0])
    E_img = read_file(files[1])
    n = len(E_img)
    Ex_mod = np.zeros(n, np.float64)
    Ex_phase = np.zeros(n, np.float64)

    for i in range(n):
        Ex_mod[i] = np.sqrt(E_real[i]**2 + E_img[i]**2)
        Ex_phase[i] = np.arctan(E_img[i]/E_real[i])

    return Ex_mod, Ex_phase

def write_binary_files(*files):
    Ex_mod, Ex_phase = quadrature_and_phase(files[0], files[1])
    Ex_mod.tofile("quadrature.outb")
    Ex_phase.tofile("phase.outb")

def write_text_file(*files):
    Ex_mod, Ex_phase = quadrature_and_phase(files[0], files[1])
    n = len(Ex_mod)
    with open("quadrature_and_phase.txt", "w") as txt:
        txt.write("\n")
        txt.write("Quadrature and Phase of field")
        txt.write("\n")
        for i in range(n):
            txt.write(f"{str(Ex_mod[i]):<24} {str(Ex_phase[i]):<24}\n")

if __name__ == "__main__":
    pass
