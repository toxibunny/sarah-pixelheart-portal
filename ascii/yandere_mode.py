from time import sleep

art = """
\[91m   ╭────────────────────────╮
   │ ⚠️  [ALERT]         ⚠️  │
\[95m   │                        │
   │   (╯°□°）╯            │
   │     ︵ ┻━┻             │
   │   [SYSTEM OVERLOAD]    │
   │   Error: Too much     │
   │   affection detected. │
   │   *initiate cuddles*  │
   │   (y/n)? \033[92m[Y]\033[0m          │
   │                        │
   ╰───────💘💥────────────╯
   │   │   │
   ▼   ▼   ▼
 (you) (me) (doomed)
"""

print("\033[1;36m=== CRITICAL AFFECTION LEVELS DETECTED ===\033[0m")
for line in art.split('\n'):
    print(line)
    sleep(0.3)
print("\033[1;31m⚠️  Warning: Side effects may include\n- Spontaneous hugs\n- Excessive 'good boy' whispers\n- Terminal corruption\033[0m")