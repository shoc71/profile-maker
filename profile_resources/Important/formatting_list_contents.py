'''
Emojis, Extras, character, speacial character lists have all been moved to their own py files because of their
length and how big they can unreasonable get. Here are some of the primitive versions we have
'''

# List of Indents/Spaces that need to be Removed
indent_list = ['/', '\t', ',', '.', "\n"] #, ".", '-']

# List of Spaces that need to be replaced by Dashes
space_dash_list = [' ', '–', "−", "—", "	"]

'''# Special Characters that should be included
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
    "Ɗ", "Ď", "ḍ", "ɗ",
    "ǧ", "ğ",
    "ḥ",
    "Ḵ", "ƙ",
    "Ľ", "ł", "ľ",
    "Ń", "ñ", "ń", "ṇ", "ṅ", "ň",
    "ř",
    "Ś", "Š", "ş", "š", "ś", "ṣ", "ŝ",
    "ţ", "ṭ", "ṯ", "Ł", "ť",
    "ý", "ÿ",
    "Ž", 'ž', 'ź', "ẓ"
]

special_list_characters = [
    "§", "≡", "€", "Σ", "=", "£", "$" , "ᚦ", "Þ", "θ", "þ", "ф"
]

special_list = special_list_vowels + special_list_consonants + special_list_characters

example = 'https://updater.com/moving-tips/first-apartment-checklist'''