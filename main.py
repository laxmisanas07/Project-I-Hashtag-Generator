import random
import pyperclip
import time

def get_hashtags(category):
    data = {
        "coding": ["#python", "#developer", "#code", "#programmer", "#tech", "#buglife", "#webdev", "#software", "#codinglife", "#git"],
        "travel": ["#travel", "#wanderlust", "#trip", "#nature", "#adventure", "#vacation", "#explore", "#mountains", "#beach", "#travelgram"],
        "fitness": ["#fitness", "#gym", "#workout", "#gains", "#bodybuilding", "#cardio", "#health", "#fitfam", "#training", "#muscle"],
        "food": ["#food", "#yummy", "#delicious", "#foodie", "#dinner", "#lunch", "#homemade", "#tasty", "#cooking", "#spicy"],
        "fashion": ["#fashion", "#style", "#ootd", "#model", "#beauty", "#outfit", "#trend", "#shopping", "#streetstyle", "#glam"],
        "photography": ["#photography", "#photooftheday", "#canon", "#nikon", "#art", "#picoftheday", "#visuals", "#camera", "#shoot"],
        "gaming": ["#gaming", "#gamer", "#ps5", "#xbox", "#pcgaming", "#videogames", "#streamer", "#twitch", "#esports", "#pubg"],
        "business": ["#business", "#entrepreneur", "#money", "#success", "#marketing", "#startup", "#hustle", "#motivation", "#growth"],
        "music": ["#music", "#song", "#artist", "#hiphop", "#dj", "#rock", "#singer", "#musician", "#guitar", "#beats"],
        "love": ["#love", "#cute", "#happy", "#couple", "#romance", "#forever", "#smile", "#relationship", "#life", "#goals"],
        "art": ["#art", "#drawing", "#sketch", "#artist", "#painting", "#illustration", "#creative", "#design", "#digitalart", "#ink"],
        "nature": ["#nature", "#earth", "#green", "#sky", "#sun", "#summer", "#flowers", "#beautiful", "#landscape", "#wildlife"],
        "pets": ["#dog", "#cat", "#pets", "#puppy", "#kitten", "#animals", "#petstagram", "#cute", "#love", "#doggo"],
        "meme": ["#meme", "#funny", "#lol", "#dankmemes", "#comedy", "#funnymemes", "#humor", "#jokes", "#memesdaily", "#lmao"],
        "motivation": ["#motivation", "#quotes", "#inspiration", "#goals", "#positive", "#mindset", "#believe", "#successquotes", "#life"]
    }

    key = category.lower()

    if key in data:
        tags = data[key]
        random.shuffle(tags)
        return " ".join(tags)
    else:
        return None

print("--- Project I: Ultimate Hashtag Generator ---")
print("Categories: Coding, Gaming, Fashion, Business, Memes, Travel, Food, Music, Art, Nature, Pets...")

user_input = input("\nEnter a category (e.g., Gaming): ")

print("\nGenerating viral tags... ")
time.sleep(1)

final_tags = get_hashtags(user_input)

if final_tags:
    print("\nHere are your tags:")
    print("-" * 50)
    print(final_tags)
    print("-" * 50)
    
    pyperclip.copy(final_tags)
    print("\nMagic! Tags have been COPIED to your clipboard.")
    print("Ready to paste on Instagram!")
else:
    print("\nError: Category not found. Please check the spelling.")