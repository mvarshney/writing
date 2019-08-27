# -*- coding: utf-8 -*-
import textwrap
import codecs

# https://www.google.com/intl/hi/inputtools/try/

begin_jap = u"ॐ श्रीपरमात्मने नमः"
end_jap = u"हरिः ॐ तत्सत् हरिः ॐ तत्सत् हरिः ॐ तत्सत्"

chapter_begin_format = u"अथ %s"
chapter_end_format = u"॥इति %s॥"

hindi_numbers = [
    u"०",
    u"१",
    u"२",
    u"३",
    u"४",
    u"५",
    u"६",
    u"७",
    u"८",
    u"९",
    u"१०",
    u"११",
    u"१२",
    u"१३",
    u"१४",
    u"१५",
    u"१६",
    u"१७",
    u"१८"
]

chapter_numbers = [
    "",  #index 0 unused
    u"प्रथमोऽध्यायः",
    u"द्वितीयोऽध्यायः",
    u"तृतीयोऽध्यायः",
    u"चतुर्थोऽध्यायः",
    u"पंचमोऽध्यायः",
    u"षष्ठोऽध्यायः"
]

chapter_names = [
    "", # index 0 unused
    u"अर्जुनविषादयोगः",
    u"सांख्ययोगः",
    u"कर्मयोगः",
    u"ज्ञानकर्मसन्यासयोगः",
    u"कर्मसन्यासयोगः",
    u"आत्मसंयमयोगः"
]

ROOT = "/Users/mvarshne/Documents/Maneesh/translation/writing/src/main/"
TEXTROOT = ROOT + "docs/hindi-gita/"
BOOKROOT = ROOT + "book/"

def mark_word(word):
    if word[:2] == '**' and word[-2:] == '**':
        return "<u>" + word[2:-2] + "??</u>"
    else:
        return word

def make_chapter(chnum):
    # making header
    chname = "%s) %s" % (hindi_numbers[chnum], chapter_names[chnum])
    header = u"""
    .. centered::
    	``~ ॐ श्रीपरमात्मने नमः ~``

    .. centered::
    	``॥ अथ %s ॥`` 
    
    .. title %s
    
    %s
    ----------------------------------------------------------
    """ % (chapter_numbers[chnum], chname, chname)
    
    header = textwrap.dedent(header)
    
    infile = TEXTROOT + ("chapter%d.txt" % chnum)
    f = codecs.open(infile, encoding='utf-8')
    body = ""
    for line in f:
        line = line.strip()
        if line == '':
            body += "\n"
            #body += "\n::\n\n"
        elif line[0] == '[' and line[-1] == ']':
            body += ".. centered::\n\t``" + line[1:-1] + "``\n"
            #body += "\t" + line[1:-1] + "\n"
        else:
            words = [mark_word(w) for w in line.split(" ")]
            line = " ".join(words)
            body += "| " + line + "\n"
    
    trailer = u"""
    .. centered::
        ``॥इति %s॥``

    .. centered::
        ``हरिः ॐ तत्सत् ~ हरिः ॐ तत्सत् ~ हरिः ॐ तत्सत्``
    """ % chapter_numbers[chnum]
    trailer = textwrap.dedent(trailer)
    
    rest = header + body + trailer
    
    outfile = BOOKROOT + ("chapter%s.rst" % chnum)
    codecs.open(outfile, "w", encoding='utf-8').write(rest)

    

for chnum in range(1, 7):
    make_chapter(chnum)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
