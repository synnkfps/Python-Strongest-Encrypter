## How does the encrypter works?
Transform your text into encrypted symbols using their dictionary

E.G:<br>
`a` = `=` (1st letter of alphabet)<br>
`b` = `==` (2nd letter of alphabet)<br>
`c` = `===` (3rd letter of alphabet)

So,<br>
`abc` = `======` (with spaces: `= == ===`)

## What makes it so hard to decrypt?
The amount of combinations that it can be.<br>
`===` can be `ab` or `ba`<br>
`=====` can be `ad`, `da`, `bc`, `bba`, `abb`, `aca`, `caa`, `aac` and many other combinations.

## How do i decrypt it?
You can't without bruteforce. You can't know what is the right text, you can't know HOW is the right text.

## How do i execute it?
It works in shell/cmd, E.G:<br>
```shell
>>> encrypt('your text', dictionary)

output: '=========================|===============|=====================|==================|/====================|=====|========================|====================|'
```

### Ways to make it easier to read
There are some ways to make it easier to read, such as:
- Replacing `/` with ` ` (space) **IF YOU WANT TO STILL USE |**
- Replacing `|` with ` ` and `/` with `-`
- Replacing `=` with the respective number, E.G: `a` = `1`, `b` = `12`

### Ways to read it
You can't if you remove the space indicators, such as | and /.<br>
If you don't remove those indicators, you can simply count how many = are there, and count the alphabet, so:<br>
`====` is `d`.<br>
`|` is a letter separation, so `=|==|` is `ab`<br>
`/` is a word separation, so `=|/==|` is `a b`

## Will you release a decrypt algorithm to that?
In future, yes.
