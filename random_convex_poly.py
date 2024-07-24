'''
   Generates a random convex polyhedron within the unit cube
   Nic Bwts
'''


import numpy as np
from numpy import random
from scipy.spatial import ConvexHull
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3

aspect = 0
n_vert = 20
aspect_ratio = 0.3

while aspect == 0:

    # Generate random points & convex hull
    points = np.random.rand(n_vert, 3)
    hull = ConvexHull(points)

    # Check aspect ratios of surface facets
    aspect_ratio_lst = []
    for simplex in hull.simplices:
        
        a = euclidean(points[simplex[0], :], points[simplex[1], :])
        b = euclidean(points[simplex[1], :], points[simplex[2], :])
        c = euclidean(points[simplex[2], :], points[simplex[0], :])
        
        circ_rad = (a*b*c)/(np.sqrt((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c)))
        in_rad   = 0.5*np.sqrt(((b+c-a)*(c+a-b)*(a+b-c))/(a+b+c))
        aspect_ratio_lst.append(in_rad/circ_rad)

    # Threshold for minium allowable aspect raio of surface facets
    if np.amin(aspect_ratio_lst) > aspect_ratio:
        aspect = 1
    

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
facet_col = random.rand(3) # [0.0, 1.0, 0.0] 

# Plot hull's vertices - uncomment to plot vertices
# for vert in hull.vertices:    
#     ax.scatter(points[vert,0], points[vert,1], zs=points[vert,2])

# Plot surface traingulation
for simplex in hull.simplices:
    vtx = [points[simplex[0],:], points[simplex[1],:], points[simplex[2],:]]
    tri = a3.art3d.Poly3DCollection([vtx], linewidths = 2, alpha = 0.8)
    tri.set_color(facet_col)
    tri.set_edgecolor('k')
    ax.add_collection3d(tri)

plt.axis('off')
plt.show()

