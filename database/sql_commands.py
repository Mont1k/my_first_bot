import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Connected")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_USER_FORM_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERENCE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_WALLET_TABLE_QUERY)

        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
        except sqlite3.OperationalError:
            pass

        self.connection.commit()

    def sql_add_referral_points(self, telegram_id, points):
        try:
            self.cursor.execute(sql_queries.ADD_REFERRAL_POINTS_QUERY, (telegram_id, points))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error adding referral points: {e}")

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name, None)
        )
        self.connection.commit()

    def sql_insert_user_form_query(self, telegram_id, nickname,
                                   bio, age, occupation, photo):
        self.cursor.execute(
            sql_queries.INSERT_USER_FORM_QUERY,
            (None, telegram_id, nickname, bio, age, occupation, photo)
        )
        self.connection.commit()

    def sql_select_balance(self, telegram_id):
        try:
            self.cursor.execute(sql_queries.SELECT_BALANCE_QUERY, (telegram_id,))
            balance = self.cursor.fetchone()
            if balance:
                return balance[0]
            else:
                return 0
        except sqlite3.Error as e:
            print(f"Error selecting balance: {e}")

    def sql_select_user_form_query(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "photo": row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_select_all_user_query(self):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_QUERY,
        ).fetchall()

    def sql_insert_ban_query(self, telegram_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_QUERY,
            (None, telegram_id, 1)
        )
        self.connection.commit()

    def sql_update_balance(self, telegram_id, balance):
        try:
            self.cursor.execute(sql_queries.UPDATE_BALANCE_QUERY, (balance, telegram_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error updating balance: {e}")

    def sql_update_ban_query(self, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_COUNT_QUERY,
            (telegram_id,)
        )
        self.connection.commit()

    def sql_select_user_query(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (telegram_id,)
        ).fetchall()

    def sql_get_ban_count(self, telegram_id):
        self.cursor.execute(sql_queries.SELECT_COUNT_QUERY, (telegram_id,))
        count = self.cursor.fetchone()
        if count:
            return count[0]
        else:
            return 0

    def sql_select_all_user_form_query(self):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "occupation": row[5],
            "photo": row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_USERS_FORM_QUERY,
        ).fetchall()

    def sql_insert_like_query(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_delete_form_query(self, owner):
        self.cursor.execute(
            sql_queries.DELETE_USER_FORM_QUERY,
            (owner,)
        )
        self.connection.commit()

    def sql_update_user_form_query(self, nickname, bio, age, occupation, photo, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_FORM_QUERY,
            (nickname, bio, age, occupation, photo, telegram_id,)
        )
        self.connection.commit()

    def sql_update_user_reference_link_query(self, link, telegram_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_REFERENCE_LINK_QUERY,
            (link, telegram_id,)
        )
        self.connection.commit()

    def sql_insert_referral_query(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral,)
        )
        self.connection.commit()

    def sql_select_user_by_link_query(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchall()

    def sql_select_all_referral_by_owner_query(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            "owner": row[1],
            "referral": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_ALL_REFERRAL_BY_OWNER_QUERY,
            (owner,)
        ).fetchall()
