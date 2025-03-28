import numpy as np
import matplotlib.pyplot as plt

from poplt import poplt
from segop import segop
from knots import knots
from globop import globop
from cpoints import cpoints
from iguess0 import iguess0
from DrawBezierCurve import drawBezierCurve
from cubicBezierToPolyline import cubicBezierToPolyline

def BezierFitDemo():
    # Demonstrate two different Bezier curve fits
    # Array Q is the set of data points to which we want to fit
    # a piecewise G1 continuous cubic Bezier curve
    # (Replace Q with your data.  You will need to adjust n = number of knots)

    demo = 1
    k = None

    if demo == 1:
        # C = np.array([[-1.72, -0.6],
        #               [0.07, -1.41],
        #               [0.41, -0.58],
        #               [0.54, 0.57],
        #               [1.45, 0.3],
        #               [1.15, -0.49]])
        # Generate a cubic Bézier polyline data with these control points

        # # C = np.array([[-1.72690252, -0.60320651],
        #                 [-0.70522179, -0.67762933],
        #                 [ 0.01382281, -1.97537992],
        #                 [ 0.43495913, -1.26875526],
        #                 [ 0.42636188, -1.28318058],
        #                 [ 0.51036741, -0.06590962],
        #                 [ 0.39913502,  0.45092671]])
        # # Q = cubicBezierToPolyline(C, 65)

        # To test with more points

        Q = np.array([[-1.72690252, -0.60320651],
                [-1.24897493, -0.62118553],
                [-0.95691139, -0.82453109],
                [-0.54693039, -1.2073633],
                [-0.29682866, -1.37491497],
                [-0.07528416, -1.41953392],
                [0.04932819, -1.41626638],
                [0.32158605, -1.35978003],
                [0.43495913, -1.26875526],
                [0.46268872, -1.21207157],
                [0.45620099, -0.99347741],
                [0.39856247, -0.78108789],
                [0.46167742, -0.37008614],
                [0.49065901, -0.12820093],
                [0.4293792, 0.10799786],
                [0.36700556, 0.31922918],
                [0.39913502, 0.45092671],
                [0.45062568, 0.51972223],
                [0.60943489, 0.60025459],
                [0.79160628, 0.61508022],
                [1.16497901, 0.66786697],
                [1.31335563, 0.64628676],
                [1.42801164, 0.5450193],
                [1.46717999, 0.39541395],
                [1.41809855, 0.15004509],
                [1.39170192, -0.23027283],
                [1.28265079, -0.42013758],
                [1.20794485, -0.45379492],
                [1.19367788, -0.45363579],
                [1.22633365, -0.52443446],
                [1.00658826, -0.37020543],
                [0.82064844,-0.10291448],
                [0.41806804, 0.16256904],
                [0.18311442, 0.37252653],
                [-0.02908209, 0.49855851],
                [-0.16199967, 0.52701975]])
        
        # Q = np.array([[-1.72690252, -0.60320651],
        #               [-1.24897493, -0.62118553],
        #               [-0.95691139, -0.82453109],
        #               [-0.54693039, -1.2073633],
        #               [-0.29682866, -1.37491497],
        #               [-0.07528416, -1.41953392],
        #               [0.04932819, -1.41626638],
        #               [0.32158605, -1.35978003],
        #               [0.43495913, -1.26875526],
        #               [0.46268872, -1.21207157],
        #               [0.45620099, -0.99347741],
        #               [0.39856247, -0.78108789],
        #               [0.46167742, -0.37008614],
        #               [0.49065901, -0.12820093],
        #               [0.4293792, 0.10799786],
        #               [0.36700556, 0.31922918],
        #               [0.39913502, 0.45092671]])

        # Q = np.array([[ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  0.00000000e+00],
        #               [ 0.00000000e+00,  2.88000000e-02],
        #               [ 0.00000000e+00,  5.76000000e-02],
        #               [ 0.00000000e+00,  8.64000000e-02],
        #               [ 0.00000000e+00,  1.15200000e-01],
        #               [ 0.00000000e+00,  1.44000000e-01],
        #               [ 0.00000000e+00,  1.72800000e-01],
        #               [ 0.00000000e+00,  2.01600000e-01],
        #               [ 0.00000000e+00,  2.59200000e-01],
        #               [ 0.00000000e+00,  3.16800000e-01],
        #               [ 0.00000000e+00,  3.74400000e-01],
        #               [ 0.00000000e+00,  4.32000000e-01],
        #               [ 0.00000000e+00,  4.89600000e-01],
        #               [ 0.00000000e+00,  5.47200000e-01],
        #               [ 0.00000000e+00,  6.04800000e-01],
        #               [ 0.00000000e+00,  6.62400000e-01],
        #               [ 0.00000000e+00,  7.20000000e-01],
        #               [ 0.00000000e+00,  7.77600000e-01],
        #               [ 0.00000000e+00,  8.35200000e-01],
        #               [ 0.00000000e+00,  8.92800000e-01],
        #               [ 0.00000000e+00,  9.50112240e-01],
        #               [-2.74639432e-04,  1.00742382e+00],
        #               [-8.23911989e-04,  1.06473343e+00],
        #               [-1.64780506e-03,  1.12203975e+00],
        #               [-2.74629972e-03,  1.17934146e+00],
        #               [-4.11937075e-03,  1.23663725e+00],
        #               [-5.74225164e-03,  1.29306575e+00],
        #               [-7.90316000e-03,  1.34947621e+00],
        #               [-1.06018993e-02,  1.40586350e+00],
        #               [-1.38382242e-02,  1.46222249e+00],
        #               [-1.76118403e-02,  1.51854806e+00],
        #               [-2.19224045e-02,  1.57483508e+00],
        #               [-2.67695249e-02,  1.63107844e+00],
        #               [-3.21527605e-02,  1.68727301e+00],
        #               [-3.80716219e-02,  1.74341370e+00],
        #               [-4.45255708e-02,  1.79949539e+00],
        #               [-5.15140204e-02,  1.85551299e+00],
        #               [-5.90363351e-02,  1.91146140e+00],
        #               [-6.68885659e-02,  1.96592566e+00],
        #               [-7.55125548e-02,  2.02027305e+00],
        #               [-8.49065663e-02,  2.07449265e+00],
        #               [-9.50687104e-02,  2.12857355e+00],
        #               [-1.05996942e-01,  2.18250487e+00],
        #               [-1.17269574e-01,  2.23434655e+00],
        #               [-1.29509209e-01,  2.28596849e+00]])
        n = 10 # Starting number of kno,t points
    elif demo == 2:
        # Or, try a Lissajous figure:,
        theta = np.arange(0, 2*np.pi, 0.05)
        x = np.sin(2*theta)
        y = np.cos(theta)
        Q = np.column_stack((x, y))
        n = 3  # Starting number of knot points
    elif demo == 3:
        # Or two cycles of a sine wave
        theta = np.arange(0, 4*np.pi, 0.05)
        x = theta
        y = np.cos(theta)
        Q = np.column_stack((x, y))
        n = 5  # Starting number of knot points

    # Now try to do a piecewise cubic Bézier fit to Q starting with n knot points
    # This computes the globally optimized only (GOO) curve.
    # (The plotting of the IG curve in iguess0.m can be commented out.)
    Qt = Q.T
    IG, k, dpkpc = iguess0(Qt, n, k)
    # Improve the fit: Segmentally Optimum Only Curve (SOO)
    SOC = segop(k, Qt, IG)
    print("SOC: ", SOC)

    # Improve it again: Segmentally then Globally Optimized Curve (SGO)
    GOC = globop(SOC, Qt, 0, k, dpkpc)

    # plot SGO curve using internal routine
    plt.figure()
    poplt(GOC, Qt)
    plt.title('Plot of SGO curve')
    # print("Q globop: ", Q.shape)

    # This section of code simply repeats the plot above (poplt) in a
    # manner that makes it easier to see the piecewise cubic Bézier sections

    # Get the Bézier control points of the curve fit
    Cnew = cpoints(GOC).T
    print("Novos pontos de controle: ", Cnew)
    P = knots(Qt, k)
    print("Novos knots: ", P)

    # Plot fitted, segment by segment using Geom2D toolkit
    plt.figure()
    for i in range(0, len(Cnew)-2, 3):
        drawBezierCurve(Cnew[i:i+4])   # Fitted cubic Bézier segment
    hc = plt.plot(Cnew[:,0], Cnew[:,1], 'o-', label='New control points')
    ho = plt.plot(Q[:,0], Q[:,1], 'k.', label='Original data')
    hn = plt.plot(P[:,0], P[:,1], 'kx', markersize=10, label='Original knot points')
    plt.legend([ho[0], hn[0], hc[0]], ['Original data',
                                        f'Original guess n = {n} knots',
                                        'New control points'])
    plt.gca().set_aspect('equal')
    plt.gca().set_facecolor('white')
    plt.show()

if __name__ == '__main__':
    BezierFitDemo()