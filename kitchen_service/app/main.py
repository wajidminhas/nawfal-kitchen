from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from app.database import create_db_table, get_session
from app.model import Dish
from sqlmodel import Session, select



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    create_db_table()
    yield
    print("Shutting down...")


app: FastAPI = FastAPI(lifespan=lifespan,
                       title="Kitchen Service",
                       description="A service for managing kitchen orders")

# Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Add a dish
@app.post("/dishes")
async def add_dish(dish: Dish, session: Session = Depends(get_session)):
    session.add(dish)
    session.commit()
    return {"message": "Dish added"}


# add a dish to the kitchen
@app.post("/kitchen")
async def add_dish_to_kitchen(dish: Dish, session: Session = Depends(get_session)):
    session.add(dish)
    session.commit()
    return {"message": "Dish added to kitchen"}

# add a single dish to the kitchen
@app.post("/kitchen/{dish_id}")
async def add_dish_to_kitchen(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = "cooking"
        session.commit()
        return {"message": "Dish added to kitchen"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")


# get all dishes
@app.get("/dishes")
async def get_all_dishes(session: Session = Depends(get_session)):
    dishes = session.exec(select(Dish)).all()
    return dishes

# get a single dish
@app.get("/dishes/{dish_id}")
async def get_dish(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        return dish
    else:
        raise HTTPException(status_code=404, detail="Dish not found")


# change the status of a dish
@app.put("/dishes/{dish_id}")
async def change_dish_status(dish_id: int, status: str, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = status
        session.commit()
        return {"message": "Dish status changed"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")

# dish is ready
@app.put("/dishes/{dish_id}/ready")
async def dish_is_ready(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = "ready"
        session.commit()
        return {"message": "Dish is ready"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")

# dish is still cooking
@app.put("/dishes/{dish_id}/cooking")
async def dish_is_still_cooking(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = "cooking"
        session.commit()
        return {"message": "Dish is still cooking"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")

# dish has delivered    
@app.put("/dishes/{dish_id}/delivered")
async def dish_has_delivered(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = "delivered"
        session.commit()
        return {"message": "Dish has delivered"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")

# get all dishes by status
@app.get("/dishes/status/{status}")
async def get_dishes_by_status(status: str, session: Session = Depends(get_session)):
    dishes = session.exec(select(Dish).where(Dish.status == status)).all()
    return dishes

# get all dishes by status and order by created at
@app.get("/dishes/status/{status}/order_by_created_at")
async def get_dishes_by_status_and_order_by_created_at(status: str, session: Session = Depends(get_session)):
    dishes = session.exec(select(Dish).where(Dish.status == status).order_by(Dish.created_at)).all()
    return dishes

# dish altered
@app.put("/dishes/{dish_id}/altered")
async def dish_altered(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = "altered"
        session.commit()
        return {"message": "Dish altered"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")

# dish is cancelled
@app.put("/dishes/{dish_id}/cancelled")
async def dish_cancelled(dish_id: int, session: Session = Depends(get_session)):
    dish = session.get(Dish, dish_id)
    if dish:
        dish.status = "cancelled"
        session.commit()
        return {"message": "Dish cancelled"}
    else:
        raise HTTPException(status_code=404, detail="Dish not found")
