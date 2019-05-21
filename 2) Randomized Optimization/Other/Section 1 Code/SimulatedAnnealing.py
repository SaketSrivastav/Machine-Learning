import mlrose
import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score


data = np.genfromtxt('AdultData.csv', skip_header=True, delimiter=",")
dataValues = data[:, :14]
dataLabels = data[:, 14] #labels

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(dataValues, dataLabels, test_size = 0.3, random_state = 3)
                                    

# Normalize feature data
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

def custom(t, c): 
    t = 0.2
    c = 0.0
    return t + c
kwargs = {'c': .05}
                                                   
# Initialize neural network object and fit object
np.random.seed(3)

start_time = time.time()
nn_model1 = mlrose.NeuralNetwork(hidden_nodes = [4], activation = 'relu',
                                 algorithm = 'simulated_annealing', max_iters = 100, schedule = mlrose.CustomSchedule(custom, **kwargs), 
                                 bias = True, is_classifier = True, learning_rate = 0.1,
                                 early_stopping = True, clip_max = 5, max_attempts = 100)
                                 



nn_model1.fit(X_train_scaled, y_train)


########Print weights########
weights = nn_model1.fitted_weights
#print(weights)

########Predict labels for train set and assess accuracy########
y_train_pred = nn_model1.predict(X_train_scaled)
y_train_accuracy = accuracy_score(y_train, y_train_pred)
print('Training accuracy: ', y_train_accuracy)
print("--- %s training seconds ---" % (time.time() - start_time))

start_time2 = time.time()
########Predict labels for test set and assess accuracy########
y_test_pred = nn_model1.predict(X_test_scaled)
y_test_accuracy = accuracy_score(y_test, y_test_pred)
print('Test accuracy: ', y_test_accuracy)
print("--- %s testing seconds ---" % (time.time() - start_time2))