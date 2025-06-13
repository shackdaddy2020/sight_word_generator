import tkinter as tk
import csv
import random
import os
import pygame

# Initialize pygame mixer for sound playback
pygame.mixer.init()
# Load your congratulatory sound (WAV format recommended)
congrats = pygame.mixer.Sound('congrats.wav')

# Sight word list (Dolch + Fry combined)
SIGHT_WORDS = [
   "the", "of", "and", "a", "to", "in", "is", "you", "that", "it", "he", "was", "for", "on", "are", "as", "with", "his", "they", "I", "at", "be", "this", "have", "from", "or", "one", "had", "by", "words", "but", "not", "what", "all", "were", "we", "when", "your", "can", "said", "there", "use", "an", "each", "which", "she", "do", "how", "their", "if", "will", "up", "other", "about", "out", "many", "then", "them", "these", "so", "some", "her", "would", "make", "like", "him", "into", "time", "has", "look", "two", "more", "write", "go", "see", "number", "no", "way", "could", "people", "my", "than", "first", "water", "been", "called", "who", "am", "its", "now", "find", "long", "down", "day", "did", "get", "come", "made", "may", "part", "over", "new", "sound", "take", "only", "little", "work", "know", "place", "years", "live", "me", "back", "give", "most", "very", "after", "things", "our", "just", "name", "good", "sentence", "man", "think", "say", "great", "where", "help", "through", "much", "before", "line", "right", "too", "means", "old", "any", "same", "tell", "boy", "follow", "came", "want", "show", "also", "around", "form", "three", "small", "set", "put", "end", "does", "another", "well", "large", "must", "big", "even", "such", "because", "turn", "here", "why", "ask", "went", "men", "read", "need", "land", "different", "home", "us", "move", "try", "kind", "hand", "picture", "again", "change", "off", "play", "spell", "air", "away", "animal", "house", "point", "page", "letter", "mother", "answer", "found", "study", "still", "learn", "should", "America", "world", "high", "every", "near", "add", "food", "between", "own", "below", "country", "plant", "last", "school", "father", "keep", "tree", "never", "start", "city", "earth", "eyes", "light", "thought", "head", "under", "story", "saw", "left", "don't", "few", "while", "along", "might", "close", "something", "seem", "next", "hard", "open", "example", "begin", "life", "always", "those", "both", "paper", "together", "got", "group", "often", "run", "important", "until", "children", "side", "feet", "car", "mile", "night", "walk", "white", "sea", "began", "grow", "took", "river", "four", "carry", "state", "once", "book", "hear", "stop", "without", "second", "late", "miss", "idea", "enough", "eat", "face", "watch", "far", "Indian", "real", "almost", "let", "girl", "sometimes", "mountains", "cut", "young", "talk", "soon", "list", "song", "being", "family", "it's", "body", "music", "color", "stand", "sun", "questions", "fish", "area", "mark", "dog", "horse", "birds", "problem", "complete", "room", "knew", "since", "ever", "piece", "told", "usually", "didn't", "friends", "easy", "heard", "order", "red", "door", "sure", "become", "top", "ship", "across", "today", "during", "short", "better", "best", "however", "low", "hours", "black", "products", "happened", "whole", "measure", "remember", "early", "waves", "reached", "listen", "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward", "war", "lay", "against", "pattern", "slow", "center", "love", "person", "money", "serve", "appeared", "road", "map", "rain", "farm", "pulled", "draw", "voice", "seen", "cold", "cried", "plan", "notice", "south", "sing", "fall", "king", "town", "I'll", "unit", "figure", "certain", "field", "travel", "wood", "fire", "upon", "done", "English", "road", "half", "ten", "fly", "gave", "box", "finally", "wait", "correct", "oh", "quickly", "person", "became", "shown", "minutes", "strong", "verb", "stars", "front", "feel", "fact", "inches", "street", "decided", "contain", "course", "surface", "produce", "building", "ocean", "class", "force", "brought", "understand", "warm", "common", "bring", "explain", "dry", "though", "language", "shape", "deep", "thousands", "yes", "clear", "equation", "yet", "government", "plane", "system", "behind", "ran", "round", "boat", "game", "rule", "among", "noun", "power", "cannot", "able", "six", "size", "dark", "ball", "material", "special", "heavy", "fine", "pair", "circle", "include", "built", "filled", "heat", "full", "hot", "check", "object", "am", "note", "nothing", "rest", "carefully", "scientists", "inside", "wheels", "stay", "green", "known", "island", "week", "less", "machine", "base", "ago", "stood", "can't", "matter", "square", "syllables", "perhaps", "bill", "felt", "suddenly", "test", "direction", "center", "farmers", "ready", "anything", "divided", "general", "energy", "subject", "Europe", "moon", "region", "return", "believe", "dance", "members", "picked", "simple", "cells", "paint", "mind", "love", "cause", "rain", "exercise", "eggs", "train", "blue", "wish", "drop", "developed", "window", "difference", "distance", "heart", "site", "sum", "summer", "wall", "forest", "legs", "sat", "main", "winter", "wide", "written", "length", "reason", "kept", "interest", "arms", "race", "present", "beautiful", "store", "job", "edge", "past", "sign", "record", "finished", "discovered", "wild", "beside", "gone", "sky", "grass", "million", "west", "lay", "weather", "root", "instruments", "meet", "brother", "months", "paragraph", "raised", "represent", "soft", "whether", "clothes", "flowers", "shall", "teacher", "held", "drive", "describe", "probably", "happy", "cross", "speak", "solve", "appear", "metal", "son", "either", "ice", "sleep", "village", "factors", "result", "jumped", "snow", "ride", "care", "floor", "pushed", "baby", "buy", "century", "outside", "everything", "tall", "already", "instead", "phrase", "amount", "scale", "pounds", "per", "broken", "melody", "trip", "nation", "gold", "quite", "milk", "poor", "themselves", "temperature", "bright", "lead", "everyone", "act", "beat", "section", "iron", "consonant", "someone", "couldn't", "hair", "age", "soil", "bed", "copy", "free", "spring", "case", "laughed", "possible", "stone", "lot", "fight", "surprise", "hill", "died", "build", "middle", "speed", "count", "cat", "sail", "rolled", "bear", "wonder", "smiled", "angle", "fraction", "Africa", "killed", "moment", "tiny", "bottom", "hole", "let's", "quiet", "natural", "French", "let's", "exactly", "remain", "dress", "within", "dictionary", "fingers", "row", "least", "catch", "climbed", "wrote", "shouted", "continued", "itself", "else", "plains", "gas", "England", "burning", "design", "joined", "foot", "law", "ears", "glass", "you're", "president", "brown", "trouble", "cool", "cloud", "lost", "sent", "symbols", "wear", "bad", "save", "experiment", "engine", "alone", "drawing", "east", "choose", "single", "touch", "information", "yourself", "control", "practice", "report", "straight", "rise", "statement", "stick", "serve", "child", "desert", "increase", "history", "cost", "maybe", "business", "separate", "break", "uncle", "hunting", "caught", "fell", "team", "God", "captain", "direct", "ring", "serve", "students", "valley", "cents", "yard", "equal", "decimal", "please", "art", "key", "feeling", "bit", "flow", "lady", "skin", "mouth", "received", "garden", "human", "strange", "suppose", "woman", "coast", "bank", "period", "wire", "pay", "clean", "visit", "grew", "express", "whose", "supply", "corner", "electric", "insects", "crops", "tone", "hit", "sand", "doctor", "provide", "thus", "won't", "cook", "bones", "mall", "board", "modern", "compound", "mine", "wasn't", "fit", "addition", "belong", "safe", "soldiers", "guess", "silent", "trade", "rather", "compare", "crowd", "poem", "enjoy", "elements", "indicate", "thin", "hat", "property", "particular", "swim", "terms", "current", "park", "string", "sense", "blow", "famous", "value", "wings", "movement", "pole", "exciting", "branches", "thick", "blood", "lie", "spot", "bell", "fun", "consider", "suggested", "army", "except", "flat", "seven", "tied", "rich", "dollars", "chief", "industry", "wash", "stream", "cattle", "eight", "wife", "science", "major", "observe", "tube", "necessary", "weight", "meat", "lifted", "process", "interesting", "position", "entered", "fruit", "send", "sell", "sight", "shoulder", "block", "rhythm", "planets", "spread", "sharp", "company", "radio", "we'll", "action", "capital", "factories", "settled", "yellow", "isn't", "southern", "truck", "fair", "printed", "wouldn't", "ahead", "chance", "born", "level", "triangle", "molecules", "France", "repeated", "column", "western", "sister", "oxygen", "plural", "various", "agreed", "opposite", "wrong", "chart", "prepared", "pretty", "solution", "fresh", "shop", "suffix", "especially", "shoes", "actually", "track", "arrived", "located", "sir", "dead", "sugar", "adjective", "fig", "gun", "total", "deal", "death", "score", "forward", "stretched", "experience", "cotton", "rope", "details", "entire", "corn", "substances", "smell", "tools", "conditions", "cows", "track", "nose", "create", "British", "difficult", "match", "win", "doesn't", "steel", "office", "determine", "evening", "hoe", "rose", "allow", "fear", "workers", "Washington", "Greek", "women", "bought", "led", "march", "northern", "afraid", "seat", "division", "church", "huge", "view", "effect", "underline",
]

