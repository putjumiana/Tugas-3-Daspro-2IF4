# Data dictionary berisi username dan password mahasiswa
data_mahasiswa = {
    'Putje': '07352111007',
    'Epuy': '07352111025',
    'Sucai': '07352111048',
    'Miyanto': '07352111029',
    'Lapoi': '07352111027',
    'Ramatin': '07352111014',
    'Dini': '07352111005',
    'Mawar': '07352111006',
    'Lini': '07352111067',
    'Yus': '07352111021'
}
# Fungsi untuk sistem login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Memeriksa apakah username ada dalam data_mahasiswa dan password cocok
    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Selamat datang, " + username + "!")
    else:
        print("Data yang dimasukkan salah.")

# Memanggil fungsi login
login()
