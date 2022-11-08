import sqlite3
import os
from datetime import date
from dbquaest.settings import BASE_DIR, MODULES
from dbquaest.tex import template, template_figure, template_document

######################################################################################################
# criando base de dados SQL
######################################################################################################

def make_database():

    database = os.path.exists('dbquaest.sqlite3')

    con = sqlite3.connect("dbquaest.sqlite3")
    cur = con.cursor()

    if bool(database) == False:
        cur.execute(r"""CREATE TABLE model(
            title varchar(255) NOT NULL,
            subtitle varchar(255) NOT NULL,
            created date NOT NULL,
            updated date NOT NULL,
            code_1 varchar(8),
            point_1 decimal,
            code_2 varchar(8),
            point_2 decimal,
            code_3 varchar(8),
            point_3 decimal,
            code_4 varchar(8),
            point_4 decimal,
            code_5 varchar(8),
            point_5 decimal
            )""")
        cur.execute(r"""CREATE TABLE test(
            created date NOT NULL,
            updated date NOT NULL,
            fk_model integer NOT NULL,
            fk_student integer NOT NULL,
            class varchar(25) NOT NULL,
            code integer NOT NULL,
            type varchar(10),
            text_1 varchar,
            figure_1 varchar(10),
            point_1 decimal,
            text_2 varchar DEFAULT NULL,
            figure_2 varchar(10) DEFAULT NULL,
            point_2 decimal DEFAULT NULL,
            text_3 varchar DEFAULT NULL,
            figure_3 varchar(10) DEFAULT NULL,
            point_3 decimal DEFAULT NULL,
            text_4 varchar DEFAULT NULL,
            figure_4 varchar(10) DEFAULT NULL,
            point_4 decimal DEFAULT NULL,
            text_5 varchar DEFAULT NULL,
            figure_5 varchar(10) DEFAULT NULL,
            point_5 decimal DEFAULT NULL,
            FOREIGN KEY (fk_model) REFERENCES model(ROWID),
            FOREIGN KEY (fk_student) REFERENCES student(ROWID)
            )""")
        cur.execute(r"""CREATE TABLE student(
            created date NOT NULL,
            updated date NOT NULL,
            name varchar(255) NOT NULL,
            email varchar(255) DEFAULT NULL,
            telephone varchar(255) DEFAULT NULL
            )""")
        cur.execute(r"""CREATE TABLE correction(
            created date NOT NULL,
            updated date NOT NULL,
            fk_test integer NOT NULL,
            choice_1 varchar(1) DEFAULT NULL,
            point_1 DEFAULT NULL,
            choice_2 varchar(1) DEFAULT NULL,
            point_2 DEFAULT NULL,
            choice_3 varchar(1) DEFAULT NULL,
            point_3 DEFAULT NULL,
            choice_4 varchar(1) DEFAULT NULL,
            point_4 DEFAULT NULL,
            choice_5 varchar(1) DEFAULT NULL,
            point_5 DEFAULT NULL,
            FOREIGN KEY (fk_test) REFERENCES test(ROWID)
            )""")
    else:
        print('The database already exists')

######################################################################################################
# classe Modelo
######################################################################################################

class Model():

    def __init__(self):

        self.con = sqlite3.connect("dbquaest.sqlite3")

    def create(self, title, subtitle, questions):

        cur = self.con.cursor()

        question_list = list()
        code_list = list()

        for item_1, item_2 in questions:
            question_list.append(item_1)
            code_list.append(item_2)

        for item in range(len(questions),5):
            question_list.append('')
            code_list.append(0)

        cur.execute(f"""
            INSERT INTO model VALUES ('{title}', '{subtitle}', '{date.today()}', '{date.today()}', '{question_list[0]}', '{code_list[0]}', '{question_list[1]}', '{code_list[1]}', '{question_list[2]}', '{code_list[2]}', '{question_list[3]}', '{code_list[3]}', '{question_list[4]}', '{code_list[4]}')
        """)

    def delete(self, title, subtitle):

        cur = self.con.cursor()

        cur.execute(f"""
            DELETE FROM model WHERE title = '{title}' AND subtitle = '{subtitle}'
        """)

    def save(self):

        self.con.commit()
        self.con.close()

######################################################################################################
# classe Estudante
######################################################################################################

class Student():

    def __init__(self):

        self.con = sqlite3.connect("dbquaest.sqlite3")

    def create(self, std):

        cur = self.con.cursor()

        cur.execute(f"""
            INSERT INTO student VALUES(
                '{date.today()}',
                '{date.today()}',
                '{std['name']}',
                '{std['email']}',
                '{std['telephone']}'
                )
            """)

    def save(self):

        self.con.commit()
        self.con.close()

######################################################################################################
# classe Teste
######################################################################################################

