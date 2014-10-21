import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def fahr_to_celsius(temperature_fahr):
    """Convert Fahrenheit to Celsius"""
    temperature_celsius = (temperature_fahr - 32) * 5 / 9.0
    return temperature_celsius
    
def analyze(data, figure_filename):
    
    """perform analysis on mosquito data
    Takes a DataFrame with columns "temperature", "rainfall" and "mosquitos" as input.
    "temperature" should be in Celsius
    figure_filename is the name of the output plot"""
    
    assert data["temperature"].max() < 70, "Check that the input temperature is in Celsius"
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.savefig(figure_filename)
    return parameters
    