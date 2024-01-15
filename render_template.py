def render_template(template_name):
    with open(template_name, 'r', encoding='utf-8') as f:
        html_str = f.read()
    return html_str
