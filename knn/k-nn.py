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
        if set_data:
            self.data = data
            self.labels = labels
            return
        return data, labels


    def get_data(self):
        return self.data

    def change_k(self,k):
        self.k = k

    def get_k(self):
        return self.k

    def most_common(self, lst):
        return max(set(lst), key=lst.count)

    def nearest(self, input):
        distance_from_input = [np.linalg.norm(data_point-input) for data_point in self.data]
        distance_array = np.array(distance_from_input).argsort()[:self.k]
        labels_from_data = list(map(lambda x : self.labels[x], distance_array))
        return self.most_common(labels_from_data)

    def calulate_best_k(self, filename_validation_set, set_k=0):
        v_data, v_labels = self.load_csv_data(filename_validation_set, 0)
        amount_correct = []
        for k in range(1, len(self.data)):
            print(k)
            self.change_k(k)
            count = 0
            for v_data_point, v_label in zip(v_data, v_labels):
                if self.nearest(v_data_point) == v_label:
                    count = count +1
            amount_correct.append(count)
        if set_k:
            self.change_k(amount_correct.index(max(amount_correct)))

        return  " best k = " , amount_correct.index(max(amount_correct)),  "amount correct" ,max(amount_correct)


#make object
B = knn(6)
#load the data
B.load_csv_data('dataset1.csv')
#calculate of first []
print(B.nearest(B.get_data()[0]))
#calculate of best k
print(B.calulate_best_k('validation1.csv'))
