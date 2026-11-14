"""Original game content: The Case of the Vanishing Birthday Cake (MYST-BDAY-01).

Format: players are detectives (no acting). 2 to 8 players or teams, ages 8-12,
about 45-60 minutes, 15 minutes of setup.

Logic design (kept here so QA can re-check it):
  Culprit: Theo. Three independent hard clues point only to Theo:
    K1 small zigzag boot print (E1 + E7 boot chart): Theo or Mia only.
    K2 blue party-streamer thread on the latch (E2 + suspect clothing): Theo only.
    K3 absence from the magic show at 3:10, 3:15 and 3:24 (E6) not explained by
       Grandma's statement (E5): Theo only.
  Each innocent is eliminated by at least one hard clue:
    Lily: sandals (E7), Grandma saw her on the phone all 20 minutes (E5).
    Felix: on stage in every video still (E6), smooth dress shoes (E7).
    Barnaby: zigzag but 31 cm boots, print is 19 cm (E1, E7), no blue (K2).
    Mia: Grandma watched her go up and come straight down the hall stairs, which
         never pass the kitchen (E5); wears yellow, no blue streamers (K2).
    Pepper: cannot carry a 2 kg cake off a 90 cm counter; the print is a boot (E8, E1).
  Red herrings: Felix's 'disappearing cake' trick list (E12), Mia's chocolate
  wrapper (E11), Barnaby's shed key (suspect card), Lily's frosting worry.
"""

SKU = "MYST-BDAY-01"
TITLE = "The Case of the Vanishing Birthday Cake"
PLACE_NAME = "Bramble House"
CASE_LABEL = "Case No. 70: the vanishing cake"
CASE_SUMMARY = ("Grandma Rosa's lemon birthday cake was on the kitchen counter at 3:00 pm. At 3:20 pm it was gone. "
                "Use the evidence to find out WHO took it, HOW you know, and WHERE it is.")
ACCUSE = ["WHO took the cake?", "Clue 1 that proves it:", "Clue 2 that proves it:",
          "Clue 3 that proves it:", "WHERE is the cake now?"]
FINALE_SHORT = "Optional finale: find the hidden cake!"
SUBTITLE = "A printable detective party game for ages 8 to 12"
TAGLINE = "Grandma Rosa's cake has vanished. Ten minutes before the candles. Can your detectives crack the case?"

FACTS = {
    "players": "2 to 8 detectives (or up to 4 teams for bigger groups)",
    "ages": "8 to 12 (younger players can join a team with an older reader)",
    "time": "45 to 60 minutes of play",
    "setup": "About 15 minutes: print, cut and put cards in 3 envelopes",
    "host": "1 adult or older child host (the host does not play)",
}

INTRO_SCRIPT = [
    "Welcome, detectives! Thank you for coming so quickly.",
    "Today is Grandma Rosa's 70th birthday party at Bramble House. Aunt Lily baked a "
    "beautiful three-layer lemon cake with blue sprinkles and a sugar crown on top.",
    "At exactly 3:00 pm someone took a photo of the cake sitting on the kitchen counter.",
    "At 3:20 pm Aunt Lily walked into the kitchen to light the candles... and the cake was GONE. "
    "No crumbs. No plate. Nothing.",
    "Six suspects were at the party. One of them took the cake. Your job is to find out WHO took it, "
    "HOW you know, and WHERE the cake is now, before the candles burn out!",
]

LOCATIONS = [
    ("Kitchen", "The cake was on the counter. A back door leads out to the garden."),
    ("Laundry room", "Next to the kitchen. Pepper the dog was shut in here at 2:45 pm."),
    ("Living room", "Uncle Felix's magic show ran here from 3:00 to 3:25 pm. A side door leads straight into the kitchen."),
    ("Front hall", "The stairs to the upstairs bathroom are here. Grandma sat on the hall bench."),
    ("Garden", "A long path runs from the kitchen back door down to the garden shed."),
    ("Garden shed", "At the very bottom of the garden, full of old blankets and flower pots. The door is never locked."),
]

