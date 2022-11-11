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
\usepackage[a4paper, portrait, margin=2cm]{geometry}

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
    \\begin{{minipage}}\[c\]{{0.50\linewidth}}
        \\includegraphics[width=\textwidth]{{{figure}.jpg}}
    \\end{{minipage}}
\\end{{center}}
"""

    return template

def template_document(code, title, subtitle, name, clss):

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
    \\begin{{minipage}}{{0.75\linewidth}}
        \\begin{{flushleft}}
            Student: {name}
        \\end{{flushleft}}
    \\end{{minipage}}
    \\begin{{minipage}}{{0.20\linewidth}}
        \\begin{{flushright}}
            Class: {clss}
        \\end{{flushright}}
    \\end{{minipage}}
    \\vspace{{0.5cm}} \\hrule \\vspace{{0.5cm}}
    """
    return template