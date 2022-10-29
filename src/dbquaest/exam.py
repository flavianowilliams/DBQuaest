import os
import random
from dbquaest.settings import BASE_DIR
from dbquaest.electromagnetism import magnetism, electrodynamics, electrostatic, induced_magnetic_field
from dbquaest.quantum_physics import particle_wave_duality, uncertainty_principle, schrodinger_equation

class test():

    def __init__(self, ntest, title, subtitle):

        self.nquestion = 0
        self.ntest = ntest
        self.title = title
        self.subtitle = subtitle
        self.question_list = list()
        self.question_point = list()

        code = 1

        self.template = r"""
\documentclass[12pt, addpoints]{exam}
\usepackage[utf8]{inputenc}
\usepackage[portuguese]{babel}
\usepackage{multicol}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{xcolor}
\usepackage{tikz,pgfplots,tikz-3dplot,bm}
\usepackage{circuitikz}
\usepackage{tkz-base}
\usepackage{tkz-fct}
\usepackage{tkz-euclide}
\usepackage[a4paper, portrait, margin=2cm]{geometry}

\usetikzlibrary{arrows,3d,calc,automata,positioning,shadows,math,fit,shapes}
\usetikzlibrary{patterns,hobby,optics,calc}
\tikzset{>=stealth, thick, global scale/.style={scale=#1,every node/.style={scale=#1}}}
\setlength{\columnsep}{1cm}
\renewcommand{\choiceshook}{\setlength{\leftmargin}{0pt}}

        """

    def template_document(self, code):

        template = f"""
        \\begin{{minipage}}[b]{{0.75\linewidth}}
            \\begin{{flushleft}}
                {{\\bf \large {self.title}}}
            \\end{{flushleft}}
            \\begin{{flushleft}}
                {{\\bf \large {self.subtitle}}}
            \\end{{flushleft}}
        \\end{{minipage}}
        \\begin{{minipage}}[b]{{0.20\linewidth}}
            \\begin{{flushright}}
                {{\\bf \large Código: {code}}}
            \\end{{flushright}}
        \\end{{minipage}}
        \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}
        \\begin{{minipage}}{{0.75\linewidth}}
            Aluno:
        \\end{{minipage}}
        \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}

        """
        return template

    def add_question(self, point, qcode):

        lista = list()

        modules = [
            electrostatic,
            electrodynamics,
            magnetism,
            induced_magnetic_field,
            particle_wave_duality,
            uncertainty_principle,
            schrodinger_equation
            ]

        for i in range(self.ntest):

            for module in modules:
                item = module.question(point, qcode)
                if bool(item) == True:
                    quest = item

            value_list = list()
            resultado = list()

            text = quest['text']
            figure = quest['figure']
            type = quest['type']

            for item in quest['alternative']:
                resultado.append(item['point'])
                value = {'choice': item['choice'], 'unit': item['unit']}
                value_list.append(value)

            lista.append({ 'code': qcode, 'test': i, 'type': type, 'text': text, 'figure': figure, 'alternative': value_list, 'result': resultado})

        self.question_list.append(lista)

        self.question_point.append(point)

        self.nquestion += 1

    def make_exam(self):

        with open('main.tex', 'w') as file:

            file.write(self.template)

            file.write(r'\begin{document}'+'\n')

            for i in range(self.ntest):

                file.write(self.template_document(i))

                if self.question_list:

                    file.write(r'\begin{questions}'+'\n')

                    file.write(r'\begin{multicols*}{2}'+'\n')

                    for j in range(self.nquestion):

                        file.writelines(r'\question['+str(self.question_point[j])+r'] '+self.question_list[j][i]['text']+'\n\n')

                        if self.question_list[j][i]['figure']:
                            os.system(f"cp {BASE_DIR}/src/dbquaest/img/{self.question_list[j][i]['figure']}.jpg .")
                            file.write(r'\begin{center}'+'\n')
                            file.write(r'\begin{minipage}[c]{0.50\linewidth}'+'\n')
                            file.write(r'\includegraphics[width=\textwidth]'+'{'+self.question_list[j][i]['figure']+'.jpg}\n')
                            file.write(r'\end{minipage}'+'\n')
                            file.write(r'\end{center}'+'\n')

                        if self.question_list[j][i]['type'] == 'objective':

                            file.write(r'\begin{oneparchoices}'+'\n')

                            for item in self.question_list[j][i]['alternative']:
                                key_1 = item['choice']
                                key_2 = item['unit']
                                if abs(key_1) < 1.e-2 or key_1 > 1.e+3:
                                    file.write(f'\\choice {key_1:.1e};')
                                else:
                                    file.write(f'\\choice {key_1:7.3f};')

                            file.write(r'\end{oneparchoices}'+'\n')

                        elif self.question_list[j][i]['type'] == 'conceptual':

                            file.write(r'\begin{choices}'+'\n')

                            for item in self.question_list[j][i]['alternative']:
                                file.write(f"\\choice {item['choice']} {item['unit']}")

                            file.write(r'\end{choices}'+'\n')

                    file.write(r'\end{multicols*}'+'\n')
                    file.write(r'\end{questions}'+'\n')

                file.write(r'\newpage')

            file.write(r'\end{document}')
            file.close()
      
        os.system('pdflatex main.tex')
        os.system('rm main.aux main.log')

    def make_correction(self):

        with open('main_result.tex', 'w') as file:

            file.write(self.template)

            file.write(r'\begin{document}'+'\n')

            for i in range(self.ntest):

                file.write(self.template_document(i))

                file.write(r'\begin{center}'+'\n'+r'\textcolor{red}{\emph\Large Correcting version}'+r'\end{center}'+'\n')

                if self.question_list:

                    file.write(r'\begin{questions}'+'\n')
                    file.write(r'\begin{multicols*}{2}'+'\n')

                    for j in range(self.nquestion):

                        file.writelines(r'\question['+str(self.question_point[j])+r'] '+self.question_list[j][i]['text']+'\n\n')

                        if self.question_list[j][i]['figure']:
                            os.system(f"cp {BASE_DIR}/src/dbquaest/img/{self.question_list[j][i]['figure']}.jpg .")
                            file.write(r'\begin{center}'+'\n')
                            file.write(r'\begin{minipage}[c]{0.75\linewidth}'+'\n')
                            file.write(r'\includegraphics[width=\textwidth]'+'{'+self.question_list[j][i]['figure']+'.jpg}\n')
                            file.write(r'\end{minipage}'+'\n\n')
                            file.write(r'\end{center}'+'\n')

                        file.write(r'\begin{oneparchoices}'+'\n')

                        for alternative in self.question_list[j][i]['result']:
                            file.write(f'\\choice {alternative}')

                        file.write(r'\end{oneparchoices}'+'\n')

                    file.write(r'\end{multicols*}'+'\n')
                    file.write(r'\end{questions}'+'\n')

                file.write(r'\newpage')

            file.write(r'\end{document}')
            file.close()
      
        os.system('pdflatex main_result.tex')
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