import os
from . import settings
from dbquaest.mechanics import work_and_energy as mwe

class Test():

    def __init__(self, nquestion, ntest):

        self.nquestion = nquestion
        self.ntest = ntest
        self.question_list = list()

    def addQuestion(self, qcode):

        lista = list()

        for i in range(self.ntest):
            question = mwe.question(qcode)
            text = question['text']
            alternative = round(question['result'],2)
            value_list = [ alternative ]
            for alternative in question['error']:
                alternative = round(alternative,2)
                value_list.append(alternative)

            value_list.sort()

            value_list = [str(item) for item in value_list]

            lista.append({'text': text, 'alternative': value_list})

        self.question_list.append(lista)

        return self.question_list

    def setPDF(self):

        template = r"""
\documentclass[addpoints]{exam}
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}

\begin{document}

        """

        template_document = r"""
\begin{center}
	{\bf \Huge Prova bimestral}
	\vspace{1cm} \hrule \vspace{0.5cm}
	Aluno: \hfill Turma: \hfill Código: XXXXX
	\vspace{0.5cm} \hrule \vspace{0.5cm}
\end{center}
        """

        end_template = r"""
\end{document}
        """

        with open('main.tex', 'w') as file:

            file.write(template)

            for i in range(self.ntest):

                file.write(template_document)

                if self.question_list:

                    file.write('\\begin'+'{'+'questions'+'}\n')

                    for j in range(2):

                        file.write('\\question[25] '+self.question_list[j][i]['text']+'\n\\linebreak\linebreak\n')
                        file.write('\\begin'+'{'+'oneparchoices'+'}\n')
                        for alternative in self.question_list[j][i]['alternative']:
                            file.write('\\choice '+alternative)
                        file.write('\\end'+'{'+'oneparchoices'+'}\n')

                    file.write('\\end'+'{'+'questions}\n')

                file.write('\\newpage')

            file.write(end_template)
            file.close()

        os.system('pdflatex main.tex')
        os.system('rm main.aux main.log')
