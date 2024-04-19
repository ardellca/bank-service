from pydantic import BaseModel
from typing import List, Optional


class BankIn(BaseModel):
    name: str
    description: str
    count_clients: int
    age: int
    clients_id: List[int]


class BankOut(BankIn):
    id: int


class CompanyUpdate(BankIn):
    name: Optional[str] = None
    description: Optional[str] = None
    count_clients: Optional[int] = None
    age: Optional[int] = None
    clients_id: Optional[List[int]] = None