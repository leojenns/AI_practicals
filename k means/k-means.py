import random as r
import numpy as np






class Kmeans:
    '''
    class kmeans  for implementation of kmeans algorithm
    '''
    def __init__(self, k):
        '''
        def init for initalitation of kmeans algorithm

        :param k: int the amount of clusters desired
        '''
        self.k = k
        self.points = []
        self.data = []
        self.clusters = [[] for _ in range(self.k)]
    def set_k(self, k):
        '''
        def set_k setter for self.k

        :param k: int new k
        '''
        self.k = k
        self.clusters = [[] for _ in range(k)]

    def set_data(self, data):
        '''
        def set_data setter for self.data

        :param data: new data

        '''
        self.data = list(data)
    def load_csv(self, filename , delimiter=';', usecols=[1, 2, 3, 4, 5, 6, 7]
                 , converters={5: lambda s: 0 if s == b"-1" else float(s),
                               7: lambda s: 0 if s == b"-1" else float(s)}):
        '''
        def load_csv load function for data from csv file

        :param filename: name of csv file
        :param delimiter: delimiter used in csv file
        :param usecols:  collums needed from csv
        :param converters: when needed converters for data from csv
        '''
        data = np.genfromtxt(filename, delimiter=delimiter, usecols=usecols,
                             converters=converters)
        self.set_data(list(data))
    def get_data(self):
        '''
        def get_data getter for self.data

        :return: self
        '''
        return self.data
    def get_clusters(self) -> list:
        '''
        def get_clusters getter for self.clusters

        :return: self.clusters
        '''
        return self.clusters

    def cluster(self):
        '''
        def cluster function to start clustering algorithm

        '''
        self.random_points()
        count = 0
        while count != len(self.data):
            count = 0
            old_cluster = self.clusters
            new_cluster = [[] for _ in range(self.k)]

            for data_point in self.data:
                if any((data_point == x).all() for x in old_cluster[self.get_closest(data_point)]):
                    count = count + 1
                    new_cluster[self.get_closest(data_point)].append(data_point)
                else:
                    new_cluster[self.get_closest(data_point)].append(data_point)
            self.clusters = new_cluster
            self.reset_points_median()

        return self.clusters

    def random_points(self):
        '''
        def random_points function to take random points from self.data
        '''
        #self.points = list(map(lambda x : self.data[x], r.sample(range(0,len(self.data)),self.k)))
        self.points = [r.choice(self.data) for _ in range(self.k)]

    def reset_points_median(self):
        '''
        def reset_points_median function to reset the points based on the median of the clusters.
        '''
        for i in range(self.k):
            self.points[i] = np.median(self.clusters[i], axis=0)
    def get_closest(self, input):
        '''
        def get_closest function to search the closest point from self.points

        :param input: point from data
        :return: index of closest point aka closest cluster
        '''
        closest_list = []
        for point in self.points:
            dist = np.linalg.norm(point - input)
            closest_list.append(dist)
        return closest_list.index(min(closest_list))

    def val(self,filename):
        '''
        def val function for validation
        :param filename: name of file with validation data
        :return: print the validation
        '''
        dates = np.genfromtxt(filename, delimiter=';', usecols=[0])
        labels = []
        for label in dates:
            if label < 20000301:
                labels.append('winter')
            elif 20000301 <= label < 20000601:
                labels.append('lente')
            elif 20000601 <= label < 20000901:
                labels.append('zomer')
            elif 20000901 <= label < 20001201:
                labels.append('herfst')
            else:  # from 01-12 to end of year
                labels.append('winter')
        count = [[] for i in range(self.k)]
        a = 0
        for cluster in self.clusters:
            for point in cluster:
                for c in range(len(labels)):
                    if list(self.data[c]) == list(point):
                        count[a].append(labels[c])
            print(count[a])
            count[a] = max(set(count[a]), key=count[a].count)
            a+= 1
        return count

A = Kmeans(3)
A.load_csv('dataset1.csv')

for x in range(10):
    for i in A.cluster():
        print (len(i))
    print (A.val('dataset1.csv'))
