# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:23:34 2021

@author: Sayedul
"""
import numpy as np
import matplotlib.pyplot as plt
magnitude_A=float(input("Enter magnitude of phase A :"))
angle_A=float(input("Enter angle of phase A (degree) :"))

magnitude_B=float(input("Enter magnitude of phase B :"))
angle_B=float(input("Enter angle of phase B (degree) :"))

magnitude_C=float(input("Enter magnitude of phase C :"))
angle_C=float(input("Enter angle of phase C (degree) :"))

#phasot to cartesian conversion
def phasor2cart(r, theta):
    theta_rad=(np.pi/180)*theta
    return r*np.exp(1j*theta_rad)
# convert cartesian to phasor
def cart2phasor(z):
    return (np.abs(z), (180/np.pi)*np.angle(z))

a=phasor2cart(1,120)

A=np.array([[1, 1, 1], [1, a**2, a], [1, a, a**2]])

unbalanced=np.array([phasor2cart(magnitude_A, angle_A), 
                    phasor2cart(magnitude_B, angle_B), 
                    phasor2cart(magnitude_C, angle_C)])
inverse_A=np.linalg.inv(A)

sequence_components_A=np.dot(inverse_A, unbalanced)

# positive negative and zero sequence components of phase A
Va_zero=sequence_components_A[0]
Va_pos=sequence_components_A[1]
Va_neg=sequence_components_A[2]

# positive negative and zero sequence components of phase B
Vb_zero=Va_zero
Vb_pos=a**2*Va_pos
Vb_neg=a*Va_neg
# positive negative and zero sequence components of phase C
Vc_zero=Va_zero
Vc_pos=a*Va_pos
Vc_neg=a**2*Va_neg
#define vector plot function
def vector_plot(x_start, y_start, x_end, y_end, color):
    x_round=np.around(x_end, 3)
    y_round=np.around(y_end, 3)
    plt.quiver(0, 0,x_round, y_round, color=color, scale_units="xy", angles="xy", scale=1)
    plt.xlim(np.min(unbalanced.real),np.max(unbalanced.real))
    plt.ylim(np.min(unbalanced.imag),np.max(unbalanced.imag))

all_components=np.array([[Va_zero, Vb_zero, Vc_zero], 
                         [Va_pos, Vb_pos, Vc_pos], 
                         [Va_neg, Vb_neg, Vc_neg]])
print(np.around(all_components, 3))
#Original unbalanced 3-phase vector plot
vector_plot(0, 0, unbalanced[0].real, unbalanced[0].imag, "red")
vector_plot(0, 0, unbalanced[1].real, unbalanced[1].imag, "blue")
vector_plot(0, 0, unbalanced[2].real, unbalanced[2].imag, "green")
