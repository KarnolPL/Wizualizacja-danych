import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlOrBr, s=10)

#Zdefiniowanie tytułu wykresu i etykiety osi
ax.set_title('Kwadrat liczb', fontsize=24)
ax.set_xlabel('Wartość', fontsize=24)
ax.set_ylabel('Kwadraty wartosci', fontsize=24)

#Zdefiniowanie wielkosci etykit.
ax.tick_params(axis='both', which='major', labelsize=14)

#Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.show()

#aby zapisac nalezy zamienic plt.show na
#plt.savefig('nazwa pliku', 'bbox_inches='tight') drugi argument usuwa biale znaki