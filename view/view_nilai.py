from model.daftar_nilai import kontak



def header():

    print("╔═════════════════════════════════════════════════════════════════════════╗")

    print("╠════════════════════ PROGRAM INPUT DATA MAHASISWA ═══════════════════════╣")

    print("╠═══════════╦════════════╦════════════╦═════════════╦══════════╦══════════╣")

    print("║   (A)dd   ║   (E)dit   ║  (D)elete  ║  (S)earch   ║  (L)ist  ║  (Q)uit  ║")

    print("╚═══════════╩════════════╩════════════╩═════════════╩══════════╩══════════╝")





def notoption():

    print(" __________")

    print("| Pilih opsi yang tersedia |")

    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    print("    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")





def cetak():

    print("\n╔═════════════════════════════════════════════════════════════════════════╗")

    print("╠═════════════════════════ DAFTAR DATA MAHASISWA ═════════════════════════╣")

    print("╠════╦═════════════════╦══════════════════╦═══════╦═══════╦═══════╦═══════╣")

    print("║ NO ║      NAMA       ║       NIM        ║ TUGAS ║  UTS  ║  UAS  ║ AKHIR ║")

    print("╠════╬═════════════════╬══════════════════╬═══════╬═══════╬═══════╬═══════╣")

    no = 1

    for tabel in kontak.values():

        print("║{0:3} ║ {1:15} ║ {2:16} ║ {3:5} ║ {4:5} ║ {5:5} ║ {6:5} ║"

              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))

        no += 1

    print("╚════╩═════════════════╩══════════════════╩═══════╩═══════╩═══════╩═══════╝")

    print("\n    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")





def nyari():

    from view.input_nilai import carive

    carive()

    print("    (A)dd       (E)dit      (D)elete     (S)earch      (L)ist     (Q)uit   ")
from view.view_nilai import nyari,cetak,header,notoption

from view.input_nilai import inputan,edit,delett

header()

while True:



    c = input("\nPilih Opsi: ")



    # EXIT PROGRAM

    if c.lower() == 'q':

        print(".:TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI:.")

        ext = input("\nPress ENTER to exit")

        if ext == '':

            break

        else:

            break



    # PRINT DATA

    elif c.lower() == 'l':

        cetak()



    # MENAMBAH DATA

    elif c.lower() == 'a':

        inputan()



    # EDIT DATA

    elif c.lower() == 'e':

        edit()



    # MENCARI DATA

    elif c.lower() == 's':

        nyari()



    # HAPUS DATA

    elif c.lower() == 'd':

        delett()



    else:

        notoption()