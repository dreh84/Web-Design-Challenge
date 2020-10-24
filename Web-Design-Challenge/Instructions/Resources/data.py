import pandas as pd

cities = pd.read_csv('./cities.csv')

html = cities.to_html('cities.html')