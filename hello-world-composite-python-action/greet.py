import os
from datetime import datetime, timezone

who = os.environ["INPUT_WHO_TO_GREET"]
print(f"Hello {who}.")

# Workflow command: show an annotation in the run summary
print(f"::notice::Greeted {who}")
print("Beepboop")

# Write outputs to the file in GITHUB_OUTPUT (not ::set-output)
with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    output.write(f"time={datetime.now(timezone.utc).isoformat()}\n")