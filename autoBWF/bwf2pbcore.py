import argparse
import re
import xml.etree.ElementTree as ET
from os import path
from autoBWF.BWFfileIO import *


def main():
    namespaces = {"xml": "http://www.w3.org/XML/1998/namespace",
                  "pbcore": "http://www.pbcore.org/PBCore/PBCoreNamespace.html",
                  "ohms": "https://www.weareavp.com/nunncenter/ohms"}

    for ns in namespaces.keys():
        ET.register_namespace(ns, namespaces[ns])

    def qualified_element(ns, element):
        return "{{{0}}}{1}".format(namespaces[ns], element)

    def add_child(parent, element_name, element_value, attributes=None, namespace="pbcore", allow_empty=False):
        if namespace is not None:
            element_name = qualified_element(namespace, element_name)
        if element_value != "" or allow_empty:
            element = ET.SubElement(parent, element_name)
            element.text = element_value
            if attributes is not None:
                for attribute in attributes.keys():
                    element.set(attribute, attributes[attribute])
            return element

    def add_multivalue_child(parent, element_name, element_value, attributes=None, namespace="pbcore"):
        wikidata_regex = re.compile(r'(.+)\s+\{(Q\d+)\}')

        if element_value != "":
            items = element_value.split(';')
            for item in items:
                m = wikidata_regex.match(item)
                if m:
                    matches = m.groups()
                    name = matches[0]
                    q_code = matches[1]
                    child = add_child(parent, element_name, name,
                                      {"source": "wikidata",
                                       "ref": "https://www.wikidata.org/wiki/{}".format(q_code)})
                else:
                    child = add_child(parent, element_name, item.strip())

                if attributes is not None:
                    for attribute in attributes.keys():
                        child.set(attribute, attributes[attribute])

    def add_complex_child(parent, element_name, subelement_name, role_name, subelement_value,
                          role_value, namespace="pbcore"):
        wikidata_regex = re.compile(r'(.+)\s+\{(Q\d+)\}')

        if namespace is not None:
            element_name = qualified_element(namespace, element_name)

        if subelement_value != "":
            items = subelement_value.split(';')
            for item in items:
                element = ET.SubElement(parent, element_name)
                m = wikidata_regex.match(item)
                if m:
                    matches = m.groups()
                    name = matches[0]
                    q_code = matches[1]
                    add_child(element, subelement_name, name,
                              {"source": "wikidata",
                               "ref": "https://www.wikidata.org/wiki/{}".format(q_code)})
                else:
                    add_child(element, subelement_name, item.strip())

                add_child(element, role_name, role_value)

    parser = argparse.ArgumentParser(
        description='Extract metadata from BWF and create PBCore XML, incorporating existing OHMS XML as an extension')
    parser.add_argument('infile', nargs="+", help="WAV file(s)")
    args = parser.parse_args()

    for infile in args.infile:
        ohmsfile = infile.rsplit('.', 1)[0] + '_ohms.xml'
        outfile = infile.rsplit('.', 1)[0] + '_pbcore.xml'

        metadata = get_bwf_core(True, infile)
        metadata.update(get_bwf_tech(True, infile))
        metadata.update(get_xmp(infile, ["bwfmetaedit", "--specialchars", "--accept-nopadding"]))

        pbcore_root = ET.Element(qualified_element("pbcore", "pbcoreDescriptionDocument"))
        pbcore_root.append(ET.Comment('Automatically generated by bwf2pbcore. DO NOT EDIT BY HAND.'))
        pbcore_root.append(ET.Comment('To make changes, edit the internal metadata in {}'.format(infile)))
        pbcore_root.append(ET.Comment('and re-run bwf2pbcore'))

        add_child(pbcore_root, "pbcoreAssetType", metadata["form"])
        add_child(pbcore_root, "pbcoreAssetDate", metadata["ICRD"])
        add_child(pbcore_root, "pbcoreIdentifier", metadata["FileContent"], {"source": "local"})
        add_child(pbcore_root, "pbcoreTitle", metadata["INAM"])

        add_multivalue_child(pbcore_root, "pbcoreSubject", metadata["topics"], {"subjectType": "topic"})
        add_multivalue_child(pbcore_root, "pbcoreSubject", metadata["names"], {"subjectType": "name"})
        add_multivalue_child(pbcore_root, "pbcoreSubject", metadata["events"], {"subjectType": "period"})
        add_multivalue_child(pbcore_root, "pbcoreSubject", metadata["places"], {"subjectType": "geographic"})

        add_child(pbcore_root, "pbcoreDescription", metadata["xmp_description"])

        add_complex_child(pbcore_root, "pbcoreContributor", "contributor",
                          "contributorRole", metadata["interviewer"], "interviewer")
        add_complex_child(pbcore_root, "pbcoreContributor", "contributor",
                          "contributorRole", metadata["interviewee"], "interviewee")
        add_complex_child(pbcore_root, "pbcoreContributor", "contributor",
                          "contributorRole", metadata["host"], "host")
        add_complex_child(pbcore_root, "pbcoreContributor", "contributor",
                          "contributorRole", metadata["speaker"], "speaker")
        add_complex_child(pbcore_root, "pbcoreContributor", "contributor",
                          "contributorRole", metadata["performer"], "performer")

        if metadata["owner"] != "":
            publisher = ET.SubElement(pbcore_root, qualified_element("pbcore", "pbcorePublisher"))
            add_child(publisher, "publisher", metadata["owner"])
            add_child(publisher, "publisherRole", "copyright holder")

        rights = ET.SubElement(pbcore_root, qualified_element("pbcore", "pbcoreRightsSummary"))
        add_child(rights, "rightsSummary", metadata["ICOP"])

        instantiation = ET.SubElement(pbcore_root, qualified_element("pbcore", "pbcoreInstantiation"))
        add_child(instantiation, "instantiationIdentifier", metadata["OriginatorReference"],
                  attributes={"source": "local"})
        add_child(instantiation, "instantiationLocation", infile)
        add_child(instantiation, "instantiationDuration", metadata["Duration"].split('.')[0])
        add_child(instantiation, "instantiationLanguage", "".join(metadata["language"].split()))  # eliminate whitespace

        add_child(pbcore_root, "pbcoreAnnotation", metadata["ISRC"], {"annotationType": "source collection"})

        if path.isfile(ohmsfile):
            ohms_root = ET.parse(ohmsfile).getroot()
            extension = add_child(instantiation, "instantiationExtension", "", allow_empty=True)
            embedded = add_child(extension, "extensionEmbedded", "", allow_empty=True)
            embedded.append(ohms_root)

        ET.ElementTree(pbcore_root).write(outfile, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    main()
