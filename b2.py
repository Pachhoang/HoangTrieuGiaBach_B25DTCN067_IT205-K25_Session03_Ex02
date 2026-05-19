print (" --- HỆ THỐNG GỬI EMAIL THƯỜNG TẾT -- ")

# Vòng Lặp chạy đúng 3 Lần cho 3 nhân viên
for employee_number in range(1, 4):
    print(" --- Đang xu lý nhan vien số", employee_number, " -- ")

# Yêu cầu kế toán nhập dữ Liệu
    working_days = int(input ("Nhập số ngày cong trong thang: "))

# Kiểm tra diều kiện
    if working_days == 0:
        print ("CANH BAO: Nhan vien nghi ca thang. Khong xet duyet thưong.")
        continue #thêm continue
    bonus_amount = working_days * 200000
    print("-> Đã gui Email: Chuc mung nhan duoc", bonus_amount, "VND tien thuong!")
    print("-------------------------- \n")

print ("Đã hoan tat qua trình duyệt thường cho 3 nhân viên!")
