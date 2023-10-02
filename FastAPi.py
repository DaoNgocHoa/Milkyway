from fastapi import FastAPI
import Topics
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Summary import Return_summary
from TestAPI import process_data
from Topics import return_topic
app = FastAPI()

# Tạo một lớp Pydantic để đại diện cho dữ liệu đầu vào
class DataItem(BaseModel):
    data: str

# Định nghĩa endpoint POST để nhận dữ liệu và phân tích nó
@app.post("/analyze/")
async def analyze_data(data_item: DataItem):

        topic = return_topic()
        summary = Return_summary()
        # Trả về kết quả phân tích
        return {
            "summarized": summary,  # Gọi hàm để lấy tóm tắt
            "topics": topic  # Gọi hàm để lấy chủ đề
        }
    


@app.post("/upload/")
async def Upload_file(Upload_data: DataItem):

        result =   process_data(Upload_data.data)

        # Trả về kết quả
        return {"result": result}
# Mở thực thi ứng dụng FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)