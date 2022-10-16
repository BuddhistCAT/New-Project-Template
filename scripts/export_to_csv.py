import sys

target_language = sys.argv[1]

file_path = 'exports/' + target_language + '.csv'

print(file_path)

f = open(file_path, 'w')

import polib
po = polib.pofile('wip/' + target_language + '/001.po')

for entry in po:

    f.write(entry.msgid.replace(' ' ,'').replace('␣', '').replace(' ', ' ') + ',')
    f.write(entry.msgstr + '\n')

f.close()
