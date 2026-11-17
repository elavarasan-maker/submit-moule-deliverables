# Module 03 — LLM APIs & Chat Application
API keys belong in environment variables, not source code. A chat request contains system, user and assistant messages. History supplies context but is limited by the model context window. Temperature affects variation; max output tokens limits response length. Reduce cost with concise context, token caps, suitable model selection, caching and usage monitoring.

Run `python 03_LLM_API_Chat_App/app.py`. Without a key, local demo mode is explicit and does not pretend to call a model. With a compatible API key, the app handles authentication, quota, timeout, network and malformed-response errors.
