'''Shafa Stevia Putri 2505976'''

# membuat deret fibonacci dengan menggunakan fungsi
def fibonacci(x):
    a, b = 1, 2
    hasil = []
    for i in range(x):
        hasil.append(a)
        a, b = b, a + b
    return hasil
    
print(fibonacci(5))

# menghitung volume tabung yang dibuat dengan fungsi
# volume tabung = pi*r*r*t
def volumeTabung(a, b, c):
    print(f"Hasilnya adalah {a * b * b * c}")

volumeTabung(22/7, 6, 4)

# Menghitung fungsi nilai total dan nilai rata-ratanya berdasarkan nilai yang diinputkan dari nilai total dimana banyaknya angka tidak dideklarasikan. 
def total_rata():
    data = input("Masukkan angka yang akan diinput (masukkan tanpa koma dan pisahkan dengan spasi): ")

    angka = [float(x) for x in data.split()]  # mengubah string menjadi float

    total = sum(angka)
    rata_rata = total/len(angka)

    print(f"Angka yang telah diinput adalah {angka}")
    print(f"Total semua angka adalah {total}")
    print(f"Rata-rata semua angka adalah {rata_rata}")

total_rata()

print("ini adalah perubahan untuk tugas ltik")
print("ini adalah perubahan kedua untuk tugas ltik")