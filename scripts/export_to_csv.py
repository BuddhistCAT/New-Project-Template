f = open('exports/en.csv', 'w')

import polib
po = polib.pofile('wip/en/001.po')

for entry in po:

    f.write(entry.msgid.replace(' ' ,'').replace('␣', '').replace(' ', ' ') + ',')
    f.write(entry.msgstr + '\n')

f.close()
