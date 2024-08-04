# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pituus = float(height)
paino = int(weight)
indeksi = (paino/pituus**2)
tasaindeksi = int(indeksi)
print (tasaindeksi)