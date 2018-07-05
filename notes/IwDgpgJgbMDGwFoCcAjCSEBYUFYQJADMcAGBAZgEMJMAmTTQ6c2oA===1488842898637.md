# Python tips

## Logging

The very basic template is setting the verbose level and use the logging function with a correct level. The [basicConfig](https://docs.python.org/2/library/logging.html#logging.basicConfig) function of the logging module is a template for quick setup. The default logging format is not very nice. 
`logging.basicConfig(level = logging.DEBUG)`

## Basic file operation
Create a new folder, `os.mkdir`, `os.path.isdir`

## Codecs
This usually happen when trying to print Chinese.
[Printing Chinese is actually pretty easy, just make sure encode the string to utf-8](http://stackoverflow.com/questions/2688020/how-to-print-chinese-word-in-my-code-using-python).

## Random

See [the documentation of the random library](https://docs.python.org/2/library/random.html)
Some random function I need, like pick one item from an array.

`random.seed()` the first thing to do.
`random.choice()` is a utility function provided by python, but might not be available from other languages.
`random.sample(population, k)` should be `random.choice()` when `k=1`?
`random.shuffle` is an in-place shuffle method

## Ping
[How to ping servers](http://stackoverflow.com/questions/2953462/pinging-servers-in-python)

## How to update a PyPI package

## Progressbar

Is it easy to implement a progressbar in python? This is useful for experiments.

## Compute the fps of a program
Save code snippets here directly.

## How to output text (print) in pytest

## How to write a progressbar

```python
sys.stdout.write('\r')
sys.stdout.write('Record %d frames' % len(camera_info))
sys.stdout.flush()
```
