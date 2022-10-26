import os
from dbquaest.settings import BASE_DIR
from dbquaest.mechanics import work_and_energy as mwe

class test():

    def __init__(self, ntest, date):

        self.nquestion = 0
        self.ntest = ntest
        self.date = date
        self.question_list = list()
        self.question_point = list()

        self.template = r"""
\documentclass[12pt, addpoints]{exam}
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}
\usepackage{multicol}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{xcolor}
\usepackage[a4paper, portrait, margin=2cm]{geometry}

\setlength{\columnsep}{1cm}

        """

        self.template_document = r"""
\begin{minipage}[l]{0.5\linewidth}
    \begin{flushleft}
        {\bf \Large Prova bimestral}
    \end{flushleft}
\end{minipage}
\begin{minipage}[r]{0.45\linewidth}
    \begin{flushright}
        {\bf \Large Código: XXXXX}
    \end{flushright}
\end{minipage}
\vspace{0.5cm} \hrule \vspace{0.5cm}
\begin{minipage}{0.75\linewidth}
    Aluno:
\end{minipage}
\begin{minipage}{0.20\linewidth}
    Data: 
\end{minipage}
\vspace{0.5cm} \hrule \vspace{0.5cm}

"""

    def add_question(self, point, qcode):

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

    def make_exam(self):

        with open('main.tex', 'w') as file:

            file.write(self.template)

            file.write(r'\begin{document}'+'\n')

            for i in range(self.ntest):

                file.write(self.template_document)

                if self.question_list:

                    file.write(r'\begin{questions}'+'\n')
                    file.write(r'\begin{multicols}{2}'+'\n')

                    for j in range(self.nquestion):

                        file.writelines(r'\question['+str(self.question_point[j])+r'] '+self.question_list[j][i]['text']+'\n')

                        if self.question_list[j][i]['figure']:
                            os.system(f"cp {BASE_DIR}/src/dbquaest/mechanics/img/{self.question_list[j][i]['figure']}.jpg .")
                            file.write(r'\begin{center}'+'\n')
                            file.write(r'\begin{minipage}[c]{0.75\linewidth}'+'\n')
                            file.write(r'\includegraphics[width=\textwidth]'+'{'+self.question_list[j][i]['figure']+'.jpg}\n')
                            file.write(r'\end{minipage}'+'\n')
                            file.write(r'\end{center}'+'\n')

                        file.write(r'\begin{oneparchoices}'+'\n')

                        for alternative in self.question_list[j][i]['alternative']:
                            file.write(r'\choice '+alternative)

                        file.write(r'\end{oneparchoices}'+'\n')

                    file.write(r'\end{multicols}'+'\n')
                    file.write(r'\end{questions}'+'\n')

                file.write(r'\newpage')

            file.write(r'\end{document}')
            file.close()
      
        os.system('pdflatex main.tex')
        os.system('rm main.aux main.log')

    def make_result(self):

        with open('main_result.tex', 'w') as file:

            file.write(self.template)

            file.write(r'\begin{document}'+'\n')

            for i in range(self.ntest):

                file.write(self.template_document)

                file.write(r'\begin{center}'+'\n'+r'\textcolor{red}{\emph\Large Correction version}'+r'\end{center}'+'\n')

                if self.question_list:

                    file.write(r'\begin{questions}'+'\n')
                    file.write(r'\begin{multicols}{2}'+'\n')

                    for j in range(self.nquestion):

                        file.writelines(r'\question['+str(self.question_point[j])+r'] '+self.question_list[j][i]['text']+'\n\n')

                        if self.question_list[j][i]['figure']:
                            os.system(f"cp {BASE_DIR}/src/dbquaest/mechanics/img/{self.question_list[j][i]['figure']}.jpg .")
                            file.write(r'\begin{center}'+'\n')
                            file.write(r'\begin{minipage}[c]{0.75\linewidth}'+'\n')
                            file.write(r'\includegraphics[width=\textwidth]'+'{'+self.question_list[j][i]['figure']+'.jpg}\n')
                            file.write(r'\end{minipage}'+'\n\n')
                            file.write(r'\end{center}'+'\n')

                        file.write(r'\begin{oneparchoices}'+'\n')

                        for alternative in self.question_list[j][i]['alternative']:
                            file.write('\\choice '+alternative)

                        file.write(r'\end{oneparchoices}'+'\n\n')
                        file.write(r'\begin{oneparchoices}'+'\n')

                        for alternative in self.question_list[j][i]['result']:
                            file.write('\\choice '+str(alternative))

                        file.write(r'\end{oneparchoices}'+'\n')

                    file.write(r'\end{multicols}'+'\n')
                    file.write(r'\end{questions}'+'\n')

                file.write(r'\newpage')

            file.write(r'\end{document}')
            file.close()
      
        os.system('pdflatex main_result.tex')
        os.system('rm main_result.aux main_result.log')

    def set_correction(self, test, options):

        self.alphabet = 'A B C D E F G H I J'.split()
        self.feedback = list()

        for i in range(self.nquestion):

            indx = self.alphabet.index(options[i])
            self.feedback.append(self.question_list[i][test]['result'][indx])

#            for i in range(2):
#                self.feedback.append(question['point'][self.alphabet.index(self.options[i])])