import math

X =  [[1,2,3],[3,3,4],[4,5,6],[1,2,1],[7,8,9],[3,5,2]]
K = 3
epoch = 10

def get_distance(a,b):
    res = 0
    for i in range(len(a)):
        res += (a[i]-b[i])**2
    return res

def get_mean(group):
    length = len(group)
    dim = len(group[0])
    res = [0 for i in range(dim)]
    for i in range(length):
        for d in range(dim):
            res[d] += group[i][d]

    for d in range(dim):
        res[d] = res[d] / length

    return res


def k_means(X,k):
    centres = {}
    for i in range(k):
        centres[tuple(X[i])] = []
    
    for t in range(epoch):
        for point in X:
            group = None
            curr_distance = math.inf
            for centre in centres.keys():
                d = get_distance(centre,point)
                if(d < curr_distance):
                    curr_distance = d
                    group = centre
            centres[group].append(point)

        new_centres = {}

        for centre in centres.keys():
            mean = get_mean(centres[centre])
            new_centres[tuple(mean)] = []
        
        print(centres)
        centres = new_centres
    return list(centres.keys())


print(k_means(X,K))