"a", "and", "away", "big", "blue", "can", "come", "down", "find", "for", "funny", "go", "help", "here", "I", "in", "is", "it", "jump", "little", "look", "make", "me", "my", "not", "one", "play", "red", "run", "said", "see", "the", "three", "to", "two", "up", "we", "where", "yellow", "you", "all", "am", "are", "at", "ate", "be", "black", "brown", "but", "came", "did", "do", "eat", "four", "get", "good", "have", "he", "into", "like", "must", "new", "no", "now", "on", "our", "out", "please", "pretty", "ran", "ride", "saw", "say", "she", "so", "soon", "that", "there", "they", "this", "too", "under", "want", "was", "well", "went", "what", "white", "who", "will", "with", "yes", "after", "again", "an", "any", "as", "ask", "by", "could", "every", "fly", "from", "give", "giving", "had", "has", "her", "him", "his", "how", "just", "know", "let", "live", "may", "of", "old", "once", "open", "over", "put", "round", "some", "stop", "take", "thank", "them", "then", "think", "walk", "were", "when", "always", "around", "because", "been", "before", "best", "both", "buy", "call", "cold", "does", "don't", "fast", "first", "five", "found", "gave", "goes", "green", "its", "made", "many", "off", "or", "pull", "read", "right", "sing", "sit", "sleep", "tell", "their", "these", "those", "upon", "us", "use", "very", "wash", "which", "why", "wish", "work", "would", "write", "your", "about", "better", "bring", "carry", "clean", "cut", "done", "draw", "drink", "eight", "fall", "far", "full", "got", "grow", "hold", "hot", "hurt", "if", "keep", "kind", "laugh", "light", "long", "much", "myself", "never", "only", "own", "pick", "seven", "shall", "show", "six", "small", "start", "ten", "today", "together", "try", "warm", "apple", "baby", "back", "ball", "bear", "bed", "bell", "bird", "birthday", "boat", "box", "boy", "bread", "brother", "cake", "car", "cat", "chair", "chicken", "children", "Christmas", "coat", "corn", "cow", "day", "dog", "doll", "door", "duck", "egg", "eye", "farm", "farmer", "father", "feet", "fire", "fish", "floor", "flower", "game", "garden", "girl", "goodbye", "grass", "ground", "hand", "head", "hill", "home", "horse", "house", "kitty", "leg", "letter", "man", "men", "milk", "money", "morning", "mother", "name", "nest", "night", "paper", "party", "picture", "pig", "rabbit", "rain", "ring", "robin", "Santa Claus", "school", "seed", "sheep", "shoe", "sister", "snow", "song", "squirrel", "stick", "street", "sun", "table", "thing", "time", "top", "toy", "tree", "watch", "water", "way", "wind", "window", "wood"


