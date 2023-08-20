# Открываем файл на чтение
with open('TEXT.txt', 'r') as file:
    # Читаем содержимое файла в переменную text
    text = file.read()


#видаляэмо коментарії
try:
    comm_start = text.index('[*')
    comm_end = text.index('*]')

    if comm_start == 0:
        text = text[comm_end+2:]
    else:
        text = text[:comm_start-1] + "\n" + text[comm_end+2:]

except ValueError:
    print("Symbol not found in string")


# беремо назву
try:
    name_start = text.index('n[')
    name_end = text.index(']n')

    name = text[name_start+2:name_end]
    if name_start == 0:
        text = text[name_end+2:]
    else:
        text = text[:name_start-1] + "\n" + text[name_end+2:]
except ValueError:
    print("Name not found in string")

#титулка
new_text = text.replace('t[', ' <td align="center" class="masthead"><h1>').replace(']t', '</h1></td></tr><tr><td class="content"><p>')

#абзацы
new_text = new_text.replace(';', '</p><p>')

#жирный текст
new_text = new_text.replace('b[', '<b>').replace(']b', '</b>')

#italic
new_text = new_text.replace('i[', '<em>').replace(']i', '</em>')

#accent
new_text = new_text.replace('a[', '</p></td></tr><tr><td class="masthead accent">').replace(']a', '</td></tr><tr><td class="content"><p>')

#h1-h6
new_text = new_text.replace('h1[', '<h1>').replace(']h1', '</h1>')
new_text = new_text.replace('h2[', '<h2>').replace(']h2', '</h2>')
new_text = new_text.replace('h3[', '<h3>').replace(']h3', '</h3>')
new_text = new_text.replace('h4[', '<h4>').replace(']h4', '</h4>')
new_text = new_text.replace('h5[', '<h5>').replace(']h5', '</h5>')
new_text = new_text.replace('h6[', '<h6>').replace(']h6', '</h6>')

#List
new_text = new_text.replace('l[', '</p><ul class="list">').replace(']l', '</ul><p>')
new_text = new_text.replace('c[', '<li>').replace(']c', '</li>')

#link
new_text = new_text.replace('r[', '<a ').replace(']r', '</a>')
new_text = new_text.replace('r{', 'href="').replace('}r', '">')

#button
new_text = new_text.replace('p[', '</p><table><tr><td align="center"><p><a class="button"').replace(']p', '</a></p></td></tr></table><p>')
new_text = new_text.replace('p{', 'href="').replace('}p', '">')


#footer
try:
    footer_start = new_text.index('f[')
    new_text = new_text.replace('f[', '<tr><td class="container"><table><tr><td class="content footer" align="center"><p>').replace(']f', '</p></td></tr></table></td></tr></table>')
    new_text = new_text[:footer_start] + '</p></td></tr></table></td></tr>' + new_text[footer_start:]
except Exception as e:
    print("Name not found in string")
    new_text = new_text + '</p></td></tr></table></td></tr>'




#Додаємо текст в форму для HTML
mail = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>

        <!-- For development, pass document through inliner -->

        <style type="text/css">

        * { margin: 0; padding: 0; font-size: 100%; font-family: 'Avenir Next', "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; line-height: 1.65; }

        img { max-width: 100%; margin: 0 auto; display: block; }

        body, .body-wrap { width: 100% !important; height: 100%; background: #f8f8f8; }

        a { color: #155ED6; text-decoration: none; }

        a:hover { text-decoration: underline; }

        .text-center { text-align: center; }

        .text-right { text-align: right; }

        .text-left { text-align: left; }

        .button { display: inline-block; color: white; background: #155ED6; border: solid #155ED6; border-width: 10px 20px 8px; font-weight: bold; border-radius: 4px; }

        .button:hover { text-decoration: none; }

        h1, h2, h3, h4, h5, h6 { margin-bottom: 20px; line-height: 1.25; }

        h1 { font-size: 32px; }

        h2 { font-size: 28px; }

        h3 { font-size: 24px; }

        h4 { font-size: 20px; }

        h5 { font-size: 16px; }

        p, ul, ol { font-size: 16px; font-weight: normal; margin-bottom: 20px; }

        .container { display: block !important; clear: both !important; margin: 0 auto !important; max-width: 580px !important; }

        .container table { width: 100% !important; border-collapse: collapse; }

        .container .masthead { padding: 50px 0; background: linear-gradient(-30deg, #155ED6, #367df1); color: white; }

        .container .masthead.accent { padding: 15px;}
        .container .masthead.accent * { margin:0; font-weight: 400;}
        .container .masthead.accent span { font-weight: bold;}

        .container .masthead h1 { margin: 0 auto !important; max-width: 90%; font-size: 48px;}

        .container .content { background: white; padding: 30px 35px; }

        .container .content.footer { background: none; }

        .container .content.footer p { margin-bottom: 0; color: #888; text-align: center; font-size: 14px; }

        .container .content.footer a { color: #888; text-decoration: none; font-weight: bold; }

        .container .content.footer a:hover { text-decoration: underline; }

        .container .list {font-weight: 600;}

        .container .list li {font-weight: 400;}


        </style>
    </head>
    <body>
    <table class="body-wrap">
        <tr>
            <td class="container">

                <table>
                    <tr>
    """ + new_text + """
    </body>
    </html>
    """

print(mail)

# Открываємо файл на запис
with open(f'{name}.html', 'w') as file:
    # Записываем новое содержимое в файл
    file.write(mail)

input()
