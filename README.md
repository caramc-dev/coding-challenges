# Codewars Practice

Repo to store and share codewars practice solutions in preparation for the CFG foundation exam.

## Index by Concept

| Concept                  | Files                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Ternary                  | even_or_odd.py                                                                                                                                 |
| Modulus                  | even_or_odd.py, count_the_divisors.py                                                                                                          |
| Maths                    | count_the_milliseconds.py, square_digits.py                                                                                                    |
| Conditional Branching    | who_likes_it.py                                                                                                                                |
| List Comprehension       | count_the_divisors.py, line_numbering.py, title_every_word.py, reverse_word.py, alphabet_position.py, spin_words.py, indexed_capitilisation.py |
| Loops                    | delete_occurances_more_than_n_times.py, create_phone_num.py, find_the_duplicate.py, mumble.py                                                  |
| Enumerate                | create_phone_num.py, mumble.py, line_numbering.py, indexed_capitilisation.py                                                                   |
| Sorting                  | sum_of_2_lowest_ints.py, find_smallest_int.py                                                                                                  |
| Built-in Functions       | min_max.py, letter_count.py, find_smallest_int.py                                                                                              |
| String Manipulation      | pig_latin.py, reverse_word.py, mumble.py, title_every_word.py, expanded_nums.py, alphabet_position.py, square_digits.py                        |
| String Slicing           | reverse_word.py, spin_words.py                                                                                                                 |
| String Formatting        | who_likes_it.py, create_phone_num.py, expanded_nums.py, sum_the_strs.py                                                                        |
| Validation               | simple_password.py                                                                                                                             |
| Dictionaries             | counting_characters.py                                                                                                                         | 
| Dictionary Comprehension | counting_characters.py                                                                                                                         | |


## Methods:

### strings:
* `.upper()`, `.lower()`, `.capitalize()` - change the case of your string.
* `.split(separator, maxsplit)` - split a string into smaller parts - defaults used if no args added.
  * `separator` arg allows you to choose a delimiter on where to split. The default is on any white space.
  * `maxsplit` arg defines the maximum number of splits to perform. The default is -1 which is unlimited.
* `.join()` - takes items from a list or tuple and merges into a single string. 
  * A separator is required, before the dot, and is often a space i.e: `" ".join` 
  * Can only be used with strings. If you have other data types within the list they must be converted before join is used. 
* `.strip()` - removes whitespace at the start and end of a string. `.lstrip()` or `.rstrip()` strips whitespace only from the left or right respectively.
* `.replace(old, new)` - replaces all occurrences of `old` with `new` within a string. As strings are immutable, this creates a new string rather than modifying the original.
* `.count(substring)` - counts the number of times a substring appears in the string. Case-sensitive.
* `.find(substring)` - returns the index position of the first occurrence of a substring. Returns -1 if not found.
* `.isalpha()`, `.isdigit()`, `.isupper()`, `.islower()` - checks if a string is made up of the respective types (letters, digits, uppercase, lowercase). Returns a Boolean value.
* `ord(character)` - returns the ASCII integer value of a single character. e.g. `ord('a')` returns 97.
* `chr(integer)` - the reverse of ord(). Returns the character that corresponds to an ASCII integer. e.g. `chr(97)` returns 'a'.


## Syntax to remember

### Basic Slicing Syntax:

1. [start : stop : step] - Slicing order; If you want to use the default value, leave it blank.
2. [start] - Where to start the slice. Defaults to 0. Negative values count from the end: [-1] is the last character, [-2] is second to last, and so on.
3. [stop] - Where to stop the slice. Not inclusive, so [0:3] returns index positions 0, 1 and 2. Add +1 if you want to include the stop position.
4. [step] - How many characters to skip between each. Defaults to 1 (every character). Step 2 returns every other character. [-1] reverses the string.

Examples:
* [::2] - slice from index position to the end position (non-inclusive), in increments of 2
* [0:3] - outputs index positions 0, 1 & 2
* [::-1] - reverses a string

### Slice function 

Another way to slice a string, is to use the slice() function with commas to denote start, stop, slice.

Example:
string = "12345678912"
slice(0, 10, 2) would slice from index position up to 9 (as the upper bound is not inclusive) skipping every other one. This would output "13579"

