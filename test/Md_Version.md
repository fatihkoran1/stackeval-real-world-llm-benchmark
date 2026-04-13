# StackEval Pilot - Human Scoring Sheet

## Scoring Rubric

- **0** = completely wrong or unhelpful
- **1** = partially correct but missing crucial details
- **2** = mostly correct and useful
- **3** = excellent answer I would trust completely

---

# Question 1

## Original Question

```text
Question:
Why is my string not changing after passing it to a function in C?

Code:
#include <stdio.h>

void changeString(char str[]) {
    str = "Hello";
}

int main() {
    char str[] = "World";
    changeString(str);
    printf("%s", str);
    return 0;
}
```

## Answer A

### Model Response

```text
`str` is not changing because inside `changeString`, you are only changing the local parameter pointer, not the contents of the original array.

### What is wrong
In this function:

```c
void changeString(char str[]) {
    str = "Hello";
}
```

`str` behaves like a local pointer to the first character of the array passed in. Assigning:

```c
str = "Hello";
```

just makes that local pointer point to the string literal `"Hello"`. It does **not** copy `"Hello"` into the original array in `main`.

So `main` still has:

```c
char str[] = "World";
```

and that is what gets printed.

### Correct solution
Copy the new string into the existing array instead of reassigning the pointer.

Use `strcpy`:

```c
#include <stdio.h>
#include <string.h>

void changeString(char str[]) {
    strcpy(str, "Hello");
}

int main() {
    char str[] = "World";
    changeString(str);
    printf("%s", str);
    return 0;
}
```

### Corrected code
```c
#include <stdio.h>
#include <string.h>

void changeString(char str[]) {
    strcpy(str, "Hello");
}

int main() {
    char str[] = "World";
    changeString(str);
    printf("%s", str);
    return 0;
}
```

Output:
```c
Hello
```

Note: this works here because `str` has enough space for `"Hello"` including the null terminator.
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

## Answer B

### Model Response

```text
## The Problem

Inside `changeString()`, you're reassigning the **local pointer** `str` to point to a string literal — this has no effect on the original array in `main()`.

When an array is passed to a function, it **decays into a pointer**. Reassigning that pointer only changes the local copy; the original array in `main()` is untouched.

---

## What's Wrong

```c
void changeString(char str[]) {
    str = "Hello";  // ❌ Only reassigns the local pointer, not the original array
}
```

---

## The Fix

Use `strcpy()` to copy the new string **into** the memory the pointer points to, rather than redirecting the pointer itself.

> ⚠️ Ensure the destination array is large enough to hold the new string.

---

## Corrected Code

```c
#include <stdio.h>
#include <string.h>

void changeString(char str[]) {
    strcpy(str, "Hello");  // ✅ Copies "Hello" into the original array's memory
}

int main() {
    char str[] = "World";  // Array is 6 bytes — large enough for "Hello" + '\0'
    changeString(str);
    printf("%s", str);     // Output: Hello
    return 0;
}
```

---

## Key Takeaway

| Action | Effect |
|---|---|
| `str = "Hello"` | Redirects the **local pointer** only |
| `strcpy(str, "Hello")` | Writes into the **original array's memory** |
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

## Answer C

### Model Response

```text
## Problem Explanation

The issue lies in how C handles string assignments and function parameter passing.

### What's Wrong

In the `changeString` function, `str = "Hello";` doesn't modify the original string passed to it. Instead, it changes the local pointer `str` to point to the string literal "Hello". This change is not reflected outside the function because `str` is passed by value (as a pointer), and modifying the pointer itself doesn't affect the original array.

### Correct Solution

To modify the original string, you should copy the new string into the array passed to the function.

### Corrected Code

```c
#include <stdio.h>
#include <string.h>

void changeString(char str[]) {
    strcpy(str, "Hello"); // Copy "Hello" into str
}

int main() {
    char str[] = "World";
    changeString(str);
    printf("%s", str);
    return 0;
}
```

**Key Change:** Using `strcpy` from `string.h` to copy "Hello" into the `str` array, modifying its contents instead of just changing the local pointer. This ensures the change is visible in `main`.
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

## Answer D

### Model Response

```text
### 1. What’s happening

`changeString(str)` does **not** change the original array in `main`.

In C, function parameters like `char str[]` are really just pointers passed by value. So inside `changeString`, `str` is a local copy of the pointer. When you do:

```c
str = "Hello";
```

you only change that local pointer to point to the string literal `"Hello"`. The original `str` in `main` still contains `"World"`.

---

### 2. What is wrong

This line is the problem:

```c
str = "Hello";
```

It does **not modify the contents** of the string. It only reassigns the local pointer.

Also, if your goal is to change the original string, you cannot assign a new string literal to a character array like that. You must copy characters into the existing array.

---

### 3. Correct solution

Use `strcpy()` to copy `"Hello"` into the array passed from `main`.

