from selene.support.shared import browser
import os
import tests


def upload_picture(element, file):
    browser.element(element).set_value(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__), os.path.pardir, file)))