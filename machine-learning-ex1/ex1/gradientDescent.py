#!/usr/bin/env python3

import numpy as np

from computeCost import computeCost


def gradientDescent(X, y, theta, alpha, num_iters):
    #GRADIENTDESCENT Performs gradient descent to learn theta
    #   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by
    #   taking num_iters gradient steps with learning rate alpha

    # Initialize some useful values
    m = y.shape[0] # number of training examples
    J_history = np.reshape(np.zeros((num_iters, 1)), (num_iters, 1))

    for i in range(num_iters):

        # ====================== YOUR CODE HERE ======================
        # Instructions: Perform a single gradient step on the parameter vector
        #               theta.
        #
        # Hint: While debugging, it can be useful to print out the values
        #       of the cost function (computeCost) and gradient here.
        #

        theta = np.subtract(theta, (alpha / m) * np.dot(np.subtract(np.dot(X, theta), y).T, X).T)

        # ============================================================

        # Save the cost J in every iteration
        J_history[i, 0] = computeCost(X, y, theta)

    return (theta, J_history)
