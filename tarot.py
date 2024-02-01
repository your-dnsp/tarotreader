import random
from datetime import datetime, timedelta

# Tarot card definitions (abbreviated for simplicity)
tarot_cards = {
    "The Fool": {"upright": "Beginnings, innocence, spontaneity, a free spirit", 
                 "reversed": "Holding back, recklessness, risk-taking"},
    "The Magician": {"upright": "Manifestation, resourcefulness, power, inspired action", 
                     "reversed": "Manipulation, poor planning, untapped talents"},
    "The High Priestess": {"upright": "Intuition, sacred knowledge, divine feminine, the subconscious mind", 
                           "reversed": "Secrets, disconnected from intuition, withdrawal and silence"},
    "The Empress": {"upright": "Femininity, beauty, nature, nurturing, abundance", 
                    "reversed": "Creative block, dependence on others"},
    "The Emperor": {"upright": "Authority, structure, control, fatherhood", 
                    "reversed": "Tyranny, rigidity, coldness"},
    "The Hierophant": {"upright": "Spiritual wisdom, religious beliefs, conformity, tradition, institutions", 
                       "reversed": "Personal beliefs, freedom, challenging the status quo"},
    "The Lovers": {"upright": "Love, harmony, relationships, values alignment, choices", 
                   "reversed": "Disharmony, imbalance, misalignment of values"},
    "The Chariot": {"upright": "Control, willpower, success, action, determination", 
                    "reversed": "Lack of control, lack of direction, aggression"},
    "Strength": {"upright": "Strength, courage, patience, control, compassion", 
                 "reversed": "Weakness, self-doubt, lack of self-discipline"},
    "The Hermit": {"upright": "Soul-searching, introspection, being alone, inner guidance", 
                   "reversed": "Isolation, loneliness, withdrawal"},
    "Wheel of Fortune": {"upright": "Good luck, karma, life cycles, destiny, a turning point", 
                         "reversed": "Bad luck, resistance to change, breaking cycles"},
    "Justice": {"upright": "Justice, fairness, truth, cause and effect, law", 
                "reversed": "Unfairness, lack of accountability, dishonesty"},
    "The Hanged Man": {"upright": "Pause, surrender, letting go, new perspectives", 
                       "reversed": "Delays, resistance, stalling, indecision"},
    "Death": {"upright": "Endings, change, transformation, transition", 
              "reversed": "Resistance to change, personal transformation, inner purging"},
    "Temperance": {"upright": "Balance, moderation, patience, purpose", 
                   "reversed": "Imbalance, excess, self-healing, re-alignment"},
    "The Devil": {"upright": "Shadow self, attachment, addiction, restriction, sexuality", 
                  "reversed": "Releasing limiting beliefs, exploring dark thoughts, detachment"},
    "The Tower": {"upright": "Sudden change, upheaval, chaos, revelation, awakening", 
                  "reversed": "Personal transformation, fear of change, averting disaster"},
    "The Star": {"upright": "Hope, faith, purpose, renewal, spirituality", 
                 "reversed": "Lack of faith, despair, self-trust, disconnection"},
    "The Moon": {"upright": "Illusion, fear, anxiety, subconscious, intuition", 
                 "reversed": "Release of fear, repressed emotion, inner confusion"},
    "The Sun": {"upright": "Positivity, fun, warmth, success, vitality", 
                "reversed": "Inner child, feeling down, overly optimistic"},
    "Judgement": {"upright": "Judgement, rebirth, inner calling, absolution", 
                  "reversed": "Self-doubt, inner critic, ignoring the call"},
    "The World": {"upright": "Completion, integration, accomplishment, travel", 
                  "reversed": "Lack of completion, lack of closure"},
    "Ace of Cups": {"upright": "New love, compassion, creativity, overwhelming emotion", 
                    "reversed": "Blocked or repressed emotions, emptiness, unrequited love"},
    "Two of Cups": {"upright": "Unified love, partnership, mutual attraction", 
                    "reversed": "Break-up, imbalance in relationship, miscommunication"},
    "Three of Cups": {"upright": "Celebration, friendship, creativity, collaborations", 
                      "reversed": "Overindulgence, gossip, isolation"},
    "Four of Cups": {"upright": "Meditation, contemplation, apathy, reevaluation", 
                     "reversed": "Sudden awareness, choosing happiness, acceptance"},
    "Five of Cups": {"upright": "Loss, regret, disappointment, despair, bereavement", 
                     "reversed": "Acceptance, moving on, finding peace, forgiveness"},
    "Six of Cups": {"upright": "Revisiting the past, childhood memories, innocence, joy", 
                    "reversed": "Stuck in the past, naivety, unrealistic"},
    "Seven of Cups": {"upright": "Opportunities, choices, wishful thinking, illusion", 
                      "reversed": "Alignment, personal values, overwhelmed by choices"},
    "Eight of Cups": {"upright": "Disappointment, abandonment, withdrawal, escapism", 
                      "reversed": "Fear of moving on, stagnation, clinginess"},
    "Nine of Cups": {"upright": "Contentment, satisfaction, gratitude, wish come true", 
                     "reversed": "Lack of fulfillment, dissatisfaction, materialism"},
    "Ten of Cups": {"upright": "Divine love, blissful relationships, harmony, alignment", 
                    "reversed": "Broken home, disharmony, unhappiness"},
    "Page of Cups": {"upright": "Creative opportunities, intuitive messages, curiosity, possibility", 
                     "reversed": "Immaturity, emotional instability, insecurity"},
    "Knight of Cups": {"upright": "Romance, charm, 'knight in shining armor', imagination", 
                       "reversed": "Unrealistic, jealousy, moodiness"},
    "Queen of Cups": {"upright": "Compassionate, caring, emotionally stable, intuitive, in flow", 
                      "reversed": "Emotional insecurity, co-dependency, manipulation, moody"},
    "King of Cups": {"upright": "Emotional balance and control, generosity, good advice", 
                     "reversed": "Manipulation, moodiness, volatility"},
    "Ace of Wands": {"upright": "New beginnings, inspiration, potential, creation", 
                     "reversed": "Lack of energy, lack of passion, boredom"},
    "Two of Wands": {"upright": "Future planning, progress, decisions, discovery", 
                     "reversed": "Fear of change, playing it safe, bad planning"},
    "Three of Wands": {"upright": "Expansion, foresight, overseas opportunities", 
                       "reversed": "Obstacles, delays, frustration"},
    "Four of Wands": {"upright": "Celebration, joy, harmony, relaxation, homecoming", 
                      "reversed": "Lack of support, transience, home conflicts"},
    "Five of Wands": {"upright": "Conflict, disagreements, competition, tension, diversity", 
                      "reversed": "Conflict avoidance, increased focus, respect for differences"},
    "Six of Wands": {"upright": "Success, public recognition, progress, self-confidence", 
                     "reversed": "Egotism, disrepute, lack of recognition, punishment"},
    "Seven of Wands": {"upright": "Challenge, competition, protection, perseverance", 
                       "reversed": "Giving up, overwhelmed, overly protective"},
    "Eight of Wands": {"upright": "Movement, fast paced change, action, alignment", 
                       "reversed": "Delays, frustration, resisting change, internal alignment"},
    "Nine of Wands": {"upright": "Resilience, courage, persistence, test of faith, close to success", 
                      "reversed": "Inner resources, struggle, overwhelm, defensive, paranoia"},
    "Ten of Wands": {"upright": "Burden, extra responsibility, hard work, completion", 
                     "reversed": "Inability to delegate, overstressed, burnt out"},
    "Page of Wands": {"upright": "Inspiration, ideas, discovery, limitless potential, free spirit", 
                      "reversed": "Lack of direction, procrastination, creating conflict"},
    "Knight of Wands": {"upright": "Energy, passion, inspired action, adventure, impulsiveness", 
                        "reversed": "Anger, impulsiveness, recklessness, lack of direction"},
    "Queen of Wands": {"upright": "Courage, determination, joy, charismatic, independent", 
                       "reversed": "Selfishness, jealousy, demanding, vengeful"},
    "King of Wands": {"upright": "Big picture, leader, overcoming challenges, visionary", 
                      "reversed": "Impulsive, overbearing, unachievable expectations, tyrannical"},
    "Ace of Pentacles": {"upright": "Opportunity, prosperity, new venture, trust", 
                         "reversed": "Missed opportunity, lack of planning and foresight"},
    "Two of Pentacles": {"upright": "Balance, adaptability, time management, prioritization", 
                         "reversed": "Loss of balance, disorganized, overwhelmed"},
    "Three of Pentacles": {"upright": "Teamwork, collaboration, learning, implementation", 
                           "reversed": "Lack of teamwork, disregard for skills"},
    "Four of Pentacles": {"upright": "Saving money, security, conservatism, scarcity, control", 
                          "reversed": "Over-spending, greed, materialism"},
    "Five of Pentacles": {"upright": "Financial loss, poverty, lack mindset, isolation", 
                          "reversed": "Recovery from financial loss, spiritual poverty"},
    "Six of Pentacles": {"upright": "Giving, receiving, sharing wealth, generosity, charity", 
                         "reversed": "Debt, selfishness, one-sided charity"},
    "Seven of Pentacles": {"upright": "Long-term view, sustainable results, perseverance, investment", 
                           "reversed": "Lack of long-term vision, limited success or reward"},
    "Eight of Pentacles": {"upright": "Apprenticeship, education, quality, engagement", 
                           "reversed": "Lack of focus, perfectionism, no motivation"},
    "Nine of Pentacles": {"upright": "Luxury, self-sufficiency, financial independence", 
                          "reversed": "Financial dependency, superficiality, no self-discipline"},
    "Ten of Pentacles": {"upright": "Wealth, inheritance, family, establishment, retirement", 
                         "reversed": "Financial failure, solitude, loss"},
    "Page of Pentacles": {"upright": "Manifestation, financial opportunity, skill development", 
                          "reversed": "Lack of progress, procrastination, learn from failure"},
    "Knight of Pentacles": {"upright": "Efficiency, routine, conservatism, methodical", 
                            "reversed": "Boredom, stagnation, laziness, feeling 'stuck'"},
    "Queen of Pentacles": {"upright": "Nurturing, practical, providing financially, luxury", 
                           "reversed": "Financial independence, self-care, work-home conflict"},
    "King of Pentacles": {"upright": "Abundance, prosperity, security, ambition, discipline", 
                          "reversed": "Greed, materialism, indulgence, not grounded"},
    "Ace of Swords": {"upright": "Breakthrough, clarity, sharp mind, mental clarity", 
                      "reversed": "Confusion, brutality, chaos, misunderstanding"},
    "Two of Swords": {"upright": "Difficult choices, indecision, stalemate, impasse", 
                      "reversed": "Lesser of two evils, no right choice, confusion"},
    "Three of Swords": {"upright": "Heartbreak, emotional pain, sorrow, grief, hurt", 
                        "reversed": "Recovery, forgiveness, moving on"},
    "Four of Swords": {"upright": "Rest, relaxation, meditation, contemplation, recuperation", 
                       "reversed": "Restlessness, burnout, stress, lack of progress"},
    "Five of Swords": {"upright": "Conflict, tension, loss, defeat, win at all costs", 
                       "reversed": "Reconciliation, making amends, past resentment"},
    "Six of Swords": {"upright": "Transition, change, rite of passage, releasing baggage", 
                      "reversed": "Emotional baggage, unresolved issues, resisting transition"},
    "Seven of Swords": {"upright": "Betrayal, deception, getting away with something, stealth", 
                        "reversed": "Imposter syndrome, self-deceit, keeping secrets"},
    "Eight of Swords": {"upright": "Restriction, limitation, self-imposed restriction, imprisonment", 
                        "reversed": "Self-acceptance, new perspective, freedom"},
    "Nine of Swords": {"upright": "Anxiety, worry, fear, depression, nightmares", 
                       "reversed": "Inner turmoil, deep-seated fears, secrets"},
    "Ten of Swords": {"upright": "Failure, collapse, defeat, betrayal, end of the road", 
                      "reversed": "Survival, recovery, regeneration, inevitable end"},
    "Page of Swords": {"upright": "Curiosity, restless, mentally agile, learning", 
                       "reversed": "Deception, manipulation, all talk and no action"},
    "Knight of Swords": {"upright": "Ambitious, action-oriented, driven to succeed, fast-thinking", 
                         "reversed": "Restlessness, unfocused, impulsive, burn-out"},
    "Queen of Swords": {"upright": "Independent, unbiased judgement, clear boundaries, direct communication", 
                        "reversed": "Overly-emotional, bitchy, cold-hearted, cruel"},
    "King of Swords": {"upright": "Intellectual power, authority, truth, analytical", 
                       "reversed": "Manipulative, tyrannical, abusive"}

}

