import sys
import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = sys.argv[1]

print "Analyzing", filename

# read the data #
data = pd.read_csv(filename)
data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])

print "Running analyze"
parameters = mosquito_lib.analyze(data, filename.replace("csv", "png"))

print "Saving parameters"
# save parameters to file #
parameters.to_csv(filename.replace("data", "parameters"))