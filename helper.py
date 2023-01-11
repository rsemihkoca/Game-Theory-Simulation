input_dict = {"5": 1, "2": 6, "9":8,"1": 10,"7": 98,"4": 56}

import numpy as np
import pandas as pd
import seaborn as sns


class calculate():
    """
    # results = calculate(input_dict, verbose=False)    
    # print(results.result)  
  
    """

    def __init__(self, input_dict, verbose=False):
        self.verbose = verbose
        self.input_dict = input_dict

        # create list of values of input_dict and sort them ascending form:

        self.values_sorted = sorted(input_dict.values())
        self.result = []
        self.process()

    def create_opponents(self, xi):
        #create copy of list of values and remove xi
        values_copy = self.values_sorted.copy()
        values_copy.remove(xi)
        #print("values_copy", values_copy)
        opponents = []
        for i in range(len(values_copy)):
            if i == len(values_copy) - 1:
                opponents.append((values_copy[i], values_copy[0]))
            else:
                opponents.append((values_copy[i], values_copy[i + 1]))
        
        return opponents

    def utility_func(self, xi, xj, xk):
        #now calculate utility
        #utility = xi*(100 - xi + xj^2 + xk^2)
        utility_xi = xi*(100 - xi + xj**(2) + xk**(2))

        return utility_xi

    
    def process(self):

        for key, value in self.input_dict.items():
            opponents = self.create_opponents(value)
            total_utility = 0
            #logging
            if self.verbose:
                print("value: ", value)
                print(opponents)
            for k, j in opponents:
                utility = self.utility_func(value, k, j)
                if self.verbose:
                    print(f"value: {value}, k: {k}, j: {j}, utility: {utility}")
                total_utility += utility 

            self.result.append((value, total_utility))
        return self.result

class generate_data():

    def __init__(self):
        pass

    def uniform(self):
        #create 128 random uniform number between 0 and 100,  columns are "players" "scores", set index starting from 1
        self.df = pd.DataFrame({"players": range(1, 129), "S": np.random.uniform(0, 100, 128)}).set_index("players")
        return self.process()

    def normal(self, mean=50, std=10):
        self.df = pd.DataFrame({'players': range(1, 129), 'S': np.clip(np.random.normal(mean, std, 128, ).round().astype(int), 0, 100)}).set_index('players')
        return self.process()
 
    def exponential(self, std=10):
        self.df = pd.DataFrame({'players': range(1, 129), 'S': np.clip(np.random.exponential(std, 128).round().astype(int), 0, 100)}).set_index('players')
        return self.process()

    def poisson(self, mean=50):
        self.df = pd.DataFrame({'players': range(1, 129), 'S': np.clip(np.random.poisson(mean, 128).round().astype(int), 0, 100)}).set_index('players')
        return self.process()

    def lognormal(self, mean=50, std=10):
        self.df = pd.DataFrame({'players': range(1, 129), 'S': np.clip(np.random.lognormal(mean, std, 128).round().astype(int), 0, 100)}).set_index('players')
        return self.process()

    def process(self):
        #now name index as "players"
        self.df.index.name = 'players'
        self.df.sort_values(by=['S'], inplace=True, ascending=False)
        #if there is utility column in the dataframe, drop it
        return self.df