SUSPECTS = [
    {
        "id": "S1", "name": "Aunt Lily", "role": "The baker",
        "look": {"skin": "#E8B98F", "hair": "#6B3E1E", "top": "#3E8E5E", "legs": "#3E8E5E",
                 "shoes": "#C8A27A", "extra": "dress"},
        "wearing": "Green dress, flat sandals",
        "said": "\"I was on the phone in the front hall from 3:00 until 3:20, ordering more candles.\"",
        "fact": "She baked the cake and said earlier: \"The frosting is a disaster, I'd rather nobody saw it!\"",
    },
    {
        "id": "S2", "name": "Uncle Felix", "role": "The magician",
        "look": {"skin": "#C68A5E", "hair": "#1C1C1C", "top": "#5A5A6E", "legs": "#2B2B33",
                 "shoes": "#111111", "extra": "silvercape"},
        "wearing": "Silver cape, shiny smooth black shoes",
        "said": "\"I was doing my magic show in the living room the whole time, from 3:00 to 3:25.\"",
        "fact": "He joked at lunch: \"My best trick today will be making the cake disappear!\"",
    },
    {
        "id": "S3", "name": "Mr. Barnaby", "role": "The neighbor",
        "look": {"skin": "#F1C9A5", "hair": "#BDBDBD", "top": "#8B5A2B", "legs": "#8B5A2B",
                 "shoes": "#3B6E3B", "extra": "boots"},
        "wearing": "Brown overalls, big green garden boots",
        "said": "\"I was trimming roses on my side of the fence. I didn't see anything.\"",
        "fact": "He has a spare key to the garden shed and says the party is too noisy.",
    },
    {
        "id": "S4", "name": "Cousin Mia", "role": "Age 11, chocolate fan",
        "look": {"skin": "#8D5A3B", "hair": "#2A1A10", "top": "#F2C230", "legs": "#2E4A7A",
                 "shoes": "#C0392B", "extra": "raincoat"},
        "wearing": "Yellow raincoat, small red rain boots",
        "said": "\"I watched the magic show. I only left once, to use the bathroom upstairs.\"",
        "fact": "She grumbled: \"Lemon cake? I wish it was chocolate.\"",
    },
    {
        "id": "S5", "name": "Theo", "role": "Age 9, Grandma's grandson",
        "look": {"skin": "#F0C8A0", "hair": "#C77B30", "top": "#2E6DB4", "legs": "#4A4A4A",
                 "shoes": "#2E6DB4", "extra": "streamercape"},
        "wearing": "Superhero cape made of blue party streamers, small blue rain boots",
        "said": "\"I watched the magic show and then I played in the garden.\"",
        "fact": "He loves building forts and he is Pepper the dog's best friend.",
    },
    {
        "id": "S6", "name": "Pepper", "role": "The family beagle",
        "look": {"dog": True},
        "wearing": "A red collar with a bone-shaped tag",
        "said": "\"Woof!\" (Translation: \"I would NEVER... probably.\")",
        "fact": "Pepper LOVES cake. Aunt Lily shut Pepper in the laundry room at 2:45 pm.",
    },
]

# Evidence cards. round: 1 = scene, 2 = witnesses and checks, 3 = the trail.
EVIDENCE = [
    {"id": "E1", "round": 1, "title": "Boot print by the back door",
     "text": "Aunt Lily spilled flour by the back door while baking. Now there is a boot print in it, "
             "pointing out toward the garden. It has a ZIGZAG sole. Detective tape measure: the print is 19 cm long.",
     "icon": "boot"},
    {"id": "E2", "round": 3, "title": "Something caught on the latch",
     "text": "A torn strip of party streamer is caught on the back-door latch. "
             "It is shiny and BLUE. Someone hurried through the door.",
     "icon": "streamer"},
    {"id": "E3", "round": 1, "title": "Paw prints",
     "text": "Little paw prints go from the laundry room to the kitchen counter and back. "
             "The laundry room door is open. Its latch is broken and pops open if pushed.",
     "icon": "paw"},
    {"id": "E4", "round": 1, "title": "The 3:00 pm photo",
     "text": "Photo of the cake on the middle of the counter, time stamp 3:00 PM. "
             "Three lemon layers, a sugar crown, and lots of BLUE sprinkles on top.",
     "icon": "cake"},
    {"id": "E5", "round": 2, "title": "Grandma Rosa's statement",
     "text": "\"I sat on the hall bench blowing up balloons from 3:00 to 3:20. "
             "Lily was on the phone next to me the WHOLE time. "
             "At 3:08 Mia ran upstairs to the bathroom. She came straight back down at 3:12. "
             "Nobody else came through the hall.\"",
     "icon": "speech"},
    {"id": "E6", "round": 2, "title": "Magic show video stills",
     "text": "Felix is on stage in every still.\n"
             "3:02 - Mia and Theo in the front row.\n"
             "3:07 - Mia there. Theo's seat EMPTY.\n"
             "3:10 - Mia's and Theo's seats empty.\n"
             "3:13 - Mia back. Theo's seat empty.\n"
             "3:20 - Mia there. Theo's seat empty.\n"
             "3:24 - Theo still missing.",
     "icon": "camera"},
    {"id": "E7", "round": 2, "title": "The great shoe check",
     "text": "Lily: flat sandals, smooth sole.\nFelix: smooth black shoes, 28 cm.\n"
             "Barnaby: garden boots, ZIGZAG sole, 31 cm.\nMia: rain boots, ZIGZAG sole, 19 cm.\n"
             "Theo: rain boots, ZIGZAG sole, 19 cm.",
     "icon": "ruler"},
    {"id": "E8", "round": 2, "title": "Could Pepper do it?",
     "text": "Pepper is 30 cm tall. The counter is 90 cm high and the cake sat in the middle. "
             "The cake and plate weigh 2 kg. There are no crumbs, no licked frosting and no "
             "broken plate anywhere. Could Pepper reach the cake AND carry it away?",
     "icon": "paw"},
    {"id": "E9", "round": 1, "title": "Sprinkle trail",
     "text": "Tiny BLUE sprinkles are scattered on the garden path. "
             "They start at the kitchen back door. They lead all the way to the garden shed.",
     "icon": "dots"},
    {"id": "E10", "round": 3, "title": "A sign on the shed",
     "text": "A paper sign is taped to the shed door in wobbly crayon: "
             "\"SECRET FORT. NO DOGS ALLOWED!\" Inside you can hear... humming?",
     "icon": "sign"},
    {"id": "E11", "round": 3, "title": "Wrapper in the living room",
     "text": "A chocolate bar wrapper in the living room bin. It is Mia's favorite brand. "
             "There are no lemon crumbs or frosting on it.",
     "icon": "wrapper"},
    {"id": "E12", "round": 3, "title": "Felix's trick list",
     "text": "Found in Felix's magic case: a trick list. "
             "\"Trick 5: The Disappearing Cake. Use the CARDBOARD cake!\" "
             "The cardboard cake is still in the case.",
     "icon": "list"},
]

