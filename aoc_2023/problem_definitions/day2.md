 Day 1 - Advent of Code 2023    window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});

[Advent of Code](/)
===================

*   [\[About\]](/2023/about)
*   [\[Events\]](/2023/events)
*   [\[Shop\]](https://teespring.com/stores/advent-of-code)
*   [\[Settings\]](/2023/settings)
*   [\[Log Out\]](/2023/auth/logout)

Dan Shernicoff 44\*

  0.0.0.0:[2023](/2023)
=======================

*   [\[Calendar\]](/2023)
*   [\[AoC++\]](/2023/support)
*   [\[Sponsors\]](/2023/sponsors)
*   [\[Leaderboard\]](/2023/leaderboard)
*   [\[Stats\]](/2023/stats)

Our [sponsors](/2023/sponsors) help make Advent of Code possible:

[Accenture Federal Services](https://www.accenture.com/us-en/industries/afs-index) - Technology & ingenuity moving missions forward – come solve problems with us. Hiring software engineers, developers, and more now. Refer someone to earn up to $20K.

\--- Day 1: Trebuchet?! ---
---------------------------

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all _fifty stars_ by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants _one star_. Good luck!

You try to ask why they can't just use a [weather machine](/2015/day/1) ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a [trebuchet](https://en.wikipedia.org/wiki/Trebuchet) ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been _amended_ by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific _calibration value_ that the Elves now need to recover. On each line, the calibration value can be found by combining the _first digit_ and the _last digit_ (in that order) to form a single _two-digit number_.

For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `142`.

Consider your entire calibration document. _What is the sum of all of the calibration values?_

Your puzzle answer was `55130`.

\--- Part Two ---
-----------------

Your calculation isn't quite right. It looks like some of the digits are actually _spelled out with letters_: `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine` _also_ count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    

In this example, the calibration values are `29`, `83`, `13`, `24`, `42`, `14`, and `76`. Adding these together produces `281`.

_What is the sum of all of the calibration values?_

Your puzzle answer was `54985`.

Both parts of this puzzle are complete! They provide two gold stars: **
