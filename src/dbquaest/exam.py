import sqlite3, os
from datetime import date
from dbquaest.utils import email_function, eval_float, eval_string, string_format
from dbquaest.settings import BASE_DIR, MODULES, DB_DIR
from dbquaest.tex import template, template_figure, template_document, template_report

######################################################################################################
# classe Modelo
######################################################################################################

class Model():

    def __init__(self):

        self.con = sqlite3.connect(DB_DIR+"dbquaest.sqlite3")

    def create(self, title, subtitle, description, questions):

        cur = self.con.cursor()

        nquest = len(questions)

        module_list = []
        submodule_list = []
        code_list = []
        point_list = []

        for item in questions:
            var1 = item['module']
            var2 = item['submodule']
            var3 = item['code']
            var4 = item['point']
            module_list.append(f'\"{var1}\"')
            submodule_list.append(f'\"{var2}\"')
            code_list.append(f'\"{var3}\"')
            point_list.append(f'\"{var4}\"')

        for item in range(nquest,5):
            module_list.append('NULL')
            submodule_list.append('NULL')
            code_list.append('NULL')
            point_list.append('NULL')

        cur.execute(f"""
            INSERT INTO model VALUES ('{title}', '{subtitle}', '{date.today()}', '{date.today()}', '{description}', '{nquest}', {module_list[0]}, {submodule_list[0]}, {code_list[0]}, {point_list[0]}, {module_list[1]}, {submodule_list[1]}, {code_list[1]}, {point_list[1]}, {module_list[2]}, {submodule_list[2]}, {code_list[2]}, {point_list[2]}, {module_list[3]}, {submodule_list[3]}, {code_list[3]}, {point_list[3]}, {module_list[4]}, {submodule_list[4]}, {code_list[4]}, {point_list[4]})
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

        self.con = sqlite3.connect(DB_DIR+"dbquaest.sqlite3")

    def create(self, std):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT ROWID FROM student
        """)

        model_list = res.fetchall()
        register = str(len(model_list)+1)
        std['name'] = std['name'].upper()

        cur.execute(f"""
            INSERT INTO student VALUES(
                '{date.today()}',
                '{date.today()}',
                '{register}',
                '{std['name']}',
                '{std['email']}',
                '{std['telephone']}'
                )
            """)

    def delete(self, name):

        cur = self.con.cursor()

        cur.execute(f"""
            DELETE FROM studento WHERE name = '{name}'
        """)

    def save(self):

        self.con.commit()
        self.con.close()

######################################################################################################
# classe Teste
######################################################################################################

