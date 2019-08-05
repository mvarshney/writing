# -*- coding: utf-8 -*-
import codecs

def header():
     return """<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name=viewport content="width=device-width, initial-scale=1">
    <style>
    p {font-size: 120%;}
    .uvach {
        margin-left: 60px;
        font-style: italic;
        font-weight: bold;
    }
    </style>
</head>
<body>
"""

def mark_word(word):
    if word[:2] == '**' and word[-2:] == '**':
        return "<u>" + word[2:-2] + "??</u>"
    else:
        return word
        

def compile(infile, outfile):
    f = codecs.open(infile, encoding='utf-8')
    html = header()
    for line in f:
        line = line.strip()
        if line == '':
            html += "<p>\n"
        elif line[0] == '[' and line[-1] == ']':
            html += '<div class="uvach">' + line[1:-1] + "</div>\n"
        else:
            words = [mark_word(w) for w in line.split(" ")]
            line = " ".join(words)
            if ":-" in line:
                before, after = line.split(":-")
                line = "<strong>" + before + " :-</strong> " + after
            html += line
            html += "<br>\n"
    html += "</body></html>"
    codecs.open(outfile, "w", encoding='utf-8').write(html)

compile("docs/hindi-gita/chapter1.txt", "html/gita1.html")
compile("docs/hindi-gita/chapter2.txt", "html/gita2.html")
compile("docs/hindi-gita/chapter3.txt", "html/gita3.html")
compile("docs/hindi-gita/chapter4.txt", "html/gita4.html")
compile("docs/saadhak_maanas.txt", "html/saadhak_maanas.html")
compile("docs/dohavali2.txt", "html/dohavali2.html")
compile("docs/dohavali3.txt", "html/dohavali3.html")
compile("docs/dohavali4.txt", "html/dohavali4.html")
compile("docs/dohavali_baapu.txt", "html/dohavali_baapu.html")
compile("docs/QA/shishya_guru1.txt", "html/samvad1.html")
compile("docs/QA/shishya_guru2.txt", "html/samvad2.html")
compile("docs/QA/shishya_guru3.txt", "html/samvad3.html")
compile("docs/QA/aadhyatmik.txt", "html/prashnotari1.html")
compile("docs/QA/shriram_vasisth.txt", "html/shreeram_vasisth.html")