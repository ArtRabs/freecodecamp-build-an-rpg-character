# RPG Character Creator

A Python lab that implements **`create_character(name, strength, intelligence, charisma)`** to validate inputs and return a formatted four-line character sheet using full dots (`●`) and empty dots (`○`).

---

### Summary
This contains a single function that:

- Validates a character name and three stats.
- Returns error messages when validation fails.
- Returns a single multi-line string representing the character when inputs are valid.

---

### Requirements
- **Python 3.6+**  
- No external packages required

---

### Function Signature
**`create_character(name, strength, intelligence, charisma)`**

- **Parameters (in order):**
  - `name` — string
  - `strength` — int
  - `intelligence` — int
  - `charisma` — int

---

### Validation Rules and Exact Messages
The function must perform validations in the order below and return the exact messages when a check fails.

**Name validation**
- If `name` is not a string → return  
  **`The character name should be a string`**
- If `name` is an empty string → return  
  **`The character should have a name`**
- If `name` length > 10 → return  
  **`The character name is too long`**
- If `name` contains spaces → return  
  **`The character name should not contain spaces`**

**Stats validation**
- If any stat is not an integer → return  
  **`All stats should be integers`**
- If any stat < 1 → return  
  **`All stats should be no less than 1`**
- If any stat > 4 → return  
  **`All stats should be no more than 4`**
- If the sum of stats ≠ 7 → return  
  **`The character should start with 7 points`**

---

### Successful Return Format
When all validations pass, the function must **return** (not print) a single string composed of four lines separated by `\n`:

1. **Line 1:** the character name (exactly)  
2. **Line 2:** `STR ` followed by `strength` full dots and `(10 - strength)` empty dots  
3. **Line 3:** `INT ` followed by `intelligence` full dots and `(10 - intelligence)` empty dots  
4. **Line 4:** `CHA ` followed by `charisma` full dots and `(10 - charisma)` empty dots

Use the Unicode characters `●` for full and `○` for empty. Do not add extra trailing newlines or extra spaces beyond the format above.

**Example returned string**:
```
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

---

### License
MIT © ArtRabs

Exercise adapted from freeCodeCamp.
