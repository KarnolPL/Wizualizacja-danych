import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Tworzenie nowego błędzenia losowego, dopóki program pozostaje aktywny
while True:
    #Przygotowanie danych bładzenia losowego
    rw = RandomWalk(100_000)
    rw.fill_walk()

    #Wyświetlenie punktów bładzenia losowego
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.inferno, edgecolor='none', s=15)
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    #Ukrycie osi.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Utworzyć kolejne bładzenie losowe? (t/n): ")
    if keep_running == 'n':
        break