# belajarrrrt
belajar = 10
tidak_belajar = 12
tidak_sekolah_tidak_belajar = 0

print(belajar)

print("tidakbelajar=", tidak_belajar)


print("\n")
print("===macam macam data dalam python")

# data yang menggunakan angka (intege/int)
data_integer = 11
print("data :", data_integer
      )
# data yang menggunakan angka koma(float))
data_float = 1.5
print("data :", data_float)
print("-data :", data_float)

# data kumpulan karakter (stringe)
data_stringe = "udin"
print("data :", data_stringe)

# data yang hanya true/fals (bolean)
data_bool = True
print("data :", data_bool)

# tipe data khusus

# bilangan kompleks (complex)
data_complex = complex(5, 6)
print("data :", data_complex)


print("\n")


print("===casting type data====")
# casting adalah kita dapat merubah data satu ke data yang lain mya contoh

print("===integer===")

data_int = 0
data_bool = bool(data_int)
data_str = str(data_int)
data_float = float(data_int)
print("data =", data_bool)
print("data =", data_str)
print("data =", data_float)

print("===bolean===")

data_bool = -8
data_int = bool(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data =", data_int)
print("data =", data_str)
print("data =", data_float)

# input data user adalah kita bisa memasukkan suatu data

#data =input("masukan data =")
#print ("data :",data)

# stringe

#data_str =str(input ("masukan data ="))
#print ("data :",data_str)


# bolean
#data_bool=bool(int(input ("masukan data =")))
#print ("data :",data_bool)
print("\n")
print("===aritmatika python===")
# aritmatika python

a = 16
b = 8

# penjumlahan +
hasil = a + b
print(a, '+', b, '=', hasil)

# pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# perpangkatan **
hasil = a ** b
print(a, '**', b, '=', hasil)

# modulus // (sisah dari pembagiannya)
hasil = a // b
print(a, '//', b, '=', hasil)

# Flour devision % (membulat kan float)

hasil = a % b
print(a, '%', b, '=', hasil)
print("\n")

# latihan perhitungan sederhana
print("===KONVERSI ARITMATIKA===")

#celcius = float(input ("masukan data ="))
#print ("hasil data =",celcius,"celcius")

# Reamur
#reamur = (4/5) * celcius
#print ("hasil data =",reamur,"reamur")


# Fahrenheit
#Fahrenheit = ((9/4) * celcius) + 32
#print ("hasil data =", Fahrenheit,"Fahrenheit")

# kelvin
#ff= celcius + 273
#print ("hasil data =",ff,"Kelvin")


# komparasi python
print("\n")
print("====Komparasi python====")
#">,<,<=,>=,==,!=,is not"
a = 4
b = 2

print("(>)", "lebih besar")
hasil = a > 3
print("a > 3=", hasil)
hasil = b > 4
print("b > 4=", hasil)
hasil = b > 2
print("b > 2=", hasil)

print("(>=)", "lebih besar samadengan")
hasil = a >= 3
print("a => 3=", hasil)
hasil = b >= 4
print("b >= 4=", hasil)
hasil = b >= 2
print("b >= 2=", hasil)

print("(<)", "kurang dari")
hasil = a < 3
print("a < 3=", hasil)
hasil = b < 4
print("b > 4=", hasil)
hasil = b < 2
print("b < 2=", hasil)

print("(<=)", "kurang dari samadengan")
hasil = a <= 3
print("a <= 3=", hasil)
hasil = b < 4
print("b <= 4=", hasil)
hasil = b <= 2
print("b <= 2=", hasil)


print("(==)", "sama dengan")
hasil = a == 3
print("a == 3=", hasil)
hasil = b == 4
print("b == 4=", hasil)
hasil = b == 2
print("b == 2=", hasil)

print("(!=)", "tidak samadengan")
hasil = a != 3
print("a != 3=", hasil)
hasil = b != 4
print("b != 4=", hasil)
hasil = b != 2
print("b != 2=", hasil)
print("\n")
# operasi logika dan bolean
print("======Operasi logika dan bolean======")
# not,and,or,xor

print("-----not------")
a = True
c = not a
print("data a", c)
print("-----and------")  # akan true jika kedua nya true(*)
a = True
b = False
c = a and b
print(a, "and", b, "=", c)
a = True
b = True
c = a and b
print(a, "and", b, "=", c)
a = False
b = True
c = a and b
print(a, "and", b, "=", c)
a = False
b = False
c = a and b
print(a, "and", b, "=", c)
print("-----or--------")  # jika salah satu true,maka hasilnya true (+)
a = True
b = False
c = a or b
print(a, "or", b, "=", c)
a = True
b = True
c = a or b
print(a, "or", b, "=", c)
a = False
b = True
c = a or b
print(a, "or", b, "=", c)
a = False
b = False
c = a and b
print(a, "or", b, "=", c)
print("-----xor--------")  # akan true jika salah satu true,sisahnya false
a = True
b = False
c = a ^ b
print(a, "xor", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "xor", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "xor", b, "=", c)
a = False
b = False
c = a ^ b
print(a, "xor", b, "=", c)
print("\n")
print("======latih\an komparasi dan logika=======")

# +++++++++3---------10++++++++++
# gabungan

#inputUser = float(input("$ masukan angka kurang dari 3 atau lebih dari 10"))

# +++++++++3-----------
#isKurangdari = (inputUser < 3)
#print ("kurang dari 3 =",isKurangdari)

# ---------10+++++++++++
#isLebihdari = (inputUser > 10)
#print ("Lebih dari 10 =",isLebihdari)

# +++++++++3---------10++++++++++
#isCorrect = isKurangdari or isLebihdari
#print ("angka yang anda masukan =",isCorrect)

# print("\n")
# ---------3++++++++++10---------
# irisan
#inputUser = float(input("$ masukan angka lebih dari 3 dan kurang dari 10"))
# ---------3++++++++++
#isLebihdari = (inputUser > 3)
#print ("Lebih dari 3 =",isLebihdari)

# ++++++++++10---------
#isKurangdari = (inputUser < 10)
#print ("kurang dari 10 =",isKurangdari)

# ---------3++++++++++10---------
#isCorrect = isKurangdari and isLebihdari
#print ("angka yang anda masukan =",isCorrect)
print("\n")
# operasi bitwise,operasi biner
print("==========operasi bitwise,operasi biner===========")

a = 9
b = 5

# bitwise or (|)
c = a | b
print("\n==========or=========")
print("nilai :", a, "binary:", format(a, "08b"))
print("nilai :", b, "binary:", format(b, "08b"))
print("===========================(|)")
print("nilai :", c, "binary:", format(c, "08b"))

# bitwise and (&)
c = a & b
print("\n==========&=========")
print("nilai :", a, "binary:", format(a, "08b"))
print("nilai :", b, "binary:", format(b, "08b"))
print("===========================(&)")
print("nilai :", c, "binary:", format(c, "08b"))

# bitwise XOR (^)
c = a ^ b
print("\n==========XOR=========")
print("nilai :", a, "binary:", format(a, "08b"))
print("nilai :", b, "binary:", format(b, "08b"))
print("===========================(^)")
print("nilai :", c, "binary:", format(c, "08b"))

# shift right (>>)
z = a >> 2
print("\n==========>>=========")
print("nilai :", a, "binary:", format(a, "08b"))
print("nilai :", b, "binary:", format(b, "08b"))
print("===========================(>>)")
print("nilai :", c, "binary:", format(z, "08b"))

# shift right (<<)
z = a << 2
print("\n==========<<=========")
print("nilai :", a, "binary:", format(a, "08b"))
print("nilai :", b, "binary:", format(b, "08b"))
print("===========================(<<)")
print("nilai :", c, "binary:", format(z, "08b"))
print("\n")
print("========Operator Asigmen======")
# OPerasi yang dapat di lakukan dengan penyingkatan
# Operasi ditambah dengan asigmen
a = 5  # Adalah assigment
print("nilai a adalah =", a)
print("\n")
print("============pertambahan===========")
a += 1  # artinya nilai a = a+1
print("nilai a += 1, adalah =", a)
print("\n")
print("============pengurangan===========")
a -= 2  # artinya nilai a = a-2
print("nilai a -= 2, adalah =", a)
print("\n")
print("============perkalian===========")
a *= 5  # artinya nilai a = a*5
print("nilai a *= 5, adalah =", a)
print("\n")
print("============pembagian===========")
a /= 2  # artinya nilai a = a/2
print("nilai a /= 2, adalah =", a)
print("\n")
print("============modulus===========")
b = 10
print("\nnilai b =", b)
b %= 3  # artinya sisah dari pembagian b = b%3
print("nilai modulus b %= 3, adalah =", b)
print("\n")
print("============mpembulatan===========")
b = 10
print("\nnilai b =", b)
b //= 3  # artinya pembulatan dari b = b//3
print("nilai modulus b //= 3, adalah =", b)
print("\n")
print("============pangkat===========")
a = 5
print("nilai a adalah =", a)
a **= 3
print("nilai a**=3=, adalah", a)
print("\n")
print("============Menggunakan Operasi Bitwise===========")
# operasi bitwise
# OR
c = True
print('\nnilai c =', c)
c |= False
print('nilai c |= False =, nilai c menjadi =', c)
c = False
c |= False
print('nilai c |= False =, nilai c menjadi =', c)
# and
c = True
print('\nnilai c =', c)
c &= False
print('nilai c &= False =, nilai c menjadi =', c)
c = True
c &= True
print('nilai c &= True =, nilai c menjadi =', c)
# XOR
c = True
print('\nnilai c =', c)
c ^= False
print('nilai c ^= False =, nilai c menjadi =', c)
c = True
c ^= True
print('nilai c ^= True =, nilai c menjadi =', c)
# geser geser
d = 0b01101110
print("\nilai d =", d)
print("nilai d =", format(d, '04b'))
d >>= 2
print("nilai d >>=2, nilai d menjadi", format(d, "04b"))
d <<= 1
print("nilai d <<=1, nilai d menjadi", format(d, "04b"))
print('\n')
print("===============pengenalan stringe=============")
data = "Saya ganteng"
print(data)
# 1 cara menbuat stringe

# 1 dengan menggunakn singgel quote ''''''

dataX = 'menggunakan singgel quote'
print(dataX)

# 2 dengan menggunakn doubel quote """?"
dataC = "menggunakan doubel quote"
print(dataC)

# 2 menggunakan tanda \
# membuat tanda ' menjadi stringe
print('mari solat jum\'at')
print('g\'day,isn\'t it')

# backlash
# print("c:\user\nurdin") >>>> ini tidak bisa karena tanda \ merupakan karakter khusus
print("c:\\uers\\udin")

# tab
# menggunakan simbol \t untuk mengetab
print("nurdin\t junedi,jauhan")

# backspace
# mengunakn simbol \b untuk backspace
print("ucup \bnurdin, deketan")

# newline atau enter
# menngunakan simbol \n untuk newline
print("baris pertama,\nbariskedua")  # LF >>>> line feed >>>> unix,macos,linux
# CR >>>> Carriage retrun >>>> commodore,acorn,lisp (sudah lama)
print("baris pertama,\rbariskedua")
# CRLF >>> carriage retrun line feed >>>>> windwos
print("baris pertama,\r\nbariskedua")

# 3 string literar atau raw
# hati hati
print("c:\new folder")  # akan salah path nya

# menggunakan raw string
print(r"c:\new folder")  # semua nya akan di anggap stringe menngunakan (r)

# multi literal stringe
print("""
Nama : Nurdin
Kelas : 8
""")
# multi literal string dan raw
print(r"""
Nama : Nurdin
Kelas : 8
website :  www.nurdin.com/my.id
""")
print("\n")
print("=======Operasi Manipulasi String========")
# operasi dan manipulasi string
# 1 Menyambung string
nama_pertama = "Ali"
nma_tengah = "Akbar"
nma_akhir = "ganteng"
nama_lengkap = nama_pertama + " " + nma_tengah+" " + nma_akhir
print(nama_lengkap)

# 2 menghitung panjang string menggunkan (Len)
panjang = len(nama_lengkap)
print("Panjang nama Ali Akbar Ganteng", "=", (panjang))
# 3 Operator untuk string

# Mengcek apakah ada komponen Char atau string di string
# menggunakan logika "in"
print("\n", 30*"=")
d = "d"
status = d in nama_lengkap
print("string", d, "ada di", nama_lengkap, "=", str(status))

d = "z"
status = d not in nama_lengkap
print("string", d, "ada di", nama_lengkap, "=", str(status))

d = "ganteng"
status = d in nama_lengkap
print("string", d, "ada di", nama_lengkap, "=", str(status))

# ngulang stringe
print("\n", 30*"=")

# indexing
print("indexing ke-0 :", nama_lengkap[0])
print("indexing ke-1 :", nama_lengkap[1])
print("indexing ke-2 :", nama_lengkap[2])
print("indexing ke-3 :", nama_lengkap[3])
print("indexing ke-4 :", nama_lengkap[4])
print("indexing ke-5 :", nama_lengkap[5])
print("indexing ke-5 :", nama_lengkap[-3])
# untuk membuat range atau sampai
print("indexing ke[3:4] :", nama_lengkap[0:2])

# item paling kecil
print("\n", 30*'=', "\n", "paling kecil :", min(nama_lengkap))
# item paling besar
print("paling kecil :", max(nama_lengkap))

# manipulasi data dengan "ord" dan "chr"
ascii_code = ord(" ")
print("\n", 30*"=", "\n", "ASCII code untuk o adalah =", str(ascii_code))
# kita bisa manipulasi data seperti di bawah ini
data = 111
print("charr untuk ASCII 111 adalah =", chr(data))

# Operator dalam method
data = "Ali AKBAR"
# Fungsi count dalam data dalah untuk nempel ke string bukan sebagai helper string,jadi method adalah fungsi yang menempel dengan string
jumlah = data.count("A")
print("\n", 30*"=", "\n", "Jumlah a pada", data, "=", str(jumlah))

# Merubah Bentuk dalam bentuk method
# Operator dalam bentuk method

# Merubah case dari string
# Merubah senua  ke upper case

salam = "broo"
print("normal =" + salam)

salam = salam.upper()
print("upper =" + salam)

# merubah semua ke lower case / ke kecil semua
alay = "aKu sEdAnGKeCE aBis"
simpulan = alay.lower()
print("lower =", simpulan)

# pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "masee"
apakah_lower = salam.islower()  # hasil nyta bolean
print("siX =" + str(apakah_lower))

haiii = "MASE"
apakah_lower = haiii.islower()  # hasil nyta bolean
print("siX =" + str(apakah_lower))

haiii = "MASE"
apakah_lower = haiii.isupper()  # hasil nyta bolean
print("siX =" + str(apakah_lower))

haiii = "MASeEeeeeeEE"
apakah_lower = haiii.isupper()  # hasil nyta bolean
print("siX =" + str(apakah_lower))

# isalpha() <-- Untuk mengecek semuanya huruf
# isalnum() <--- Huruf dan angka
# isdesimal() <---- angka saja
# isspace () <---  string kosong space,tab,newline \n

# istitle () <---- semua kata dimuali dengan huruf besar
judul = "Ayah Ku Ternyata Bapak Ku"
Cek_judul = judul.istitle()
print(judul + "istitle" + "=" + str(Cek_judul))

##Mengecek Komponen strawitch() endswitch() <---- Keren Melihat kata yang paling awal
cek_strat = "Jono Markotop Sekolokotop".startswith('Jono')
print("Start :" + str(cek_strat))
cek_strat = "Jono Markotop Sekolokotop".startswith('Markotop')
print("Start :" + str(cek_strat))

cek_end ="Jono Markotop Sekolokotop".endswith('Sekolokotop')
print("end :" + str(cek_end))
cek_end ="Jono Markotop Sekolokotop".endswith('Jono')
print("end :" + str(cek_end))

##Penggabungan Komponen join() dan menghilangkan komponen split ()
Pisah = ['aku','cinta','dia']
gabungan = ','.join(Pisah)
print("Gabungan :",gabungan)
print ("pisah :",Pisah)

gabungan = ' '.join(Pisah)
print("Gabungan :",gabungan)

gabungan = "alijelekganteng"
print(gabungan.split("jelek"))

##alokasi karakter menggunakan rjust() ljust() center()
kanan = "kanan".rjust(10)
print ("," + kanan + ',')

kiri = "kiri".ljust(10)
print ("," + kiri + ',')

tengah = "tengah".center(10,"=")
print ("," + tengah + ',')

#kebalikan nya strip()
tengah = tengah.strip("=") #meghilankan tanda "="
print (tengah)

print("\n","==============IF and ELSE=================")
#if and else statemen

#if nya
#KOndisinya
#statemen nya

#Program sebelum nya
# IF Kondisi : Aksi
# Program Sebelumnya


# 1. Pemrograman aksi if inline
#nama = input("siapa nama kamu :")

#if nama=="ali" :  pertanyaan = input("gantengan ali atau reza rahadian : ")
#if pertanyaan=="ali" : print("kamu Teapt sekali💖😍😍😍")
#if pertanyaan=="reza" : print("BODOHHHHHHHHHHHHH")

# 2. Pemrograman if indetetition
#if nama=="ucup" :
#      print("gantengan ali tau")
#     print("emang benersihhhhh")

# 3. else statemen
#if nama=="otong" :
      #print("hai otong")

#elif nama=="ali":
      #print("halo tuan")
#elif nama=="nurdin":
      #print("siapa kamu")
#else:
      #print("ah kamu jelek tauuu")


print("\n","=========Looping=============")
#Looping (Perulangan)
#for kondisi :
#aksi


#ini dengan list
anka2_list=[0,1,2,3,4]#ini dengan list

for i in anka2_list:
      print("i sekarang>>>>{i}")








