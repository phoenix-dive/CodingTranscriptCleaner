# Coding Transcript Optimizer

This is a Python script that cleans up scripts made by Zoom's automated transcript feature. You can install Python [here](https://www.python.org/).

# How to run this?

A reminder that as always, do make backups before you run your files into a Python script, especially one that has the potential to overwrite files. 

Put the transcripts you wish to clean into the Input folder. Then, run a command prompt:
`python3 main.py`, then, a lot of other things
`"Transcripts/<filename>"`, where `<filename>` is the name of the file you wish to clean.
`"Output/<outputname>", where `<outputname>` is the name of the file you wish to output to.
Then, optional flags below:
`-o "Yes"` will override the file entirely, if it has already been made. Without this, the script will simply add on the contents of the cleaned transcript to the output file if it already exists.
`-n "[NAME1]" "[NAME2]" ...` following `-n`, any strings will be considered a name that the script will attempt to clean from. By defalut, this is `[INTERVIEWER]` and `[PARTICIPANT]`.
`-r "<regexpattern>` will remove any text that matches a particular regex script.

Examples:
```python3 main.py "Input/test2" "Output/hello"```
Will take a file named test2 in the Input folder, clean it, and post the cleaned version in the Output file and name it `hello`.

```python3 main.py "Input/test2" "Output/hello" -n "[INTERVIEWER]" "[PARTICIPANT]" "[STUFF]" -o "Yes"``` will do the Input/Output stuff, except it will override "hello", and the names that will be condensed together will be "[INTERVIEWER]", "[PARTICIPANT]", and "[STUFF]".


