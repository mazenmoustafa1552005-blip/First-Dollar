"""Original game content: The Midnight Snack Mystery (MYST-FAM-01).

Occasion: family night or sleepover. Expert tier (ages 10-12, younger with a team).
Format: all players are detectives (no acting). 2 to 8 detectives or up to 4 teams.

Design rules applied (research/game-design-psychology.md):
  6 suspects (Expert max), 12 evidence cards, 4 per round. Non-violent "crime"
  (a midnight cookie snack), sympathetic culprit, confession ends with a fix.
  Culprit is an adult (variety vs MYST-BDAY-01, where it was a child).
  One detectable lie: Grandpa says he "slept like a log"; E9 (crossword timed
  12:20 am) exposes it. Two eliminations need two cards combined (Ruby: E4 + E5;
  Noor: E6 + the house map; Grandpa via E5 + E6).

Logic design:
  Culprit: Grandpa Walt. WHERE: 4 cookies wrapped in a napkin in his robe pocket.
  Hard clues pointing only to Grandpa:
    K1 brown reading glasses with chocolate smudge left by the tin (E2) + glasses
       on suspect cards: only Grandpa wears brown frames (Ruby wears red).
    K2 hallway motion light at 12:14 and 12:31 (E6). The hallway joins the den,
       the stairs and the kitchen; the stair never squeaked after 11:04 (E5), so
       the trip came from the den.
    K3 crumbs on Grandpa's slippers and a lumpy, chocolate-smelling robe pocket (E8).
    Lie: crossword finished at 12:20 am with a chocolate fingerprint (E9).
  Eliminations:
    Mom: sleep watch shows asleep 10:05 pm to 6:30 am (E7); no glasses.
    Ruby: counted all 12 cookies at 11:02 (E4) and the stairs squeaked back up at
          11:04 and never again (E5); red frames, not brown (E2). Flashlight is a
          red herring (E12).
    Max: upstairs, the squeaky stair never sounded after 11:04 (E5); no glasses;
         chocolate on his sleeve is from pudding at lunch (E11).
    Noor: the living room opens straight into the kitchen, so she would not pass
          the hallway light (E6 + map); no glasses (E2); no crumbs on her (E8).
    Biscuit the cat: the tin lid was pressed back on neatly (E3); cats cannot do that.
  Window: 12 cookies at 11:02 (E4), 6 left at 7:00 am (E1); 6 missing = 2 eaten + 4 in pocket.
"""

SKU = "MYST-FAM-01"
TITLE = "The Midnight Snack Mystery"
PLACE_NAME = "the Pemberton house"
CASE_LABEL = "Case No. 12: the missing cookies"
CASE_SUMMARY = ("Mom baked 12 cookies for the school bake sale. At 7:00 am only 6 were left. "
                "Someone snuck a midnight snack. Find out WHO did it, HOW you know, and WHERE the other cookies went.")
ACCUSE = ["WHO took the cookies?", "Clue 1 that proves it:", "Clue 2 that proves it:",
          "Clue 3 that proves it:", "WHERE are the missing cookies now?"]
FINALE_SHORT = "Optional finale: share a plate of cookies!"
SUBTITLE = "A printable family night detective game for ages 8 to 12"
TAGLINE = "Six cookies vanished in the night. Somebody in this house is not telling the truth."

FACTS = {
    "players": "2 to 8 detectives (or up to 4 teams)",
    "ages": "10 to 12 on their own; 8 to 9 with an older teammate",
    "time": "45 to 55 minutes of play",
    "setup": "About 15 minutes: print, cut and fill 3 envelopes",
    "host": "1 adult or older child host (the host does not play)",
}

INTRO_SCRIPT = [
    "Good morning, detectives. We have a problem in the Pemberton house.",
    "Last night Mom baked 12 chocolate chip cookies for the school bake sale. "
    "She put them in a tin on the kitchen table.",
    "This morning at 7:00 the tin had only 6 cookies inside.",
    "Everyone says they were fast asleep. But somebody had a midnight snack, "
    "and somebody is not telling the truth.",
    "Your job: find out WHO took the cookies, HOW you know, and WHERE the other cookies went. "
    "The bake sale starts at 9:00. Hurry!",
]

LOCATIONS = [
    ("Kitchen", "The cookie tin sat on the kitchen table."),
    ("Den", "Grandpa sleeps here, downstairs, at one end of the hallway."),
    ("Hallway", "It joins the den, the bottom of the stairs and the kitchen. Its night light records a time whenever it switches on."),
    ("Living room", "Cousin Noor slept on the couch. The living room opens straight into the kitchen, not into the hallway."),
    ("Stairs", "They come down into the hallway. The 5th stair squeaks loudly."),
    ("Upstairs", "Mom, Ruby and Max have bedrooms up here."),
]

