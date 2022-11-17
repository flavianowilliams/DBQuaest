import sqlite3
from sqlite3 import Error
from dbquaest.settings import DB_DIR

######################################################################################################
# criando base de dados SQL
######################################################################################################

def make_database():
    """Create a database connection to a SQLite database """

#    database = os.path.exists(DB_DIR+'dbquaest.sqlite3')

    con = None

    try:
        con = sqlite3.connect(DB_DIR+"dbquaest.sqlite3")
        cur = con.cursor()
        print(sqlite3.version)
        cur.execute(r"""CREATE TABLE model(
            title varchar(255) NOT NULL,
            subtitle varchar(255) NOT NULL,
            created date NOT NULL,
            updated date NOT NULL,
            questions integer NOT NULL,
            constants DEFAULT NULL,
            module_1 varchar(255),
            submodule_1 varchar(255),
            code_1 varchar(3),
            point_1 decimal DEFAULT 0,
            module_2 varchar(255),
            submodule_2 varchar(255),
            code_2 varchar(3),
            point_2 decimal DEFAULT 0,
            module_3 varchar(255),
            submodule_3 varchar(255),
            code_3 varchar(3),
            point_3 decimal DEFAULT 0,
            module_4 varchar(255),
            submodule_4 varchar(255),
            code_4 varchar(3),
            point_4 decimal DEFAULT 0,
            module_5 varchar(255),
            submodule_5 varchar(255),
            code_5 varchar(3),
            point_5 decimal DEFAULT 0
            )""")

        cur.execute(r"""CREATE TABLE test(
            created date NOT NULL,
            updated date NOT NULL,
            date date NOT NULL,
            fk_model integer NOT NULL,
            fk_student integer NOT NULL,
            class varchar(25) NOT NULL,
            code integer NOT NULL,
            type varchar(10),
            text_1 varchar,
            figure_1 varchar(10),
            point_1,
            consideration_1 varchar,
            text_2 varchar DEFAULT NULL,
            figure_2 varchar(10) DEFAULT NULL,
            point_2,
            consideration_2 varchar,
            text_3 varchar DEFAULT NULL,
            figure_3 varchar(10) DEFAULT NULL,
            point_3,
            consideration_3 varchar,
            text_4 varchar DEFAULT NULL,
            figure_4 varchar(10) DEFAULT NULL,
            point_4,
            consideration_4 varchar,
            text_5 varchar DEFAULT NULL,
            figure_5 varchar(10) DEFAULT NULL,
            point_5,
            consideration_5 varchar,
            FOREIGN KEY (fk_model) REFERENCES model(ROWID),
            FOREIGN KEY (fk_student) REFERENCES student(ROWID)
            )""")

        cur.execute(r"""CREATE TABLE student(
            created date NOT NULL,
            updated date NOT NULL,
            register varchar(13) NOT NULL UNIQUE,
            name varchar(255) NOT NULL UNIQUE,
            email varchar(255) DEFAULT NULL,
            telephone varchar(255) DEFAULT NULL
            )""")

        cur.execute(r"""CREATE TABLE correction(
            created date NOT NULL,
            updated date NOT NULL,
            fk_test integer NOT NULL,
            choice_1 varchar(1) DEFAULT NULL,
            point_1 decimal DEFAULT NULL,
            consideration_1 varchar DEFAULT NULL,
            choice_2 varchar(1) DEFAULT NULL,
            point_2 decimal DEFAULT NULL,
            consideration_2 varchar DEFAULT NULL,
            choice_3 varchar(1) DEFAULT NULL,
            point_3 decimal DEFAULT NULL,
            consideration_3 varchar DEFAULT NULL,
            choice_4 varchar(1) DEFAULT NULL,
            point_4 decimal DEFAULT NULL,
            consideration_4 varchar DEFAULT NULL,
            choice_5 varchar(1) DEFAULT NULL,
            point_5 decimal DEFAULT NULL,
            consideration_5 varchar DEFAULT NULL,
            FOREIGN KEY (fk_test) REFERENCES test(ROWID)
            )""")
    except:
        print(Error)
