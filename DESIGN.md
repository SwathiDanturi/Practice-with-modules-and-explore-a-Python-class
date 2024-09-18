**Developer**: Swathi
**Collaborator(s)**: 

### Design of `only_integers()` core function
- define `only_integers()` method and `self`, current instance of the class `Sentence` is the parameter
- `self.sentence`is an instance variable of the class `Sentence`
- `self.sentence` is initialized in constructor to a string which is passed as an argument when the class instance is created
- define the accumulator `integer_lst` and assign it to a empty list
- split `self.sentence` using `.split()` and generate the list of words
- `for` each `word` in `self.sentence.split()`, iterate through the following statements:
    - check whether the `word` is a digit using `isdigit()`
    - if it is a digit then append the `word` to the accumulator `integer_lst`
- using `.join()` convert the `integer_lst` to a string and assign it to `self.sentence`

### Design of `filter_words()` core function
- define `filter_words()` method and `self`, current instance of the class `Sentence` is the first parameter
- `word_lst` is the list of words to be removed from `self.sentence` is the second parameter
- `self.sentence`is an instance variable of the class `Sentence`
- `self.sentence` is initialized in constructor to a string which is passed as an argument when the class instance is created
- define an empty list `result_list` to store the result
- split `self.sentence` using `.split()` and generate the list of words
- `for` each `string` in `self.sentence.split()`, iterate through the following statements:
    - check whether `string` is `not in` the `word_lst`
    - if it is not then append the `string` to the list `result_list`
- using `.join()` convert the `result_list` to a string and assign it to `self.sentence`