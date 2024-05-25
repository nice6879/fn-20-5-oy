import matplotlib.pyplot as plt

# Grafikdagi nuqtalarning koordinatalari
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = [56,55,55,70,56,65,70,70,58,66,68,55,67,65,55,55]

# Chizma yaratish
plt.plot(x, y, marker='o')

# O'qlar nomlari
plt.xlabel('X')
plt.ylabel('Y')

# Grafik nomi
plt.title('Grafik Chizma')

# Grafikni ko'rsatish
plt.show()
