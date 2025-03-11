print("Tugas Sistem Operasi")
print("Kalkulator Sederhana")

a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))

opsi = input("masukan opsi: (+/-): ")

print("Tugas Sistem Operasi")
print("Kalkulator Sederhana")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

opsi = input("Masukkan opsi (+/-): ")

if opsi == "+":
    hasil = a + b
    print("Hasil:", hasil)
elif opsi == "-":
    hasil = a - b
    print("Hasil:", hasil)
else:
    print("Opsi tidak valid!")
