import os
import notepad
import random

'''
I got tired of copying and putting in the same names over and over agian from the internet,
I thought it would be a good idea to try and make a bunch of names on my own. [Note: You will
resort to doing anything when you get deseparate for 'significant' progress.]

Little did I know, by automating that process I created a bunch of nonsense words and names that
make nosense whatsoever. Words like 'Frswyz' were in the list and I couldn't properly open my
notepad file without it neither crashing or slowing down the program significantly.

Distrubing them into different notepads and shuffling them every time I ran 'main.py' made it a 
headache to track each one down and eliminate them. So I gave up on manually looking for each one
and decided to focus my efforts elsewhere. Hence, this mess of a code below you.

I started focusing my efforts on removing any assortment of four-consonants put together since
the odds of them being an existing word were very limited and googling if that word existed, did not
help.

Some of you might be asking yourself, why didn't you put the information into a SQL Database or excel 
or do anything else of the sort. One, I am still very new to the world of programming and computer
science and with a laptop older than my highschool degree, this was the best way I could think of 
doing things.

Two, I wanted to open the file and see my results and check if everything is running correctly. 
Excel took too long to update and open while SQL was going to take up a lot space on the computer 
(i.e. I'm going giving up space on my computer, it's super slow as it is). Why not get a new one? 
I will, just not in this economy. (Check when this was last signed off now).

Three, after 900_000 words (of varying lengths, not sure of the average was, yet), roughly 0.9 Gbs,
the computer would slow down and after ACCIDENTALLY duplicating it on someone's else computer 
I effectively created a zip_bomb and knocked out their computer and any poor online servers that 
were runnning any vital servers (my uni). Sadly, I didn't know what it was until I accidentally 
did it and google randomly started recommended me on how to create a zip_bomb.

My main mission was to get to 1 million unique names since there is no other online website
that either willing to provide that info. nor they didn't have enough because they decided to 
stop after 100_000 or something (which was the smart and sane idea). I respect both decisions but
I wanted the glory of being the biggest one there ever was.

I didn't think something this silly would not only open my eyes to the world of coding and 
programming on a deeper level but also drive me insane as nobody nor nothing on the internet had
ever tried something like this and I was the first. It was frustating because everyone copied
each other and no one bothered trying to double-check uniqueness since many lists online had
multiple intries.

Of course coming this far, I striped wikipedia articles and lists, babynames.org (the more diverse,
the better), dictionaries that could be scarpped, criminal records, scientific papers, any naming
websites and so much more. It got so bad I opened random websites and just Ctrl+A, Ctrl+C, and then
Ctrl+V into input.txt and sumbit that into the lists ('remove_tabs_n_spaces.py' took care of any
formatting issues so I didn't have to do any manual labour work about that).

Doing this since September 26, 2023 - it only dawned how long I have been at this. Such an
insignificant task that has spiralled completely out of anyone's (my) control that I wanted to
reach the goal and the end, that I thought it was time that I would do the unthinkable.
I would 'make my own words' (*horror*).

I made up those words, I added them to the list, and worst of all, I default shuffled the whole 
thing (*scream*). Yep, I goofed up and the file could not be opened normally and the damage was done.
I couldn't open up the file and just Ctrl+Z my whole career, my beautiful baby.
My mistake has come to haunt me and now this code is an attempt to fix it. By doing this I was at
753_432 words, I believe at the time before I made that commit (on my computer, not on github).

The new list count was at over 1.2 million words. I did it. I beat my goal. I can finally put this
thing to rest and peacefully give-up on this nigthmare scenario. 
(Check out 'word_creation/x-word-combo.py', if you want to scream) But no, it couldn't be. When it
came time to finally put this thing to use, all it threw back at me was garbage. NOOOOOOOOOOOO.

How could this be. I did everything right. Not even google text_to_speech (or google_translate) could
pronounce this word. Sometimes it would deny me even a sound, if it was nice it would spell it out 
for me. At this point, it was time to undo my mess and fix my mistake and admit, making your own
words... was an ok idea in hindsight. 

The English-language according to Oxford English Dictionary (2nd edition): Approximately 600,000 word 
forms are defined, including many outdated words that are no longer in common use. So what was I suppose
to do knowing this information. Was I doomed to fail?

No, I won't surrender. I will take as many English sounding letters and words and put it altogether
to make this list and dream of mine come true. English is a broken language anyways, with no consistency
overall what-so-ever. Millions of speakers across the global and we all can't communicate properly to 
anyone at all. Accents, Origins, different languages of inspirations, new-gen words be damned.

Not only have I gained a deeper understanding of how words could be possibly be constructed but I even
realized that you could make a ton of random words that sound like Englsh but they are complete
gibberish. Don't believe me? Put two consonants and then a vowel and then follow it up with another
two consonants max and then a vowel. Repeat this process as much as you see fit. The sweet spot is
(__insert_average_word_length_here__) with a standard deviation of 
(__I_have_no_idea_how_to_calculate_this__). For now, it's seven. Mix-n-match but have a vowel
every two or three letters out and you'll surprised. You might have even guessed a new word that
maybe used in the future (when the english_language is still alive and not going to replaced
by a new language with different hieroglyphics).

If there's a formula for it, someone has definitely made a code out of it (Rule 0101). That's me,
baby. This is one of those things I will long live enough to regret it. But for now, you can see
a group of legit words that I have found and categorized as alien_words since no mother would be
cruel enough to name their baby after this or she is truly convinced she have given birth to
an alien. Which by all means, explain to us how. 

Anyways, I have gone from a count of 1_223_754 to 906_276, just by doing this. If you want 
to have fun, (or laugh at my mistake) open up alien_names folder and like on any .txt file.

Thanks for reading this and I hope I made you laugh at least. (You are reading the process of
someone going insane, make notes to prevent yourself from becoming like me).

- Created and Signed off on 30th/July/2024 - 21:16 by local-exe
'''

