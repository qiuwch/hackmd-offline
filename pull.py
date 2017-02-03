import json, urllib2, argparse, os, logging
logging.basicConfig(level=logging.INFO)

# TODO: How to avoid downloading a note without any update?
# Is the time in the json update time?

# TODO: Some the files can not be downloaded because they are not publicly available. Print out these files.

parser = argparse.ArgumentParser()
parser.add_argument('jsonfile', help = 'The json file with notes information')
args = parser.parse_args()

jsonfile = args.jsonfile
notes = json.load(open(jsonfile))
note_folder = 'notes' # Where to save markdown files
if not os.path.isdir(note_folder):
    os.mkdir(note_folder)

print 'Number of notes: %d' % len(notes)

template = 'https://hackmd.io/{id}/download'
for note in notes:
    url = template.format(**note)
    title = note['text'].encode('utf-8')
    # filename = title.replace(' ', '-') + '.md'
    filename = '{folder}/{id}{time}.md'.format(id=note['id'], time=note['time'], folder=note_folder)
    logging.debug('Dump note to file: %s' % filename)
    # The old version will remain
    if not os.path.isfile(filename): # If does not exist
        try:
            txt = urllib2.urlopen(url)
            with open(filename, 'w') as f:
                f.write(txt.read())
            print 'Save {title} to {filename}'.format(title=title, filename=filename)
        except Exception as e:
            print 'Fail to save {title}, maybe this is a private note'.format(title=title)
            print '\t' + str(e)
    else:
        pass # Skip exsiting version
