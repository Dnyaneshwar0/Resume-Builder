# formatter/latex_formatter.py

def format_to_latex(resume_data, industry="general"):
    templates = {
        "general": r"""
\documentclass{{article}}
\usepackage[margin=1in]{{geometry}}
\begin{{document}}

\section*{{{name}}}
\textbf{{Email:}} {email} \\
\textbf{{Phone:}} {phone} \\

\section*{{Experience}}
{experience}

\section*{{Education}}
{education}

\section*{{Skills}}
{skills}

\end{{document}}
""",
        # You can add 'tech', 'finance', etc. templates here
    }

    return templates[industry].format(
        name=resume_data["name"],
        email=resume_data["email"],
        phone=resume_data["phone"],
        experience=resume_data["experience"],
        education=resume_data["education"],
        skills=", ".join(resume_data["skills"])
    )
