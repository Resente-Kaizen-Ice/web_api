from fastapi import HTTPException, APIRouter
from database_connector import get_connector
from models import Register, Login, UpdateUser
from typing import List, Optional
from mysql.connector import Error

# create router
router = APIRouter()


@router.get("/api/v1/get_all")
async def get_all_user():
    conn = get_connector()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM users"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        raise HTTPException(status_code=404, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.post("/api/v1/register")
async def register_user(register: Register):
    conn = get_connector()
    cursor = conn.cursor()
    try:

        insert_account_query = """INSERT INTO account(email, password) VALUES(%s,%s)"""
        cursor.execute(insert_account_query, (register.email, register.password))
        conn.commit()

        account_id = cursor.lastrowid
        insert_user_query = """INSERT INTO users(account_id,first_name, middle_name, last_name, nickname) VALUES(%s,%s,%s,%s,%s)"""
        cursor.execute(
            insert_user_query,
            (
                account_id,
                register.first_name,
                register.middle_name,
                register.last_name,
                register.nickname,
            ),
        )
        conn.commit()
        return {"message": "register successfully!"}
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
        cursor.close()


@router.post("/api/v1/login")
async def user_login(login: Login):
    conn = get_connector()
    cursor = conn.cursor()
    try:
        account_exist_query = "SELECT id FROM account WHERE email = %s"
        cursor.execute(account_exist_query, (login.email,))
        result = cursor.fetchone()
        if result:
            return {"message": "login successfully!"}
        else:
            raise HTTPException(status_code=404, detail="account not found")
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
        cursor.close()


@router.put("/api/v1/{id}")
async def update_user(id: int, update: UpdateUser):
    conn = get_connector()
    cursor = conn.cursor()
    try:
        update_account_query = (
            "UPDATE account SET email = %s, password =%s WHERE id = %s"
        )
        cursor.execute(update_account_query, (update.email, update.password, id))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        update_user_query = "UPDATE users SET first_name = %s, middle_name = %s, last_name = %s, nickname = %s WHERE account_id = %s"
        cursor.execute(
            update_user_query,
            (
                update.first_name,
                update.middle_name,
                update.last_name,
                update.nickname,
                id,
            ),
        )
        conn.commit()
        return {"message": "user update successfully!"}
    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
        cursor.close()
