# C20 and C28 contained extra character "
# I decided to remove this character on both lines
# I assume that it was a mistype
# Tab-separated values should not contain these extra charachters
# please compare data.txt and data2.txt
''' I decided to work with data2.txt because if we had data coming
with an extra character, we should probably ensure that this data is fixed
'''

'''
# please uncomment this section for comparison

with open('data.txt') as tab_data:
    print(tab_data.read())

with open('data2.txt') as tab_data2:
    print(tab_data2.read())

# end comparison
'''

def main():
    create_simple_html()
    
def create_simple_html():
    f = open('data-to-html.html','w')
    text_data = open_read_data()
    # print(text_data)
    # multi-line 'f strings' are used to insert into <pre> element
    message = f"""<html>
    <head></head>
    <body><p>customer data</p>
    <pre>{text_data}</pre></body>
    </html>"""
    message.format(text_data=text_data)
    f.write(message)
    f.close()

def open_read_data():
    with open('data2.txt') as customers:
        c =customers.read()
        # print(c)
        # print(type(c))
    return c


main()