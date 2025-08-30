from sqlalchemy.orm import Session
from MyDB.db_models import User, Order, Product, OrderStatusEnum


def create_user(db: Session, telegram_id: int, username: str):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if user:
        user.username = username
    else:
        user = User(telegram_id=telegram_id, username=username)
        db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_order(db: Session, user_id: int, items: list, total: float):
    order = Order(user_id=user_id, items=items, total=total)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_all_orders(db: Session):
    return db.query(Order).join(User).order_by(Order.created_at.desc()).all()


def update_order_status(db: Session, order_id: int, status: OrderStatusEnum):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order
