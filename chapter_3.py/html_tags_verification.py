from pythonds3 import Stack, Queue

def html_2_string(html_code):
    """converts the html code to string"""
    pseudo_tag_list = [i for i in html_code if i != "\n" or i != "/s"]
    tag_li = ""
    for i in pseudo_tag_list:
        if i != " " and i != "\n":
            if i == "<":
                tag_li += " "
            tag_li += i
            if i == ">":
                tag_li += " "
    tags_only = tag_li.split(" ")
    tags_fc = []
    for i in tags_only:
        if "<" in i and ">" in i:
            tags_fc.append(i)
    return tags_fc

def remove_slash(tag):
    temp_tag = ''
    for i in tag:
        if i == "/":
            continue
        temp_tag += i
    return temp_tag

def html_tag_matcher(html_code):
    """matches the tags"""
    stack = Stack()
    html_tags = html_2_string(html_code)
    if not html_tags:
        raise ValueError("Enter HTML code for validation...")
    del html_tags[0]
    for tag in html_tags:
        if "/" in tag:
            ind_tag = stack.pop()
            if ind_tag != remove_slash(tag):
                raise ValueError(f"Clsoing and opening tags doesn't match..- clo - {remove_slash(tag)} -- open --- {ind_tag}")
        else:
            stack.push(tag)
    if not stack.is_empty():
        print(f"Missing match {stack.peek()}")
    
    return stack.is_empty()


tags = """<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
</body>
</html>"""

a = html_tag_matcher(tags)
print(a)