class Test():

    def __init__(self, clss):

        self.con = sqlite3.connect(DB_DIR+"dbquaest.sqlite3")

        self.clss = clss

    def create(self, model, std, var_date):

        ntest = len(std)

        std = [item.upper() for item in std]

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT questions, module_1, submodule_1, code_1, point_1, module_2, submodule_2, code_2, point_2, module_3, submodule_3, code_3, point_3, module_4, submodule_4, code_4, point_4, module_5, submodule_5, code_5, point_5
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
        for i in range(0,model_list[0]):
            question_list.append({
                'module': model_list[4*i+1],
                'submodule': model_list[4*i+2],
                'code': model_list[4*i+3],
                'point': model_list[4*i+4]
                })

        for i in range(ntest):

            data_txt = []
            data_figure = []
            data_point = []
            data_consideration = []
            data_constants = []
            data_formulas = []

            for code in question_list:

                for module in MODULES:                   
                    if module.__name__ == f"dbquaest.{code['module']}.{code['submodule']}":
                        quest = module.question(code['point'], code['code'], max(ntest,10))

                text = quest['text']
                figure = quest['figure']
                unit = quest['unit']
                type = quest['type']
                alternatives = quest['alternative']

                cte_list = quest['constants']
                constants = []
                for cte in cte_list:
                    constants.append(str(cte))

                data_constants = data_constants+constants

                form_list = quest["formulas"]
                formulas = []
                for form in form_list:
                    formulas.append(format(form))

                data_formulas = data_formulas+formulas

                point = []
                consideration = []

                if figure:
                    fig = template_figure(figure)
                else:
                    fig = ''

                if type == 'conceptual':

                    choice = f'\\begin{{choices}}\n'

                    for alternative in alternatives:
                        point.append(round(alternative['point'],1))
                        cons = str(alternative['consideration'])
                        consideration.append(cons)
                        choice = format(choice+'\choice '+alternative["choice"]+' '+unit+'\n')

                    txt = f"\'\\question[{code['point']}] {text}\n\n{choice}\\end{{choices}}\n\'"

                elif type == 'objective':

                    choice = f'\\begin{{oneparchoices}}\n'

                    for alternative in alternatives:
                        point.append(alternative['point'])
                        cons = str(alternative['consideration'])
                        consideration.append(cons)
                        key = alternative['choice']
                        if abs(key) < 1.e-2 or key > 1.e+3:
                            choice = f"{choice}\\choice \\num{{{key:.1e}}} {unit}"
                        else:
                            choice = f"{choice}\\choice \\num{{{key:7.3f}}} {unit}"

                    txt = f"\'\\question[{code['point']}] {text}\n{fig}\n{choice}\n\\end{{oneparchoices}}\'"

                data_txt.append(txt)
                data_figure.append(f"\'{figure}\'")
                data_point.append(f"\'{point}\'")
                data_consideration.append(f'\"{consideration}\"')

            data_constants = list(dict.fromkeys(data_constants))
            data_constants = f'\"{data_constants}\"'

            data_formulas = list(dict.fromkeys(data_formulas))
            data_formulas = f'\"{data_formulas}\"'

            for j in range(len(question_list),5):
                data_txt.append('NULL')
                data_figure.append('NULL')
                data_point.append('NULL')
                data_consideration.append('NULL')

            cur.execute(f"""
                INSERT INTO test VALUES (
                    '{date.today()}',
                    '{date.today()}',
                    '{var_date}',
                    '{model}',
                    '{std_data[i]}',
                    '{self.clss}',
                    '{i}',
                    {data_constants},
                    {data_formulas},
                    {data_txt[0]},
                    {data_figure[0]},
                    {data_point[0]},
                    {data_consideration[0]},
                    {data_txt[1]},
                    {data_figure[1]},
                    {data_point[1]},
                    {data_consideration[1]},
                    {data_txt[2]},
                    {data_figure[2]},
                    {data_point[2]},
                    {data_consideration[2]},
                    {data_txt[3]},
                    {data_figure[3]},
                    {data_point[3]},
                    {data_consideration[3]},
                    {data_txt[4]},
                    {data_figure[4]},
                    {data_point[4]},
                    {data_consideration[4]}
                    )
            """)

    def delete(self):

        cur = self.con.cursor()

        cur.execute(f"""
            DELETE FROM test WHERE class='{self.clss}'
        """)

    def generate_PDF(self):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT model.title, model.subtitle, student.name, test.date, test.code, test.constants, test.formulas, test.text_1, test.figure_1, test.text_2, test.figure_2, test.text_3, test.figure_3, test.text_4, test.figure_4, test.text_5, test.figure_5
            FROM((test
            INNER JOIN student ON test.fk_student = student.ROWID)
            INNER JOIN model ON test.fk_model = model.ROWID)
            WHERE class = '{self.clss}'
        """)

        model_list = res.fetchall()

        res = cur.execute(f"""
            SELECT COUNT(*) FROM test WHERE class = '{self.clss}'
        """)

        ntest = res.fetchone()
        ntest = ntest[0]

        title = model_list[0][0]
        subtitle = model_list[0][1]

        with open('main.tex', 'w') as file:

            tmplt = template()

            file.write(tmplt)

            file.write(r'\begin{document}'+'\n')

            for i in range(0,ntest):
                name = model_list[i][2]
                var_date = model_list[i][3]
                code = model_list[i][4]
                constants = model_list[i][5]
                formulas = model_list[i][6]

                constants_list = string_format(constants)

                formula_list = string_format(formulas)

                file.write(template_document(code, title, subtitle, name, self.clss, var_date))
    #
                file.write(f'\\begin{{questions}}\n')
    #
                file.write(f'\\begin{{multicols*}}{{2}}\n')
    #
                for j in range(0,10,2):
                    txt = model_list[i][j+7]
                    if txt:
                        figure = model_list[i][j+8]

                        if figure:
                            os.system(f"cp {BASE_DIR}/src/dbquaest/img/{figure}.jpg .")

                        file.write(txt)

                file.write(f'\\end{{multicols*}}\n')

                file.write(f'\\end{{questions}}\n')

                file.write(r'\begin{minipage}[b]{\linewidth}')
                file.write(f'\\begin{{flushleft}}')
                file.write(f'Constants:')
                file.write(f'\linebreak')
                for cte in constants_list:
                    file.writelines(f'{cte}; ')

                file.write(f'\\end{{flushleft}}')
                file.write(r'\end{minipage}')
                file.write(f'\\vspace{{0.5cm}}\\linebreak')
                file.write(r'\begin{minipage}[b]{\linewidth}')
                file.write(f'\\begin{{flushleft}}')
                file.write(f'Formulas:')
                file.write(f'\linebreak')
                for form in formula_list:
                    file.writelines(f'{form}; ')
                file.write(f'\\end{{flushleft}}')
                file.write(r'\end{minipage}')

                file.write(f'\\newpage\n')

            file.write(f'\\end{{document}}')

            file.close()
      
        os.system('pdflatex main.tex')
        os.system('rm main.aux main.log')

    def save(self):

        self.con.commit()
        self.con.close()

######################################################################################################
# classe Resultado
######################################################################################################

class Result():

    def __init__(self, clss_input):

        self.con = sqlite3.connect(DB_DIR+"dbquaest.sqlite3")

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT test.date, test.code, test.ROWID, test.point_1, test.point_2, test.point_3, test.point_4, test.point_5, test.consideration_1, test.consideration_2, test.consideration_3, test.consideration_4, test.consideration_5, student.name, student.email, model.title, model.subtitle
            FROM test, student, model
            WHERE class = '{clss_input}'
            AND test.fk_model = model.ROWID
            AND test.fk_student = student.ROWID;
        """)

        list = res.fetchall()

        self.var_date = [item[0] for item in list]
        self.code = [item[1] for item in list]
        self.test = [item[2] for item in list]

        self.point_1 = [item[3] for item in list]
        self.point_2 = [item[4] for item in list]
        self.point_3 = [item[5] for item in list]
        self.point_4 = [item[6] for item in list]
        self.point_5 = [item[7] for item in list]

        self.cons_1 = [item[8] for item in list]
        self.cons_2 = [item[9] for item in list]
        self.cons_3 = [item[10] for item in list]
        self.cons_4 = [item[11] for item in list]
        self.cons_5 = [item[12] for item in list]

        self.name = [item[13] for item in list]
        self.email = [item[14] for item in list]
        self.title = [item[15] for item in list]
        self.subtitle = [item[16] for item in list]

        self.clss = clss_input

    def create(self,option_list):

        cur = self.con.cursor()

        for option in option_list:

            indx = self.code.index(option['code'])

            lst = option['choice']

            feedback_list = [eval_float(self.point_1[indx], lst[0])]
            fback_cons = [eval_string(self.cons_1[indx], lst[0])]

            if bool(self.point_2[indx]) != False:
                feedback_list.append(eval_float(self.point_2[indx], lst[1]))
                fback_cons.append(eval_string(self.cons_2[indx], lst[1]))
            else:
                feedback_list.append('NULL')
                fback_cons.append('NULL')

            if bool(self.point_3[indx]) != False:
                feedback_list.append(eval_float(self.point_3[indx], lst[2]))
                fback_cons.append(eval_string(self.cons_3[indx], lst[2]))
            else:
                feedback_list.append('NULL')
                fback_cons.append('NULL')

            if bool(self.point_4[indx]) != False:
                feedback_list.append(eval_float(self.point_4[indx], lst[3]))
                fback_cons.append(eval_string(self.cons_4[indx], lst[3]))
            else:
                feedback_list.append('NULL')
                fback_cons.append('NULL')

            if bool(self.point_5[indx]) != False:
                feedback_list.append(eval_float(self.point_5[indx], lst[4]))
                fback_cons.append(eval_string(self.cons_5[indx], lst[4]))
            else:
                feedback_list.append('NULL')
                fback_cons.append('NULL')

            self.chk = [f'\'{item}\'' for item in option['choice']]

            nx = len(option['choice'])

            for i in range(nx, 5):
                self.chk.append('NULL')

            cur.execute(f"""
                INSERT INTO correction VALUES(
                    '{date.today()}',
                    '{date.today()}',
                    '{self.test[indx]}',
                    {self.chk[0]},
                    {feedback_list[0]},
                    {fback_cons[0]},
                    {self.chk[1]},
                    {feedback_list[1]},
                    {fback_cons[1]},
                    {self.chk[2]},
                    {feedback_list[2]},
                    {fback_cons[2]},
                    {self.chk[3]},
                    {feedback_list[3]},
                    {fback_cons[3]},
                    {self.chk[4]},
                    {feedback_list[4]},
                    {fback_cons[4]}
                    )
                """)

    def generate_PDF(self):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT correction.choice_1, correction.choice_2, correction.choice_3, correction.choice_4, correction.choice_5, correction.point_1, correction.point_2, correction.point_3, correction.point_4, correction.point_5
            FROM test, correction, student
            WHERE class = '{self.clss}'
            AND correction.fk_test = test.ROWID;
        """)

        list = res.fetchall()

        self.choice_1 = [item[0] for item in list]
        self.choice_2 = [item[1] for item in list]
        self.choice_3 = [item[2] for item in list]
        self.choice_4 = [item[3] for item in list]
        self.choice_5 = [item[4] for item in list]

        self.result_1 = [item[5] for item in list]
        self.result_2 = [item[6] for item in list]
        self.result_3 = [item[7] for item in list]
        self.result_4 = [item[8] for item in list]
        self.result_5 = [item[9] for item in list]

        os.system('mkdir result')

        for i in range(len(self.code)):

            output = f'result_{self.code[i]}'

            with open(f'result/{output}.tex', 'w') as file:

                tmplt = template()

                file.write(tmplt)

                file.write(r'\begin{document}'+'\n')

                file.write(template_document(self.code[i], self.title[i], self.subtitle[i], self.name[i], self.clss[i]))
    
                file.write(f'\\begin{{questions}}\n')

                if self.choice_1[i]:
                   file.write(f'\question Question 1.')
                   file.write(r'\begin{itemize}')
                   file.write(f'\item You chose the alternative {self.choice_1[i]}.')
                   file.write(f'\item You got {self.result_1[i]} points.')
                   file.write(f'\item Considerations: ')
                   file.write(r'\end{itemize}')

                file.write(f'\\end{{questions}}\n')

                file.write(f'\\end{{document}}')

                file.close()
      
            os.system(f'pdflatex -halt-on-error -output-directory result result/{output}.tex')
            os.system(f'rm result/{output}.aux result/{output}.log')

    def make_report(self):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT test.ROWID, correction.point_1, correction.point_2, correction.point_3, correction.point_4, correction.point_5
            FROM test, correction
            WHERE class = '{self.clss}'
            AND correction.fk_test = test.ROWID;
        """)

        list = res.fetchall()

        test_list = [item[0] for item in list]

        result_1 = [item[1] for item in list]
        result_2 = [item[2] for item in list]
        result_3 = [item[3] for item in list]
        result_4 = [item[4] for item in list]
        result_5 = [item[5] for item in list]

        result = []
        for item in list:
            soma = 0.0
            for i in range(1,6):
                if item[i]:
                    soma += item[i]
            result.append(soma)

        with open(f'report.tex', 'w') as file:

            tmplt = template()

            file.write(tmplt)

            file.write(r'\begin{document}'+'\n')

            file.write(template_report(self.title[0], self.subtitle[0], self.clss, self.var_date[0]))
    
            file.write(r'\begin{table}[h!]'+'\n')

            file.write(r'\centering'+'\n')

            file.write(r'\begin{tabular}{lccccccc}'+'\n')

            file.write(r'\hline'+'\n')

            file.write(r'Student & Code & Q. 1 & Q. 2 & Q. 3 & Q. 4 & Q. 5 & Total\\'+'\n')

            file.write(r'\hline'+'\n')

            for i in range(len(test_list)):

                indx = self.test.index(test_list[i])

                file.write(f'{self.name[indx]} & {self.code[indx]} & {result_1[i]} & {result_2[i]} & {result_3[i]} & {result_4[i]} & {result_5[i]} & {result[i]}\\\\')

            file.write(r'\hline'+'\n')

            file.write(r'\end{tabular}'+'\n')

            file.write(r'\end{table}'+'\n')

            file.write(f'\\end{{document}}')

            file.close()
      
            os.system(f'pdflatex report.tex')
            os.system(f'rm report.aux report.log')

    def send_mail(self):

        cur = self.con.cursor()

        res = cur.execute(f"""
            SELECT correction.choice_1, correction.choice_2, correction.choice_3, correction.choice_4, correction.choice_5, correction.point_1, correction.point_2, correction.point_3, correction.point_4, correction.point_5, correction.consideration_1, correction.consideration_2, correction.consideration_3, correction.consideration_4, correction.consideration_5, test.ROWID
            FROM test, correction
            WHERE class = '{self.clss}'
            AND correction.fk_test = test.ROWID;
        """)

        list = res.fetchall()

        choice_1 = [item[0] for item in list]
        choice_2 = [item[1] for item in list]
        choice_3 = [item[2] for item in list]
        choice_4 = [item[3] for item in list]
        choice_5 = [item[4] for item in list]

        result_1 = [float(item[5]) for item in list if item[5] is not None]
        result_2 = [float(item[6]) for item in list if item[6] is not None]
        result_3 = [float(item[7]) for item in list if item[7] is not None]
        result_4 = [float(item[8]) for item in list if item[8] is not None]
        result_5 = [float(item[9]) for item in list if item[9] is not None]
   
        cons_1 = [str(item[10]) for item in list if item[10] is not None]
        cons_2 = [str(item[11]) for item in list if item[11] is not None]
        cons_3 = [str(item[12]) for item in list if item[12] is not None]
        cons_4 = [str(item[13]) for item in list if item[13] is not None]
        cons_5 = [str(item[14]) for item in list if item[14] is not None]

        test_list = [item[15] for item in list]

        result = []
        for item in list:
            sum = 0.0
            if item[5]:
                sum += item[5]
            if item[6]:
                sum += item[6]
            if item[7]:
                sum += item[7]
            if item[8]:
                sum += item[8]
            if item[9]:
                sum += item[9]
            result.append(sum)

        for i in range(len(test_list)):

            indx = self.test.index(test_list[i])

            mail_subject = f"{self.title[indx]}"

            mail_body = f"""
                <p>Avaliação: <strong>{self.title[indx]} - {self.subtitle[indx]}</strong></p>
                <p>Data: {self.var_date[indx]}</p>
                <p>Aluno: {self.name[indx]}</p>

            """

            if choice_1[i]:
                mail_body = mail_body+f"""
                <p>Questão 1</p>
                <ul>
                    <li> Alternativa escolhida: {choice_1[i]};
                    <li> Considerações: {cons_1[i]}.
                    <li> Pontos obtidos na questão: {result_1[i]}.
                </ul>
            """

            if choice_2[i]:
                mail_body = mail_body+f"""
                <p>Questão 2</p>
                <ul>
                    <li> Alternativa escolhida: {choice_2[i]};
                    <li> Considerações: {cons_2[i]}.
                    <li> Pontos obtidos na questão: {result_2[i]}.
                </ul>
            """

            if choice_3[i]:
                mail_body = mail_body+f"""
                <p>Questão 3</p>
                <ul>
                    <li> Alternativa escolhida: {choice_3[i]};
                    <li> Considerações: {cons_3[i]}.
                    <li> Pontos obtidos na questão: {result_3[i]}.
                </ul>
            """

            if choice_4[i]:
                mail_body = mail_body+f"""
                <p>Questão 4</p>
                <ul>
                    <li> Alternativa escolhida: {choice_4[i]};
                    <li> Considerações: {cons_4[i]}.
                    <li> Pontos obtidos na questão: {result_4[i]}.
                </ul>
            """

            if choice_5[i]:
                mail_body = mail_body+f"""
                <p>Questão 5</p>
                <ul>
                    <li> Alternativa escolhida: {choice_5[i]};
                    <li> Considerações: {cons_5[i]}.
                    <li> Pontos obtidos na questão: {result_5[i]}.
                </ul>
            """

            mail_body = mail_body+f"""
            <p> Total de pontos obtidos: <strong>{result[i]} pontos</strong>.</p>
            """

            mail_body = mail_body+r"<p>Este email foi gerado automaticamente pelo programa gerador de testes DBQuaest. Procure o seu professor para esclarecimento de dúvidas sobre este teste.</p>"

            mail_body = mail_body+r"<p><em>Acesse o <a href='https://github.com/flavianowilliams/DBQuaest'>Readme</a> no repositório do GitHub para obter mais informações sobre o programa.</em></p>"

            mail_body = mail_body+r"&#169; 2022 <a href='https://github.com/flavianowilliams/DBQuaest/blob/master/LICENSE'>MIT License</a>"

            print('Sending mail to {}...'.format(self.email[indx]))
            email_function(mail_subject, mail_body, self.email[indx])
            print('OK')

    def delete(self):

        cur = self.con.cursor()

        for test in self.test:
            cur.execute(f"""
                DELETE FROM correction WHERE fk_test='{test}';
            """)

    def save(self):

        self.con.commit()
        self.con.close()
