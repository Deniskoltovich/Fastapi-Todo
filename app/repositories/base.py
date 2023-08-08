from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _create(self, instance):
        self.session.add(instance)
        await self.session.flush()
        return instance

    async def _get(self, model_cls, primary_key):
        result = await self.session.execute(
            select(model_cls).filter_by(id=primary_key)
        )
        return result.scalar()

    async def _get_all(self, model_cls):
        result = await self.session.execute(select(model_cls))
        return result.scalars().all()

    async def _update(self, model_csl, instance, values: dict):
        query = (
            update(model_csl)
            .where(model_csl.id == instance.id)
            .values(**values)
        )
        result = await self.session.execute(query)
        await self.session.flush()
        return result

    async def delete(self, instance):
        await self.session.delete(instance)
        await self.session.flush()
