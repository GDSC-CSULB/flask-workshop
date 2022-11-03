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

# Filter Courses by attribute
Course.query.filter_by(name='Introduction to Programming').all()

# Get a single Course by primary key
Course.query.get(('CECS', 174))

# Update Course 
db.session.query(Course).filter(Course.department == 'CECS', Course.number == 174).update({'units': 4})

# Delete Course
db.session.query(Course).filter(Course.department == 'CECS', Course.number == 174).delete()
```

Populate the Course table

```python
from app import db
from app.models import Course

cecs_courses = [Course(department='CECS', number=105, name='CECS Intro', units=1, desc='Intro to CECS'),
                Course(department='CECS', number=174, name='Python', units=3, desc='Intro to Python'),
                Course(department='CECS', number=225, name='Digital Logic', units=3,
                       desc='Digital logic and assembly programming'),
                Course(department='CECS', number=228, name='Discrete Math I', units=3,
                       desc='First discrete mathematics course'),
                Course(department='CECS', number=274, name='Data Structures', units=3, desc='Data structures'),
                Course(department='CECS', number=277, name='OOP', units=3, desc='Object-oriented programming')]

db.session.add_all(cecs_courses)

math_courses = [Course(department='MATH', number=122, name='Calculus I', units=4, desc='Derivatives'),
                Course(department='MATH', number=224, name='Calculus III', units=4, desc='Multivariable'),
                Course(department='MATH', number=247, name='Linear Algebra', units=3,
                       desc='Linear algebra course')]
db.session.add_all(math_courses)

db.session.commit()
Course.query.all()

# Primary Key Violation
math_12 = Course(department='MATH', number=122, name='Another calculus course', units=2)
```