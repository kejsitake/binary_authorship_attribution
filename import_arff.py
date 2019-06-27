#matplotlib inline


from scipy.io import arff
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline


data = arff.loadarff('../BinaryStylometry/arffs/final_IG.arff')
df = pd.DataFrame(data[0])
print (df.columns.values)
print (df.shape)
df.head()

np.random.seed(200)
k = 10
# centroids[i] = [x, y]
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}
    

fig = plt.figure(figsize=(5, 5))
plt.show()
'''plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()'''
