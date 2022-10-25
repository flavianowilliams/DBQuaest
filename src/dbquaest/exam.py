import os
from . import settings
from dbquaest.mechanics import work_and_energy as mwe

class Test():

    def __init__(self, ntest):

        self.nquestion = 0
        self.ntest = ntest
        self.question_list = list()
        self.question_point = list()

    def addQuestion(self, point, qcode):

        lista = list()

        for i in range(self.ntest):

            value_list = list()
            resultado = list()

            question = mwe.question(point, qcode)

            text = question['text']
            figure = question['figure']
            for item in question['alternative']:
                resultado.append(item['point'])
                value = (str(round(item['value'],2))+' '+item['unit'])
                value_list.append(value)

            lista.append({ 'code': qcode, 'test': i,'text': text, 'figure': figure, 'alternative': value_list, 'result': resultado})

        self.question_list.append(lista)

        self.nquestion +=1

        self.question_point.append(point)

        return self.question_list

    def makeExam(self):

        template = r"""
\documentclass[12pt, addpoints]{exam}
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}
\usepackage{multicol}
\usepackage{graphicx}
\usepackage{amsmath}

\setlength{\columnsep}{1cm}

\begin{document}

        """

        template_document = r"""
\begin{minipage}[l]{0.5\linewidth}
    \begin{flushleft}
        {\bf \Large Prova bimestral}
    \end{flushleft}
\end{minipage}
\begin{minipage}[r]{0.5\linewidth}
    \begin{flushright}
        {\bf \Large Código: XXXXX}
    \end{flushright}
\end{minipage}
\vspace{1cm} \hrule \vspace{0.5cm}
\begin{minipage}{0.70\linewidth}
    Aluno:
\end{minipage}
\begin{minipage}{0.25\linewidth}
    Turma:
\end{minipage}
\vspace{0.5cm} \hrule \vspace{0.5cm}

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
                    file.write('\\begin'+'{'+'multicols*'+'}'+'{'+'2'+'}''\n')

                    for j in range(self.nquestion):

                        file.write('\\question['+str(self.question_point[j])+'] '+self.question_list[j][i]['text']+'\n\n')

                        if self.question_list[j][i]['figure']:
                            file.write('\\begin'+'{'+'center'+'}\n')
                            file.write('\\begin'+'{'+'minipage'+'}[c]'+'{0.75\\linewidth'+'}\n')
                            file.write('\\includegraphics[width=\\textwidth]'+'{'+self.question_list[j][i]['figure']+'.jpg}\n')
                            file.write('\\end'+'{'+'minipage'+'}\n\n')
                            file.write('\\end'+'{'+'center'+'}\n')

                        file.write('\\begin'+'{'+'oneparchoices'+'}\n')

                        for alternative in self.question_list[j][i]['alternative']:
                            file.write('\\choice '+alternative)

                        file.write('\\end'+'{'+'oneparchoices'+'}\n')

                    file.write('\\end'+'{'+'multicols*'+'}\n')
                    file.write('\\end'+'{'+'questions'+'}\n')

                file.write('\\newpage')

            file.write(end_template)
            file.close()
      
        os.system('pdflatex main.tex')
        os.system('rm main.aux main.log')

    def setCorrection(self, test, options):

        self.alphabet = 'A B C D E F G H I J'.split()
        self.feedback = list()

        for i in range(self.nquestion):

            indx = self.alphabet.index(options[i])
            self.feedback.append(self.question_list[i][test]['result'][indx])

#            for i in range(2):
#                self.feedback.append(question['point'][self.alphabet.index(self.options[i])])