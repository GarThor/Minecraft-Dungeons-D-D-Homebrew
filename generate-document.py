#!/usr/bin/python3

def read_content(file_name = ""):
    page = open("source/" + file_name, "r")
    content = page.read()
    page.close()
    return content

def add_pagebreak(doc):
    doc.write("\n\\page\n\n")

def main():
    # Clear/Create the document
    doc = open("document.md", "w+")
    doc.write("")
    doc.close()

    # Open the document for writing
    doc = open("document.md", "a")
    page = read_content("title-page.md")
    doc.write(page)
    add_pagebreak(doc)

    page = read_content("table-of-contents.md")
    doc.write(page)
    add_pagebreak(doc)

    page = read_content("character-building.md")
    doc.write(page)
    add_pagebreak(doc)

    doc.write('# Gear <a id="Gear" name="Gear"></a>\n\n')

    doc.write("## Melee Weapons\n\n")
    page = read_content("melee-weapons-common.md")
    doc.write(page)
    add_pagebreak(doc)
    page = read_content("melee-weapons-unique.md")
    doc.write(page)
    add_pagebreak(doc)
    page = read_content("melee-weapon-enchantments.md")
    doc.write(page)
    add_pagebreak(doc)

    doc.write("## Ranged Weapons\n\n")
    page = read_content("ranged-weapons-common.md")
    doc.write(page)
    add_pagebreak(doc)
    page = read_content("ranged-weapons-unique.md")
    doc.write(page)
    add_pagebreak(doc)
    page = read_content("ranged-weapon-enchantments.md")
    doc.write(page)
    add_pagebreak(doc)

    doc.write("## Armor\n\n")
    page = read_content("armor-common.md")
    doc.write(page)
    add_pagebreak(doc)
    page = read_content("armor-unique.md")
    doc.write(page)
    add_pagebreak(doc)
    page = read_content("armor-enchantments.md")
    doc.write(page)
    add_pagebreak(doc)

    page = read_content("monsters.md")
    doc.write(page)

    doc.close()

if __name__ == '__main__':
    main()