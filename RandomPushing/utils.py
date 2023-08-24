from copy import copy
import numpy as np
from numpy.random import default_rng
import scipy.optimize
import functools
import matplotlib.pyplot as plt

rng = default_rng()


#RANSAC implementationa
class RANSAC:
    def __init__(self, n=8, k=100, t=0.03, d=10, model=None, loss=None, metric=None):
        self.n = n              # `n`: Minimum number of data points to estimate parameters
        self.k = k              # `k`: Maximum iterations allowed
        self.t = t              # `t`: Threshold value to determine if points are fit well
        self.d = d              # `d`: Number of close data points required to assert model fits well
        self.model = model      # `model`: class implementing `fit` and `predict`
        self.loss = loss        # `loss`: function of `y_true` and `y_pred` that returns a vector
        self.metric = metric    # `metric`: function of `y_true` and `y_pred` and returns a float
        self.best_fit = None
        self.best_error = np.inf

    def fit(self, x, y, z):
        for _ in range(self.k):
            ids = rng.permutation(x.shape[0])

            maybe_inliers = ids[: self.n]
            maybe_model = copy(self.model).fit(list(zip(x[maybe_inliers], y[maybe_inliers], z[maybe_inliers])))

            thresholded = (
                self.loss(z[ids][self.n :], maybe_model.predict(x[ids][self.n :], y[ids][self.n :]))
                < self.t
            )

            inlier_ids = ids[self.n :][np.flatnonzero(thresholded).flatten()]

            if inlier_ids.size > self.d:
                inlier_points = np.hstack([maybe_inliers, inlier_ids])
                better_model = copy(self.model).fit(list(zip(x[inlier_points], y[inlier_points], z[inlier_points])))

                this_error = self.metric(
                    z[inlier_points], better_model.predict(x[inlier_points], y[inlier_points])
                )

                if this_error < self.best_error:
                    self.best_error = this_error
                    self.best_fit = maybe_model

        return self

    def predict(self, x, y):
        return self.best_fit.predict(x,y)

def square_error_loss(z_true, z_pred):
    return (z_true - z_pred) ** 2


def mean_square_error(z_true, z_pred):
    return np.sum(square_error_loss(z_true, z_pred)) / z_true.shape[0]


class PlanarRegressor:
    def __init__(self):
        self.stored_params = [0, 0, 0]

    def error(self, params, points):
        result = 0
        for (x,y,z) in points:
            plane_z = self.plane(x, y, params)
            diff = abs(plane_z - z)
            result += diff**2
        return result

    def fit(self, points):
        fun = functools.partial(self.error, points=points)
        res = scipy.optimize.minimize(fun, self.stored_params)

        self.stored_params = res.x
        return self

    def plane(self, x, y, params):
        a = params[0]
        b = params[1]
        c = params[2]
        return a*x + b*y + c
    
    def predict(self, xx, yy):
        a = self.stored_params[0]
        b = self.stored_params[1]
        c = self.stored_params[2]
        zz = []
        for i, _ in enumerate(xx):
            z = a*xx[i] + b*yy[i] + c
            zz.append(z)
        return np.array(zz) 



if __name__ == "__main__":
    regressor = RANSAC(model=PlanarRegressor(), loss=square_error_loss, metric=mean_square_error)

    grid_res = 16
    x, y, z = [], [], []
    for i in range(grid_res):
        for j in range(grid_res):
            x.append(1-i*2/grid_res)
            y.append(1-j*2/grid_res)
            z.append(x[i]+y[i])

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    for i, _ in enumerate(z):
        x[i] += .08*(np.random.random()-0.5)
        y[i] += .08*(np.random.random()-0.5)
        if(np.random.random()<.25):
            z[i] += (np.random.random()-0.5)

        z[i] += .02*(np.random.random()-0.5)

    regressor.fit(x, y, z)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z)


    xx, yy = np.meshgrid([-1,1], [-1,1])
    z = regressor.predict(xx, yy)
    ax.plot_surface(xx, yy, z, alpha=0.2, color=[0,1,1])
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal')
    plt.show()