Note: the destination array must be large enough to hold the new string.

---

### 4. Corrected code

```c
#include <stdio.h>
#include <string.h>

void changeString(char str[]) {
    strcpy(str, "Hello");
}

int main() {
    char str[20] = "World";
    changeString(str);
    printf("%s\n", str);
    return 0;
}
```

This will print:

```c
Hello
```
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

---

# Question 2

## Original Question

```text
Question:
Why am I getting a segmentation fault when accessing an array in C?

Code:
#include <stdio.h>

int main() {
    int *arr;
    arr[0] = 10;
    printf("%d\n", arr[0]);
    return 0;
}
```

## Answer A

### Model Response

```text
`arr` is a pointer, but it does not point to valid memory.

### What’s wrong
```c
int *arr;
arr[0] = 10;
```

Here, `arr` is an uninitialized pointer. It contains an indeterminate address, so writing to `arr[0]` tries to access random memory. That causes **undefined behavior**, often a **segmentation fault**.

### Correct fix
Make `arr` point to valid memory before using it.

For a single element, the simplest fix is to use a normal variable or allocate memory. Since you asked for one clear fix, here is the dynamic allocation version:

### Corrected code
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(sizeof(int));
    if (arr == NULL) {
        return 1;
    }

    arr[0] = 10;
    printf("%d\n", arr[0]);

    free(arr);
    return 0;
}
```

### Summary
- `arr` was never initialized.
- You must allocate memory or point it to an existing valid object before indexing it.
- After `malloc`, `arr[0]` is valid.
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

## Answer B

### Model Response

```text
## The Problem

`arr` is a **pointer that has never been initialized** — it contains a garbage memory address. Writing to `arr[0]` attempts to write to that random address, causing a segmentation fault.

---

## What's Wrong

```c
int *arr;   // Uninitialized pointer — points to garbage address
arr[0] = 10; // Writing to unknown memory → SEGFAULT
```

You declared a pointer but never allocated (or pointed it to) valid memory.

---

## The Fix

You have two options:

**Option 1 — Stack allocation (fixed size):**
```c
int arr[5]; // Allocates array directly on the stack
```

**Option 2 — Heap allocation (dynamic size):**
```c
int *arr = malloc(5 * sizeof(int)); // Allocates memory on the heap
// ... use arr ...
free(arr); // Always free when done
```

---

## Corrected Code

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(5 * sizeof(int)); // Allocate memory for 5 integers

    if (arr == NULL) {       // Always check if malloc succeeded
        return 1;
    }

    arr[0] = 10;
    printf("%d\n", arr[0]); // Output: 10

    free(arr);               // Release allocated memory
    return 0;
}
```

---

## Key Takeaway

| Declaration | Valid? | Why |
|---|---|---|
| `int *arr;` | ❌ | Uninitialized pointer |
| `int arr[5];` | ✅ | Stack memory allocated |
| `int *arr = malloc(...)` | ✅ | Heap memory allocated |

**Rule:** Always ensure a pointer points to valid allocated memory before dereferencing it.
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

## Answer C

### Model Response

```text
**Problem Explanation**

The segmentation fault occurs because you're attempting to access memory that hasn't been allocated.

**What's Wrong**

The issue lies in these lines:
```c
int *arr;
arr[0] = 10;
```
Here, `arr` is a pointer to an integer, but it doesn't point to a valid memory location. You're trying to access and modify the memory it points to, which is undefined behavior.

**Correct Solution**

To fix this, you need to allocate memory for `arr` before accessing it. You can do this using dynamic memory allocation with `malloc`.

**Corrected Code**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Allocate memory for one integer
    int *arr = malloc(sizeof(int));
    
    if (arr == NULL) {
        // Handle memory allocation failure
        printf("Memory allocation failed\n");
        return 1;
    }
    
    arr[0] = 10;
    printf("%d\n", arr[0]);
    
    // Don't forget to free the allocated memory
    free(arr);
    return 0;
}
```
This code allocates memory for one integer using `malloc`, checks for allocation failure, and then frees the memory when done to prevent a memory leak.
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

## Answer D

### Model Response

```text
1. **Problem**

`arr` is only a pointer. It does **not** point to valid memory yet, so `arr[0] = 10;` tries to write to an invalid address, which causes a segmentation fault.

2. **What is wrong**

```c
int *arr;
```

This declares a pointer, but it does not allocate or assign storage for any integers. Before using `arr[0]`, you must make it point to allocated memory or to an existing array.

3. **Correct solution**

Allocate memory for one `int` before using `arr[0]`, then free it when done.

4. **Corrected code**

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(sizeof(int));
    if (arr == NULL) {
        return 1;
    }

    arr[0] = 10;
    printf("%d\n", arr[0]);

    free(arr);
    return 0;
}
```

If you only need one value, you could also use a normal `int` instead of a pointer.
```

### Evaluation

**Score (0-3):** ______

**Comment:**

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

---

