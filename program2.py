# Data list pertama sebagai kunci
keys = ['1 Minggu', '1 Bulan', '1 Tahun']

# Data list kedua sebagai nilai
values = [ '7 Hari' , '4 Minggu', '12 Bulan']

# Menggabungkan kedua list menjadi dictionary
data_dict = dict(zip(keys, values))

# Mencetak data dictionary
print("Data Dictionary:")
print(data_dict)
