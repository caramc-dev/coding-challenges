# Codewars Practice

Repo to store and share codewars practice solutions in preparation for the CFG foundation exam.

## Index by Concept

| Concept                  | Files                                                                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ternary                  | even_or_odd.py, boolean_to_string.py, string_ends_with.py                                                                                                      |
| Modulus                  | even_or_odd.py, count_the_divisors.py                                                                                                                          |
| Maths                    | count_the_milliseconds.py, square_digits.py, first_factorial.py                                                                                                |
| Conditional Branching    | who_likes_it.py                                                                                                                                                |
| List Comprehension       | vowel_count.py, count_the_divisors.py, line_numbering.py, title_every_word.py, reverse_word.py, alphabet_position.py, spin_words.py, indexed_capitilisation.py |
| Loops                    | delete_occurances_more_than_n_times.py, create_phone_num.py, find_the_duplicate.py, mumble.py, question_marks.py                                               |
| Enumerate                | create_phone_num.py, mumble.py, line_numbering.py, indexed_capitilisation.py, question_marks.py                                                                |
| Zip                      | find_missing_letter.py, question_marks.py                                                                                                                      |
| Sorting                  | sum_of_2_lowest_ints.py, find_smallest_int.py                                                                                                                  |
| Built-in Functions       | min_max.py, letter_count.py, find_smallest_int.py                                                                                                              |
| String Manipulation      | pig_latin.py, reverse_word.py, mumble.py, title_every_word.py, expanded_nums.py, alphabet_position.py, square_digits.py                                        |
| String Slicing           | reverse_word.py, spin_words.py, question_marks.py                                                                                                              |
| String Formatting        | who_likes_it.py, create_phone_num.py, expanded_nums.py, sum_the_strs.py                                                                                        |
| Tuples                   | question_marks.py                                                                                                                                              |
| Validation               | simple_password.py                                                                                                                                             |
| Dictionaries             | counting_characters.py                                                                                                                                         |
| Dictionary Comprehension | counting_characters.py                                                                                                                                         |
| Recursion                | first_factorial.py                                                                                                                                             |
|                          |                                                                                                                                                                |

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

### lists:
* `.append(item)` - appends a single item to the end of a list. Mutates the original list.
* `.insert(index, element)` - inserts a new element at the index position, mutating the original list. 2 arguments are always required.
* `.remove(item)` - removes the first occurrence of a specified item from the list. Raises a ValueError if the item is not found. Mutates the original list.
* `.pop(index)` - removes and returns the item at the given index. Defaults to the last item if no index is provided. Mutates the original list.
* `.sort()` - sorts the original list in place. By default, sorts in ascending order. `reverse=True` will sort in descending order. Mutates the original list.
* `sorted()` - does the same job as .sort() but returns a new list, leaving the original unchanged.
* `.index(item)` - returns the index position of the first occurrence of an item. Raises a ValueError if not found.
* `.count(value)` - counts the number of times a value appears in a list. Linear search so best used on smaller lists.
* `.reverse()` - reverses the items in a list in place - [1, 2, 3] becomes [3, 2, 1]. Mutates the original list.

### Dictionaries:
* `.keys()` - returns all keys in the dictionary as a view object, for example: `dict_keys(['a', 'b', 'c'])`. Can be converted to a list with `list()`.
* `.values()` - returns all values in the dictionary as a view object, for example: `dict_values(['a', 'b', 'c'])`. Can be converted to a list with `list()`.
* `.items()` - returns all key-value pairs as tuples in a view object. Useful for iterating: `for k, v in dict.items()`.
* `.get(key, default)` - returns the value for a key if it exists. Returns `None` by default if not found, or a specified default value. Safer than `dict[key]` which raises a KeyError if missing.
* `.update(other_dict)` - merges another dictionary into the current one. If a key already exists, its value is overwritten. Mutates the original dictionary.

### Built-ins:
* `len(object)` - returns the number of items in an object (string, list, dict etc).
* `range(start, stop, step)` - generates a sequence of numbers. Stop is not inclusive. Commonly used in for loops.
* `min(iterable)`, `max(iterable)` - returns the smallest or largest item in an iterable.
* `sum(iterable)` - returns the total of all items in an iterable. Items must be numeric.
* `enumerate(iterable, start=0)` - returns an index and value pair for each item. Useful when you need both the position and value in a loop.
* `zip(iterable1, iterable2)` - combines two or more iterables into tuples, pairing items by index position. Stops at the shortest iterable.
* `int()`, `str()`, `float()` - convert a value to an integer, string, or float respectively.
* `set(iterable)` - converts an iterable to a set, removing all duplicates. Unordered so index positions cannot be relied on.
* `any(iterable)` - returns True if at least one item in the iterable is True.
* `all(iterable)` - returns True only if every item in the iterable is True.
* `type(object)` - returns the data type. For example `type(1)` returns `<class 'int'>`.

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

## List comprehension patterns

Standard - apply an expression to every item:
`[expression for item in iterable]`

Filter - only include items where condition is true:
`[expression for item in iterable if condition]`

Ternary - apply one of two expressions based on a condition:
`[expression_if_true if condition else expression_if_false for item in iterable]`