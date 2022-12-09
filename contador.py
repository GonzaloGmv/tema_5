from collections import Counter

animales = "gato perro canario perro canario perro"
c = Counter(animales.split())
print(c)