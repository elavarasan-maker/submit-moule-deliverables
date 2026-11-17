import os,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from dotenv import load_dotenv
from shared.llm_client import chat,LLMError
load_dotenv()
DEFAULT="You are a helpful assistant. Be accurate, clear and honest about uncertainty."
def demo(history):
 q=next((m["content"] for m in reversed(history) if m["role"]=="user"),"")
 return "[LOCAL DEMO — no LLM API call]\nYou asked: "+q+"\nConfigure a key for real model output."
def main():
 print("LLM Chat App. /exit quits; /clear resets history.")
 system=input("Custom instruction (Enter for default): ").strip() or DEFAULT
 history=[{"role":"system","content":system}]
 use_api=bool(os.getenv("OPENAI_API_KEY")); print("Mode:", "API" if use_api else "LOCAL DEMO")
 while True:
  q=input("\nYou: ").strip()
  if q=="/exit": break
  if q=="/clear": history=[history[0]]; print("Cleared."); continue
  if not q: continue
  history.append({"role":"user","content":q})
  try: answer=chat(history) if use_api else demo(history)
  except LLMError as e: answer="Request failed: "+str(e)
  history.append({"role":"assistant","content":answer}); print("\nAssistant:",answer)
  if len(history)>13: history=[history[0]]+history[-12:]
if __name__=="__main__": main()
