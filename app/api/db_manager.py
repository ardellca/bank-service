from app.api.models import BankIn, BankOut,BankUpdate
from app.api.db import banks, database


async def add_(payload: BankIn):
    query = banks.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_banks():
    query = banks.select()
    return await database.fetch_all(query=query)


async def get_bank(id):
    query = banks.select(banks.c.id == id)
    return await database.fetch_one(query=query)


async def delete_bank(id: int):
    query = banks.delete().where(banks.c.id == id)
    return await database.execute(query=query)


async def update_bank(id: int, payload: BankIn):
    query = (
        banks
        .update()
        .where(banks.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