# Child identifiers and mastery threshold
CHILDREN = ['alexander', 'rowan', 'luka', 'isaac']
MASTERY_THRESHOLD = 3

# Single CSV file to track all progress
DATA_FILE = 'sight_progress.csv'

def load_progress(filename):
    progress = {}
    if os.path.exists(filename):
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                w = row['word']
                progress[w] = {c: int(row[c]) for c in CHILDREN}
    # Ensure every sight word is in the data
    for w in SIGHT_WORDS:
        if w not in progress:
            progress[w] = {c: 0 for c in CHILDREN}
    return progress

def save_progress(progress, filename):
    with open(filename, 'w', newline='') as f:
        fieldnames = ['word'] + CHILDREN
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for w, counts in progress.items():
            writer.writerow({'word': w, **counts})

def get_practice_word(progress):
    pool = [w for w in SIGHT_WORDS if any(progress[w][c] < MASTERY_THRESHOLD for c in CHILDREN)]
    return random.choice(pool) if pool else None

def play_congrats_sound():
    congrats.play()

class SightWordApp:
    def __init__(self, master):
        self.master = master
        master.title('Sight Word Mastery')

        self.progress = load_progress(DATA_FILE)

        # Checkboxes for each child
        self.child_vars = {c: tk.IntVar() for c in CHILDREN}
        cb_frame = tk.Frame(master)
        cb_frame.pack(pady=10)
        for idx, c in enumerate(CHILDREN):
            tk.Checkbutton(cb_frame, text=c.title(), variable=self.child_vars[c], font=('Helvetica', 14))\
              .grid(row=0, column=idx, padx=5)

        # Word display
        self.word_label = tk.Label(master, text='', font=('Helvetica', 120))
        self.word_label.pack(expand=True)

        # Action buttons
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text='Mastered',   command=self.mark_mastered,   width=15, height=2, font=('Helvetica',16), bg='green',  fg='white')\
          .grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text='Not Mastered',command=self.next_word,      width=15, height=2, font=('Helvetica',16), bg='orange', fg='white')\
          .grid(row=0, column=1, padx=10)
        tk.Button(master, text='Quit', command=self.quit_program, width=10, height=1, font=('Helvetica',14))\
          .pack(pady=10)

        self.current_word = None
        self.next_word()

    def next_word(self):
        for var in self.child_vars.values():
            var.set(0)
        w = get_practice_word(self.progress)
        self.current_word = w
        self.word_label.config(text=w if w else 'All Done!')

    def mark_mastered(self):
        for c, var in self.child_vars.items():
            if var.get() == 1 and self.current_word:
                self.progress[self.current_word][c] += 1
        play_congrats_sound()
        save_progress(self.progress, DATA_FILE)
        self.next_word()

    def quit_program(self):
        save_progress(self.progress, DATA_FILE)
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))
    app = SightWordApp(root)
    root.mainloop()
