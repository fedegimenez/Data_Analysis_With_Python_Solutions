import numpy as np

def calculate(numbers):
    #Checking if 'numbers' only has 9 numbers
    if len(numbers) != 9: 
        raise ValueError("List must contain nine numbers.")
    
    #Reshaping the numbers into a 3x3 matrix
    data = np.reshape(np.array(numbers), (3,3))

    #Creating Dictionary for the return
    calculations = {}

    # Calculate mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
    calculations['mean'] = [list(np.mean(data, axis=0)), list(np.mean(data, axis=1)), np.mean(data)]
    calculations["variance"] = [list(np.var(data, axis=0)), list(np.var(data, axis=1)), np.var(data)]
    calculations["standard deviation"] = [list(np.std(data, axis=0)), list(np.std(data, axis=1)), np.std(data)]
    calculations["max"] = [list(np.max(data, axis=0)), list(np.max(data, axis=1)), np.max(data)]
    calculations["min"] = [list(np.min(data, axis=0)), list(np.min(data, axis=1)), np.min(data)]
    calculations["sum"] = [list(np.sum(data, axis=0)), list(np.sum(data, axis=1)), np.sum(data)]

    return calculations