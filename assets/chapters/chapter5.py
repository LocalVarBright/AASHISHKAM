from datetime import date

bebruary = date(2026, 2, 15)
today = date.today()

def start(funcs):

    doDialogText = funcs['doDialogText']

    doDialogText("Loading Chapter 5.#.#.#", afterdelay=3)
    print()

    if today >= bebruary:
        doDialogText("SIDDUMON:# Sorry, but i was making sure you were actually studying for the scholarship exam.")
        doDialogText("          Chapter 5 is not done yet")
    else:
        doDialogText("SIDDUMON:# Go study for Brilliant's Scholarship exam you twat")
        doDialogText("           Even I'M studying for once.")
    doDialogText(" - Siddumon")

    