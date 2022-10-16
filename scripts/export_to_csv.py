import sys

target_language = sys.argv[0]

f = open('exports/' + target_language + '.csv', 'w')

import polib
po = polib.pofile('wip/' + target_language + '/001.po')

for entry in po:

    f.write(entry.msgid.replace(' ' ,'').replace('␣', '').replace(' ', ' ') + ',')
    f.write(entry.msgstr + '\n')

f.close()
