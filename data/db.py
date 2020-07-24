from datetime import datetime

import aiosqlite as lite


data = 'data/data.db'


async def add_new_user(user_id, user_username, user_name):
    """Добавление нового пользователя в базу, присваивание ему стандартных настроек"""
    async with lite.connect(data) as con:
        cur = await con.cursor()
        await cur.execute("SELECT user_id FROM tbl_users WHERE user_id = ?", (user_id,))

        if not (user_id,) in await cur.fetchall():
            today = datetime.now()
            today = today.strftime("%d.%m.%Y")

            await cur.execute("INSERT INTO tbl_users(user_id, user_username, user_name, time_reg) VALUES(?, ?, ?, ?)",
                              (user_id, user_username, user_name, str(today)))
            await con.commit()
