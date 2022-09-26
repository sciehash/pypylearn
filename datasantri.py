# Applied Data Dictionary and Tuples
santri_kelas_7 = {
    'qeysa' : ("Annura Qeysa M.", 2009, "Nganjuk")
} 
santri_kelas_8 = {
    'firda' : ("Nur Laila Farida", 2008, "Nganjuk/Kalimantan")
}
santri_kelas_9 = {
    'fina' : ("Alfina Permadani Ainun Nu'ma", 2007, "Nganjuk"),
    'fatma' : ("(empty)", 2007, "Nganjuk"),
    'kinan': ("Naufalyn Kinan Nuha", 2007, "Surabaya")
}
santri_kelas_10 = {
    'fala' : ( "Falailia Rahmadhani" , 2005, "Malang"),
    'selva' : ("Selva Angerainny", 2007, "Palembang/Ogan Ilir"),
    'anis' : ("Anis Afifah", 2007, "Palembang/Ogan Ilir"),
    'tia' : ("Sri Ramadhania Scientia Sacra Hashina", 2006, "Tulungagung")
}
santri_kelas_11 = {
    'rifa' : ("Rifa Estiningtyas", 2006, "Bekasi"),
}
santri_kelas_12 = {
    'imro' : ("Siti Imroatus Solikhah", 2004, "Nganjuk"),
    'delima' : ("Delima Tsamrotul Khumairo Rohmah", 2004, "Nganjuk"),
    'dianti' : ("Siti Nur Rahma Dianti", 2004, "Nganjuk")
}
print("Daftar kata kunci: ")
for x in santri_kelas_7:
    print(x)
for x in santri_kelas_8:
    print(x)
for x in santri_kelas_9:
    print(x)
for x in santri_kelas_10:
    print(x)
for x in santri_kelas_11:
    print(x)
for x in santri_kelas_12:
    print(x)
print("Itulah Santri Pondok Pesantren Al-Khoiriyah Putri.")
kelas = input(str("Masukkan kelas dari santri yang datanya ingin anda cari (Masukkan angka 7-12): "))
if kelas == "7":
    dst = input(str("Masukkan kata kunci: "))
    print(f"{santri_kelas_7.get(dst)}")
elif kelas == "8":
    dsp = input(str("Masukkan kata kunci: "))
    print(f"{santri_kelas_8.get(dsp)}")
elif kelas == "9":
    dsr = input(str("Masukkan kata kunci: "))
    print(f"{santri_kelas_9.get(dsr)}")
elif kelas == "10":
    dss = input(str("Masukkan kata kunci: "))
    print(f"{santri_kelas_10.get(dss)}")
elif kelas == "11":
    dsu = input(str("Masukkan kata kunci: "))
    print(f"{santri_kelas_11.get(dsu)}")
elif kelas == "12":
    dsv = input(str("Masukkan kata kunci: "))
    print(f"{santri_kelas_12.get(dsv)}")
else:
    print("Invalid input, please re-run this program")
print("Thank you.")
