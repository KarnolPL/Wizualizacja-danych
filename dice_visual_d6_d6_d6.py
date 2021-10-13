from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Tworzymy 3 kosci do gry
die_1 = Die()
die_2 = Die()
die_3 = Die()

#Wykonanie zadanej ilosci rzutów kośćmi
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#Analiza wyników
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Wizualizacja wyników
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwosc wystepownia wartosci'}
my_layout = Layout(title='Wynik rzucania trzema kośćmi D6 1000 razy',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3_d6.html')