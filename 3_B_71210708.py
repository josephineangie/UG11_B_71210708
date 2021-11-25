awal = str(input("Masukkan kalimat awal: "))
sisipan = str(input("Masukkan kata untuk disisipkan: "))
index = int(input("Masukkan index: "))

potongan = awal.find(awal[index-1])

print(awal[:potongan] + sisipan + awal[potongan:])

