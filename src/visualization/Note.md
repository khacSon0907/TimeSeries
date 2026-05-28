Load data 
    Xong rồi kiểm tra xem nó có null không , nếu có thì sẽ điền vào bằng giá trị trung bình của cột đó ,
Nếu nhìn line chart mà không thấy trend rõ ràng, thì chưa kết luận vội là “không có trend” nha. Có 3 khả năng chính:    

    1. Thật sự không có trend
2. Có trend nhưng bị noise che mất
3. Có trend ngắn hạn / dài hạn nhưng nhìn bằng mắt chưa rõ


1. Vẽ thêm rolling mean để làm mượt dữ liệu
Rolling mean giúp giảm noise để nhìn xu hướng rõ hơn. Nếu rolling mean có xu hướng tăng thì có thể kết luận là có trend tăng, nếu rolling mean có xu hướng giảm thì có thể kết luận là có trend giảm. Nếu rolling mean vẫn không thấy xu hướng rõ ràng thì có thể kết luận là không có trend.

Exponential Moving Average — EMA

Sau rolling mean, kỹ thuật smoothing tiếp theo rất hay dùng là:

Exponential Moving Average, gọi tắt là EMA.

Rolling mean tính trung bình đều cho các điểm trong window.

𝐸
𝑀
𝐴
𝑡
=
𝛼
𝑦
𝑡
+
(
1
−
𝛼
)
𝐸
𝑀
𝐴
𝑡
−
1
EMAt​=αyt​+(1−α)EMAt−1​