import pandas as pd

# series example
city_names = pd.Series(['San Fransisco', 'San Jose', 'Sacramento'])
city_population = pd.Series([131, 43425, 5353])

# dataframe example
cities = pd.DataFrame({'city name': city_names, 'population': city_population})
print(cities)

cities['area square miles'] = pd.Series([131, 1414, 333])
cities['population density'] = cities['population']/cities['area square miles']

print(cities)

cities['is wide and has saint name'] = (cities['area square miles'] > 300) & (cities['city name'].apply(lambda name: name.startswith('San')))

print(cities)
