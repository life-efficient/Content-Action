# Content-Action

This action checks that your content contains everything necessary

## Example usage

uses: life-efficient/Content-Action@v1

# Tests

## Missing files

### Meta files 🚧
- `.lesson.yaml`
- `.module.yaml`
- `.unit.yaml`

### Lesson notebook ✅
- Checks for `Lesson.ipynb` within lesson folders

### Quizzes 🚧
- Checks for `.quiz.yaml` within lesson folders 🚧
- Checks for `.quiz.yaml` within module folders 🚧
- Checks for `.quiz.yaml` within unit folders 🚧

### Challenges ✅
- Checks for `.challenges.yaml` within lesson folders

---
## File content
 
### Quiz length 🚧
- Checks quiz contains at least 5 questions

### Number of challenges 🚧
- Checks `.challenges.yaml` contains at least 5 challenges

### Meta file keys 🚧
- Checks for the following keys in `.unit.yaml`
    - `description`