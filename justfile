[private]
jf_aoc:
   @just -g --list --unsorted

# Create the directories for the year
mkdir year:
    @mkdir -p aoc_{{ year }}/data


# Create the Python file for the new day 
new-day year day: (mkdir year)
  sed -e 's/day\*\*\*.txt/day{{ day }}.txt/g' .idea/fileTemplates/AOC.py > aoc_{{ year }}/day{{ day }}.py
  touch aoc_{{ year }}/data/day{{ day  }}.txt

# Run the code for a given day
run year day:
  #! /bin/bash
  cd aoc_{{ year }}
  uv run --with .. day{{ day }}.py
