import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
# import the lxml parser
from lxml import etree
import glob, os

#xsd = etree.XSD('bitcamp/Investment Adviser Firm Reports/IAPDSECBulkFeed.xsd')
IA_FIRM_SEC_Feed = etree.parse('Investment Adviser Firm Reports/IA_FIRM_SEC_Feed_04_11_2019.xml')
IA_FIRM_STATE_Feed = etree.parse('Investment Adviser Firm Reports/IA_FIRM_STATE_Feed_04_11_2019.xml')

def build_tree(Feed, root='//Firm'):
    node_list = []
    for firm in Feed.findall(root):
        # create an empty dictionary
        node_dict = {}
        # iterate over the elements that contain our data
        for child in firm.getchildren():
            # use the element name as the key and set that to the text
            node_dict[child.tag] = dict(child.items())
            for l2_child in child:
                l2_children = l2_child.getchildren()
                node_dict[l2_child.tag] = dict(l2_child.items())
                for l3_child in l2_child:
                    l3_children = l3_child.getchildren()
                    node_dict[l3_child.tag] = dict(l3_child.items())
                    type(l3_child)
                    for l4_child in l3_child:
                        l4_children = l4_child.getchildren()
                        node_dict[l4_child.tag] = dict(l4_child.items())
                        for l5_child in l4_child:
                            l5_children = l5_child.getchildren()
                            node_dict[l5_child.tag] = dict(l5_child.items())
        node_list.append(node_dict)
    node_list = [flatten(node) for node in node_list]
    df = pd.DataFrame(node_list)
    return df

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


# df_IA_FIRM_SEC_Feed = (build_tree(IA_FIRM_SEC_Feed))
# df_IA_FIRM_STATE_Feed = (build_tree(IA_FIRM_STATE_Feed))

# os.chdir("Investment Adviser Representatives Report")
df_feed = pd.DataFrame()
for file in glob.glob("Investment Adviser Representatives Report/IA_Indvl_Feeds*"):
    print(file)
    feed = etree.parse(file)
    df_feed = df_feed.append(build_tree(feed,"//Indvl"))
print(df_feed)
df_feed.to_csv('resps.csv')