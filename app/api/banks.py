from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import BankOut, BankIn, BankUpdate
from app.api import db_manager
from app.api.service import is_clients_present

bank = APIRouter()

@bank.post('/', response_model=BankIn, status_code=201)
async def create_bank(payload: BankIn):
    for clients_id in payload.clients_id:
        if not is_clients_present(clients_id):
            raise HTTPException(status_code=404, detail=f"Client with given id:{clients_id} not found")

    bank_id = await db_manager.add_bank(payload)
    response = {
        'id': bank_id,
        **payload.dict()
    }

    return response

@bank.get('/', response_model=List[BankOut])
async def get_banks():
    return await db_manager.get_all_banks()

@bank.get('/{id}/', response_model=BankOut)
async def get_bank(id: int):
    bank = await db_manager.get_bank(id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    return bank

@bank.put('/{id}/', response_model=BankOut)
async def update_bank(id: int, payload: BankUpdate):
    bank = await db_manager.get_bank(id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    update_data = payload.dict(exclude_unset=True)

    if 'clients_id' in update_data:
        for clients_id in payload.clients_id:
            if not is_clients_present(clients_id):
                raise HTTPException(status_code=404, detail=f"Clint with given id:{clients_id} not found")

    bank_in_db = BankIn(**bank)

    updated_bank = bank_in_db.copy(update=update_data)

    return await db_manager.update_bank(id, updated_bank)

@bank.delete('/{id}/', response_model=None)
async def delete_bank(id: int):
    bank = await db_manager.get_bank(id)
    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")
    return await db_manager.delete_bank(id)