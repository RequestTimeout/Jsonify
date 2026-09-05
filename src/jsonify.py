import json
import os
from html import escape

def convert(value):
    if isinstance(value, dict):
        result = '<div class="par">{</div>'

        items = list(value.items())

        for i, (key, val) in enumerate(items):
            result += f'<div class="key">"{escape(key)}"</div>'
            result += '<div class="par">:</div>'
            result += convert(val)

            if i < len(items) - 1:
                result += '<div class="par">,</div>'

        result += '<div class="par">}</div>'
        return result

    if isinstance(value, list):
        result = '<div class="par">[</div>'

        for i, item in enumerate(value):
            result += convert(item)

            if i < len(value) - 1:
                result += '<div class="par">,</div>'

        result += '<div class="par">]</div>'
        return result

    if isinstance(value, int) and not isinstance(value, bool):
        return f'<div class="val-int">{value}</div>'

    if isinstance(value, float):
        return f'<div class="val-int">{value}</div>'

    if isinstance(value, str):
        return f'<div class="val-str">"{escape(value)}"</div>'

    if value is True:
        return '<div class="val-bool">true</div>'

    if value is False:
        return '<div class="val-bool">false</div>'

    if value is None:
        return '<div class="val-null">null</div>'
    return NotImplemented

while True:
    fp = input("Enter file path: ")
    try:
        with open(fp) as f:
            pretty_json = json.load(f)
        break
    except FileNotFoundError:
        print("ERR: File not found.")

html_ = convert(pretty_json)
html = f"""
<!DOCTYPE html>
<html>
    <head>
        <style>""" + """@import url("https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap");

body {
    font-family: "JetBrains Mono", monospace;
}

body div {
    display: inline-block
}

html {
    background-color: rgb(60, 60, 60);
    text-align: left;
}

.par {
    color: azure;
}

.key {
    color: blueviolet;
}

.val-int {
    color: darkturquoise;
}

.val-str {
    color: rgb(10, 250, 110)
}

.val-bool {
    color: rgb(150, 43, 50);
}

.val-null {
    color: rgb(150, 43, 50);
}
        """ + f"""
        </style>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta name="author" content="RequestTimeout"/>
        <title>Viewing {escape(fp)}</title>
    </head>
    <body>
        {html_}
        <span>
            Made By Jsonify
            <span>
                Copyright RequestTimeout
            </span>
        </span>
    </body>
</html>
"""
try:
    with open(os.path.join(os.getcwd(), "Jsonify.html"), "w+") as f:
        f.write(html)

except FileNotFoundError:
    print("ERR: File not found.")
