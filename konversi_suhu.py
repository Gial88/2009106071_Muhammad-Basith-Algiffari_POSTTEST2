print("Konversi Suhu")
print("="*50)
print("Pilihan Menu")
print("="*50)
print("1.Konversi Ke Farenheit")
print("2.Konversi Ke Reamur")
print("3.Konversi Ke Kelvin")
print("="*50)

stop = False

while (not stop):
	pil = int(input("Pilih 1/2/3 : "))

	if pil == 1:
		suhu = int(input("Masukkan Besaran Suhu : "))
		print("Rumus Farenheit = 9/5* C + 32")
		far = float(9/5*suhu+32)
		print("suhu sebesar "+str(far)+"Farenheit")
	elif pil == 2:
		suhu = int(input("Masukkan Besaran Suhu : "))
		print("Rumus Farenheit = 4/5* C")
		rea = float(4/5*suhu)
		print("suhu sebesar "+str(rea)+"Farenheit")
	elif pil == 3:
		suhu = int(input("Masukkan Besaran Suhu : "))
		print("Rumus Farenheit = C + 273")
		kel = float(suhu+273)
		print("suhu sebesar "+str(kel)+"Kelvin")
	else:
		print("Error")

	ulang = input("Apakah Anda Ingin Mengukur Suhu Kembali ? (ya/tidak) ")
	if (ulang == "tidak") :
		stop = True
print("Terima Kasih")	



