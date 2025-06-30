from backend.prompt_listener import listen_for_prompts
from backend.code_planner import plan_code_edits
from backend.code_writer import write_code_files

def process_edit_cycle():
    """
    Runs one edit cycle: listen, plan, write.
    """
    prompt = input("Enter edit prompt: ")
    plan = plan_code_edits(prompt)
    success, notes = write_code_files(plan)
    print(f"Edit success: {success}, notes: {notes}")

if __name__ == "__main__":
    while True:
        process_edit_cycle()
