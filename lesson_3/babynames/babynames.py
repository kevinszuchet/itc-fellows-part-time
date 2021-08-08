#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import os.path
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

# Person
# In Dict: key: name, value: rank
# In a tuple: (name, rank)
PERSON_NAME = 0
PERSON_RANK = 1


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    html = get_text(filename)
    year = get_year(html)
    ranking = get_ranking_dict(html)
    sorted_ranking = [build_showable_person(person) for person in sorted(ranking.items(), key=sorted_by_name)]
    return [year, *sorted_ranking]


def sorted_by_name(person):
    """Gets a tuple, returns the name in order to sort the ranking alphabetically."""
    return person[PERSON_NAME]


def build_showable_person(person):
    """Gets a tuple, returns the 'name rank' format."""
    return f"{person[PERSON_NAME]} {person[PERSON_RANK]}"


def get_year(html):
    """Given the html, searches the pattern of the year and returns it."""
    year_match = re.search(r'Popularity in (?P<year>\d*)', html)
    if year_match:
        return year_match.group("year")

    print("The file doesn't have a year. Please provide a file with the correct format.")
    sys.exit(1)


def get_ranking_dict(html):
    """Given the html, finds all the names and their rank. Then, returns the ranking."""
    pattern = r'<tr align="right"><td>(?P<rank>\d+)</td><td>(?P<boy_name>\w+)</td><td>(?P<girl_name>\w+)</td>'
    ranking = {}
    for rank, boy_name, girl_name in re.findall(pattern, html):
        # We iterate above the names sorted by rank. This solution takes only the 1st time that the name appears.
        if not ranking.get(boy_name):
            ranking.update({boy_name: rank})

        if not ranking.get(girl_name):
            ranking.update({girl_name: rank})
    return ranking


def get_text(filename):
    """Given a filename, tries to read the text inside and returns it."""
    text_file = open(filename, 'r')
    text = text_file.read()
    text_file.close()
    return text


def create_summary(filename, names):
    """Given a filename and the names ranking, writes a summary file with the ranking sorted alphabetically."""
    new_filename = filename + '.summary'
    summary_file = open(new_filename, "w+")
    summary_file.write('\n'.join(names) + '\n')
    summary_file.close()
    print("New summary created:", filename)


def build_summary(filename, summary):
    """Given the filename and the summary flag, it creates the summary and shows the output or create the new file."""
    names = extract_names(filename)
    if summary:
        create_summary(filename, names)
    else:
        print('\n'.join(names) + '\n')
        print('=====================')  # For readability


def try_to_build_summaries(summary, *filenames):
    """
    Given a flag to know if it's necessary to create a summary file and a list of filenames.
    Iterates over each filename to create the summary and prints it or creates the new file.
    """
    unreadable_filenames = []
    for filename in filenames:
        try:
            build_summary(filename, summary)
        except FileNotFoundError:
            unreadable_filenames.append(filename)
            continue

    if unreadable_filenames:
        front_message = "The provided filename" if len(unreadable_filenames) == 1 else "The following filenames"
        end_message = "doesn't" if unreadable_filenames == 1 else "don't" + " exist"
        print(f"{front_message} '{', '.join(unreadable_filenames)}' {end_message}.")


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    try_to_build_summaries(summary, *args)


if __name__ == '__main__':
    main()
