# Another attempt on making data dictionary
amtsilati = {
    'huruf_jer': "la, ila, min, 'an, 'ala, fi,",
    'mabni': "tetap",
    'origin': "PP Darul Falah - Jepara",
    'writer': "H. Taufiqul Hakim"
}
glosamsi = 'origin'
amtsilati.update({'origin': "Pondok Pesantren Darul Falah Amtsilati - Jepara"})
print(amtsilati.get(glosamsi))
glosamsi2 = amtsilati.copy()
print(amtsilati)
print(glosamsi2)