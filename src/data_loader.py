import pandas as pd
#---------------------------------------------------------------
#csv file path
csv_path = '../Data/co2_emission.csv'
#---------------------------------------------------------------
#loading the csv file from Data/co2_emission.csv
print('Loading data...')
print('---'*5)
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f'Data not found: {csv_path}')
#---------------------------------------------------------------
#rename the 'Entity' columns to 'Countries', 'Annual CO₂ emissions (tonnes )' to 'CO2(Ton)'
new_entity_columns = {'Entity': 'Countries', 'Annual CO₂ emissions (tonnes )': 'CO2(Ton)'}
df = df.rename(columns=new_entity_columns)


#---------------------------------------------------------------
#check Year: lower and upper
class year_checker:
    """
    input: year, df
    output: pandas dataframe
    """
    def __init__(self, my_df):
        self.df = my_df
    # ---------------------------------------------------------------
    def lower(self, year):
        lower_year = self.df.loc[self.df['Year'] <= year]
        if lower_year.empty:
            return 'Year Not Found'
        else:
            return lower_year
    # ---------------------------------------------------------------
    def upper(self, year):
        upper_year = self.df.loc[self.df['Year'] >= year]
        if upper_year.empty:
            return 'Year Not Found'
        else:
            return upper_year
    # ---------------------------------------------------------------
    def lowest(self):
        lowest_year = self.df['Year'].min()
        if lowest_year:
            return lowest_year
        else:
            return 'Year Not Found'
    # ---------------------------------------------------------------
    def highest(self):
        highest_year = self.df['Year'].max()
        if highest_year:
            return highest_year
        else:
            return 'Year Not Found'
    # ---------------------------------------------------------------
