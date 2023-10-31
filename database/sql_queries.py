CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users 
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER UNIQUE,
        USERNAME CHAR(50),
        FISRT_NAME CHAR(50),
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""

ALTER_USER_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN REFERENCE_LINK TEXT
"""

CREATE_BAN_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS ban (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER UNIQUE,
        COUNT INTEGER,
        FOREIGN KEY (TELEGRAM_ID) REFERENCES telegram_users(TELEGRAM_ID)
    )
"""

CREATE_USER_FORM_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS user_form 
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        BIO TEXT,
        AGE INTEGER,
        OCCUPATION CHAR(50),
        PHOTO TEXT,
        UNIQUE (TELEGRAM_ID)
        )
"""

CREATE_LIKE_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS like_user 
        (
        ID INTEGER PRIMARY KEY,
        OWNER_TELEGRAM_ID INTEGER,
        LIKER_TELEGRAM_ID INTEGER,
        UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
        )
"""

CREATE_REFERENCE_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS referral 
        (
        ID INTEGER PRIMARY KEY,
        OWNER_TELEGRAM_ID INTEGER,
        REFERRAL_TELEGRAM_ID INTEGER,
        UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
        )
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_user VALUES (?,?,?)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?)
"""

INSERT_USER_FORM_QUERY = """
INSERT INTO user_form VALUES (?,?,?,?,?,?,?)
"""

INSERT_REFERRAL_QUERY = """
INSERT INTO referral VALUES (?,?,?)
"""

SELECT_ALL_USERS_FORM_QUERY = """
SELECT * FROM user_form
"""

SELECT_ALL_USERS_QUERY = """
SELECT * FROM telegram_users
"""
SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

SELECT_USER_FORM_QUERY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
"""

INSERT_BAN_QUERY = """
INSERT OR IGNORE INTO ban VALUES (?,?,?)
"""
UPDATE_BAN_COUNT_QUERY = """
UPDATE ban SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_REFERENCE_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

SELECT_COUNT_QUERY = """SELECT COUNT FROM ban WHERE TELEGRAM_ID = ?"""

SELECT_ALL_USERS_FORM_QUERY = """SELECT * FROM user_form"""

SELECT_USER_BY_LINK_QUERY = """
SELECT * FROM telegram_users WHERE REFERENCE_LINK = ?
"""

SELECT_ALL_REFERRAL_BY_OWNER_QUERY = """
SELECT * FROM referral WHERE OWNER_TELEGRAM_ID = ?
"""
DELETE_USER_FORM_QUERY = """
DELETE FROM user_form WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_FORM_QUERY = """
UPDATE user_form SET NICKNAME = ?, BIO = ?, AGE = ?, OCCUPATION = ?, PHOTO = ? WHERE TELEGRAM_ID = ?
"""
