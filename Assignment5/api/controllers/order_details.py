from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, sandwich):
    # Create a new instance of the Sandwich model with the provided data
    db_order_details = models.Sandwich(
        amount=sandwich.amount,
    )
    # Add the newly created Sandwich object to the database session
    db.add(db_order_details)
    # Commit the changes to the database
    db.commit()
    # Refresh the Sandwich object to ensure it reflects the current state in the database
    db.refresh(db_order_details)
    # Return the newly created Sandwich object
    return db_order_details

def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_detail):
    # Query the database for the specific Sandwich to update
    db_order_detail = db.query(models.Sandwich).filter(models.Sandwich.id == order_detail_id)
    # Extract the update data from the provided 'Sandwich' object
    update_data = order_detail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order_detail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_order_detail.first()

def delete(db: Session, order_detail_id):
    # Query the database for the specific order to delete
    db_order = db.query(models.OrderDetail).filter(models.Sandwich.id == order_detail_id)
    # Delete the database record without synchronizing the session
    db_order.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)



