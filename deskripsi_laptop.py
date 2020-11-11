print("Dekripsi Laptop Anda")
print("="*50)
laptop = []

nama_laptop = input("Masukkan nama laptop : ")
laptop.append(nama_laptop)

tahun_laptop = int(input("Tahun Rilis : "))
laptop.append(tahun_laptop)

berat_laptop = float(input("Berat Laptop dalam Kg : "))
laptop.append(berat_laptop)

spek_laptop = [input("Processor : "),
				input("VGA : "), 
				input("RAM : "), 
				input("Storage : ")]
laptop.append(spek_laptop)


pilih = input("Laptop baru atau second (baru/second) : ")
if pilih == "baru":
	ket = "Baru"
	harga_laptop = int(input("Masukkan Harga Laptop pada saat beli : Rp "))
	laptop.append(ket)
	laptop.append(harga_laptop)
else : 
	ket = "Second"
	harga_laptop = int(input("Masukkan Harga Laptop pada saat beli : Rp "))
	laptop.append(ket)
	laptop.append(harga_laptop)
print("="*50)
print("Saya Memiliki laptop "+ laptop[0])
print("Yang rilis pada tahun "+ str(laptop[1]))
print("Berat bersih laptop ini "+ str(laptop[2]) +" Kg")
print("Dengan Spek Diantaranya :")
print("Processor "+ laptop[3][0])
print("VGA "+ laptop[3][1])
print("RAM "+ laptop[3][2])
print("Storage "+ laptop[3][3])
print("Status Laptop ini "+ laptop[4])
print("Yang saya beli dengan harga Rp "+ str(laptop[5]))

