from PyQt5.QtWidgets import QApplication
def screenRes(app):
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()

    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    print("Screen Width:", screen_width)
    print("Screen Height:", screen_height)
    return screen_width, screen_height