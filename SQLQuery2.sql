use QLSachThu4

--1. Cho biết danh sách các cuốn sách mà đã được cập nhật nhà xuất bản, Thông tin hiển thị gồm có masach, tensach, sotrang, ngayxb, tennxb 
select Sach.MaSach, Sach.TenSach, Sach.SoTrang,Sach.NgayXB, NhaXB.TenXB
from Sach inner join NhaXB on sach.MaXB = NhaXB.MaXB

--2. Cập nhật 2 nhân viên có mã số ‘0000000002’ và ‘0000000003’ có manvql là ‘0000000001’ 
update NhanVien set MaNVQL = '0000000001' where MaNV in ('0000000002','0000000003')
select * from NhanVien

--3. Cho biết những nhân viên nào chưa thực hiện xử lý đơn hàng bao giờ mà có tuổi lớn hơn 32
-- Thông tin hiển thị mã nhân viên, họ tên nhân viên, phái, tuoi
select distinct NhanVien.MaNV, NhanVien.HotenNV, NhanVien.GT, DATEDIFF(YEAR,NhanVien.NS,GETDATE()) as Tuoi
from DonDatHang right join NhanVien on DonDatHang.MaNV = NhanVien.MaNV
where DonDatHang.MaNV is null and DATEDIFF(YEAR,NhanVien.NS,GETDATE()) > 32

--4. Cho biết những khách hàng nào chưa đặt hàng bao giờ mà có email là ‘ueh.edu.vn’. Thông tin hiển thị mã kh, họ và tên khách hàng, phone, email
select KhachHang.MaKH, CONCAT(KhachHang.HoKH,' ',KhachHang.TenKH) as hovaten, KhachHang.Phone, KhachHang.Email
from KhachHang
where KhachHang.Email like '%ueh.edu.vn'
--5. Tính tổng thành tiền và tổng tiền giảm giá, tổng thu của từng hóa đơn 
select DonDatHang.SoDH, 
	sum(DonDatHang.TrangThaiDH * SoLuong * GiaTien) as TongThanhTien,
	sum(DonDatHang.TrangThaiDH * SoLuong * GiaTien * ChiTietDonHang.GiamGia) as GiamGia,
	(sum(DonDatHang.TrangThaiDH * SoLuong * GiaTien) - sum(DonDatHang.TrangThaiDH * SoLuong * GiaTien * ChiTietDonHang.GiamGia)) TongThu
from DonDatHang inner join ChiTietDonHang on DonDatHang.SoDH = ChiTietDonHang.SoDH
where DonDatHang.TrangThaiDH != 0 
group by DonDatHang.SoDH
--6. Cho biết những tác giả nào viết nhiều hơn 1 cuốn, thông tin hiển thị gồm tên tác giả, số lượng sách tác giả viết 
select TacGia.TenTG, count(*) as Dem
from TacGia inner join Sach_TacGia on TacGia.MaTG = Sach_TacGia.MaTG
group by TacGia.TenTG
having count(*) > 1
--7. Lập bảng dữ liệu tổng số lượng của sách trong mỗi hóa đơn 
declare @col NVARCHAR(MAX) = '';
declare @query7 NVARCHAR(MAX);
select @col += QUOTENAME(ChiTietDonHang.SoDH) + ','
from ChiTietDonHang
group by ChiTietDonHang.SoDH
order by ChiTietDonHang.SoDH
set @col = LEFT(@col,LEN(@col)-1);
print @col
set @query7 =
'select TenSach, '+@col+'
from
(select  Sach.TenSach, ChiTietDonHang.SoDH, ChiTietDonHang.SoLuong
from Sach inner join ChiTietDonHang on Sach.MaSach = ChiTietDonHang.MaSach) s1
pivot
(sum(SoLuong) for SoDH in ('+@col+')) as pivottable'
-- 8. Viết 1 hàm dạng trả về table đặt tên là TongDoanhThu 
select * from ChiTietDonHang

create function doanhthu
(	@quantity int,
	@price dec(10,2),
	@discount dec(10,2)
)
returns dec
as
begin
return @quantity*@price*(1-@discount);
end;
select sum(DonDatHang.TrangThaiDH * dbo.doanhthu(ChiTietDonHang.SoLuong,ChiTietDonHang.GiaTien,ChiTietDonHang.GiamGia)) as doanhthu
from ChiTietDonHang inner join DonDatHang on ChiTietDonHang.SoDH = DonDatHang.SoDH

select sum(dbo.doanhthu(ct.SoLuong,ct.GiaTien,ct.GiamGia)) as doanhthu
from ChiTietDonHang ct
--9.	Viết 1 thủ tục thêm dữ liệu cho bảng sách 
-- Mô tả là khi truyền vào @sodh thì kiểm tra sự tồn tại trong đơn đặt hàng nếu tồn tại thì xóa dữ liệu các bảng liên quan đến số đơn hàng đó, nếu không tồn tại thì thông báo không tồn tại
create procedure kiemtra4(@sodh nvarchar(max))
as
begin
	if exists (select * from DonDatHang where SoDH = @sodh)
	delete from DonDatHang where SoDH = @sodh
end
exec kiemtra4 002
select * from DonDatHang