HINTS = [
    {"id": "H1", "minute": 15, "text": "Compare the boot print (E1) with the shoe check (E7). "
     "Which suspects have a zigzag sole AND a 19 cm boot? Cross off everyone else for that clue."},
    {"id": "H2", "minute": 30, "text": "Look at the video stills (E6). Who was missing from the show? "
     "Then read Grandma's statement (E5): does it explain where each missing person went?"},
    {"id": "H3", "minute": 40, "text": "The streamer caught on the latch (E2) is BLUE. "
     "Look at what every suspect is wearing. Then follow the sprinkles (E9) to find the cake!"},
]

SOLUTION = {
    "who": "Theo",
    "where": "In Theo's secret fort in the garden shed, safe and sound.",
    "story": [
        "Sometime between 3:02 and 3:07 (about 3:05) Theo slipped out of the magic show to check on his best friend Pepper.",
        "The laundry door's latch is broken (E3), so Pepper had pushed it open and was jumping "
        "at the counter, trying to reach the cake (paw prints, E3).",
        "Theo panicked. To keep Grandma's cake safe from Pepper, he picked it up and carried it "
        "out of the back door. His blue streamer cape snagged on the latch (E2) and his small "
        "zigzag rain boots left a 19 cm print on the mat (E1, E7).",
        "Blue sprinkles fell off the cake all the way down the garden path (E9) to the shed, "
        "where Theo hid it in his \"NO DOGS ALLOWED\" fort (E10).",
        "The shed is never locked, so Barnaby's key does not matter. Then Theo decided to decorate the fort as a surprise party room for Grandma and completely "
        "forgot the time!",
    ],
    "eliminations": [
        ("Aunt Lily", "Sandals have no zigzag sole (E7), and Grandma saw her on the phone the whole time (E5)."),
        ("Uncle Felix", "On stage in every video still (E6). Smooth shoes (E7). His 'cake' trick uses a cardboard prop (E12)."),
        ("Mr. Barnaby", "His zigzag boots are 31 cm, much bigger than the 19 cm print (E1, E7). No blue streamers."),
        ("Cousin Mia", "Grandma watched her go up and come straight back down the hall stairs (E5), "
                       "which never pass the kitchen. She wears yellow, not blue streamers. The wrapper (E11) is a red herring."),
        ("Pepper", "Too small to lift a 2 kg cake off a 90 cm counter, no crumbs (E8), and the print is a boot, not a paw (E1)."),
    ],
}

SCORING = [
    ("Correct culprit", 3),
    ("Each correct piece of evidence (up to 3)", 1),
    ("Correct location of the cake", 1),
]

FINALE = ("Optional finale: before the party, hide the real cake (or cupcakes) somewhere in your home "
          "and tape the printed \"SECRET FORT\" sign to it. After the reveal, the detectives follow a "
          "trail of blue paper 'sprinkles' to find it and Theo's case is closed with candles!")
