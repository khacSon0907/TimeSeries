# 5. Cycle — Chu kỳ dài hạn

## Định nghĩa

**Cycle** là dao động lên xuống theo chu kỳ, nhưng **không cố định** như seasonality. Đây là thành phần bị nhầm lẫn nhiều nhất với seasonality.

## Ví dụ thực tế

### Chu kỳ kinh tế
Nền kinh tế có xu hướng tăng trưởng, sau đó suy thoái, rồi lại tăng trưởng. Mỗi chu kỳ có thể kéo dài 5-10 năm, không cố định.

### Chu kỳ bất động sản
Giá bất động sản có giai đoạn tăng nóng, sau đó sụt giảm, rồi phục hồi. Thời gian mỗi chu kỳ không cố định.

### Chu kỳ công nghiệp
Sản xuất của một ngành công nghiệp có thể chu kỳ 3-7 năm, không lặp lại theo mô hình cố định như seasonality.

## Seasonality vs Cycle - So sánh chi tiết

| Tiêu chí | Seasonality | Cycle |
|---------|-------------|-------|
| **Có lặp lại không?** | Có | Có |
| **Chu kỳ có cố định không?** | Gần như cố định | Không cố định |
| **Theo lịch không?** | Có (hàng ngày, tuần, tháng, năm) | Không nhất thiết |
| **Thời gian chu kỳ** | Rõ ràng (1 năm, 1 tuần, v.v.) | Mơ hồ (có thể 5-10 năm) |
| **Ví dụ** | Tết, mùa hè, cuối tuần | Khủng hoảng kinh tế, chu kỳ bất động sản |
| **Dự báo** | Dễ, vì lặp lại đều | Khó, vì không biết khi nào chu kỳ thay đổi |

## Đặc điểm của Cycle

1. **Dài hạn**: Thường kéo dài từ vài năm đến hàng chục năm
2. **Không cố định**: Thời gian mỗi chu kỳ có thể khác nhau
3. **Phức tạp**: Do ảnh hưởng của nhiều yếu tố kinh tế, xã hội
4. **Thường do nước ngoài**: Có thể bị ảnh hưởng bởi chu kỳ kinh tế toàn cầu

## Cách nhận biết Cycle

1. **Biểu đồ dài hạn**: Nhìn dữ liệu 10+ năm để thấy chu kỳ
2. **Spectral Analysis**: Phân tích tần số để tìm chu kỳ
3. **ACF plot**: Có spike nhưng không định kỳ như seasonality
4. **Domain Knowledge**: Hiểu biết về ngành để nhận diện chu kỳ

## Tại sao cần biết Cycle?

- **Dự báo dài hạn**: Hiểu chu kỳ giúp dự báo được tương lai xa
- **Đầu tư**: Nhà đầu tư cần hiểu chu kỳ để quyết định thời điểm mua/bán
- **Lập kế hoạch chiến lược**: Doanh nghiệp cần lên kế hoạch dài hạn dựa vào chu kỳ
- **Phân biệt với Seasonality**: Lỗi này khiến mô hình dự báo sai lệch lớn
