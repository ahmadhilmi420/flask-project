# Flask Project

This is a simple Flask project that demonstrates how to create a web application using Flask.

## Installation

To install the project, run the following command in your terminal:

## how to build and run in docker

### BUILD
```bash
docker build -t flask-project:latest .
```

### RUN
```bash
docker run -p 5000:8000 -it --rm --name flask-api flask-project:latest
```

## How to Run the Application

1. Ensure you are in the project directory.
2. Run the application:

   ```bash
    uv run flask --app main run --port 8000 --reload --debug
   ```

3. The API will be accessible at: `http://127.0.0.1:8000`

## API Endpoints

### Create a Task
- **Endpoint:** `api/v1/users`
- **Method:** POST

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/users" -Method Post -Body '{ "email": "adidadang.com", "password": "langitke
5", "first_name": "adi", "last_name": "dadang"}' -ContentType "application/json"
```

### Retrieve All Tasks
- **Endpoint:** `/api/v1/users`
- **Method:** GET

Example:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/users"  -Method Get
```

### Users Id
- **Endpoint:** `/users/<users_id>`
- **Method:** GET

Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/v1/users/4" -Method Get
```
```JSON
{
  "data": {
    "email": "ujangasep.com",
    "full_name": "ujang asep"
  },
  "success": true
}
```



