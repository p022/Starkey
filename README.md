## Starkey Firmware Engineering: Interview Question

## Steps for running code

1. Download and save the Starkey folder in a directory.
2. Go into the Starkey folder through the command prompt and run the program with the following command:   
```
python main.py
```
3. To get useful user statistics from the parsed event logs, run the following command:   
```
python statistics.py
```
## Sample input.json file:
```
[
  {
    "user": "user_1",
    "timestamp": "12345",
    "command": "red"
  },
  {
    "user": "user_1",
    "timestamp": "12345",
    "command": "blue"
  },
  {
    "user": "user_1",
    "timestamp": "123456",
    "command": "red"
  },
  {
    "user": "user_1",
    "timestamp": "1234578",
    "command": "red"
  },
  {
    "user": "user_2",
    "timestamp": "12345",
    "command": "red"
  },
  {
    "user": "user_3",
    "timestamp": "12345",
    "command": "red"
  }
]
```

## Sample output.json file generated:
```
{"user_1": {"red": ["12345", "123456", "1234578"], "blue": ["12345"]}, "user_2": {"red": ["12345"]}, "user_3": {"red": ["12345"]}}
```


