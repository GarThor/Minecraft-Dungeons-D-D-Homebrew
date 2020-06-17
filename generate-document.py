
def read_content(file_name = ""):
    page = open(file_name, "r")
    content = page.read()
    page.close()
    return content

def main():
    # Clear/Create the document
    doc = open("document.md", "w+")
    doc.write("")
    doc.close()

    # Open the document for writing
    doc = open("document.md", "a")
    page = read_content("title-page.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")

    page = read_content("table-of-contents.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")

    page = read_content("character-building.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")

    page = read_content("melee-weapons-common.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")
    page = read_content("melee-weapons-unique.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")
    page = read_content("melee-weapon-enchantments.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")

    page = read_content("ranged-weapons-common.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")
    page = read_content("ranged-weapons-unique.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")
    page = read_content("ranged-weapon-enchantments.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")

    page = read_content("armor-common.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")
    page = read_content("armor-unique.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")
    page = read_content("armor-enchantments.md")
    doc.write(page)
    doc.write("\r\n\r\n\\page\r\n\r\n")

    doc.close()

if __name__ == '__main__':
    main()