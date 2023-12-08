from fastapi import FastAPI
import schemas
import requests
from bs4 import BeautifulSoup


app = FastAPI()



params = {
    'eID': 'rsm_personal_programme_requirements_search',
}

json_data = {
    'country': '528',
    'programme': 'MBUINMA',
}


 
 
@app.get('/')
def index():
    return "Hi there, you're on the main page. Please select a subdomain, or don't. Boeit niet"
 

@app.get('/bim')
def index():
    response = requests.post('https://www.rsm.nl/', params=params, json=json_data)
    soup = BeautifulSoup(response.json()['content'])
    aanmeldingen = int([x.text for x in soup.find_all("li") if 'Current number of applications' in x.text][0].split(': ')[1]) 
    
    
    return {'BIM Aanmeldingen':aanmeldingen, 'Procentueel':f'{int(aanmeldingen/245 * 100)} %'} 
 
 
 
def fibonacci_of(n):
    return n if n in {0, 1} else fibonacci_of(n - 1) + fibonacci_of(n - 2)
 
@app.get('/fib/{k}')
def fibo(k):
    k = int(k)
    return {'data':[fibonacci_of(n) for n in range(k)]}
     
 

 
 
# Ik was bij 1:22 



