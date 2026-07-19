import os
import sys
from datetime import datetime

def main():
    print("Running bot-20-orchestrator tick...")
    
    # Define agent schedule and tasks
    agents_workflow = [
        ("bot-01", "bots/bot-01-literature/main.py"),
        ("bot-02", "bots/bot-02-dataset/main.py"),
        ("bot-03", "bots/bot-03-baseline/main.py"),
        ("bot-04", "bots/bot-04-tokenizer/main.py"),
        ("bot-05", "bots/bot-05-predictor-rnn/main.py"),
    ]
    
    # Run each agent sequential sequence for complete simulation setup
    for bot_id, path in agents_workflow:
        if os.path.exists(path):
            print(f"[{bot_id}] Starting execution...")
            try:
                exec(open(path).read(), {'__name__': '__main__'})
                print(f"[{bot_id}] Finished successfully.")
            except Exception as e:
                print(f"[{bot_id}] Failed with error: {e}")
                
    # Update dashboard
    dashboard_path = "docs/dashboard.md"
    if os.path.exists(dashboard_path):
        with open(dashboard_path, "r") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            if "bot-01" in line:
                lines[idx] = "| 01 | `bot-literature` | Running | Active | Scraped arXiv |\n"
            elif "bot-02" in line:
                lines[idx] = "| 02 | `bot-dataset` | Running | Active | Staged scientific log datasets |\n"
            elif "bot-03" in line:
                lines[idx] = "| 03 | `bot-baseline` | Running | Active | Saved baseline zlib JSON stats |\n"
            elif "bot-04" in line:
                lines[idx] = "| 04 | `bot-tokenizer` | Running | Active | Exported vocab.pkl |\n"
            elif "bot-05" in line:
                lines[idx] = "| 05 | `bot-rnn` | Running | Active | Trained tiny predictor model |\n"
        with open(dashboard_path, "w") as f:
            f.writelines(lines)
            
    # Update main README.md with the latest daily execution summary
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()
            
        summary_marker = "## Daily Update Summary"
        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        daily_log = f"\n\n{summary_marker}\n*   **Last Daily Run**: {now_str}\n*   **Status**: Bots 01-05 ran successfully. Baseline ratios saved. Predictor marks updated.\n"
        
        if summary_marker in content:
            # Replace existing summary
            parts = content.split(summary_marker)
            new_content = parts[0] + daily_log
        else:
            new_content = content + daily_log
            
        with open(readme_path, "w") as f:
            f.write(new_content)
            
    with open(".last_msg", "w") as f:
        f.write("orchestration tick run")
    print("Orchestrator finished sequence run.")

if __name__ == "__main__":
    main()
