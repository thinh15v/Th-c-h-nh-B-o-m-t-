from SinhVien import SinhVien

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