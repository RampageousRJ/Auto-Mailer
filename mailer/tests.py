import pytest
from flask import Flask
from flask_mail import Mail
from mailer import app, validEmail
from mailer.forms import UploadForm
from werkzeug.datastructures import FileStorage
import os
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['MAIL_SUPPRESS_SEND'] = True  # Disable actual email sending
    app.config['UPLOAD_FOLDER'] = "./tests/uploads/"
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    client = app.test_client()
    yield client
    # Teardown
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

# Test Email Validation
def test_valid_email():
    assert validEmail("test@example.com") is True
    assert validEmail("invalid-email") is False
    assert validEmail("user@domain.co.uk") is True
    assert validEmail("@missinguser.com") is False

# Test Home Route Exists
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    response = client.get('/home')
    assert response.status_code == 200

# Test Form Validation
def test_upload_form():
    form = UploadForm(name="John Doe", title="Test Email", upload=None, body="Test Body")
    assert form.validate() is False  # File upload is required

    form = UploadForm(name="John Doe", title="Test Email", body="Test Body")
    assert form.validate() is False  # File upload is still required

# Test File Upload Handling
def test_file_upload(client):
    data = {
        'name': 'Test User',
        'title': 'Test Title',
        'body': 'Test Body'
    }
    file = (FileStorage(stream=open("tests/sample.xlsx", "rb"), filename="sample.xlsx"), 'upload')
    response = client.post('/home', data={**data, 'upload': file}, content_type='multipart/form-data')
    assert response.status_code in [200, 302]  # Redirects after success or failure

# Mock Email Sending
def test_email_sending(client):
    with patch("flask_mail.Mail.send") as mock_send:
        data = {
            'name': 'Test User',
            'title': 'Test Title',
            'body': 'Test Body'
        }
        response = client.post('/home', data=data)
        assert response.status_code in [200, 302]
        mock_send.assert_not_called()  # Since no valid email is present

        # Now, mock a valid email scenario
        mock_send.reset_mock()
        with patch("mailer.routes.validEmail", return_value=True):
            response = client.post('/home', data=data)
            mock_send.assert_called()
