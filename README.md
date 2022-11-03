# Flask Workshop

An advanced Python workshop on back-end development using Flask. 

## Model
```
Course
- department: String (PK)
- number: int (PK)
- name: String
- units: int
- desc?: String
```

## Routes
- /courses (GET, POST)
- /course/{department}/{number} (GET, PUT, DELETE)