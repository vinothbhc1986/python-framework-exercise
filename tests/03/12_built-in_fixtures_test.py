import os
import logging

def test_file_creation(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("content123")
    assert p.read_text() == "content123"

def test_env_var(monkeypatch):
    monkeypatch.setenv("API_KEY", "test_secret")
    #Code under test reads the environment variable
    assert os.environ["API_KEY"] == "test_secret"

def test_print(capsys):
    print("hello")  #print("hello", end="")
    captured = capsys.readouterr()
    assert captured.out == "hello\n" #Because print() sends "hello" followed by \n to standard output
    assert captured.out.strip() == "hello"  #.strip() to remove whitespace/newlines
#
def test_logging_message(caplog):
    # Code that emits a log message
    logger = logging.getLogger("my_logger")
    logger.warning("This is a warning log")

    # Verify the log message was captured
    assert "This is a warning log" in caplog.text
    assert "warning" in caplog.text

    # Alternatively, inspect specific records
    assert caplog.records[0].levelname == "WARNING"