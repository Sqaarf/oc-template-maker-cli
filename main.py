from docx import Document

def parseConf():
    content = []
    with open("./template.conf", "r", encoding="utf-8") as f:
        for line in f.readlines():
            content.append(line.strip())
    return content

content_conf_file = parseConf()
main_title, entries = (content_conf_file[0], content_conf_file[1:])

document = Document()

document.add_heading(main_title, 0)

for entry in entries:
    entry_title, entry_content = entry.split(":")
    document.add_heading(entry_title, level=1)
    p = document.add_paragraph(entry_content)

document.save('demo.docx')