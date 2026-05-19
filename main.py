def statistika(sonlar):
    if len(sonlar) == 0:
        print("bo‘sh!")
        return

    yigindi = sum(sonlar)
    ortacha = yigindi / len(sonlar)
    maksimum = max(sonlar)

    print(f"Yig‘indi: {yigindi}")
    print(f"O‘rtacha qiymat: {ortacha}")
    print(f"Eng katta element: {maksimum}")

if __name__ == "__main__":
    personal_salom("Sanjar", "uz")
    kvadrat_royxat([1, 2, 3, 4])
    matn_formatlash("Python Dars", "katta")
    juft_oraliq(1, 10)
    foydalanuvchi_malumot("Sanjar", 20, "Toshkent")
    statistika([10, 20, 30, 40])
