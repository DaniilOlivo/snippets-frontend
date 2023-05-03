import shutil
from os import path, listdir, mkdir
from jinja2 import Environment, PackageLoader

PATH_SCRIPT = path.dirname(__file__)

FOLDER_BUILD = path.join(PATH_SCRIPT, "page")
FOLDER_SNIPPETS = path.join(PATH_SCRIPT, "snippets")
FOLDER_STATIC_SNIPPETS = path.join(FOLDER_BUILD, "static")

HTML_SNIPPET = "index.html"
CSS_SNIPPET = "style.css"
JS_SNIPPET = "script.js"

env = Environment(loader=PackageLoader("src"))

def build_template(name_tempalte: str, context={}, name_build_html=""):
    full_name_template = name_tempalte + ".html.jinja"

    list_category = listdir(FOLDER_SNIPPETS)
    format_list_category = map(
        lambda category: category.title(),
        list_category
    )

    context["list_category"] = format_list_category

    template = env.get_template(full_name_template)

    if not name_build_html:
        name_build_html = full_name_template.rstrip(".jinja")
    else:
        name_build_html += ".html"

    with open(path.join(FOLDER_BUILD, name_build_html), "w") as f:
        f.write(template.render(**context))


def copy_static(path_src_file: str, new_name_file: str):
    shutil.copyfile(path_src_file, path.join(FOLDER_STATIC_SNIPPETS, new_name_file))


def create_structure():
    mkdir(FOLDER_BUILD)
    mkdir(FOLDER_STATIC_SNIPPETS)


def read_file(path_file: str):
    with open(path_file, "r") as f:
        return f.read()


def format_html(html):
    formated_html = ""
    for symbol in html:
        new_symbol = symbol
        if symbol == "<":
            new_symbol = "&lt"
        if symbol == ">":
            new_symbol = "&gt"

        formated_html += new_symbol
        
    return formated_html


def build():
    if not path.exists(FOLDER_BUILD):
        create_structure()

    build_template("index")

    for category in listdir(FOLDER_SNIPPETS):
        snippets_title = []
        folder_category = path.join(FOLDER_SNIPPETS, category)
        for snippet in listdir(folder_category):
            snippet_folder = path.join(folder_category, snippet)
            snippets_title.append(snippet)

            html_code = read_file(path.join(snippet_folder, HTML_SNIPPET))
            
            snippet_css = path.join(snippet_folder, CSS_SNIPPET)
            snippet_js = path.join(snippet_folder, JS_SNIPPET)
            copy_static(snippet_css, snippet + ".css")
            copy_static(snippet_js, snippet + ".js")

            context = {
                "title_snippet": snippet,
                "html": html_code,
                "code_html": format_html(html_code),
                "code_css": read_file(snippet_css),
                "code_js": read_file(snippet_js),
            }

            build_template("snippet", context, snippet)

        build_template("category", {"snippets": snippets_title}, category)


if __name__ == "__main__":
    build()
