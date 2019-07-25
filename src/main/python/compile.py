# -*- coding: utf-8 -*-
import codecs

def header():
     return """<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
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
            html += " ".join(words)
            html += "<br>\n"
    html += "</body></html>"
    codecs.open(outfile, "w", encoding='utf-8').write(html)

compile("docs/saadhak_maanas.txt", "saadhak_maanas.html")