from xml.etree import ElementTree

tree = ElementTree.parse("xml-example-modified.xml")
root = tree.getroot()

greg = root[0]
# print(root.tag, root.attrib)

# for child in root:
# print(child.tag, child.attrib)

# print(root[0][0].text)
#
# for element in root.iter("scores"):
#     sum_score = 0
#     for child in element:
#         sum_score += float(child.text)
#     print(sum_score)

description = greg.find("description")

tree.write("xml-example-modified.xml")
