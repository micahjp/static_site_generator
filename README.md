# Static Site Generator

This program generates a static site from markdown files.

### How to use

Simply drop the markdown files you would like to use into the 'content' directory.
* If you have multiple pages you will have to create subdirectories and add relative links to the Markdown files [(see example)](/content/index.md).
* If you have images or css style sheets you want to use drop them inside the 'static' directory, just make sure your css file name matches the linked style sheet in 'template.html'.

Next, run the main.sh script. This will generate your html files and start a python server that locally hosts your site. Navigate to the URL displayed inside the parenthesis to see your site!

Keep in mind every time you run the main.sh file everything that was previously generated is removed and new files are generated based on the 'content' and 'static' directories so any changes you make to those files will be reflected in the site after running.

Also all of the generated files will, by default, be placed in a directory called 'public'. If this directory does not exist it will be created.

### Markdown Guidelines

This project supports the following markdown elements:
    * Headings,
    * Regular text,
    * Bold text,
    * Italic text,
    * Hyperlinked text,
    * Code snippets,
    * Code blocks,
    * Quote blocks,
    * Unordered lists,
    * Ordered lists
