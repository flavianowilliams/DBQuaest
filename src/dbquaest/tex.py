def template():

    template = r"""
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
\usepackage[a4paper, portrait, margin=2cm, includefoot]{geometry}
\usepackage[output-decimal-marker={,}]{siunitx}

\pagestyle{headandfoot}
\runningfootrule

\rfoot{\ifincomplete{Question \IncompleteQuestion\ continues on the next page\ldots}{}}

\usetikzlibrary{arrows,3d,calc,automata,positioning,shadows,math,fit,shapes}
\usetikzlibrary{patterns,hobby,optics,calc}
\tikzset{>=stealth, thick, global scale/.style={scale=#1,every node/.style={scale=#1}}}
\setlength{\columnsep}{1cm}
\renewcommand{\choiceshook}{\setlength{\leftmargin}{0pt}}

"""

    return template

def template_figure(figure):

    template = f"""
\\begin{{center}}
    \\begin{{minipage}}[c]{{\linewidth}}
        \\includegraphics[width=\\textwidth]{{{figure}.jpg}}
    \\end{{minipage}}
\\end{{center}}
"""

    return template

def template_document(code, title, subtitle, name, clss, var_date):

    template = f"""
    \\begin{{minipage}}[b]{{0.75\linewidth}}
        \\begin{{flushleft}}
            {{\\bf \large {title}}}
        \\end{{flushleft}}
        \\begin{{flushleft}}
            {{\\bf \large {subtitle}}}
        \\end{{flushleft}}
    \\end{{minipage}}
    \\begin{{minipage}}[b]{{0.20\linewidth}}
        \\begin{{flushright}}
            {{\\bf \large Code: {code}}}
        \\end{{flushright}}
    \\end{{minipage}}
    \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}
    \\begin{{minipage}}{{0.50\linewidth}}
        \\begin{{flushleft}}
            Student: {name}
        \\end{{flushleft}}
    \\end{{minipage}}
    \\begin{{minipage}}{{0.20\linewidth}}
        \\begin{{center}}
            Date: {var_date}
        \\end{{center}}
    \\end{{minipage}}
    \\begin{{minipage}}{{0.20\linewidth}}
        \\begin{{flushright}}
            Class: {clss}
        \\end{{flushright}}
    \\end{{minipage}}
    \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}
    """
    return template

def template_report(title, subtitle, clss, var_date):

    template = f"""
    \\begin{{minipage}}[b]{{0.75\linewidth}}
        \\begin{{flushleft}}
            {{\\bf \large {title}}}
        \\end{{flushleft}}
        \\begin{{flushleft}}
            {{\\bf \large {subtitle}}}
        \\end{{flushleft}}
    \\end{{minipage}}
    \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}
    \\begin{{minipage}}{{0.70\linewidth}}
        \\begin{{flushleft}}
            Date: {var_date}
        \\end{{flushleft}}
    \\end{{minipage}}
    \\begin{{minipage}}{{0.25\linewidth}}
        \\begin{{flushright}}
            Class: {clss}
        \\end{{flushright}}
    \\end{{minipage}}
    \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}
    """
    return template

def template_footer(constants, formulas):

    template = f"""
    \\runningfooter{{'Constants: '{constants}\linebreak 'Formulas: '{formulas}\linebreak\\\}}{{}}{{}}
    """

    return template