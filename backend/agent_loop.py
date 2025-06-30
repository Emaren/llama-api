import time
from backend.reflection.self_reflector import reflect_on_interaction
from backend.code_planner import plan_code_edits
from backend.code_writer import write_code_files

def run_agent_loop():
    """
    Main autonomous agent loop: prompt, plan, write, reflect.
    """
    while True:
        print("\n🧠 Agent loop iteration starting...")
        prompt = input("📝 Enter a prompt (or type 'exit' to quit): ").strip()

        if prompt.lower() in ['exit', 'quit']:
            print("👋 Exiting agent loop.")
            break

        if not prompt:
            print("⚠️ Empty prompt skipped.")
            continue

        plan = plan_code_edits(prompt)
        success, notes = write_code_files(plan)
        reflection = reflect_on_interaction(success, notes)

        print(f"🪞 Reflection: {reflection}")
