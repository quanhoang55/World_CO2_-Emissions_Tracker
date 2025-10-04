from data_loader import *
import numpy as np

# ---------------------------------------------------------------
#Statistical Analysis
mean_of_co2 = df['CO2(Ton)'].mean()
median_of_co2 = df['CO2(Ton)'].median()
std_of_co2 = df['CO2(Ton)'].std()
var_of_co2 = df['CO2(Ton)'].var()

#Mean / Median / Std / Var
print(f'Mean CO2:______{mean_of_co2} (Ton)')
print(f'Median CO2:____{median_of_co2} (Ton)')
print(f'Std CO2:_______{std_of_co2} (Ton)')
print(f'Var CO2:_______{var_of_co2} (Ton)')