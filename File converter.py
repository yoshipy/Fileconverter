import pypandoc
import easygui
from easygui import *
import pathlib
import os

print('please select a file to convert...')


inputfile = easygui.fileopenbox(multiple=True)

inputsuffix = inputfile[0]
inputsuffix = pathlib.Path(inputsuffix).suffix

print(inputsuffix)

inputsuffix = inputsuffix.replace('.', '')


choices = ['pptx', 'html', 'revealjs', 'rst', 'rtf', 's5', 'slideous', 'slidy', 'tei', 'texinfo', 'textile', 'xwiki', 'zimwiki', 'json','docx', 'md']


msg = "What would you like to convert the file to?"
reply = buttonbox(msg, choices=choices)

print(reply)

print('please select a folder to save the converted files in...')
outputfolder = easygui.diropenbox()

print(outputfolder)


for element in inputfile:
    path = os.path.basename(element)
    output = pypandoc.convert_file(element, format=inputsuffix, to=reply, outputfile=outputfolder+'/'+path+'.'+reply, extra_args=['-RTS'])



print('your file has been saved as ')
