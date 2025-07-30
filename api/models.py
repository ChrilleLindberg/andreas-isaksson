from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class Notice(Base):
    __tablename__ = "notices"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

class FileText(Base):
    __tablename__ = "file_texts"

    id = Column(Integer, primary_key=True)
    notice_id = Column(Integer, ForeignKey("notices.id"), nullable=False)
    content = Column(Text, nullable=False)

    notice = relationship("Notice", backref="files")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    embedding = Column(Vector(384))
