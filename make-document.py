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

# def find_attribute(node, name):
#       if node == None:
#             return None
#       if node.attributes == None or len(node.attributes) == 0:
#             return None
#       for attr in node.attributes:
#             if attr.name == name:
#                   return node

def title_to_anchor_link(title=""):
      return title.replace(" ", "-").lower()

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
                        result += " [{0}](#{1})".format(attr.value, title_to_anchor_link(attr.value))
                        if level == 0:
                              result += "**"
                        result += "\n"
                  childSections = section.childNodes
                  result += process_section_for_toc(childSections, level+1, indexStack)
                  indexStack.pop()
      return result

def generate_table_of_contents(collection):
      table = "<div class='toc'>\n\n# Table Of Contents\n\n"

      sections = collection.childNodes

      table += process_section_for_toc(sections)
      
      table += "\n</div>\n\n\page\n\n"
      return table

def process_section_for_doc(sections, level = 0):
      result = ""
      curIdx = 0
      for section in sections:
            if section.nodeType == section.ELEMENT_NODE:
                  title = section.getAttributeNode("title")
                  page = section.getAttributeNode("page")
                  appendPage = section.getAttributeNode("appendPage")
                  if title != None:
                        curIdx = curIdx + 1
                  if title != None:
                        result += ("#" * (level+1)) + " " + title.value
                        result += " <a id=\"{0}\" name=\"{0}\"></a>".format(title_to_anchor_link(title.value))
                        result += "\n\n"
                  if page != None:
                        pageFile = open(page.value, "r")
                        result += pageFile.read()
                        pageFile.close()
                  if appendPage == None:
                        result += "\n\page\n\n"
                  elif appendPage != None and appendPage.value == True:
                        result += "\n\page\n\n"
                  else:
                        result+= "\n"
                  childSections = section.childNodes
                  result += process_section_for_doc(childSections, level+1)
      return result

def generate_doc(collection):
      sections = collection.childNodes
      data = process_section_for_doc(sections)
      return data

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

      data = generate_doc(collection)
      write_content(data, doc)

      doc.close()

if __name__ == '__main__':
    main()