from fastapi.testclient import TestClient

from analyzer_service.main import create_app


class DummyAsyncTask:
    def __init__(self, task_id: str):
        self.id = task_id


class DummyTask:
    def __init__(self, task_id: str):
        self._task_id = task_id
        self.calls = []

    def delay(self, *args):
        self.calls.append(args)
        return DummyAsyncTask(self._task_id)


class DummyContainer:
    def __init__(self, analyze_task, email_task):
        self.task_dispatcher = type('D', (), {'analyze_task': analyze_task, 'email_task': email_task})()


def test_health_endpoint():
    with TestClient(create_app()) as client:
        response = client.get('/health')

    assert response.status_code == 200
    assert response.json() == {"detail": "ok"}


def test_analyze_doc_dispatches_task():
    analyze_task = DummyTask("analyze-1")
    email_task = DummyTask("email-unused")
    app = create_app()

    with TestClient(app) as client:
        app.state.container = DummyContainer(analyze_task=analyze_task, email_task=email_task)
        response = client.post('/api/v1/analyze_doc', json={"image_path": "img.png"})

    assert response.status_code == 200
    assert response.json()["task_id"] == "analyze-1"
    assert analyze_task.calls == [("img.png",)]


def test_send_email_dispatches_task():
    analyze_task = DummyTask("analyze-unused")
    email_task = DummyTask("email-1")
    app = create_app()

    with TestClient(app) as client:
        app.state.container = DummyContainer(analyze_task=analyze_task, email_task=email_task)
        response = client.post('/api/v1/send_message_to_email', json={"email": "u@test.com", "text": "done"})

    assert response.status_code == 200
    assert response.json()["task_id"] == "email-1"
    assert email_task.calls == [("u@test.com", "done")]


def test_validation_error_shape():
    with TestClient(create_app()) as client:
        response = client.post('/api/v1/send_message_to_email', json={"email": "not-email", "text": "x"})

    assert response.status_code == 422
    assert "detail" in response.json()


def test_not_found_error_shape():
    with TestClient(create_app()) as client:
        response = client.get('/unknown')

    assert response.status_code == 404
    assert response.json()["detail"]