names_directory = []
aliens_directory = []
main_names_list = []
alien_names_list = []
DIVISIBLE_COUNT = 100_000
DISPLAY_SUS_LIST = False

''''''

looking_for_alien_x = input("\nWhat alien names are we looking for? : ")
alien_scaner_true = looking_for_alien_x

''''''
name_folder = 'profile_resources/names_list/'
alien_folder = 'profile_resources/alien_names/'

name_files = os.listdir(name_folder)
alien_files = os.listdir(alien_folder)

for name_file in name_files:
    names_directory.append(name_folder + name_file)

for alien_file in alien_files:
    aliens_directory.append(alien_folder + alien_file)

for names_path in names_directory:
    main_names_list += notepad.notepad_function(file=names_path, mode='r')

for alien_path in aliens_directory:
    alien_names_list += notepad.notepad_function(file=alien_path, mode='r')

print(f"\nSearching for aliens with '{alien_scaner_true}' as the search_term...")

def alien_search(string: str):
    return alien_scaner_true.lower() in string.lower()

def human_search(string: str):
    return user_filter_text.lower() in string.lower()

aliens_filtered = list(filter(alien_search, main_names_list))
# combined_alien_list = list(set(alien_names_list)) + aliens_filtered
old_total_name_count = len(main_names_list)
old_alien_count = len(alien_names_list)

alien_count = len(list(aliens_filtered))
main_names_list = [alien_name for alien_name in main_names_list if alien_name not in aliens_filtered]
suspicious_filtered_length = list(filter(lambda x: len(x) != 6, aliens_filtered))

# random.shuffle(main_names_list)
# random.shuffle(alien_names_list)

