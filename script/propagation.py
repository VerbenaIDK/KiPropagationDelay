#! /bin/python

import math

### Vars

    # Er (dielectric constant) for FR4
fr_er = 4.5

    # Approximate Ereff for FR4
fr_ereff = 3.24

    # Vc? important for calculation, mm/ns, see:
    # https://www.protoexpress.com/blog/signal-propagation-delay-pcb/
    # 33,464566

### Body of the code

print("Input length of trace (mm):")
length = float(input())
float(length)

print("")

print("Stripline or microstrip? (s/m)")
opt = input()
print("")

# Currently only FR4 supported, ignore
#material = input()

def propagation_delay_calc_stripline(length, fr_er):
    # Tpd calculation
    i = 33.464566 * math.sqrt(fr_er)
    print("The propagation delay in a stripline in FR4 is ", i, " mm/ps")

    float(i)
    float(length)
    # Rough approximation of total Tpd by Tpd*length
    tpd = length / i
    float(tpd)

    print("")
    print("The propagation delay total is roughly ", tpd, " ps")
    print("Roughly calculated by propagation delay / length")
    print(" ")
    print("Remember to do it multiple times per interconnect")
    print("These calculations do not include impedance and are for reference or feeding into other calculations in different scripts.")

def propagation_delay_calc_microstrip(length, fr_ereff):
    i = 33.464566 * math.sqrt(fr_ereff)
    print("The propagation delay in a microstrip in FR4 is ", i, " mm/ps")

    float(i)
    float(length)
    tpd = length / i
    float(tpd)

    print("")
    print("The propagation delay total is roughly ", tpd, " ps")
    print("Roughly calculated by propagation delay / length")
    print(" ")
    print("Remember to do it multiple times per interconnect")
    print("These calculations do not include impedance and are for reference or feeding into other calculations in different scripts.")


match opt:
    case "s":
        propagation_delay_calc_stripline(length, fr_er)
    case "m":
        propagation_delay_calc_microstrip(length, fr_ereff)

print(" ")
print("Not production tested, script by VerbenaIDK")

