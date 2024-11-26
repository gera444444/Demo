from datetime import datetime
from fastapi import FastAPI


class Order:
    def __init__(self, number, view, model, description, client, phone, status, day, month, year):
        self.number =  number
        self.view = view
        self.model = model
        self.description = description
        self.client = client
        self.phone = phone
        self.status = status
        self.startDate = datetime(year,month,day)
        self.endDate = None
        

from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

repo = [
Order(1, "обработка", "х913", "нет", "да", "89002011445", "завершена", 30,11,2025),
Order(2, "тестировка", "х923", "да", "нет", "89002837482", "новая заявка", 21,10,2025)            
] 

for o in repo:
    o.endDate = datetime.now()
    o.status = "завершена"
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

isupdatedStatus = False
massage = ""
#отображение списка заявок
@app.get("/")
def get_orders():
    global isupdatedStatus
    global massage
    if(isupdatedStatus):
        buffer = massage
        isupdatedStatus = False
        massage = ""
        return repo, buffer
    else:  
        return repo


@app.post("/")
def create_order(data = Body()):
    order = Order(
          data["number"],
          data["day"],
          data["month"], 
          data["year"],
          data["view"],
          data["model"],
          data["description"],
          data["client"],
          data["phone"],
          data["status"]
    )
    repo.append(order)
    return order
