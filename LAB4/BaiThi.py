from abc import ABC, abstractmethod

class AbcHo(ABC):
    @abstractmethod

    def tinh_don_gia_dien(self):
        pass
    @abstractmethod
    def __str__(self):
        pass


class Ho(AbcHo):
    loai1 = 3500
    loai2 = 5500
    loai3 = 7000

    def __init__(self, maKH, ten_chu_ho, chi_so_cu, chi_so_moi):
        self._maKH = maKH
        self._ten_chu_ho = ten_chu_ho
        self._chi_so_cu = chi_so_cu
        self._chi_so_moi = chi_so_moi
        self._don_gia_dien = 0
        
    def update_gia_dien(self, loai1, loai2, loai3):
        self.loai1 = loai1
        self.loai2 = loai2
        self.loai3 = loai3

    def get_makh(self):
        return self._maKH

class HoGiaDinh(Ho):
    
    def __init__(self, maKH, ten_chu_ho, chi_so_cu, chi_so_moi):
        super().__init__(maKH, ten_chu_ho, chi_so_cu, chi_so_moi)

    def tinh_don_gia_dien(self):
        dien_su_dung = self._chi_so_moi - self._chi_so_cu
        if dien_su_dung <= 100:
            self._don_gia_dien = dien_su_dung*Ho.loai1
        else:
            self._don_gia_dien = dien_su_dung*Ho.loai2
    
    def __str__(self):
        return str([self._maKH, self._ten_chu_ho, self._chi_so_cu, self._chi_so_moi, self._don_gia_dien])

class HoKinhDoanh(Ho):
    
    def __init__(self, maKH, ten_chu_ho, chi_so_cu, chi_so_moi, he_so_sd):
        super().__init__(maKH, ten_chu_ho, chi_so_cu, chi_so_moi)
        self.__he_so_sd = he_so_sd
    
    def tinh_don_gia_dien(self):
        dien_su_dung = self._chi_so_moi - self._chi_so_cu

        if dien_su_dung > 500:
            self._don_gia_dien = dien_su_dung*Ho.loai3*self.__he_so_sd
        else:
            self._don_gia_dien = dien_su_dung*Ho.loai2*self.__he_so_sd
    def __str__(self):
        return str([self._maKH, self._ten_chu_ho, self._chi_so_cu, self._chi_so_moi, self.__he_so_sd, self._don_gia_dien])
     

class HoSanXuat(Ho):
    def __init__(self, maKH, ten_chu_ho, chi_so_cu, chi_so_moi, he_so_sd):
        super().__init__(maKH, ten_chu_ho, chi_so_cu, chi_so_moi)
        self.__he_so_sd = he_so_sd

    def tinh_don_gia_dien(self):
        dien_su_dung = self._chi_so_moi - self._chi_so_cu
        self._don_gia_dien = dien_su_dung*Ho.loai3*self.__he_so_sd
    
    def __str__(self):
        return str([self._maKH, self._ten_chu_ho, self._chi_so_cu, self._chi_so_moi, self.__he_so_sd, self._don_gia_dien])

class AbcPhuong(ABC):
    @abstractmethod

    def init_du_lieu(self):
        pass

    def tinh_don_gia_dien(self):
        pass

class Phuong(AbcPhuong):

    def __init__(self, ma_phuong, ten_phuong):
        self.__ma_phuong = ma_phuong
        self.__ten_phuong = ten_phuong
        self.__ds_kh = []

    """Cau 1: Khoi tao danh sach khach hang"""
    def init_du_lieu(self, ds = None):
        if ds is None:

            kh1 = HoKinhDoanh(123, "A", 120, 960, 1.8)
            kh2 = HoGiaDinh(124, "B", 400, 450)
            kh3 = HoKinhDoanh(125, "C", 300, 689, 1.3)
            kh4 = HoSanXuat(125, "D", 150, 965, 1.5)
            kh5 = HoGiaDinh(126, "E", 500, 900)
            kh6 = HoSanXuat(127, "F", 350, 987, 1.6)
            kh7 = HoSanXuat(128, "G", 100, 989, 1.9)

            self.__ds_kh.extend([kh1, kh2, kh3, kh4, kh5, kh6, kh7])
        else:
            self.__ds_kh.extend(ds)
        

    def print_ds_kh(self):
       for kh in self.__ds_kh:
           print(kh)

    """Cau 2: Tinh tien dien cho tung khach hang"""

    def tinh_don_gia_dien(self):
       list(map(lambda kh : kh.tinh_don_gia_dien(), self.__ds_kh))
    
    """Cau 3: Tim kiem khach hang theo ma khach hang"""
    def tim_kh_theo_maKH(self, maKh)->list:
        return list(filter(lambda kh: kh.get_makh() == maKh, self.__ds_kh))

    """Cau 4: Tinh trung binh tien dien cua tat ca khach hang trong phuong """

    def tinh_trung_binh_tien_dien_cua_tat_ca_KH(self)->float:
        self.tinh_don_gia_dien()
        return sum(kh._don_gia_dien for kh in self.__ds_kh)/len(self.__ds_kh)
    
    """Cau 5: Tim khach hang co so tien dien lon nhat"""

    def tim_khach_hang_co_don_gia_dien_cao_nhat(self)->list:
        self.tinh_don_gia_dien()
        m = max(self.__ds_kh, key= lambda kh: kh._don_gia_dien)
        return list(filter(lambda kh: kh._don_gia_dien == m._don_gia_dien, self.__ds_kh))

    """Cau 6: Tim khach hang loai ho san xuat co tien dien nho nhat """
    def tim_khach_hang_loai_ho_san_xuat_co_tien_dien_nho_nhat(self)->list:
        self.tinh_don_gia_dien()
        ds_ho_san_xuat = list(filter(lambda kh: isinstance(kh, HoSanXuat),  self.__ds_kh))
        m = min(ds_ho_san_xuat, key= lambda kh: kh._don_gia_dien)
        return list(filter(lambda kh: kh._don_gia_dien == m._don_gia_dien, ds_ho_san_xuat ))

    """Cau 7: Viet ham main, thuc hien cac testcase kiem tra cac yeu cau tren """

if __name__ == "__main__":
    P = Phuong(833,"UIT")

    print("\n Test1: Khởi tạo nhanh 7 khách hàng:")
    P.init_du_lieu()
    P.print_ds_kh()

    print("\n Test2: Tính tiền điện cho từng khách hàng:")
    P.tinh_don_gia_dien()
    P.print_ds_kh()

    print("\n Test3: Tìm kiếm khách hàng theo mã khách hàng:")
    for kh in P.tim_kh_theo_maKH(124):
        print (kh)

    print("\n Test4: Tính trung bình tiền điện của tất cả khách hàng:")
    print(P.tinh_trung_binh_tien_dien_cua_tat_ca_KH())

    print("\n Test5: Tìm khách hàng có số tiền điện cao nhất:")
    for kh in P.tim_khach_hang_co_don_gia_dien_cao_nhat():
        print(kh)

    print("\n Test6: Tìm khách hàng loại hộ sản xuất có số tiền điện nhỏ nhất:")
    for kh in P.tim_khach_hang_loai_ho_san_xuat_co_tien_dien_nho_nhat():
        print(kh)