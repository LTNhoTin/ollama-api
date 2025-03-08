# Ollama Phi-4 API

Dự án này cung cấp một API đơn giản để giao tiếp với mô hình **Phi-4** thông qua **Ollama** và **FastAPI**. API cho phép gửi yêu cầu hội thoại và nhận phản hồi từ mô hình Phi-4 một cách nhanh chóng.

## Chuẩn Bị

### 1. Tải Model Phi-4

Nếu chưa có, hãy tải model Phi-4:

```sh
ollama pull phi4
```

Kiểm tra model đã tải:

```sh
ollama list
```

### 2. Chạy Server Ollama

Khởi động **Ollama**:

```sh
ollama serve
```

Lệnh này sẽ chạy Ollama trên `http://localhost:11434`.

## Chạy API Server

Cài đặt các thư viện cần thiết:

```sh
pip install fastapi uvicorn requests
```

Chạy API:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API sẽ hoạt động tại `http://localhost:8000`.

## Cách Sử Dụng API

### Kiểm Tra API Đang Hoạt Động

Dùng trình duyệt hoặc `curl`:

```sh
curl http://localhost:8000/
```

Phản hồi:

```json
{"message": "Ollama Phi-4 API is running!"}
```

### Gửi Yêu Cầu Chat

Sử dụng `curl` hoặc Postman:

```sh
curl -X POST "http://localhost:8000/chat/"      -H "Content-Type: application/json"      -d '{"prompt": "Xin chào, bạn là ai?", "stream": false}'
```

Phản hồi từ API (ví dụ):

```json
{
  "response": "Tôi là một AI chạy mô hình Phi-4!",
  "model": "phi4",
  "context": []
}
```

## Lưu Ý

- Cần chạy `ollama serve` trước khi gọi API.
- API hỗ trợ thử nghiệm trực tiếp tại `http://localhost:8000/docs`.