'''
afjmrw
gnorvx
Dfgmps
bghlsw
ahoprx
pfjpvy
Uloaku
Aegkop
Lmtuwy
Aegiuv
Mprtwx
Cgnouy
Cdfiju
hinpvz
Bimqux
Bcdgwy
Bdhpqy
cfkpqv
Degknt
Apsuwz
Bdmrux
dgmqxt
'''
print((aliens_filtered))
print(f"\nNumber of aliens found with '{alien_scaner_true}' is {alien_count}\n")
print(f"Words of interest : {suspicious_filtered_length} - length '{len(suspicious_filtered_length)}'\n")
display_sus_check = input("Before we continue, would you like to continue to see the list of words that have been filtered outbefore the conditions have been set? (Y/N) : ").lower()

if display_sus_check == "y":
    DISPLAY_SUS_LIST = True

running = True

# Loop list to catch and remove all the human names caught
while running:

    if alien_count == 0:
        running = False
        user_input = "n" # prevent user_input not declared error from raising
        print(f"No aliens with '{alien_scaner_true}' in their name has been found.", end=" " 
              f"This part of the program has been skipped.\n")
        main_names_list += aliens_filtered
    else:
        user_input = input("This is the current list. Would you like to remove any accidental human adductions? (Y/N) : ")

    if user_input in ["no", "n", "not", "nah"]:
        running = False
        alien_count = len(list(aliens_filtered))
        new_total_name_count = len(main_names_list)
        # main_names_list += aliens_filtered

    elif user_input in ["yes", "y", "ye", "yea"]:
        old_alien_count_beta = len(list(aliens_filtered))
        user_filter_text = input("Please enter the words/characters that you want removed. : ")
        if user_filter_text == "quit":
            continue
        user_filter = list(filter(human_search, aliens_filtered))
        aliens_filtered = [item for item in aliens_filtered if item not in user_filter]
        suspicious_filtered_length = [item for item in suspicious_filtered_length if item not in user_filter]
        aliens_filtered = [item for item in aliens_filtered if item not in suspicious_filtered_length]
        alien_count = len(list(aliens_filtered))
        print((aliens_filtered))
        print(f"\nHumans with '{user_filter_text}' have been removed from the list.")
        print(f"The old count is '{old_alien_count_beta}' and new count is '{alien_count}' - length {len(suspicious_filtered_length)}" 
              f" BUT list reduction {old_alien_count_beta - alien_count}")
        print(f"Number of aliens found with '{alien_scaner_true}' is {alien_count}\n")
        if DISPLAY_SUS_LIST == True:
            print(f"Words of interest : {suspicious_filtered_length} - length {len(suspicious_filtered_length)}\n")

    else:
        print("Please input YES or NO. Depending on your response.")

combined_alien_list = list(set(alien_names_list)) + aliens_filtered
alien_notepad_count = int(round((alien_count / 100_000), 0) + 1)
print(f"\nNumber of list names for aliens: {alien_notepad_count + 1}")
for i in range(1, alien_notepad_count + 1):
        if i <= 999:
            file_name = f"{alien_folder}names_{i:04d}.txt" 
            combined_alien_list = notepad.writing_into_file(total_list=combined_alien_list, file_name=file_name, divisible_count=DIVISIBLE_COUNT)

main_notepad_count = int(round((len(main_names_list) / 100_000), 0))
print(f"Number of list names for humans: {main_notepad_count}")
for i in range(1, main_notepad_count + 1):
        if i <= 999:
            file_name = f"{name_folder}names_{i:04d}.txt" 
            main_names_list = notepad.writing_into_file(total_list=main_names_list, file_name=file_name, divisible_count=DIVISIBLE_COUNT)

print(f"\nOld Total_Names count: {old_total_name_count}\n"
      f"New Total_Names count: {new_total_name_count}\n"
      f"Old Total_Aliens count: {old_alien_count}\n"
      f"New Total_Aliens count: {alien_count + old_alien_count}\n"
      f"Difference Count for Names: {old_total_name_count - new_total_name_count}.\n"
      f"Difference Count for Aliens: {alien_count}.")