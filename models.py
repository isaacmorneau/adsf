from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Enum,
    ForeignKey,
)
from sqlalchemy.sql import func

metadata = MetaData()

book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("isbn", String, nullable=False),
    Column("title", String),
    Column("description", Text),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column(
        "updated_at",
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    ),
)

#for tagged boxes/shelves

# location = Table(
#     "location",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("barcode", String, nullable=False),
#     Column("description", String),
#     Column("created_at", DateTime(timezone=True), server_default=func.now()),
#     Column(
#         "updated_at",
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now(),
#     ),
# )
