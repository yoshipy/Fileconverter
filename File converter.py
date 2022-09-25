import pypandoc
import easygui
from easygui import *
import pathlib

print('please select a file to convert...')


inputfile = easygui.fileopenbox()

inputsuffix = pathlib.Path(inputfile).suffix

print(inputsuffix)

inputsuffix = inputsuffix.replace('.', '')


choices = ['pptx', 'revealjs', 'rst', 'rtf', 's5', 'slideous', 'slidy', 'tei', 'texinfo', 'textile', 'xwiki', 'zimwiki', 'json','docx']


msg = "What would you like to convert the file to?"
reply = buttonbox(msg, choices=choices)

print(reply)

outputfile = easygui.filesavebox()

output = pypandoc.convert_file(inputfile, format=inputsuffix, to=reply, outputfile=outputfile+'.'+reply, extra_args=['-RTS'])



print('your file has been saved as ' + outputfile)
