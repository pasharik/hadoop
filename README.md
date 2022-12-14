# hadoop

To run java:

```bash
hadoop fs -put input.txt /
hadoop jar word.jar ru.pasharik.WordCountJob /input.txt results
```

Here `results` is a folder, `input.txt` is a file with words