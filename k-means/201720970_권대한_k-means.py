import numpy as np
from scipy.spatial.distance import cdist 
import matplotlib.pyplot as plt

# k-means 함수 선언
def kmeans(mat, k, iteration):
    idx = np.random.choice(len(mat), k, replace=False)

    # 함수 실행 시 랜덤으로 무게 중심을 선택한다.
    centroids = mat[idx, :] 
     
    # 모든 데이터와 중점과의 거리를 구한다.
    #distnaces = np.linalg.norm(x - centroids)
    distances = cdist(mat, centroids ,'euclidean')
     
    # 최소 거리를 가지는 중점을 표시해둔다.
    points = np.array([np.argmin(i) for i in distances]) #Step 3
     
    # 반복 횟수 만큼 중점을 구하는 코드
    for _ in range(iteration): 
        centroids = []
        for idx in range(k):
            #Updating Centroids by taking mean of Cluster it belongs to
            temp_cent = mat[points==idx].mean(axis=0) 
            # 선택된 중점을 합친다.
            centroids.append(temp_cent)
        
        centroids = np.vstack(centroids)
        #distnaces = np.linalg.norm(x - centroids)
        distances = cdist(mat, centroids ,'euclidean')
        points = np.array([np.argmin(i) for i in distances])
    return points 
 
# 정규분포를 따지는 1부터 1000까지의 랜덤 변수 선언
data = np.random.uniform(low=1.0, high=1000.0, size=(100, 3))
 
label = kmeans(data, 3, 10)
u_labels = np.unique(label)

for i in u_labels:
    plt.scatter(data[label == i , 0] , data[label == i , 1] , label = i)
plt.legend()
plt.show()