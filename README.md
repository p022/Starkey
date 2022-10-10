## Starkey Firmware Engineering: Interview Question

## Steps for running code

1. Download and save the Starkey folder in a directory.
2. Go into the Starkey folder through the command prompt and run the program with the following command:   
```
python main.py
```
## Sample input.json file:
```
[
  {
    "user": "u1",
    "timestamp": "12345",
    "command": "Red"
  },
  {
    "user": "u1",
    "timestamp": "12345",
    "command": "Blue"
  },
  {
    "user": "u1",
    "timestamp": "123456",
    "command": "Red"
  },
  {
    "user": "u1",
    "timestamp": "1234578",
    "command": "Red"
  },
  {
    "user": "u2",
    "timestamp": "12345",
    "command": "Red"
  },
  {
    "user": "u3",
    "timestamp": "12345",
    "command": "Red"
  }
]
```

## Sample output.json file generated:
```
{"u1": {"Red": ["12345", "123456", "1234578"], "Blue": ["12345"]}, "u2": {"Red": ["12345"]}, "u3": {"Red": ["12345"]}}
```


