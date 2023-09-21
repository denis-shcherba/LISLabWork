import matplotlib.pyplot as plt

def viewPointCloud(points):
    x = [v[0] for v in points]
    y = [v[1] for v in points]
    z = [v[2] for v in points]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='b', marker='o')
    
    plt.show()