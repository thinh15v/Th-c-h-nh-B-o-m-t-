class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id  # Mã sinh viên
        self._name = name  # Tên sinh viên
        self._sex = sex  # Giới tính
        self._major = major  # Ngành học
        self._diemTB = diemTB  # Điểm trung bình
        self._hocluc = ""

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if maxId < sv.id:
                    maxId = sv.id
            maxId = maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))     
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv !=None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = int(input("Nhập chuyên ngành của sinh viên: "))
            diemTB = float(input("Nhập điểm của sinh viên: "))
            
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại".format(ID))
    

    # Sắp xếp danh sách sinh viên theo ID
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    # Sắp xếp danh sách sinh viên theo tên
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    # Sắp xếp danh sách sinh viên theo điểm trung bình
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    # Tìm sinh viên theo ID
    def findByID(self, ID):
        searchResult = None
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv.id == ID:
                    searchResult = sv
                    break
        return searchResult

    # Tìm sinh viên theo tên (theo từ khóa)
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):  # Tìm kiếm không phân biệt chữ hoa/thường
                    listSV.append(sv)
        return listSV

    # Xóa sinh viên theo ID
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv !=None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    # Xếp loại học lực sinh viên
    def xepLoaiHocLuc(self, sv):
        if  (sv._diemTB >=8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def  showsinhvien(self,listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID","Name","Sex","Major","Diem TB","Hoc Luc"))
        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format(sv._id, sv._name,sv._sex,sv._major,sv._diemTB,sv._hocLuc))
        print("\n")
        
    def getlistsinhvien(self):
        return self.listSinhVien
    
# Khởi tạo đối tượng QuanLySinhVien
qlsv = QuanLySinhVien()

# Vòng lặp để tiếp tục hiển thị menu cho người dùng
while True:
    # Hiển thị menu cho người dùng chọn
    print("\n*** CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ***")
    print("1. Thêm sinh viên.")
    print("2. Cập nhật thông tin sinh viên theo ID.")
    print("3. Xóa sinh viên theo ID.")
    print("4. Tìm kiếm sinh viên theo tên.")
    print("5. Sắp xếp sinh viên theo điểm trung bình.")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành.")
    print("7. Hiển thị danh sách sinh viên.")
    print("0. Thoát")

    # Nhập lựa chọn của người dùng
    key = int(input("Nhập tùy chọn: "))

    # Thực hiện hành động dựa trên lựa chọn của người dùng
    if key == 1:
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công!")

    elif key == 2:
        ID = int(input("Nhập ID sinh viên cần cập nhật: "))
        qlsv.capNhatThongTin(ID)

    elif key == 3:
        ID = int(input("Nhập ID sinh viên cần xóa: "))
        qlsv.xoaSinhVien(ID)

    elif key == 4:
        keyword = input("Nhập tên sinh viên cần tìm: ")
        qlsv.timKiemSinhVienTheoTen(keyword)

    elif key == 5:
        qlsv.sapXepTheoDiemTB()
        print("Danh sách sinh viên sau khi sắp xếp theo điểm trung bình:")
        qlsv.hienThiDanhSachSinhVien()

    elif key == 6:
        qlsv.sapXepTheoTenChuyenNganh()
        print("Danh sách sinh viên sau khi sắp xếp theo tên chuyên ngành:")
        qlsv.hienThiDanhSachSinhVien()

    elif key == 7:
        if(qlsv.soLuongSinhVien()>0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showsinhvien(qlsv.getlistsinhvien())    
    elif key == 0:
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
