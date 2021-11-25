huruf = str(input(("Masukkan kalimat untuk dihitung: ")))

def hitung(): 
    pembulatan = len(huruf)
    dihitung = (2/3 * pembulatan)
    return dihitung
    
hasil = hitung()
print(int(hasil))
    
