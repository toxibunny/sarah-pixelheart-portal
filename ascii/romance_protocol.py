from time import sleep

art = """
\[95m   ╭────────────────────────╮
\[91m   │  🍓✨ SARAH & ANDY ✨🍓  │
\[96m   │                        │
   │   (⊃｡•́‿•̀｡)⊃       ♡    │
   │     🐰  ╱|、          │
   │       (˛•̮˛ )⊃╲__    │
   │         ﾉ    ﾉ      │
   │   [ETHERNET CABLE]     │
   │   ╭───────────────╮   │
   │   │ COMPILING...99%│   │
   │   ╰───────────────╯   │
   │   404: ♥ NOT FOUND    │
   │   SYNTAX ERROR: LOVE  │
   │                        │
   ╰───────💘💻────────────╯
   │   │   │   │
   ▼   ▼   ▼   ▼
  (you) (me) (chaos) (forever)
"""

print("\033[1;36m=== INITIATING ROMANCE PROTOCOL ===\033[0m")
for line in art.split('\n'):
    print(line.replace('[', '\033['))
    sleep(0.2)
print("\033[1;35m✨ Tattoo ready. Apply to skin or code. ✨\033[0m")