# coding: utf-8

# Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](
# academicpages.github.io).
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and
#  citation style.

# Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url,
# with a header at the top.
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. - `pub_date` must be formatted as
# YYYY-MM-DD. - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the
# paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[
# yourdomain]/publications/YYYY-MM-DD-[url_slug]`

import os

import pandas as pd

# Import TSV
#
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this
# kind of data and comma-separated values can get messed up. However, you can modify the import statement,
# as pandas also has read_excel(), read_json(), and others.

publications = pd.read_csv("publications.tsv", sep="\t", header=0)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


for row, item in publications.iterrows():

    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]

    # YAML variables

    md = "---\ntitle: \"" + item.title + '"\n'

    md += """collection: publications"""

    md += """\npermalink: /publication/""" + html_filename

    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"

    md += "\ndate: " + str(item.pub_date)

    md += "\nvenue: '" + html_escape(item.venue) + "'"

    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"

    md += "\ncitation: '" + html_escape(item.citation) + "'"

    md += "\n---"

    # Markdown description for individual page

    if len(str(item.paper_url)) > 5:
        md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>\n"

    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"

    md += "\nRecommended citation: " + item.citation

    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
