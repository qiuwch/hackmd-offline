import json, urllib2
notes = json.load(open('./hackmd_history_20170126160244.json'))

print 'Number of notes: %d' % len(notes)
# for f in files:
#     print f
# for f in files:
#     print f['id']

template = 'https://hackmd.io/{id}/download'
for note in notes:
    url = template.format(**note)
    title = note['text']
    filename = title.replace(' ', '-') + '.md'
    try:
        print 'Save {title} to {filename}'.format(title=title, filename=filename)
        txt = urllib2.urlopen(url)
        with open(filename, 'w') as f:
            f.write(txt.read())
    except Exception as e:
        print e
