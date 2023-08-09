from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from config.config import settings

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)
Base = declarative_base()
