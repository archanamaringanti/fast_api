
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import create_connection, create_employee, get_employees, get_employee_by_id, update_employee, delete_employee

app = FastAPI()
connection = create_connection()

class Employee(BaseModel):
    name: str
    sal: float
    role: str

@app.post("/employees/")
def api_create_student(employee: Employee):
    create_employee(connection, employee.name, employee.sal, employee.role)
    return {"message": "Employee created successfully"}

@app.get("/employees/")
def api_get_employees():
    employees = get_employees(connection)
    return employees

@app.get("/employees/{employee_id}")
def api_get_employee(employee_id: int):
    employee = get_employee_by_id(connection, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.put("/employees/{employee_id}")
def api_update_employee(employee_id: int, employee: Employee):
    update_employee(connection, employee_id, employee.name, employee.sal, employee.role)
    return {"message": "Employee updated successfully"}

@app.delete("/employees/{employee_id}")
def api_delete_student(employee_id: int):
    delete_employee(connection, employee_id)
    return {"message": "Employee deleted successfully"}
