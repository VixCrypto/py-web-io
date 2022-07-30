import pywebio

def completed():
    pass

alltasks = []
while True:
    name = pywebio.input.input(label="enter your name", placeholder="sama", required=True )
    alltasks.append(name)
    #pywebio.input.textarea(rows=20, code={"mode":"python", "theme":"cobalt"})
    pywebio.output.put_text(alltasks)
    pywebio.output.put_button(label="complete", onclick= completed)
