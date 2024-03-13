# Data dictionary jadwal daspro IF2
jadwalDasproIF2 = {
    'Senin': 'Jam 10.50 - 14.10',
    'Selasa': 'Jam 08.00 - 11.30',
}

# Data dictionary jadwal daspro IF3
jadwalDasproIF3 = {
    'Rabu': 'Jam 14.20 - 17.00',
    'Kamis': 'Jam 10.50 - 14.10',
}

# Menggabungkan kedua dictionary
jadwal_gabung = {}
jadwal_gabung.update(jadwalDasproIF2)
jadwal_gabung.update(jadwalDasproIF3)

# Mencetak data dictionary gabungan
print("Jadwal Mata Kuliah Gabungan:")
print(jadwal_gabung)

