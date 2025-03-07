from fastapi import FastAPI, HTTPException
from sqlmodel import Session
from model import Order, OrderItem
from database import engine, create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/orders/", response_model=Order)
def create_order(order: Order):
    with Session(engine) as session:
        session.add(order)
        session.commit()
        session.refresh(order)
        return order

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

@app.put("/orders/{order_id}/status", response_model=Order)
def update_order_status(order_id: int, status: str):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        order.status = status
        session.commit()
        session.refresh(order)
        return order

@app.post("/orders/{order_id}/items", response_model=OrderItem)
def add_order_item(order_id: int, item: OrderItem):
    with Session(engine) as session:
        item.order_id = order_id
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.delete("/orders/{order_id}/items/{item_id}")
def remove_order_item(order_id: int, item_id: int):
    with Session(engine) as session:
        item = session.get(OrderItem, item_id)
        if not item or item.order_id != order_id:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return {"message": "Item removed from order"}

@app.post("/orders/{order_id}/cancel", response_model=Order)
def cancel_order(order_id: int):
    with Session(engine) as session:
        order = session.get(Order, order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        order.status = "canceled"
        session.commit()
        session.refresh(order)
        return order