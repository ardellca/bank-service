from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/banks/openapi.json", docs_url="/api/v1/banks/docs")

banks_router = APIRouter()

banks = [{'banks_id': 1,
          'name': 'Альфа-Банк',
          'description': 'Крупнейшее финансово-кредитное учреждение с универсальным подходом к ведению бизнеса',
          'count_clients': 10000,
          'age': 34},
         {'banks_id': 2,
          'name': 'ВТБ',
          'description': 'Крупнейший российский банк, предоставляющий полный спектр финансовых услуг для корпоративных и частных клиентов',
          'count_clients': 15000,
          'age': 30},
         {'banks_id': 3,
          'name': 'Ozon',
          'description': 'Ведущая мультикатегорийная платформа электронной коммерции и одна из крупнейших интернет-компаний в России',
          'count_clients': 'MarketPlace',
          'age': 26},
         {'banks_id': 4,
          'name': 'Apple',
          'description': 'Американская корпорация, разработчик персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения и цифрового контента',
          'count_clients': 'Electronic Device',
          'age': 47}]


@banks_router.get("/")
async def read_banks():
    return banks


@banks_router.get("/{banks_id}")
async def read_bank(banks_id: int):
    for bank in banks:
        if bank['banks_id'] == banks_id:
            return bank
    return None


app.include_router(banks_router, prefix='/api/v1/banks', tags=['banks'])

if __name__ == '__main__':
    import uvicorn
    import os
    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
