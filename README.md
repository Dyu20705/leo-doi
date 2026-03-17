# LEO-DOI

Mô phỏng thuật toán **Hill Climbing** trên đồ thị có heuristic, hiển thị từng bước mở rộng trạng thái bằng **Tkinter**.

## 1) Mục tiêu dự án

- Đọc dữ liệu đồ thị từ file test.
- Chạy thuật toán leo đồi theo heuristic nhỏ nhất.
- Hiển thị bảng từng bước (`Current`, `Neighbors`, `L1`, `L`) trên giao diện Tkinter.
- Hiển thị luôn `Path` (thứ tự mở rộng node) và trạng thái đạt đích.

## 2) Cấu trúc thư mục

```text
leo-doi/
├─ main.py          # Điểm chạy chính
├─ parser.py        # Đọc file test -> start, goal, graph
├─ search.py        # Thuật toán hill climbing
├─ gui.py           # Hiển thị bảng bằng Tkinter
├─ test/
│  ├─ test1.txt
│  ├─ test2.txt
│  ├─ test3.txt
│  ├─ test4.txt
│  └─ test5.txt
└─ README.md
```

## 3) Yêu cầu môi trường

- Windows/Linux/macOS
- Python 3.10+ (khuyến nghị 3.14 theo môi trường hiện tại)
- Tkinter (thường có sẵn trong Python chuẩn)

## 4) Cách chạy

Tại thư mục gốc dự án, chạy một trong hai lệnh:

```bash
py src/main.py
```

hoặc

```bash
python src/main.py
```

Sau đó nhập số test khi được hỏi:

```text
Test number: 1
```

## 5) Định dạng file test

Mỗi file test có cấu trúc:

```text
<START>
<GOAL>

<NODE> <HEURISTIC> <NEIGHBOR_1> <NEIGHBOR_2> ...
...
```

Ví dụ:

```text
A
B

A 20 C D E
C 15 F
...
```

## 6) Output

- Cửa sổ Tkinter gồm:
 `Path`: chuỗi node đã mở rộng (ví dụ: `A -> D -> E -> G -> B`)
 `Trạng thái`: đã tới đích hoặc không tới được đích
 Bảng chi tiết từng bước của thuật toán
- Console in thêm:

```text
Path: A -> D -> E -> G -> B
```

## 7) Lỗi thường gặp

### `'python' is not recognized ...`

- Dùng `py src/main.py` trên Windows.
- Hoặc cài Python và thêm vào PATH.

### `KeyError` khi truy cập graph

- Kiểm tra node kề trong file test có được định nghĩa đầy đủ hay chưa.
- Đảm bảo đúng format: `NODE HEURISTIC [DANH SÁCH KỀ]`.

## 8) Gợi ý phát triển tiếp

- Thêm chế độ lưu ảnh/chụp bảng kết quả.
- Thêm nhiều chiến lược tìm kiếm để so sánh (Greedy, A*, BFS...).
- Thêm test tự động để kiểm tra path cho từng bộ dữ liệu.
