# API Document

Tài liệu này được viết để các thành viên nắm bắt cách hoạt động của các module.

## __init__.py

- **Mô tả:** Đảm bảo rằng mọi thứ được khởi tạo và cấu hình đúng cách từ đầu.

## data_loader.py

- **Mô tả:** Module này được sử dụng để load dữ liệu và trả về dưới dạng tokenized.

## preprocess.py

- **Mô tả:** Tiền xử lý text để loại bỏ nhiễu và chuẩn hóa.

## vectorizer.py

- **Mô tả:** Chuyển đổi từ dữ liệu text thành dạng vector.


## model.py

- **Mô tả:** Chứa mô hình SVC và các hàm liên quan như fit, predict, các hàm metrics như accuracy, precision, recall, f1. 


## training.py

- **Mô tả:** Sử dụng để huấn luyện và tuning model, cung cấp các hàm evaluate để so sánh base vs best model.

## demo.py

- **Mô tả:** Trình bày hệ thống thông qua việc đưa ra dự đoán và biểu đồ. Có thể chạy **độc lập** không cần khởi chạy thông qua init.py

