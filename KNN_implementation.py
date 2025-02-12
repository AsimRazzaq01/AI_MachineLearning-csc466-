import math
from collections import Counter

class KNN : 
    # Initialization
    def __init__(self,k=3):
        self.k = k 
        self.training_data = []
        self.testing_label = []
    
    
    def fit(self,x,y):
        # method to store/hold values for training data/labels
        self.training_data = x
        self.training_label = y
    
    
    def ecludian_distance(self, point1, point2):
        # function to calculate distance between two points
        distance = 0
        for i in range(len(point1)):
            distance += (point1[i] - point2[i]) **2
        return math.sqrt(distance)
    
    
    def predict(self, x_test):
        # predicts the class for each sample in x_test
        predictions = []
        for test_point in x_test:
            distances = []
            # compute distance from test point to -> all training points
            for i, train_point in enumerate(self.training_data):
                dist = self.ecludian_distance(test_point, train_point)
                distances.append((dist,self.training_label[i]))
            # sort by distance sml -> lrg and get K nearest neighbors 
            distances.sort(key = lambda x:x[0])
            knn = distances[:self.k]
            # get the most common label (Majority)
            labels = [label for _, label in knn]
            most_common_label = Counter(labels).most_common(1)[0][0]
            
            predictions.append(most_common_label)
        return predictions


if __name__ == "__main__":    
    x_train = []
    y_train = []
    
    Iris = "/Users/asim/Desktop/Spring2025/AI_MachineLearning(csc466)/IRIS.csv"
    
    with open(Iris, "r") as file:
        for line in file:
            values = line.strip().split(",")  # strip a line and make list using = ","
            try:
            # Convert all except the last column to floats (numerical features)
                numbers = [float(v) for v in values[:-1]]  
                x_train.append(numbers) # Convert to float and store in X_train
                # The last column is for labels
                y_train.append(values[-1].strip('"'))  # Remove quotes if present & store in y_train
            except ValueError:
                pass  # Ignore errors 
    # print(x_train,y_train)    //test to see if parseing works
    
    #         "Setosa"          "Versicolor"      "Virginica"   should be correct answers
    x_test = [[5.1,3.3,1.7,.5], [6.9,3.1,4.9,1.5], [7.2,3.2,6,1.8]]
    
    knn = KNN(k=3)  # instantiate KNN with k=3
    knn.fit(x_train, y_train)  # train model
    predictions = knn.predict(x_test)
    print("Prediction: ", predictions)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#/ Original Class implimentation
# class KNN : 
#     # Initialization
#     def __init__(self,k=3):
#         self.k = k 
#         self.training_data = []
#         self.testing_label = []
        
#     def fit(self,x,y):
#         # method to store training data/labels
#         self.training_data = x
#         self.training_label = y
        
#     def ecludian_distance(self, point1, point2):
#         # function to calculate distance between two points
#         distance = 0
#         for i in range(len(point1)):
#             distance += (point1[i] - point2[i]) **2
#         return math.sqrt(distance)
#    
#     def predict(self, x_test):
#         # predicts the class for each sample in x_test
#         predictions = []
#         for test_point in x_test:
#             distances = []
#             # compute distance from test point to -> all training points
#             for i, train_point in enumerate(self.training_data):
#                 dist = self.ecludian_distance(test_point, train_point)
#                 distances.append((dist,self.training_label[i]))
#             # sort by distance sml -> lrg and get K nearest neighbors 
#             distances.sort(key= lambda x:x[0])
#             knn = distances[:self.k]
#             # get the most common label (Majority)
#             labels = [label for _, label in knn]
#             most_common_label = Counter(labels).most_common(1)[0][0]
            
#             predictions.append(most_common_label)
#         return predictions
    

# if __name__ == "__main__":
#     # example data set
#     x_train = [[2,4],[4,6],[4,2],[6,4],[6,6],[8,8]]
#     y_train = ['A','A','B','B','A','B']
    
#     x_test = [[5,5],[7,7],[3,3]]
    
#     knn = KNN(k=3)  # instantiate KNN with k=3
#     knn.fit(x_train, y_train)  # train model
#     #predictions = knn.predict([[3,9]])   #predict
#     #print("Prediction [[3,9]]", predictions)
#     predictions = knn.predict(x_test)
#     print("Prediction: ", predictions)
#     #predictions = knn.predict(x_test)
#     #print(x_test,predictions)
    








    # def ecludian_distance_4point(self, point1, point2, point3, point4):
    #     # function to calculate distance between two points
    #     distanceSepal = 0
    #     distancePetal = 0
    #     for i in range(len(point1)):
    #         distanceSepal += (point1[i] - point2[i]) **2
    #         distancePetal += (point3[i] - point4[i]) **2
    #     return math.sqrt(distanceSepal , distancePetal)