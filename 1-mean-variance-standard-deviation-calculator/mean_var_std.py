import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    npArr =  np.array(list)
    newArr = npArr.reshape(3,3)

    calculations = {}
    calculations["mean"] = [newArr.mean(axis=0).tolist() ,newArr.mean(axis=1).tolist(),newArr.mean()]
    calculations["variance"] = [newArr.var(axis=0).tolist() ,newArr.var(axis=1).tolist(),newArr.var()]
    calculations["standard deviation"] = [newArr.std(axis=0).tolist() ,newArr.std(axis=1).tolist(),newArr.std()]
    calculations["max"] = [newArr.max(axis=0).tolist() ,newArr.max(axis=1).tolist(),newArr.max()]
    calculations["min"] = [newArr.min(axis=0).tolist() ,newArr.min(axis=1).tolist(),newArr.min()]
    calculations["sum"] = [newArr.sum(axis=0).tolist() ,newArr.sum(axis=1).tolist(),newArr.sum()]

    return calculations
