''' Class to read the lists and transform them into a pandas dataframe'''

import pandas as pd
import re

class Reader:

    def __init__(self) -> None:
        pass

    def read_dataframe(self, filepath:str) -> pd.DataFrame:
        # Read the contents of the filepath
        with open(filepath, 'r') as f:
            data = f.read()
            # Split the contents into a list
            data = data.split('\n')
            # Remove the first element, supposed to be "Deck"
            if data[0] == 'Deck':
                data.pop(0)
            # Remove the last element, supposed to be empty
            if data[-1] == '':
                data.pop(-1)
        
        # Each element of the list must be separated into a tuple
        # with elements (quantity: int, name: str)
        df_dict = {'quantity': [], 'name': []}

        for element in data:
            # Separate from spaces
            element = element.split(' ')
            # Take the first element as quantity
            quantity = int(element[0])
            # Take the rest as name
            name = ' '.join(element[1:])
            # Add to the dictionary
            df_dict['quantity'].append(quantity)
            df_dict['name'].append(name)

        df = pd.DataFrame(df_dict)
        return df
    
if __name__ == '__main__':
    reader = Reader()
    df = reader.read_dataframe('/home/sergio/Workspace/list_checker_mtg/data/wishlists/wants.txt')
    df = reader.read_dataframe('/home/sergio/Workspace/list_checker_mtg/data/sharelists/Lista_Dobbie.txt')
    print(df)
        