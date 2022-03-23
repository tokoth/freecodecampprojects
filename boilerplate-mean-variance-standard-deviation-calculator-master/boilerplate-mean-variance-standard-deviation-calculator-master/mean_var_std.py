import numpy as np

def calculate(list):
     if len(list) == 9:
    b = np.array(list)
    b = b.reshape(3,3)
    calculations = {
        'mean' : [(b.mean(axis=0)), (b.mean(axis=1)),(b.flatten().mean())],
        'variance' : [(b.var(axis=0)),(b.var(axis=1)),(b.flatten().var())],
        'standard deviation' : [(b.std(axis=0)),(b.std(axis=1)),(b.flatten().std())],
        'max' : [(b.max(axis=0)),(b.max(axis=1)),(b.flatten().max())],
        'min' : [(b.min(axis=0)),(b.min(axis=1)),(b.flatten().min())],
        'sum' : [(b.sum(axis=0)),(b.sum(axis=1)),(b.flatten().sum())]       
                            }
    else:
        raise ValueError("List must contain nine numbers.")
    return calculations