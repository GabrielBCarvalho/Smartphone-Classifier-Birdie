# encoding: iso-8859-1
import json_lines as jl
import sys
import csv


def main():
    if(len(sys.argv) < 3):
        print("Usage: 'python helper.py jl_file site_name'")
    else:
        write_file(sys.argv[1], sys.argv[2])


def write_file(source, site):
    with open(source, 'rb') as f:
        id = 0
        filename = "collected_datas_" + site + ".tsv"

        with open(filename, "w+", encoding='latin-1') as output_file:
            tsv_writer = csv.writer(output_file, delimiter = "\t")
            tsv_writer.writerow(['ID', 'TITLE', 'URL'])

            for item in jl.reader(f):
                document = []
                
                this_id = str(id)
                title = item['title']
                url = (item['url'])
                
                title = title.replace(u"\u00e2", "â")
                title = title.replace("\u201d", '"')
                title = title.replace(u"\u00e1", u"á")
                title = title.replace(u"\u00c1", u"à")
                title = title.replace(u"\u00ed", u"í")
                title = title.replace(u"\u00e9", u"é")
                title = title.replace(u"\u00e7", u"ç")
                title = title.replace(u"\u00e3", u"ã")
                title = title.replace(u"\u00cd", u"I")
                title = title.replace(u"\u00f3", u"ó")
                title = title.replace(u"\u00f5", u"õ")
                title = title.replace(u"\u00ea", u"ê")
                title = title.replace(u"\u00b4", u'"')
                title = title.replace(u"\u00fd", u'y')
                title = title.replace(u"\u00f4", u'ô')
                title = title.replace(u"\u2019\u2019", u'"')
                title = title.replace(u"\u2019", u"'")
                title = title.replace(u"\u2013", u'-')
                title = title.replace(u"\u2122", u'')
                title = title.replace(u"''", u'"')
                
                tsv_writer.writerow([id, title, url])
                id += 1

    print("File successfully created!")

main()