header = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tibetan Reader</title>
    <link rel="stylesheet" href="https://unpkg.com/flowbite@1.5.3/dist/flowbite.min.css" />
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+Tibetan&display=swap" rel="stylesheet">
</head>
<body>'''

tibetan = '<p class="ml-7 mb-1 mt-12 tracking-wide text-3xl text-gray-900 dark:text-white" style="font-family: Noto Serif Tibetan, serif;">'
translation = '<p class="ml-7 text-2xl text-gray-900 dark:text-white" style="font-family: Noto Serif, serif;">'
footer = '<script src="https://unpkg.com/flowbite@1.5.3/dist/flowbite.js"></script></body></html>'

import sys

target_language = sys.argv[1]

file_path = 'exports/' + target_language + '.html'

print(file_path)

f = open(file_path, 'w')

import polib
po = polib.pofile('wip/en/001.po')

f.write(header)
out = []
for entry in po:

    f.write(tibetan + entry.msgid.replace(' ' ,'').replace('␣', '').replace(' ', ' ') + '\n')
    f.write(translation + entry.msgstr + '\n')

f.write(footer)
f.close()
