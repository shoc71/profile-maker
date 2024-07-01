# Filepath and File
filepath = 'profile_resources/input.txt'

# List of Characters that need to be Removed
char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(' , ')',  '=', "+", "·", '›',
             '"', "?", ":", ";", "”", "“", "[", "]", "|", "}", "{", "\\", "•", "<", ">", "ʿ",
             "\"", "!", "@", "#", "$", "%", "^", "&", "*", "~", "`", "§", "®", "»", "«", "★",
             '©', '™', "’", "‘", "’", "●", "ː", "°"] #, "\'", '—'] 

# List of Indents/Spaces that need to be Removed
indent_list = ['/', '\t', ',', '.'] #, ".", '-']

# List of Extras Characters that need to be Removed
extras_list = ['©', '🍓', '🔥', '🏆', '🦸', '🍑', '�', '💚', '🕊', '🌳', '🌙',
              '🐅', '🏔', '🎨', '💙', '🧚', '💸', '⭐', '☀', '❄', '🌊', '\\u200e',
              '🌐', '💀', '😍', '👌', '👍', '🚀', '📈', '🤖', '☆', "‎", 
              "▾", "🏔️", "✅", "👋", "→", "‎", "\u200e"
              "🎤"]

# List of Spaces that need to be replaced by Dashes
space_dash_list = [' ', '–', "−", "—", "	"]

# List of Brand_names that need to be Removed
brands_list = ["Discord", "Twitter", "Instagram", "YouTube", "News", "PayPal", "Patreon", "Ko-fi", "®"
               "At&T"]

# Special Characters that should be included
special_list_vowels = ["Á", "À", "Â", "Å", "Ā", "â", "ä", "ã", "å", "ā", "á", "à", "ā", "ą", "ă",
                        "Æ", "æ",
                        "È", "Ê", "É", "é", "è", "ë", "ê", "ę", "ě", "ẹ", "ē", "ə", "ẹ́", "ĕ","ɛ",
                        "Í", "Î", "Ĭ", "Ì", "í", "ì", "î", "ī", "آ", "ï", "¡", "ĩ", "ĭ", "ị", "ı",
                        "Ö", "Ō", "Ó", "Ø", "Ọ", "ô", "ö", "ŏ", "ø", "ō", "ó", "ò", "ọ̀", "ő", "õ", "ọ́",
                        "Œ", "œ",
                        "Ú", "Ù", "Ü", "ú", "ù", "ü", "ū", "ů", "ŭ", "ũ", "û"
                ]

special_list_consonants = [
    "ß",
    "Č", "Ç", "ç", "ć", "č", "ć",
    "Ɗ", "ḍ", "ɗ",
    "ḥ",
    "ǧ", "ğ",
    "Ḵ", "ƙ",
    "ł",
    "Ń", "ñ", "ń", "ṇ", "ṅ", "ň",
    "ř",
    "Ś", "Š", "ş", "š", "ś", "ṣ", "ŝ",
    "ţ", "ṭ", "ṯ", "Ł",
    "ý", "ÿ",
    "Ž", 'ž', 'ź', "ẓ"
]

special_list_characters = [
    "§", "≡", "€", "Σ", "=", "£", "$" , "ᚦ", "Þ", "θ", "þ", "ф"
]

special_list = special_list_vowels + special_list_consonants + special_list_characters

example = 'https://updater.com/moving-tips/first-apartment-checklist'