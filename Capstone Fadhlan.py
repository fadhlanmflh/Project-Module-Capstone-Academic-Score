import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Fadhlan10!",
    database = "nilai"
)

print(conn)

connection = conn.cursor()

#Menu Utama

PilihanMenu = True
while PilihanMenu:
    print ('===============================\n')
    print('Daftar Nilai MTK SMA 01 Pagi : ')
    print('1. Menampilkan Data Nilai Siswa') 
    print('2. Menambahkan Data Nilai Siswa')
    print('3. Memperbarui Data Nilai Siswa') 
    print('4. Menghapus Data Nilai Siswa')
    print('5. Keluar Program')
    print('===============================\n')

    Input_PilihanMenu = int(input('Masukkan Angka yang ingin dijalankan : '))

    # READ DATA

    if (Input_PilihanMenu == 1):
        A= True
        while A:
            print('===============================\n')
            print(' 1. Perlihatkan Nilai Keseluruhan')
            print(' 2. Cari Nilai Siswa')
            print(' 3. Kembali ke Pilihan Menu ')
            print('===============================\n')

            Input_A = int(input("Masukkan Angka yang ingin dijalankan : "))

            #Perlihatkan Nilai Siswa Keseluruhan

            if (Input_A == 1):
                connection.execute("select * from nilai")
                myresult = connection.fetchall()
                nilai = None
                for x in myresult:
                    nilai = x
                    print('Nama,NISN,Nilai')
                    if (nilai != None ):            
                        print(nilai)
                    else:
                        print("Data Tidak Ditemukan")

            #Cari Nilai Siswa
            
            elif (Input_A == 2):
                nisn_Siswa = input (" NISN : ")
                connection.execute("select * from nilai where nisn_Siswa = "+nisn_Siswa+" LIMIT 1")
                myresult = connection.fetchall()
                nisn_siswa: None            
                for x in myresult:
                    nisn_Siswa = x
                    print('Nama,NISN,Nilai')
                    if (nisn_Siswa != None):
                        print(x)
                    else:
                        print("Data Tidak Ditemukan")

            #Kembali Ke Menu Utama
            elif(Input_A == 3):
                checker = input ("Apakah anda yakin untuk kembali ke Pilihan Menu? (ya/tidak)")
                if (checker == "ya"):
                    break
            else:
                break

    #CREATE DATA

    if (Input_PilihanMenu == 2):
        B = True
        while B:
            print('===============================\n')
            print("1. Menambahkan Nilai Siswa")
            print("2. Kembali ke Pilihan Menu")
            print('===============================\n')
            
            Input_B = int(input("Masukkan Angka yang ingin dijalankan : "))

            # 1. Menambahkan Nilai Siswa

            if (Input_B == 1):
                nisn_Siswa = input (' NISN :')
                connection.execute ('select * from nilai where nisn_Siswa = "+nisn_Siswa+" LIMIT 1')
                myresult = connection.fetchall()
                nilai = None
                for x in myresult:
                    nilai = x
                if (nilai != None ):
                    print("Data telah diinput")
                else:
                    nama_Siswa = input ("Nama Siswa : ")
                    nisn_Siswa = int (input("NISN : "))
                    nilai_Siswa = int(input("Nilai Siswa :"))                    
                    val = (nama_Siswa,nisn_Siswa,nilai_Siswa)
                    print(val)                    
                    
                    checker = input ("Apakah anda ingin menyimpan data? (ya/tidak)")
                    if (checker == "ya"):
                        sql = "INSERT INTO nilai (nama_Siswa,nisn_Siswa,nilai_Siswa) VALUES (%s, %s, %s)"                   
                        connection.execute(sql, val)
                        conn.commit() 
                        print("Nilai berhasil ditambahkan !")       

            #Kembali Ke Pilihan Menu            

            elif(Input_B == 2):
                checker = input ("Apakah anda yakin untuk kembali ke Pilihan Menu? (ya/tidak)")
                if (checker == "ya"):
                   break
            else:
                break

    #UPDATE DATA
                
    if (Input_PilihanMenu == 3):
        C = True
        while C:
            print('===============================\n')
            print("1. Perbarui Data")
            print("2. Kembali ke Pilihan Menu")
            print('===============================\n')
            
            Input_C = int(input("Masukkan Angka yang ingin dijalankan:"))

            # Perbarui Data

            if (Input_C == 1):
                nisn_Siswa = input(" NISN :")
                connection.execute ("select * from nilai where nisn_Siswa = "+nisn_Siswa+" LIMIT 1")
                myresult = connection.fetchall()
                nisn_siswa = None
                for x in myresult:
                    nisn_Siswa = x
                if (nisn_Siswa != None ):
                    checker = input ("Apakah anda ingin memperbarui data? (ya/tidak)")
                    if (checker == "ya"):
                        nama_Siswa = input ("Nama Siswa: ")
                        nisn_Siswa = input ("NISN : ") 
                        nilai_Siswa = input ("Nilai : ")  
                        print("Nama,NISN,Nilai") 
                        val = (nama_Siswa,nisn_Siswa,nilai_Siswa)
                        print(val)
                        update_data = input("Apakah anda yakin untuk memperbarui data? (ya/tidak)")
                        if (update_data == "ya"):
                            sql = "UPDATE nama SET nama_siswa=%s,nisn_siswa=%s,nilai_siswa=%s"
                            val = (nama_Siswa,nisn_Siswa,nilai_Siswa)
                            print("Data telah diperbarui")
                    else:
                       break    
                elif(nilai_Siswa == None ):
                    print("Data yang anda cari tidak ditemukan")

            #Kembali ke Menu Utama

            elif(Input_C == 2):
                checker = input ("Apakah anda yakin untuk kembali ke Pilihan Menu? (ya/tidak)")
                if (checker == "ya"):
                   break
            else:
                break    

    # 4. DELETE DATA
    if (Input_PilihanMenu == 4):
        D = True
        while D:
            print('===============================\n')
            print("1. Menghapus data")
            print("2. Kembali ke Pilihan Menu")
            print('===============================\n')
            
            Input_D = int(input("Masukkan angka yang ingin dijalankan :"))

            # Menghapus Data

            if (Input_D == 1):
                nisn_Siswa = input(" NISN :")
                connection.execute("select * from nilai where nisn_Siswa = "+nisn_Siswa+" LIMIT 1")
                myresult = connection.fetchall()
                nilai_Siswa = None
                for x in myresult:
                    nilai_Siswa = x
                if (nilai_Siswa != None ):
                    print(nilai_Siswa)
                    checker = input ("Apakah anda ingin Menghapus data? (ya/tidak)")
                    if (checker == "ya"):
                        print("Hapus nilai_siswa:", nilai_Siswa)
                        sql = "DELETE FROM nilai WHERE nisn_Siswa = "+nisn_Siswa+""
                        connection.execute(sql)
                        conn.commit()
                        print("Data Terhapus")
                    else:
                        ()

                else:
                    print("Data Tidak Ditemukan")

            # Kembali ke Menu Utama
                    
            elif(Input_D == 2):
                checker = input ("Apakah anda yakin untuk kembali ke Pilihan Menu? (ya/tidak)")
                if (checker == "ya"):
                   break
            else:
                break

    #EXIT PROGRAM

    elif (Input_PilihanMenu == 5):
        checker = input ("Apakah anda yakin untuk keluar dari Pilihan Menu? (ya/tidak)")
        if (checker == "ya"):
            print("TERIMA KASIH!")
            break
        else:
            print("PILIHAN YANG ANDA MASUKKAN SALAH")
            
