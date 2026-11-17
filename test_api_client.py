import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from shared.llm_client import chat,LLMError
def test_missing_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 try: chat([{"role":"user","content":"hi"}])
 except LLMError as e: assert "not set" in str(e)
 else: raise AssertionError("Expected missing key error")
