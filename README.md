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


## Summary Service-API

- [Service-API Structure](#service-api-structure)
- [Events](#events)
- [Members](#members)
    - [Exceptions](#exceptions)
- [Test](#Test)

### Service-API Structure

service/  
service/{name-of-service} 
  * ex:  
*    service/events
	 *   model  
	 *   views    
*    service/members  
	 *   model  
	 *   views  
        
service/util  
  - Módulos utilitários comuns a todos os serviços.  


##Events

### EventsMeetup:  

* **Route**: /events_meetup  
* **Method**: GET  
* **Description**: retorna os meetups recebidos por parâmetro
* **Parameters**:  
``` 
{  
     groups_meetup="['nome-do-grupo']"
}  
```
* **Return**: ```{"html": "html"}, 200```   


##Members

### MemberList
 
**Route**: /members 
  
----  

* **Method**: GET  
    * **Description**: Retorna a lista de membros filtrando pelos parâmetros, mas se receber
email, filtra somente pelo email.
    * **Parameters**:  
    ``` 
    {   
        course_ids=[int, int, ...] opcional
        education_ids=[int, int, ...] opcional
        visa_ids=[int, int, ...] opcional
        occupation_ids=[int, int, ...] opcional
        technology_ids=[int, int, ...] opcional
        gender_ids=[int, int, ...] opcional
        experience_ids=[int, int, ...] opcional
        email=<string> opcional
    }  
    ```
    * **Return**: ```{"members":  [lista de membros]}, 200```   
    * **Raises**:  
        * [MemberNotFound](#membernotfound)  
   
* **Method**: POST  
    * **Description**: realiza o cadastro de um novo membro no grupo.
    * **Parameters**:  
    ``` 
    {
	    "gender_id": <int> 
	    "full_name": <string> 
	    "short_name": <string> 
        "email": <string>
        "experience_time_id":<int> 
        "about":<string> optcional
        "birth": <string> opcional
        "phone": <string> opcional, 
        "github":<string>  
        "linkedin":<string>   
        "visa_id": <int>  
        "education_id": <int>  
        "occupation_area_id": <int>   
        "course_id": <int>  
        "technologies": [int, int, ..] 
        "is_working": (true or false or null) opcional
    }
    ```
    * **Return**: ```member, 201```   
    * **Raises**:  
        * [InvalidArgument](#invalidargument)    
        * [InvalidValueError](#invalidvalueerror)     
        * [MemberAlreadyExists](#memberalreadyexists)  
  
  
### MemberItem
 No Yet Implemented
 
 
### EducationList
 
**Route**: /educations

----
* **Method**: GET  
    *   **Description**: Retorna a lista de tipos de Educação
    *   **Return**: ```{"Education":  [lista de educations]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra um novo tipo de educação
    *   **Parameters**:  
    ``` 
    {
	"level": <string>
    }
    ```
    *   **Return**: ```{"id": id, "level": <string>}, 201```   
    *   **Raises**:  
          * [InvalidArgument](#invalidargument)    
          * [InvalidValueError](#invalidvalueerror)     
          * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
  

### EducationItem

**Route**: /educations/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna a educação pelo ID
* **Return**: ```{"id": id, "level": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound](#auxmodelnotfound)
  

### CourseList
 
**Route**: /courses

----
* **Method**: GET  
    *   **Description**: Retorna a lista de Cursos
    *   **Return**: ```{"Course":  [lista de cursos]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra um novo Curso
    *   **Parameters**:  
    ``` 
    {
	"name": <string>
    }
    ```
    *   **Return**: ```{"id": id, "name": <string>}, 201```   
    *   **Raises**:  
          * [InvalidArgument](#invalidargument)    
          * [InvalidValueError](#invalidvalueerror)     
          * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
  

### CourseItem

**Route**: /courses/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna  curso pelo ID
* **Return**: ```{"id": id, "name": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound]
    

### VisaList
 
**Route**: /visas

----
* **Method**: GET  
    *   **Description**: Retorna a lista de Vistos
    *   **Return**: ```{"Visa":  [lista de vistos]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra um novo Visto
    *   **Parameters**:  
    ``` 
    {
	"name": <string>
	"description": <string> opcional
    }
    ```
    *   **Return**: ```{"id": id, "name": <string>, "description": <string>}, 201```   
    *   **Raises**:  
          * [InvalidArgument](#invalidargument)    
          * [InvalidValueError](#invalidvalueerror)     
          * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
          

### VisaItem

**Route**: /visas/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna o visto pelo ID
* **Return**: ```{"id": id, "name": <string>, "desctiption": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound]


### OccupationAreaList
 
**Route**: /occupations

----
* **Method**: GET  
    *   **Description**: Retorna a lista de Ocupações
    *   **Return**: ```{"Occupation":  [lista de ocupações]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra uma nova Ocupação
    *   **Parameters**:  
    ``` 
    {
	"name": <string>
    }
    ```
    *   **Return**: ```{"id": id, "name": <string>}, 201```   
    *   **Raises**:  
        * [InvalidArgument](#invalidargument)    
        * [InvalidValueError](#invalidvalueerror)     
        * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
  

### OccupationAreaItem

**Route**: /occupations/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna a ocupação pelo ID
* **Return**: ```{"id": id, "name": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound](#auxmodelnotfound)


### TechnologyList
 
**Route**: /technologies

----
* **Method**: GET  
    *   **Description**: Retorna a lista de Tecnologias
    *   **Return**: ```{"Technologies":  [lista de tecnologias]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra uma nova Technologia
    *   **Parameters**:  
    ``` 
    {
	"name": <string>
    }
    ```
    *   **Return**: ```{"id": id, "name": <string>}, 201```   
    *   **Raises**:  
          * [InvalidArgument](#invalidargument)    
          * [InvalidValueError](#invalidvalueerror)     
          * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
  

### TechnologyItem

**Route**: /technologies/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna a technologia pelo ID
* **Return**: ```{"id": id, "name": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound](#auxnotfound)


### GenderList
 
**Route**: /genders

----
* **Method**: GET  
    *   **Description**: Retorna a lista de genêros
    *   **Return**: ```{"Gender":  [lista de gender]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra um novo Genêro
    *   **Parameters**:  
    ``` 
    {
	"name": <string>
    }
    ```
    *   **Return**: ```{"id": id, "name": <string>}, 201```   
    *   **Raises**:  
          * [InvalidArgument](#invalidargument)    
          * [InvalidValueError](#invalidvalueerror)     
          * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
  

### GenderItem

**Route**: /genders/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna o genêro pelo ID
* **Return**: ```{"id": id, "name": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound](#auxmodelnotfound)


### ExperienceTimeList
 
**Route**: /experiences

----
* **Method**: GET  
    *   **Description**: Retorna a lista de tempo de experiência
    *   **Return**: ```{"ExperienceTime":  [lista de tempo de experiencia]}, 200```   


* **Method**: POST  
    *   **Description**: Cadastra um novo tempo de experiência
    *   **Parameters**:  
    ``` 
    {
	"name": <string>
    }
    ```
    *   **Return**: ```{"id": id, "name": <string>}, 201```   
    *   **Raises**:  
          * [InvalidArgument](#invalidargument)    
          * [InvalidValueError](#invalidvalueerror)     
          * [AuxModelAlreadyExists](#auxmodelalreadyexists)     
  

### ExperienceTimeItem

**Route**: /experiences/\<int:obj_id>

----

* **Method**: GET  
* **Description**: Retorna o tempo de experiência pelo ID
* **Return**: ```{"id": id, "name": <string>}, 200```  
* **Raises**:  
    * [AuxModelNotFound](#auxmodelnotfound)



## Exceptions

### InvalidArgument - 400

``` {
  "message": "",
  "field_name": "<invalid_field>",
  "error": "InvalidValueArgument"
} ```

### InvalidValueError - 400

``` {
  "field_value": <field_value>,
  "field_name": "<field_name>",
  "error": "InvalidValueError",
  "message": "Invalid column '<field_name>' ; value was '<value>' but expected '<type>'"
} ```

### AuxModelAlreadyExists - 409

``` {
  "field_value": "<value>",
  "message": "",
  "error": "<MODEL>AlreadyExists",
  "field_key": "<field_name>"
} ```

### AuxModelNotFound - 404

``` {
  "field_value": <value>,
  "message": "",
  "error": "<MODEL>NotFound",
  "field_key": "id"
}```

### MemberNotFound - 404

``` {
  "field_value": <value>,
  "message": "",
  "error": "<MODEL>NotFound",
  "field_key": "id"
}```

### MemberAlreadyExists - 409

``` {
  "message": "",
  "field_key": "email",
  "error": "MemberAlreadyExists",
  "field_value": "<email>"
}```