SUSPECTS = [
    {
        "id": "S1", "name": "Grandpa Walt", "role": "Crossword champion",
        "look": {"skin": "#F1C9A5", "hair": "#D0D0D0", "top": "#3E6FA8", "legs": "#3E6FA8",
                 "shoes": "#8B5A2B", "extra": "dress", "glasses": "#6E3B12"},
        "wearing": "Striped pajamas, a robe, fuzzy slippers, brown reading glasses",
        "said": "\"I slept like a log all night. I didn't hear a thing.\"",
        "fact": "He sleeps in the den, downstairs. He says he is 'crumb-pletely' innocent.",
    },
    {
        "id": "S2", "name": "Mom", "role": "The baker",
        "look": {"skin": "#C68A5E", "hair": "#2A1A10", "top": "#9B59B6", "legs": "#5B2C6F",
                 "shoes": "#5B2C6F", "extra": None},
        "wearing": "Purple pajamas and a sleep watch. No glasses.",
        "said": "\"I went to bed at 10:00. I wake up at every squeak on the stairs.\"",
        "fact": "She baked the cookies. She says the bake sale is 'the yeast' of her worries.",
    },
    {
        "id": "S3", "name": "Ruby", "role": "Age 12, night owl",
        "look": {"skin": "#E8B98F", "hair": "#B03A2E", "top": "#E67E22", "legs": "#34495E",
                 "shoes": "#34495E", "extra": None, "glasses": "#C0392B"},
        "wearing": "Orange hoodie, red glasses",
        "said": "\"I went down for water at 11:00. Then I went straight back to bed.\"",
        "fact": "She reads late with a flashlight. She loves a good 'whodunnit'.",
    },
    {
        "id": "S4", "name": "Max", "role": "Age 7, cookie fan",
        "look": {"skin": "#F0C8A0", "hair": "#C77B30", "top": "#27AE60", "legs": "#1E8449",
                 "shoes": "#1E8449", "extra": None},
        "wearing": "Green dinosaur pajamas. No glasses.",
        "said": "\"I was asleep! Dinosaurs need their sleep.\"",
        "fact": "He has a chocolate smudge on his sleeve. He says it is 'dino-mite' pudding.",
    },
    {
        "id": "S5", "name": "Cousin Noor", "role": "Age 10, sleepover guest",
        "look": {"skin": "#8D5A3B", "hair": "#1C1C1C", "top": "#F2C230", "legs": "#2E4A7A",
                 "shoes": "#2E4A7A", "extra": None},
        "wearing": "Yellow pajamas, a sleeping bag. No glasses.",
        "said": "\"A noise woke me around midnight. Then I fell back asleep.\"",
        "fact": "She slept on the living room couch. She says she is 'sofa' so innocent.",
    },
    {
        "id": "S6", "name": "Biscuit", "role": "The family cat",
        "look": {"cat": True},
        "wearing": "A blue collar with a bell",
        "said": "\"Meow.\" (Translation: \"Purr-haps.\")",
        "fact": "Biscuit loves knocking things off tables. Biscuit has paws, not hands.",
    },
]

