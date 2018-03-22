\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{4af14}[1]
\LoadClass[a4paper, 11pt]{article}
\usepackage[french,english]{babel}
%\RequirePackage[english]{babel}
\RequirePackage{fancyhdr}
\RequirePackage{hyperref}

%%%%%% Macros liees a une conf particuliere %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\@conftitle}{\textit{Jeanne Ventre}}
\newcommand{\@confdate}{\textit{\today}}

%%%%%% definition des marges %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\setlength{\paperwidth}{210mm}
\setlength{\paperheight}{297mm}

\setlength{\hoffset}{-5.4mm}     % marge gauche 2 cm
\setlength{\textwidth}{170mm}    % marge droite 2 cm
\setlength{\oddsidemargin}{0mm}  % pas de marge de note
\setlength{\marginparsep}{0mm}
\setlength{\marginparwidth}{0mm}
\setlength{\marginparpush}{0mm}


\setlength{\voffset}{-7.9mm}     % marge haute 1.25 cm
\setlength{\textheight}{245mm}   % marge basse 1 cm
\setlength{\topmargin}{-8mm}      % entete
\setlength{\headheight}{7mm}
\setlength{\headsep}{3mm}
\setlength{\footskip}{13mm}      % pied de page

%%%%%%% Definition des fonts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\renewcommand\normalsize{\fontsize{11pt}{13pt}\selectfont} %\fontsize{taille}{interligne}
\renewcommand\large{\fontsize{14pt}{16pt}\selectfont}
\renewcommand\LARGE{\fontsize{18pt}{22pt}\selectfont}
\renewcommand\tiny{\fontsize{10pt}{12pt}\selectfont}

%%%%%%% En-tete %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\pagestyle{fancy}
\lhead{\@conftitle}
\chead{}
\rhead{\@confdate}
\lfoot{}
\cfoot{\thepage}
\rfoot{}

%%%%%%% Paragraphe de base %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 2pt minus 1 pt}

%%%%%%% Titre %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% redefinition de la commande \author
\global\let\@author\@empty
\global\let\author\relax
\def\author#1{\gdef\@author{#1}}

\newcommand{\inst}[1]{\textsuperscript{\normalfont\bfseries #1}}

\def\addtoks#1\to#2{%
  \begingroup
  \toks0={#1}%
  \toks1=\expandafter{#2}%
  \edef\next{\def\noexpand#2{\the\toks1 \the\toks0 }}%
  \expandafter\endgroup\next
}

% redefinition de la commande \instlabel
\global\let\@instlabel\@empty
\global\let\instlabel\relax
\newcommand{\instlabel}[2]{\addtoks{#1. \textit{#2}\\}\to\@instlabel }


\renewcommand\maketitle{%
  \newpage
  \null
  \vskip 20pt%2em%
  \begin{center}%
  \let \footnote \thanks
    {\LARGE\bfseries \@title \par}%
    \vskip 1.5em%
    {\scshape \bfseries 
      \lineskip .5em%
       \@author\par}%
    %\vskip .5em%
    {  \lineskip .5em%
       \@instlabel\par}%
    \vskip 1em%
  \end{center}%
  \par
  \vskip 1.5em}

%%%%%%% Abstract %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newenvironment{resume}{%
{\large\bfseries R\'{e}sum\'{e}~:}\par\vspace{0.5mm}}%
{\par\vspace{5pt}}

\renewenvironment{abstract}{%
{\large\bfseries Abstract~:}\par\vspace{0.5mm}}%
{\par\vspace{5pt}}

%%%%%%% Mot clefs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% /!\ verifier ce qui se passe lorsqu'il y a trop de mot pour tenir
% sur une seule ligne.

\newcommand{\keywords}[1]{{\large\bfseries Mots clefs~:~}{\bfseries #1}\par\vspace{3mm}}



%%%%%%%% Les sections %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% http://help-csli.stanford.edu/tex/latex-sections.shtml

\renewcommand\section{\@startsection {section}{1}{\z@}%
                                     {-1.4ex}%
                                     {0.1ex}%
                                   {\normalfont\large\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
                                     {-1.4ex}%
                                     {0.1ex}%
                                     {\normalfont\large\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-1.4ex}%
                                     {0.1ex}%
                                     {\normalfont\large\bfseries}}

%%%%%%%% Les figures %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
