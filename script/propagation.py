#! /bin/python

import numpy as np

### Vars

    # Dk (dielectric constant), initialize variable

dk = float(0.0)

cvac = float(299792458.0000)

# Other vars:
#   mat = material
#   opt = option

### Body of the code

### --> Instructions <--

print(" ")
print("All measurements are in mm (millimiters) and ps (picoseconds)")
print("Decimal place must be separated by dot ( . ) and not comma")
print(" ")

### --> Inputs <---

# Input material

print(" Inputs:")
print(" ")
print("Material:")
print("Obs: currently only FR4 is supported, format it all lowercase (ex: fr4)")

# --> Input material <--
mat = input()

print(" ")

# --> Input trace length <--

print("Trace length (mm):")

length = float(input())

print("")

# --> Input option (stripline or microstrip) <--

print("Stripline or microstrip? (s/m)")

opt = input()

print("")

match opt:
    case "m":
        print("Microstrip chosen.")
        print(" ")

        # --> Input trace width <--

        print("Width of the trace (mm): ")

        width = float(input())

        print(" ")

        # --> Input distance to ground plane <--

        print("Distance to ground plane (mm): ")

        dgnd = float(input())
    case "s":
        pass
    case _:
        print("Error: invalid inputs")






# Print newline

print("")

### --> End of inputs <--

def propagation_delay_calc_stripline(cvac, dk, length):
    x = np.pow(10, float(9)) / float(299792458.0000) * np.sqrt(dk)
    
    tpd = x * length

    print(" ---> STRIPLINE <--- ")
    print(" ")
    print("The propagation delay in ps/mm not accounting for legnth is approx: ", x, " ps/mm in the stripline")
    print("Accounting for length is: ", tpd, " ps based on the length: ", length, " mm")
    print(" ")
    print("Chosen material's dielectric constant:    ", dk)


def propagation_delay_calc_microstrip(cvac, dk , width, dgnd, length):

    term_1 = (dk + 1) / 2
    term_2 = (dk - 1) / 2
    term_3 = np.pow((1 + ((12*dgnd) / width)), float(-0.5))
    term_4 = np.pow(float( 1 - (width / dgnd ) ), 2)

    ### --> Effective dielectric constant for microstrip <---

    dk_eff = float(0.0)

    if width < dgnd:
        dk_eff = (term_1 + term_2 * (term_3 + 0.04 * (term_4)))

    if width > dgnd:
        dk_eff = (term_1 + term_2 * term_3)

    ### --> Propagation delay microstrip calculation <---
    
    x = np.pow(10, float(9)) / float(299792458.0000) * np.sqrt(dk_eff)

    tpd = x * length

    print(" ---> MICROSTRIP <--- ")
    print("The propagation delay in ps/mm not accounting for legnth is approx: ", x, " ps/mm in the microstrip")
    print("Accounting for length is: ", tpd, " ps based on the length: ", length, " mm")
    print(" ")
    print("Chosen material's dielectric constant:    ", dk)
    print("Microstrip effective dielectric constant: ", dk_eff)


match mat:
    case "fr4":
        dk = float(4.5)
    case _:
        print("Error: material not implemented or wrong input")
        print("Possible inputs:")
        print(" input: fr4: PCB FR4, Dielectric constant = 4.5")

match opt:
    case "s":
        propagation_delay_calc_stripline(cvac, dk, length)
    case "m":
        propagation_delay_calc_microstrip(cvac, dk, width, dgnd, length)
    case _:
        print("Error: invalid inputs")

print(" ")
print("NOT PRODUCTION TESTED.")
print("Does not account for impedance.")
print("Version: pre_release_1.0")
print("Script by VerbenaIDK")

