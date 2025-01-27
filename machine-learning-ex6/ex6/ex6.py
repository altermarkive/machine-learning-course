#!/usr/bin/env python3

import numpy as np
import scipy.io
import matplotlib
# Force matplotlib to not use any X Windows backend (must be called befor importing pyplot)
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from plotData import plotData
from linearKernel import linearKernel
from svmTrain import svmTrain
from visualizeBoundaryLinear import visualizeBoundaryLinear
from gaussianKernel import gaussianKernel
from visualizeBoundary import visualizeBoundary
from dataset3Params import dataset3Params


def ex6():
    # Machine Learning Online Class
    #  Exercise 6 | Support Vector Machines
    #
    #  Instructions
    #  ------------
    # 
    #  This file contains code that helps you get started on the
    #  exercise. You will need to complete the following functions:
    #
    #     gaussianKernel.m
    #     dataset3Params.m
    #     processEmail.m
    #     emailFeatures.m
    #
    #  For this exercise, you will not need to change any code in this file,
    #  or any other files other than those mentioned above.
    #

    # Initialization
    #clear ; close all; clc

    # =============== Part 1: Loading and Visualizing Data ================
    #  We start the exercise by first loading and visualizing the dataset. 
    #  The following code will load the dataset into your environment and plot
    #  the data.
    #

    print('Loading and Visualizing Data ...')

    # Load from ex6data1: 
    # You will have X, y in your environment
    mat = scipy.io.loadmat('ex6data1.mat')
    X = mat['X'].astype(float)
    y = mat['y'][:, 0]

    # Plot training data
    plotData(X, y)
    plt.savefig('figure1.png')

    print('Program paused. Press enter to continue.')
    #pause;

    # ==================== Part 2: Training Linear SVM ====================
    #  The following code will train a linear SVM on the dataset and plot the
    #  decision boundary learned.
    #

    # Load from ex6data1: 
    # You will have X, y in your environment
    mat = scipy.io.loadmat('ex6data1.mat')
    X = mat['X'].astype(float)
    y = mat['y'][:, 0]

    print('\nTraining Linear SVM ...')

    # You should try to change the C value below and see how the decision
    # boundary varies (e.g., try C = 1000)
    C = 1
    model = svmTrain(X, y, C, linearKernel, 1e-3, 20)
    visualizeBoundaryLinear(X, y, model)
    plt.savefig('figure2.png')

    print('Program paused. Press enter to continue.')
    #pause;

    # =============== Part 3: Implementing Gaussian Kernel ===============
    #  You will now implement the Gaussian kernel to use
    #  with the SVM. You should complete the code in gaussianKernel.m
    #
    print('\nEvaluating the Gaussian Kernel ...')

    x1 = np.array([1, 2, 1,])
    x2 = np.array([0, 4, -1])
    sigma = 2
    sim = gaussianKernel(x1, x2, sigma)

    print('Gaussian Kernel between x1 = [1; 2; 1], x2 = [0; 4; -1], sigma = 0.5 :\n\t%f\n(this value should be about 0.324652)' % sim)

    print('Program paused. Press enter to continue.')
    #pause;

    # =============== Part 4: Visualizing Dataset 2 ================
    #  The following code will load the next dataset into your environment and 
    #  plot the data. 
    #

    fig = plt.figure()

    print('Loading and Visualizing Data ...')

    # Load from ex6data2: 
    # You will have X, y in your environment
    mat = scipy.io.loadmat('ex6data2.mat')
    X = mat['X'].astype(float)
    y = mat['y'][:, 0]

    # Plot training data
    plotData(X, y)
    plt.savefig('figure3.png')

    print('Program paused. Press enter to continue.')
    #pause;

    # ========== Part 5: Training SVM with RBF Kernel (Dataset 2) ==========
    #  After you have implemented the kernel, we can now use it to train the 
    #  SVM classifier.
    # 
    print('\nTraining SVM with RBF Kernel (this may take 1 to 2 minutes) ...')

    # Load from ex6data2: 
    # You will have X, y in your environment
    mat = scipy.io.loadmat('ex6data2.mat')
    X = mat['X'].astype(float)
    y = mat['y'][:, 0]

    # SVM Parameters
    C = 1
    sigma = 0.1

    # We set the tolerance and max_passes lower here so that the code will run
    # faster. However, in practice, you will want to run the training to
    # convergence.
    model= svmTrain(X, y, C, gaussianKernel, args=(sigma,))
    visualizeBoundary(X, y, model)
    plt.savefig('figure4.png')

    print('Program paused. Press enter to continue.')
    #pause;

    # =============== Part 6: Visualizing Dataset 3 ================
    #  The following code will load the next dataset into your environment and 
    #  plot the data. 
    #

    fig = plt.figure()

    print('Loading and Visualizing Data ...')

    # Load from ex6data3: 
    # You will have X, y in your environment
    mat = scipy.io.loadmat('ex6data3.mat')
    X = mat['X'].astype(float)
    y = mat['y'][:, 0]

    # Plot training data
    plotData(X, y)
    plt.savefig('figure5.png')

    print('Program paused. Press enter to continue.')
    #pause;

    # ========== Part 7: Training SVM with RBF Kernel (Dataset 3) ==========

    #  This is a different dataset that you can use to experiment with. Try
    #  different values of C and sigma here.
    # 

    # Load from ex6data3: 
    # You will have X, y in your environment
    mat = scipy.io.loadmat('ex6data3.mat')
    X = mat['X'].astype(float)
    y = mat['y'][:, 0]
    Xval = mat['Xval'].astype(float)
    yval = mat['yval'][:, 0]

    # Try different SVM Parameters here
    C, sigma = dataset3Params(X, y, Xval, yval)

    # Train the SVM
    model= svmTrain(X, y, C, gaussianKernel, args=(sigma,))
    visualizeBoundary(X, y, model)
    plt.savefig('figure6.png')

    print('Program paused. Press enter to continue.')
    #pause;

