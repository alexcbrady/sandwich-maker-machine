from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, recipes, sandwiches, order_details, resources
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

#RECIPES

@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipes: schemas.OrderCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipes=recipes)


@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipe(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.OrderUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)


@app.delete("/recipes/{recipes_id}", tags=["Recipes"])
def delete_one_order(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipes.delete(db=db, recipe_id=recipe_id)


#Sandwich


@app.post("/sandwiches/", response_model=schemas.Recipe, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.OrderCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwhich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwich(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich


@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Recipe, tags=["Sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.OrderUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, sandwhich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.update(db=db, sandwich=sandwich, sandwhich_id=sandwich_id)


@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_one_order(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)

#Resources

@app.post("/resources/", response_model=schemas.Recipe, tags=["Resources"])
def create_resource(resource: schemas.OrderCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Sandwich], tags=["Resources"])
def read_resource(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resource_id}", response_model=schemas.Sandwich, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resources/{resource_id}", response_model=schemas.Recipe, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.OrderUpdate, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)


@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_order(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resources.delete(db=db, resource_id=resource_id)


#Order_details


@app.post("/order_details/", response_model=schemas.Recipe, tags=["Order_details"])
def create_order_detail(order_detail: schemas.OrderCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_detail=order_details)


@app.get("/order_details/", response_model=list[schemas.Sandwich], tags=["Order_details"])
def read_order_detail(db: Session = Depends(get_db)):
    return order_details.read_all(db)


@app.get("/order_details/{order_details_id}", response_model=schemas.Sandwich, tags=["Order_details"])
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail


@app.put("/order_details/{order_details_id}", response_model=schemas.Recipe, tags=["Order_details"])
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.update(db=db, order_detail=order_detail, order_detail_id=order_detail_id)


@app.delete("/order_details/{order_details_id}", tags=["Order_details"])
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.delete(db=db, order_detail_id=order_detail_id)

