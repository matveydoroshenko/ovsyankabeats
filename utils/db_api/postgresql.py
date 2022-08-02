import contextlib
import asyncpg
from typing import Optional, AsyncIterator
from data import config


class Database:

    def __init__(self):
        self._pool: Optional[asyncpg.Pool] = None

    async def create_table_balance(self):
        sql = """
        CREATE TABLE IF NOT EXISTS balance (
        gem_amount BIGINT,
        user_id BIGINT UNIQUE
        );"""
        await self.execute(sql, execute=True)

    async def create_table_homework(self):

        sql = """CREATE TABLE IF NOT EXISTS homework (
        number SERIAL PRIMARY KEY,
        photo VARCHAR(255) NULL,
        file VARCHAR(255) NULL,
        text VARCHAR(255) NULL,
        video VARCHAR(255) NULL
        );"""
        await self.execute(sql, execute=True)

    async def create_table_products(self):
        sql = """CREATE TABLE IF NOT EXISTS products (
                number SERIAL PRIMARY KEY,
                photo VARCHAR(255) NULL,
                video VARCHAR(255) NULL,
                file VARCHAR(255) NULL,
                title VARCHAR(255) NULL,
                description VARCHAR(255) NULL,
                price VARCHAR(255) NULL
                );"""
        await self.execute(sql, execute=True)

    async def create_table_user_files(self):
        sql = """CREATE TABLE IF NOT EXISTS user_files (
                 user_id BIGINT UNIQUE,
                 file VARCHAR(255) NULL
                 );"""
        await self.execute(sql, execute=True)

    async def create_table_user_respond(self):
        sql = """CREATE TABLE IF NOT EXISTS user_respond (
                user_id BIGINT UNIQUE,
                file VARCHAR(255) NULL,
                content_type VARCHAR(255) NULL,
                text VARCHAR(255) NULL
                );"""
        await self.execute(sql, execute=True)

    async def create_table_users(self):
        sql = """CREATE TABLE IF NOT EXISTS users (
                 user_id BIGINT UNIQUE,
                 name VARCHAR(255) NULL,
                 username VARCHAR(255) NULL,
                 date VARCHAR(255) NULL
                    );"""
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id, name, username, date):
        sql = "INSERT INTO users (user_id, name, username, date) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, user_id, name, username, date, fetchrow=True)

    async def add_user_files(self, user_id, file):
        sql = "INSERT INTO user_files (user_id, file) VALUES($1, $2) returning *"
        return await self.execute(sql, user_id, file, fetchrow=True)

    async def add_user_balance(self, user_id, gem_amount):
        sql = "INSERT INTO balance (user_id, gem_amount) VALUES($1, $2) returning *"
        return await self.execute(sql, user_id, gem_amount, fetchrow=True)

    async def add_task(self, photo, file, text, video):
        sql = "INSERT INTO homework (photo, file, text, video) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, photo, file, text, video, fetchrow=True)

    async def add_user_respond(self, user_id, content_type, file, text):
        sql = "INSERT INTO user_respond (user_id, content_type, file, text) VALUES($1, $2, $3, $4) returning *"
        return await self.execute(sql, user_id, content_type, file, text, fetchrow=True)

    async def add_product(self, photo, video, file, price, title, description):
        sql = "INSERT INTO products " \
              "(photo, video, file, price, title, description) " \
              "VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, photo, video, file, price, title, description, fetchrow=True)

    async def update_gem_amount(self, gem_amount, user_id):
        sql = "UPDATE balance SET gem_amount=$1 WHERE user_id=$2"
        return await self.execute(sql, gem_amount, user_id, execute=True)

    async def update_user_files(self, file, user_id):
        sql = "UPDATE user_files SET file=$1 WHERE user_id=$2"
        return await self.execute(sql, file, user_id, execute=True)

    async def select_all_products_title(self):
        sql = "SELECT title FROM products"
        return await self.execute(sql, fetch=True)

    async def select_all_users_responds(self):
        sql = "SELECT * FROM user_respond"
        return await self.execute(sql, fetch=True)

    async def select_product_file(self, **kwargs):
        sql = "SELECT file FROM products WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM users"
        return await self.execute(sql, fetch=True)

    async def select_all_users_id(self):
        sql = "SELECT user_id FROM users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_task(self, **kwargs):
        sql = "SELECT * FROM homework WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_gem_amount(self, **kwargs):
        sql = "SELECT gem_amount FROM balance WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_product(self, **kwargs):
        sql = "SELECT * FROM products WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_user_files(self, **kwargs):
        sql = "SELECT file FROM user_files WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users"
        return await self.execute(sql, fetchval=True)

    async def count_tasks(self):
        sql = "SELECT COUNT(*) FROM homework"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM users WHERE TRUE", execute=True)

    async def delete_respond(self, **kwargs):
        sql = "DELETE FROM user_respond WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE IF EXISTS users", execute=True)

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self._transaction() as connection:  # type: asyncpg.Connection
            if fetch:
                result = await connection.fetch(command, *args)
            elif fetchval:
                result = await connection.fetchval(command, *args)
            elif fetchrow:
                result = await connection.fetchrow(command, *args)
            elif execute:
                result = await connection.execute(command, *args)
        return result

    @contextlib.asynccontextmanager
    async def _transaction(self) -> AsyncIterator[asyncpg.Connection]:
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME,
            )
        async with self._pool.acquire() as conn:  # type: asyncpg.Connection
            async with conn.transaction():
                yield conn

    async def close(self) -> None:
        if self._pool is None:
            return None

        await self._pool.close()
