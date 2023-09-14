from IPython.display import display_markdown

def print_menu():
    
    mdtext = '# Here are our Quantum Games: <p style="color:blue;font-size:18px;"><large><a href=./games/stiritup.ipynb> Stir it up </a></large></p> </br>
    <p style="color:blue;font-size:18px;">Atomic shuttle</large></p> </br>
    <p style="color:blue;font-size:18px;">Algorithm puzzle</large></p>"'
    
    display_markdown(mdtext)
