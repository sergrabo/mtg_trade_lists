''' Class to perform all necessary operations to join the lists'''

import pandas as pd

class Joiner:

    def __init__(self,
                 sharelist_df: pd.DataFrame,
                 wishlist_df: pd.DataFrame) -> None:
        self.sharelist_df = sharelist_df
        self.wishlist_df = wishlist_df
        # Clean the quantities
        del self.sharelist_df['quantity']
        del self.wishlist_df['quantity']

    def mix_lists(self, method: str) -> pd.DataFrame:

        # Check if method is correct
        if method not in ('inner', 'outer'):
            raise ValueError('method must be either inner or outer')
        
        # Join both lists and return the resulting dataframe
        df_out = self.sharelist_df.merge(self.wishlist_df, on = 'name', how=method)
        return df_out
    
if __name__ == '__main__':
    from reader import Reader
    # Read the dataframes
    reader = Reader()
    sharelist_df = reader.read_dataframe('/home/sergio/Workspace/list_checker_mtg/data/sharelists/Lista_Dobbie.txt')
    wishlist_df = reader.read_dataframe('/home/sergio/Workspace/list_checker_mtg/data/wishlists/wants.txt')
    joiner = Joiner(sharelist_df, wishlist_df)
    df = joiner.mix_lists('inner')
    print(df)
