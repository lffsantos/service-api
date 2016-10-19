[![Build Status](https://travis-ci.org/lffsantos/service-api.svg?branch=members)](https://travis-ci.org/lffsantos/service-api?branch=members)
[![Coverage Status](https://coveralls.io/repos/github/lffsantos/service-api/badge.svg?branch=members)](https://coveralls.io/github/lffsantos/service-api?branch=members)
[![Code Health](https://landscape.io/github/lffsantos/service-api/master/landscape.svg?style=flat)](https://landscape.io/github/lffsantos/service-api/master)


## Como desenvolver?

1. clone o respositório.
2. crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância .env
6. Execute os testes.

```console
git clone git@github.com:lffsantos/service-api.git service-api
cd service-api
python -m venv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
py.test
```

## API Service

Para visualizar a api basta rodar o projeto localmente

```console
cd service-api
source .virtualenv/bin/activate
python manage.py runserver
```

acesse a url [http://localhost:5000](http://localhost:5000) é possível visualizar a 
documentação Swagger UI gerada automaticamente  


## Serviços 

## Summary Service-API

- [Service-API Structure](#service-api-structure)
- [Events](#events)
- [Members](#members)
- [test](#test)

### Service-API Structure

service/

- Os serviços serão criados aqui  

ex:
 service/events  
 service/members  
 service/<name-service>  
 
service/util/  
 
- Módulos utilitários comuns a todos os serviços.   
 