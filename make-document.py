#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom

def read_content(file_name = ""):
    page = open(file_name, "r")
    content = page.read()
    page.close()
    return content

def write_content(content, outFile, title="", anchor=""):
      if title != "":
            if anchor == "":
                  outFile.write("# " + title + "\n\n")
            else:
                  outFile.write("# " + title + 
                        "<a id='{0}' name='{0}'></a>\n\n".format(anchor))
      outFile.write(content)

def find_attribute(node, name):
      if node == None:
            return None
      if node.attributes == None or len(node.attributes) == 0:
            return None
      for attr in node.attributes:
            if attr.name == name:
                  return node

def process_section_for_toc(sections, level = 0, indexStack = []):
      result = ""
      curIdx = 0
      for section in sections:
            if section.nodeType == section.ELEMENT_NODE:
                  attr = section.getAttributeNode("title")
                  if attr != None:
                        curIdx = curIdx + 1
                  indexStack.append(curIdx)
                  if attr != None:
                        result += ("  " * level) + "- "
                        if level == 0:
                              result += "**"
                        for item in indexStack:
                              result += "{}.".format(item)
                        result += " [{0}]({1})".format(attr.value, attr.value.replace(" ", ""))
                        if level == 0:
                              result += "**"
                        result += "\n"
                  childSections = section.childNodes
                  result += process_section(childSections, level+1, indexStack)
                  indexStack.pop()
      return result

def generate_table_of_contents(doc):
      table = "<div class='toc'>\n\n# Table Of Contents\n\n"

      sections = doc.childNodes

      table += process_section_for_toc(sections)
      
      table += "\n</div>\n"
      return table

def main(indexFile="index.xml", outputFile="document.md"):
      # Clear/Create the document
      doc = open(outputFile, "w+")
      doc.write("")
      doc.close()

      doc = open(outputFile, "a")

      DOMTree = xml.dom.minidom.parse( indexFile )
      collection = DOMTree.documentElement
      titlePg = collection.getAttribute("titlePage")
      content = read_content(titlePg)
      write_content(content, doc)

      write_content("\n\\page\n\n", doc)

      toc = generate_table_of_contents(collection)
      write_content(toc, doc)

      section = collection.getElementsByTagName('section')

if __name__ == '__main__':
    main()