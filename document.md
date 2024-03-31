# API Document

Tài liệu này được viết để các thành viên nắm bắt cách hoạt động của các module.

## __init__.py

- **Mô tả:** Đảm bảo rằng mọi thứ được khởi tạo và cấu hình đúng cách từ đầu.
- **Input:** Không có tham số đầu vào cần được chỉ định trong tài liệu, vì đây là quy trình khởi tạo và cấu hình ban đầu.
- **Output:** Không có đầu ra cụ thể, nhưng cần đảm bảo rằng mọi thứ đã được khởi tạo và cấu hình đúng cách từ đầu.

## data_loader.py

### Mô tả
Module này được sử dụng để load dữ liệu từ các file CSV vào chương trình.

**`clean_n_tokenize_data`**
   - Mô tả: Hàm này được sử dụng để làm sạch và mã hóa văn bản đầu vào.
   - Input:
     - `sent` (str): Văn bản đầu vào cần xử lý.
     - `w2v`: Mô hình Word2Vec để mã hóa.
   - Output:
     - `tokenized_sent` (list): Biểu diễn đã mã hóa của văn bản đầu vào.

**`read_data_from_csv`**
   - Mô tả: Hàm này đọc dữ liệu từ các file CSV.
   - Input: Không có tham số truyền vào.
   - Output:
     - `train` (DataFrame): Dữ liệu huấn luyện.
     - `val` (DataFrame): Dữ liệu validation.
     - `test` (DataFrame): Dữ liệu kiểm tra.

**`load_data`**
   - Mô tả: Hàm này tải và tiền xử lý dữ liệu.
   - Input:
     - `data` (DataFrame): Dữ liệu đầu vào chứa cột 'Comments'.
     - `w2v`: Mô hình Word2Vec để mã hóa.
   - Output:
     - `tokenized_reviews` (ndarray): Các đánh giá đã được mã hóa.
     - `labels` (DataFrame): Nhãn liên quan đến các đánh giá.

## preprocess.py

### Mô tả
Tiền xử lý dữ liệu để loại bỏ nhiễu và chuẩn hóa.

**`text_preprocess`**
   - Mô tả: Hàm này được sử dụng để làm sạch văn bản đầu vào.
   - Input:
     - `text` (str): Văn bản đầu vào cần xử lý.
   - Output:
     - `text` (str): Văn bản đầu vào đã được xử lý.

## vectorizer.py

- **Mô tả:** Chuyển đổi từ dữ liệu văn bản thành dạng số học.


## model.py

- **Mô tả:** Tạo và huấn luyện các mô hình.


## training.py

- **Mô tả:** Sử dụng dữ liệu và mô hình để huấn luyện.

## demo.py

- **Mô tả:** Trình bày hệ thống thông qua việc đưa ra dự đoán và biểu đồ.
- **Input:** Một câu hoặc một đoạn văn bản cần được dự đoán.
- **Output:** Các biểu đồ hoặc biểu diễn đầu ra của mô hình dưới dạng xác suất, có thể được trình bày cho người dùng.
