#!/usr/bin/python
#Diego A-Z
#ideas by Justin19932012
import math

pi = 3.14

# Converting rectangular to polar coordinates. "x" and "y" cartesian cordinates are calculated, and then converted to polar format(r, theta).
def rectangular_to_polar(x, y):

    angle = math.atan((y/x))

    angle = angle * (180/pi)

    magnitude = (math.sqrt((x*x)+(y*y)))

    polar = magnitude, angle

    return polar



# Convering polar to rectangular cordinates. Calculates a polar format to "x" and "y" cordinates.
def polar_to_rectangular(polar_number):

    y = polar_number[0] * (math.sin(polar_number[1] * pi/180))

    x = polar_number[0] * (math.cos(polar_number[1] * pi/180))

    rectangular = x, y

    return rectangular


#Finding Magnitude. Calculate a real and imaginary number to get the magnitude.
def magnitude(number):

    magnitude = math.sqrt((number[0] * number[0]) + (number[1]* number[1]))

    return magnitude



# complex_add returns the sum of complex numbers. def complex_division returns the quotient from a-b. complex_mul retuns the product of a and b.

def complex_add(complex_a, complex_b):
    if complex_a[1] == 0:
        x1 = complex_a[0]
        y1 = 0
    else:
        x1 = float(complex_a[0]) * math.cos(pi/180 * complex_a[1])
        y1 = float(complex_a[0]) * math.sin(pi/180 * complex_a[1])
    if complex_b[1] == 0:
        x2 = complex_b[0]
        y2 = 0
    else:
        x2 = float(complex_b[0]) * math.cos(pi/180 * complex_b[1])
        y2 = float(complex_b[0]) * math.sin(pi/180 * complex_b[1])


    x_total =  x1 + x2
    y_total =  y1 + y2
    answer = rectangular_to_polar(x_total, y_total)
    return answer[0], answer[1]

def complex_division(complex_a, complex_b):
    real_answer = complex_a[0] / complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return (real_answer, imag_answer)

def complex_multiplication(complex_a, complex_b):
    real_answer = complex_a[0] * complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return (real_answer, imag_answer)
#Choosing parallel or series methode.
mode_whichone = raw_input('series or parallel? :')

if (mode_whichone == 'series'):
    print('pi calculating series with AC with R, L AND C.\n')
    print('type 0, if there is no value?:')
    frequency = input(' frequency (in Hz)?:')
    voltage = input(' voltage (in RMS)?:')
    resistor_value = input('resistance (in Ohms)?:')
    inductor_value = input('value of the inductor (in Henrys)?:')
    inductor_resistance = input('\nresistance of the inductor? (in Ohms): ')
    capacitor_value = input('\nvalue of capacitor? (in Farads): ')


# Calculations and values
    total_resistance = inductor_resistance + resistor_value
    inductor_reactance = 2 * pi * frequency * inductor_value
    magnitude_inductor_reactance = (inductor_resistance, inductor_reactance)
    magnitude_inductor_reactance = magnitude(magnitude_inductor_reactance)
    capacitor_reactance = (1/(2 * pi * frequency * capacitor_value))
    impedance = total_resistance, (inductor_reactance + -capacitor_reactance)
    magnitude_impedance = magnitude(impedance)
    current = float(voltage) / float(magnitude_impedance)
    V_R = current * resistor_value
    V_L = current * inductor_reactance
    V_C = current * capacitor_reactance

# Calculating + $ - angle phases.

    if inductor_reactance > capacitor_reactance:

     calculation_made = impedance[1] / impedance[0]

    else:

        if capacitor_reactance > inductor_reactance:

         calculation_made = impedance[0] / impedance[1]

        else:

         calculation_made = 0

    phase_radians = math.atan(calculation_made)

    phase_angle = phase_radians * 180/pi

# Getting the results ...

    if capacitor_reactance > inductor_reactance:

         print('current leads voltage by %f degrees ' % phase_angle)

    if inductor_reactance > capacitor_reactance:

        print('current follows voltage by %f degrees' % phase_angle)

    print('\n total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))

    print(' magnitude of impedance is: %.2f' % magnitude_impedance)

    print(' current is: %f A' % current)

    print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (V_R, V_L, V_C))

# Choosing parallel
if (mode_whichone == 'parallel'):
    print('pi calculating parallel with AC with R, L AND C.\n')
    print('type 0, if there is no value?:')
    frequency = input(' frequency (in Hz)?:')
    voltage = input(' voltage (in RMS)?:')
    resistor_value = input('resistance (in Ohms)?:')
    inductor_value = input('value of the inductor (in Henrys)?:')
    inductor_resistance = input('\nresistance of the inductor? (in Ohms): ')
    capacitor_value = input('\nvalue of capacitor? (in Farads): ')

# Calculating with polar format(r,theta)

    polar_voltage = voltage, 0

    resistor_value = float(resistor_value)

    resistance = float(resistor_value), 0

    inductor_resistance = (float(inductor_resistance), 0)

    inductor_reactance = (2 * pi * frequency * inductor_value, 90)

    capacitor_reactance = (1 / (2 * pi * frequency * capacitor_value), -90)

    inductor_path = complex_add(inductor_resistance, inductor_reactance)

    one = (float(1), 0)

# Calculation impedance inversions

    inverse_resistance = complex_division(one, resistance)

    inverse_p_capacitor_reactance = complex_division(one, capacitor_reactance)

    inverse_p_inductor_reactance = complex_division(one, inductor_path)

    print'R-1 = %f %f, C-1 = %f, %f L-1 = %f, %f' % (inverse_resistance[0], inverse_resistance[1], inverse_p_capacitor_reactance[0], inverse_p_capacitor_reactance[1], inverse_p_inductor_reactance[0], inverse_p_inductor_reactance[1])

# calculating impedance with denominators.

# Using ((1/Xl) + (1/R) + (1/Xc))

    denominator = complex_add(inverse_p_capacitor_reactance, inverse_p_inductor_reactance)

    print 'L-1 + C-1 = %f, %f' % (denominator[0], denominator[1])

    denominator_f = complex_add(inverse_resistance, denominator)

    print ' L-1 + C-1 + R-1 = %f, %f' % (denominator_f[0], denominator_f[1])

    total_impedance = complex_division(one, denominator_f)

# Current calculations. Utilizes current divider equation for impedances in parallel

    total_current = complex_division(polar_voltage, total_impedance)

#   inductor_branch_current = total_current * (total_impedance[0] / inductor_branch[0])

#    cap_branch_current = total_current * (total_impedance[0] / capacitance[0])

#   resistor_branch_current = total_current * (total_impedance[0] / resistance[0])



    print ' total current is %f with a %f phase shift' % total_current

# Printing out the results for the user!

    print('The magnitude of the impedance is %f' % total_impedance[0])
