# Database Commands

Create a Flask shell

```shell
flask shell
```

SQL Alchemy methods

```python
from app import db
from app.models import Course

cecs_174 = Course(department='CECS', number=174, name='Introduction to Programming', units=3,
                  desc='Introductory course to programming in Python')

# Insert Course into database
db.session.add(cecs_174)
db.session.commit()

# Get all Course
Course.query.all()

# Filter Departments by attribute
Course.query.filter_by(name='Introduction to Programming').all()

# Get a single Department by primary key
Course.query.get(('CECS', 174))

# Update Department 
db.session.query(Course).filter(Course.department == 'CECS', Course.number == 174).update({'units': 4})

# Delete Department
db.session.query(Course).filter(Course.department == 'CECS', Course.number == 174).delete()
```

Test and populate the Course table

```python
from app import db
from app.models import Course

cecs_174 = Course(department='CECS', number=174, name='Introduction to Programming', units=3,
                  desc='Introductory course to programming in Python')
db.session.add(cecs_174)
db.session.commit()
Course.query.all()

cecs_228 = Course(department='CECS', number=228, name='Discrete Math', units=3,
                  desc='Discrete mathematics')
cecs_274 = Course(department='CECS', number=274, name='Data Structures', units=3,
                  desc='Learn about arrays, linked lists, trees, etc.')
math_122 = Course(department='MATH', number=122, name='Calculus', units=3)
db.session.add(cecs_228)
db.session.add(cecs_274)
db.session.add(math_122)
db.session.commit()
Course.query.all()

# Primary Key Violation
math_12 = Course(department='MATH', number=122, name='Culus', units=2)
```