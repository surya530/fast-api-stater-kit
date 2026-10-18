from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# DATABASE_URL = "postgresql://neondb_owner:npg_TViI8PUZq2fw@ep-sparkling-boat-b5mdxqpc-pooler.c-7.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"



DATABASE_URL = (
    "postgresql+asyncpg://neondb_owner:npg_TViI8PUZq2fw"
    "@ep-sparkling-boat-b5mdxqpc-pooler.c-7.us-east-2.aws.neon.tech/"
    "neondb?ssl=require"
)


engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session