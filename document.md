# API Document

Tài liệu này được viết để các thành viên nắm bắt cách hoạt động của các module.

## __init__.py

- **Mô tả:** Đảm bảo rằng mọi thứ được khởi tạo và cấu hình đúng cách từ đầu.
- **Input:** Không có tham số đầu vào cần được chỉ định trong tài liệu, vì đây là quy trình khởi tạo và cấu hình ban đầu.
- **Output:** Không có đầu ra cụ thể, nhưng cần đảm bảo rằng mọi thứ đã được khởi tạo và cấu hình đúng cách từ đầu.

## data_loader.py

- **Mô tả:** Sử dụng module này để load dữ liệu từ các file csv vào chương trình.
- **Input:** Đường dẫn đến file Train.csv và Val.csv.
- **Output:** Hai đối tượng `train` và `val` có thể là pandas DataFrame hoặc pandas Series chứa dữ liệu từ các file csv tương ứng.

## preprocess.py

- **Mô tả:** Tiền xử lý dữ liệu để loại bỏ nhiễu và chuẩn hóa.
- **Input:** Một câu văn cần được tiền xử lý.
- **Output:** Một câu văn bản đã được xử lý để loại bỏ nhiễu và chuẩn hóa dữ liệu.

## vectorizer.py

- **Mô tả:** Chuyển đổi từ dữ liệu văn bản thành dạng số học.
- **Input:** Một từ.
- **Output:** Một vector số học biểu diễn cho từ.

## model.py

- **Mô tả:** Tạo và huấn luyện các mô hình.
- **Input:** Loại mô hình cần tạo và huấn luyện.
- **Output:** Một đối tượng mô hình đã được khởi tạo hoặc huấn luyện, sẵn sàng cho việc sử dụng.

## training.py

- **Mô tả:** Sử dụng dữ liệu và mô hình để huấn luyện.
- **Input:** Dữ liệu huấn luyện và mô hình đã được khởi tạo.
- **Output:** Các thông số đánh giá như accuracy, F1 score, precision của mô hình sau quá trình huấn luyện.

## metrics.py

- **Mô tả:** Sử dụng các hàm để đánh giá chất lượng của mô hình.
- **Input:** Không có đầu vào cụ thể, vì các hàm đánh giá được sử dụng cho việc đánh giá chất lượng mô hình.
- **Output:** Không có đầu ra cụ thể, nhưng cần đảm bảo rằng các hàm đánh giá được cung cấp đúng cách.

## demo.py

- **Mô tả:** Trình bày hệ thống thông qua việc đưa ra dự đoán và biểu đồ.
- **Input:** Một câu hoặc một đoạn văn bản cần được dự đoán.
- **Output:** Các biểu đồ hoặc biểu diễn đầu ra của mô hình dưới dạng xác suất, có thể được trình bày cho người dùng.