EVIDENCE = [
    {"id": "E1", "round": 1, "title": "The cookie tin",
     "text": "At 7:00 am the tin has 6 cookies. Mom baked 12. "
             "A trail of crumbs leads from the table toward the hallway.",
     "icon": "dots"},
    {"id": "E2", "round": 3, "title": "Glasses by the tin",
     "text": "A pair of reading glasses lies next to the tin. "
             "The frames are BROWN. One lens has a chocolate smudge.",
     "icon": "list"},
    {"id": "E3", "round": 1, "title": "The tin lid",
     "text": "The tin lid is pressed back on, neat and tight. "
             "Nothing was knocked over. Who could close a lid like that?",
     "icon": "wrapper"},
    {"id": "E4", "round": 1, "title": "Ruby's text message",
     "text": "Ruby texted Mom at 11:02 pm: \"Counted the cookies. All 12 are here. "
             "Can I have one tomorrow?\"",
     "icon": "speech"},
    {"id": "E5", "round": 1, "title": "The squeaky stair",
     "text": "Mom woke up twice when the 5th stair squeaked. "
             "First at 11:00 pm, going down. Then at 11:04 pm, going up. "
             "It never squeaked again. It is too wide to step over.",
     "icon": "speech"},
    {"id": "E6", "round": 2, "title": "Hallway night light",
     "text": "The motion light switched on at these times:\n11:01 pm, 11:03 pm, 12:14 am, 12:31 am.\n"
             "(12:14 am is just after midnight.) It notices people, not pets.\n"
             "The hallway joins the den, the stairs and the kitchen.",
     "icon": "camera"},
    {"id": "E7", "round": 2, "title": "Mom's sleep watch",
     "text": "Mom's watch shows she was asleep from 10:05 pm to 6:30 am. "
             "It recorded two short wake-ups: 11:00 pm and 11:04 pm.",
     "icon": "ruler"},
    {"id": "E8", "round": 3, "title": "The crumb check",
     "text": "Chocolate crumbs are found on Grandpa's fuzzy slippers. "
             "His robe hangs on the den door. One pocket is lumpy and smells of chocolate. "
             "No crumbs on anyone else.",
     "icon": "paw"},
    {"id": "E9", "round": 3, "title": "Grandpa's crossword",
     "text": "On the den armchair: last night's crossword, all finished. "
             "Next to the last answer Grandpa wrote the time: 12:20 am. "
             "The corner has a chocolate fingerprint and a cookie crumb.",
     "icon": "list"},
    {"id": "E10", "round": 2, "title": "What Noor heard",
     "text": "Noor says the noise was a soft cough from the hallway side. "
             "Then she saw the hallway light glow through the kitchen.",
     "icon": "speech"},
    {"id": "E11", "round": 2, "title": "Max's sleeve",
     "text": "The school lunch menu for Thursday says: chocolate pudding cup. "
             "Max's sleeve smudge is dry and old. It has no cookie crumbs.",
     "icon": "wrapper"},
    {"id": "E12", "round": 3, "title": "A flashlight in the kitchen",
     "text": "Ruby's flashlight is on the kitchen counter, still switched on. "
             "Its battery is almost empty. Ruby says she forgot it at 11:03 pm.",
     "icon": "sign"},
]

HINTS = [
    {"id": "H1", "minute": 15, "text": "Read Ruby's text (E4) and the squeaky stair (E5) together. "
     "When did the cookies go missing? Who could still come downstairs after 11:04?"},
    {"id": "H2", "minute": 30, "text": "The hallway light (E6) switched on after midnight. "
     "Look at the house map. Which room can reach the hallway without using the stairs?"},
    {"id": "H3", "minute": 40, "text": "Whose glasses are BROWN (E2)? Someone said they \"slept like a log\". "
     "Does the crossword (E9) agree? Then read E8 to find the missing cookies."},
]

SOLUTION = {
    "who": "Grandpa Walt",
    "where": "4 cookies are wrapped in a napkin in Grandpa's robe pocket. He ate the other 2.",
    "story": [
        "Grandpa could not sleep, so he did his crossword in the den.",
        "At 12:14 am he tiptoed through the hallway to the kitchen (the night light switched on, E6).",
        "He ate 2 cookies by the tin and left his brown reading glasses behind (E2). "
        "Then he wrapped 4 more in a napkin for breakfast and put them in his robe pocket (E8).",
        "He had brought his crossword and glasses along, and finished the puzzle at the kitchen table at 12:20 am, "
        "with chocolate on his fingers (E9). He pressed the lid back on neatly (E3) and "
        "carried the crossword back to the den at 12:31 am (E6), and forgot his glasses by the tin.",
        "So when Grandpa said he \"slept like a log\", it was not true. "
        "He says sorry, and he is baking 12 fresh cookies for the bake sale right now.",
    ],
    "eliminations": [
        ("Mom", "Her sleep watch shows she was asleep from 10:05 pm to 6:30 am, except at 11:00 and 11:04 (E7). She wears no glasses (E2)."),
        ("Ruby", "She counted all 12 cookies at 11:02 (E4). The stair squeaked her back up at 11:04 and never again (E5). Her glasses are red, not brown (E2). The flashlight is a red herring (E12)."),
        ("Max", "He sleeps upstairs and the stair never squeaked after 11:04 (E5). No glasses. His smudge is old pudding from lunch (E11)."),
        ("Cousin Noor", "The living room opens straight into the kitchen, so she would not pass the hallway light (E6 and the house map). No glasses (E2). No crumbs (E8)."),
        ("Biscuit", "A cat cannot press a tin lid back on neatly (E3), or wear glasses (E2)."),
    ],
}

SCORING = [
    ("Correct snacker", 3),
    ("Each correct piece of evidence (up to 3)", 1),
    ("Found the missing cookies", 1),
    ("Spotted the suspect who did not tell the truth", 1),
]

FINALE = ("Optional finale: before the game, hide a plate of real cookies (or any snack) wrapped in a napkin "
          "inside a robe or jacket pocket at home. When the detectives name the right pocket, the snack is theirs to share.")
