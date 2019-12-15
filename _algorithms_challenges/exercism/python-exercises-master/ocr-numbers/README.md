# Ocr Numbers

## Step One

To begin with, convert a simple binary font to a string containing 0 or 1.

The binary font uses pipes and underscores, four rows high and three columns wide.

```
     _   #
    | |  # zero.
    |_|  #
         # the fourth row is always blank
```

Is converted to `0`

```
         #
      |  # one.
      |  #
         # (blank fourth row)
```

Is converted to `1`.

If the input is the incorrect size, your program should return an error.

If the input is the correct size, but not recognizable, your program should return `?`.

## Step Two

Update your program to recognize multi-character binary strings, replacing garbled numbers with `?`.

## Step Three

Update your program to recognize all numbers 0 through 9, both individually and as part of a larger string.

```
 _ 
 _|
|_ 
   
```

Is converted to `2`

```
      _  _     _  _  _  _  _  _  #
    | _| _||_||_ |_   ||_||_|| | # decimal numbers.
    ||_  _|  | _||_|  ||_| _||_| #
                                 # fourth line is always blank
```

Is converted to `1234567890`

## Step Four

Add a function which does the inverse, so that digits get converted to
LCD style numbers.

`2` is converted to

```
 _
 _|
|_

```

`1234567890` is converted to

```
      _  _     _  _  _  _  _  _
    | _| _||_||_ |_   ||_||_|| | # decimal numbers.
    ||_  _|  | _||_|  ||_| _||_| #
                                 # fourth line is always blank
```


## Step Five

Update your program to handle multiple numbers, one per line. When converting several lines, join the lines with commas.

```
    _  _ 
  | _| _|
  ||_  _|
         
    _  _ 
|_||_ |_ 
  | _||_|
         
 _  _  _ 
  ||_||_|
  ||_| _|
         
```

Is converted to `123,456,789`

## Source

Inspired by the Bank OCR kata [http://codingdojo.org/cgi-bin/wiki.pl?KataBankOCR](http://codingdojo.org/cgi-bin/wiki.pl?KataBankOCR)

