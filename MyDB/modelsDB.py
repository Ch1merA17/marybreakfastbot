from sqlalchemy import Column, Integer, String, BigInteger, TIMESTAMP, Enum, JSON, DECIMAL, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from MyDB.mydatabase import Base
import enum
from datetime import datetime


class OrderStatusEnum(enum.Enum):
    new = "new"
    preparing = "preparing"
    ready = "ready"
    delivered = "delivered"
    canceled = "canceled"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    items = Column(JSON, nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.new)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    user = relationship("User", back_populates="orders")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    category = Column(String(100))
    image_url = Column(String(500))
    is_available = Column(Boolean, default=True)
