import os
import httpx

CAST_SERVICE_HOST_URL = 'http://localhost:8020/api/v1/clients/'

def is_clients_present(client_id: int):
    return True