def draw_tarot_cards(question):
    # Count the number of words in the question
    word_count = len(question.split())

    # Determine the number of cards to draw
    if word_count <= 6:
        num_cards = 1
    elif 7 <= word_count <= 12:
        num_cards = 2
    else:
        num_cards = 3

    # Draw the cards
    drawn_cards = random.sample(tarot_cards.keys(), num_cards)

    # Display the results
    for card in drawn_cards:
        orientation = "upright" if random.choice([True, False]) else "reversed"
        print(f"Card: {card} - {orientation.capitalize()}")
        print(f"Meaning: {tarot_cards[card][orientation]}\n")

def daily_card():
    start_date = datetime(2024, 1, 1)  # Set a start date for the cycle
    today = datetime.now()
    days_passed = (today - start_date).days

    card_index = days_passed % len(tarot_cards)
    daily_tarot_card = list(tarot_cards.keys())[card_index]

    # You can also determine if the card is upright or reversed randomly
    orientation = "upright" if random.choice([True, False]) else "reversed"

    print(f"Today's card ({today.strftime('%Y-%m-%d')}): {daily_tarot_card} - {orientation.capitalize()}")
    print(f"Meaning: {tarot_cards[daily_tarot_card][orientation]}\n")


# Loop to keep asking for user input
while True:
    user_input = input("Type your question, or type 'daily' for the daily card (Type 'exit' to end): ").strip()

    # Check for disallowed characters - hehe security
    if any(char in user_input for char in ["\\", "/", "%", "'"]):
        print("Invalid characters detected. Try again.")
        continue

    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'daily':
        daily_card()
    else:
        draw_tarot_cards(user_input)

