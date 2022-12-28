from demoqa_tests.model.pages import registration_form


def test_submit_student_registration_form():
    registration_form.given_opened()

    # WHEN
    registration_form.set_name('Test')
    registration_form.set_last_name('Testov')
    registration_form.set_email('test@gmail.com')
    registration_form.set_gender('Female')
    registration_form.set_phone_number('1234567890')
    registration_form.set_birthday('5', '1995', '24')
    registration_form.set_subjects('Computer Science')
    registration_form.set_hobbies('Reading')
    registration_form.picture_upload('resourses/foto.jpg')
    registration_form.set_address('Saratovskaya 19')
    registration_form.scroll_to_bottom()
    registration_form.set_state('NCR')
    registration_form.set_city('Delhi')

    registration_form.submit()

    # THEN
    registration_form.should_have_submitted(
        [
            ('Student Name', 'Test Testov'),
            ('Student Email', 'test@gmail.com'),
            ('Mobile', '1234567890'),
            ('Date of Birth', '24 June,1995'),
            ('Subjects', 'Computer Science'),
            ('Hobbies', 'Reading'),
            ('Picture', 'foto.jpg'),
            ('Address', 'Saratovskaya 19'),
            ('State', 'NCR Delhi'),
        ],
    )