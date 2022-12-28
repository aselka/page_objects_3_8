from selene import have


def checkboxes_click(locator, *by_texts):
    for value in by_texts:
        locator.element_by(have.text(value)).click()