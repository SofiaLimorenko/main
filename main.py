from fastapi import FastAPI
import requests
app = FastAPI()
@app.get('/get_data')
async def get_data():
    source_url ='https://github.com/SofiaLimorenko/api'
    response = requests.get(source_url)
    if response.status_code == 200:
        data = response.json()
        coordinates = data.get('coordinates')
    destination_url = 'https://github.com/SofiaLimorenko/android'
    response = requests.post(destination_url, json={'coordinates': coordinates})
