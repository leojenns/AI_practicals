import numpy as np

class knn:

    def __init__(self, k):
        self.data = []
        self.labels = []
        self.k = k

    def load_csv_data(self,filename,set_data = 1):
        data = np.genfromtxt(filename, delimiter=';', usecols=[1, 2, 3, 4, 5, 6, 7],
                             converters={5: lambda s: 0 if s == b"-1" else float(s),
                                         7: lambda s: 0 if s == b"-1" else float(s)})

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
            elif label < 20010301:
                labels.append('winter')
            elif 20010301 <= label < 20010601:
                labels.append('lente')
            elif 20010601 <= label < 20010901:
                labels.append('zomer')
            elif 20010901 <= label < 20011201:
                labels.append('herfst')
            else:  # from 01-12 to end of year
                labels.append('winter')
        if (set_data):
            self.data = data
            self.labels = labels
            return
        else:
            return data,labels

    def get_data(self):
        return self.data

    def change_k(self,k):
        self.k = k

    def get_k(self):
        return self.k

    def most_common(self, lst):
        return max(set(lst), key=lst.count)

    def nearest(self,input):
        distance_from_input  = list(map(lambda x : np.linalg.norm(x-input),self.data))
        a = np.array(distance_from_input).argsort()[:self.k]
        labels_from_data = list(map(lambda x : self.labels[x], a))
        return self.most_common(labels_from_data)

    def calulate_best_k(self,filename_validation_set,set_k= 0):
        v_data , v_labels = self.load_csv_data(filename_validation_set,0)
        amount_correct = []
        for k in range(1,len(self.data)):
            print(k)
            self.change_k(k)
            count = 0
            for j, k in zip( v_data,v_labels):
                if self.nearest(j) == k:
                    count = count +1
            amount_correct.append(count)
        if (set_k):
            self.change_k(amount_correct.index(max(amount_correct)))

        return amount_correct.index(max(amount_correct)) ,max(amount_correct)


#make object
b= knn(6)
#load the data
b.load_csv_data('dataset1.csv')
#calculate of first []
print(b.nearest(b.get_data()[0]))
#calculate of best k
print(b.calulate_best_k('validation1.csv'))
















