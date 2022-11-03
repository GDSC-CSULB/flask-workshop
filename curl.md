# cURL Commands

```shell
# Get all courses
curl 127.0.0.1:5000/courses

# Create a new course
curl -d '{"department": "MATH", "number": 123, "name": "Calculus II", "units": 4}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/courses

# Get a single course
curl 127.0.0.1:5000/course/MATH/123

# Update a course
curl -d '{"desc": "Second calculus course"}' -H "Content-Type: application/json" -X PUT 127.0.0.1:5000/course/MATH/123

# Delete a course
curl -X DELETE 127.0.0.1:5000/course/MATH/123
```