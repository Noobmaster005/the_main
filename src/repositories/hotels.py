from sqlalchemy import select, func, delete
from repositories.base import BaseRepository
from models.hotels import HotelsOrm



class HotelsRepository(BaseRepository):
    model = HotelsOrm

    async def get_all(
            self,
            location,
            title,
            limit,
            offset,
                
    ):
        query = select(HotelsOrm)
        if location:
            query = query.filter(func.lower(HotelsOrm.location).contains(location.strip().lower()))
        if title:
            query = query.filter(func.lower(HotelsOrm.title).contains(title.strip().lower()))
            query = (
             query
            .limit(limit)
            .offset(offset)
        )
        print(query.compile(compile_kwargs={"literal_binds": True}))
        result = await self.session.execute(query)
        
        return result.scalars().all()
    

    async def delete_hotel(self, hotel_id: int):
        await super().delete_hotel(self.model, hotel_id)

    
    