from selene import have


def set_value(element, text):
    element.element_by(have.value(text)).element('..').click()