class Test():

    def __init__(self):

        self.con = sqlite3.connect("dbquaest.sqlite3")

    def create(self, model, std, clss):

        ntest = len(std)

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT code_1, point_1, code_2, point_2, code_3, point_3, code_4, point_4, code_5, point_5
            FROM model
            WHERE ROWID = {model};
        """)

        model_list = res.fetchone()

        std_data = []

        for name in std:
            res = cur.execute(f"""
                SELECT ROWID
                FROM student
                WHERE name = '{name}';
            """)

            var = res.fetchone()
            std_data.append(var[0])

        question_list = []
        for i in range(0,10,2):
            if model_list[i] != '':
                question_list.append({'code': model_list[i], 'point': model_list[i+1]})

        for i in range(ntest):

            data_txt = []
            data_figure = []
            data_point = []

            for code in question_list:

                for module in MODULES:
                    item = module.question(code['point'], code['code'])
                    if bool(item) == True:
                        quest = item

                text = quest['text']
                figure = quest['figure']
                unit = quest['unit']
                type = quest['type']
                alternatives = quest['alternative']

                point = []

                if figure:
                    fig = template_figure(figure)
                else:
                    fig = ''

                if type == 'conceptual':

                    choice = f'\\begin{{choices}}\n'

                    for alternative in alternatives:
                        point.append(round(alternative['point'],1))
                        choice = format(choice+'\choice '+alternative["choice"]+' '+unit+'\n')

                    txt = f"\\question {text}\n\n{choice}\\end{{choices}}\n"

                elif type == 'objective':

                    choice = f'\\begin{{oneparchoices}}\n'

                    for alternative in alternatives:
                        point.append(alternative['point'])
                        key = alternative['choice']
                        if abs(key) < 1.e-2 or key > 1.e+3:
                            choice = f"{choice}\\choice {key:.1e} {unit}"
                        else:
                            choice = f"{choice}\\choice {key:7.3f} {unit}"

                    txt = f"\\question {text}\n{fig}\n{choice}\n\\end{{oneparchoices}}"

                data_txt.append(txt)
                data_figure.append(figure)
                data_point.append(point)

            for j in range(len(question_list),5):
                data_txt.append('')
                data_figure.append('')
                data_point.append('')

            cur.execute(f"""
                INSERT INTO test VALUES (
                    '{date.today()}',
                    '{date.today()}',
                    '{model}',
                    '{std_data[i]}',
                    '{clss}',
                    '{i}',
                    '{type}',
                    '{data_txt[0]}',
                    '{data_figure[0]}',
                    '{data_point[0]}',
                    '{data_txt[1]}',
                    '{data_figure[1]}',
                    '{data_point[1]}',
                    '{data_txt[2]}',
                    '{data_figure[2]}',
                    '{data_point[2]}',
                    '{data_txt[3]}',
                    '{data_figure[3]}',
                    '{data_point[3]}',
                    '{data_txt[4]}',
                    '{data_figure[4]}',
                    '{data_point[4]}'
                    )
            """)

    def delete(self, id):

        cur = self.con.cursor()

        cur.execute(f"""
            DELETE FROM test WHERE rowid='{id}'
        """)

    def make_exam(self, clss):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT model.title, model.subtitle, student.name, test.class, test.code, test.text_1, test.figure_1, test.text_2, test.figure_2, test.text_3, test.figure_3, test.text_4, test.figure_4, test.text_5, test.figure_5
            FROM((test
            INNER JOIN student ON test.fk_student = student.ROWID)
            INNER JOIN model ON test.fk_model = model.ROWID)
            WHERE class = '{clss}'
        """)

        model_list = res.fetchall()

        res = cur.execute(f"""
            SELECT COUNT(*) FROM test WHERE class = '{clss}'
        """)

        ntest = res.fetchone()

        ntest = ntest[0]

        title = model_list[0][0]
        subtitle = model_list[0][1]
        clss = model_list[0][3]

        with open('main.tex', 'w') as file:

            tmplt = template()

            file.write(tmplt)

            file.write(r'\begin{document}'+'\n')

            for i in range(0,ntest):
                name = model_list[i][2]
                code = model_list[i][4]

                file.write(template_document(code, title, subtitle, name, clss))
    #
                file.write(f'\\begin{{questions}}\n')
    #
                file.write(f'\\begin{{multicols*}}{{2}}\n')
    #
                for j in range(0,10,2):
                    txt = model_list[i][j+5]
                    figure = model_list[i][j+6]

                    if figure:
                        os.system(f"cp {BASE_DIR}/src/dbquaest/img/{figure}.jpg .")

                    file.write(txt)

                file.write(f'\\end{{multicols*}}\n')

                file.write(f'\\end{{questions}}\n')

                file.write(f'\\newpage\n')

            file.write(f'\\end{{document}}')

            file.close()
      
        os.system('pdflatex main.tex')
        os.system('rm main.aux main.log')

    def save(self):

        self.con.commit()
        self.con.close()

######################################################################################################
# classe Correção
######################################################################################################

class Correction():

    def __init__(self):

        self.con = sqlite3.connect("dbquaest.sqlite3")

    def create(self, code, option_list):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT ROWID, point_1, point_2, point_3, point_4, point_5
            FROM test
            WHERE code = '{code}';
        """)

        model_list = res.fetchone()

        feedback_list = []

        for i in range(5):

            eval = evaluate(model_list[i+1], option_list[i])

            feedback_list.append(eval)

        id = model_list[0]

        cur.execute(f"""
            INSERT INTO correction VALUES(
                '{date.today()}',
                '{date.today()}',
                '{id}',
                '{option_list[0]}',
                '{feedback_list[0]}',
                '{option_list[1]}',
                '{feedback_list[1]}',
                '{option_list[2]}',
                '{feedback_list[2]}',
                '{option_list[3]}',
                '{feedback_list[3]}',
                '{option_list[4]}',
                '{feedback_list[4]}'
                )
            """)

    def delete(self, id):

        cur = self.con.cursor()

        cur.execute(f"""
            DELETE FROM correction WHERE rowid='{id}'
        """)

    def save(self):

        self.con.commit()
        self.con.close()

def evaluate(var, option):

    alphabet_list = 'A B C D E F G H I J'.split()

    var = var.replace('[', '').replace(']', '').replace(' ', '')
    var = var.split(',')

    point_list = [float(u) for u in var]

    indx = alphabet_list.index(option)

    feedback = point_list[indx]

    return feedback

