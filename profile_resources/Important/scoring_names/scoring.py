from parameters import Parameters

def score_name(name):
    score = 100
    deductions = []

    # Parameter 1: Names can not shorter than two characters
    if not Parameters.check_name_length(name):
        score -= 50
        deductions.append("1. <= 3 characters Rule")

    # Parameter 2: No more than 5 consecutive consonants
    if not Parameters.check_consonant_streak(name):
        score -= 100  # Penalty for having more than 5 consecutive consonants
        deductions.append("2. 4+ Consecutive Consonants Rule")

    # Parameter 3: Vowel every 2-3 consonants
    if not Parameters.check_vowel_spacing(name):
        score -= 50  # Penalty for improper vowel spacing
        deductions.append("3. Vowel spacing Rule")

    # Parameter 4: First three consonants
    if Parameters.check_first_three_consonants(name):
        score -= 50  # Deduct 50 points
        deductions.append("4. First Three Consonants Rule")

    # Parameter 5: First three consonants
    if Parameters.check_last_three_consonants(name):
        score -= 30  # Deduct 50 points
        deductions.append("5. Last Three Consonants Rule")

    # Parameter 6: First three letters have two or more vowels
    if Parameters.check_first_three_vowels(name):
        score -= 25  # Deduct 25 points
        deductions.append("6. First Three Vowels Rule")

    # Parameter 7: Basic words Exception
    exception_status, exception_word = Parameters.dictionary_word_exception(name)
    if exception_status:
        score += 190  # Add points for exception
        deductions.append(f"7. Dictionary Word Exception: '{exception_word}'")

    # Parameter 8: Check for Alphabetical Sequence
    if Parameters.check_alphabetical_sequence(name):
        score -= 15
        deductions.append("8. Alphabetical Sequence Rule")

    # Parameter 9: 4+ vowels consecutive check
    if Parameters.check_consecutive_vowels(name):
        score -= 30  # Deduct points
        deductions.append("9. 4+ Consecutive Vowels Rule")

    # Parameter 10: Semi-vowel check
    semi_vowel_score = Parameters.check_semi_vowels(name)
    if semi_vowel_score > 0:
        score += semi_vowel_score
        deductions.append(f"10. Semi-Vowel Rule: +{semi_vowel_score} points")

    # Parameter 11: Prefix Rule
    prefix_status, prefix = Parameters.check_prefix(name)
    if prefix_status:
        score += 20  # Deduct points for matching prefix
        deductions.append(f"11. Prefix Rule: '{prefix}'")

    # Parameter 12: Suffix Rule
    suffix_status, suffix = Parameters.check_suffix(name)
    if suffix_status:
        score += 20  # Deduct points for matching suffix
        deductions.append(f"12. Suffix Rule: '{suffix}'")

    # Parameter 13: Inverse Scramble Rule, Scoring points for common words
    scramble_score = Parameters.get_letter_frequency_score(name)
    score += scramble_score
    deductions.append(f"13. Inverse Scramble Rule: +{scramble_score} points")

    # Parameter 14: Scramble Rule, Reducing points for un-common words
    scramble_deduction = Parameters.scramble_score(name)
    score -= scramble_deduction
    deductions.append(f"14. Scramble Rule Deduction: {scramble_deduction} points")

    # Cap the score at 100
    score = min(score, 100)

    return max(score, 0), deductions  # Ensure score is not below 0

