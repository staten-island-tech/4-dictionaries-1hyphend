Skip to main content
Google Classroom
Classroom
Comp Sci/Engineering T1
SKS21T_30 (Period 3) 2025 1
Home
Calendar
Enrolled
To-do
N
NHS Cohort Class of 2029
Current Freshmen
U
US HISTORY REG ACC
HXZKE-8
S
SITHS Career Development Center 2025-26
C
Class of 2029 - College Advisement
GAS11QC_9 (Period 13) 2025 1
P
Period 1 T1- Freshman Russian T1
31R605_2025_1_FRS61H_1
C
Comp Sci/Engineering T1
SKS21T_30 (Period 3) 2025 1
H
Health Education
PHS11_22 (Period 2) 2025 1
P
Period 4: Geometry T1
MGS21H_45 (Period 4) 2025 1
I
Intro Tech Careers T1
RZS21TF_71 (Period 7) 2025 1
A
AP World History T1
HGS41X_58 (Period 5) 2025 1
p
p9 FRIDAY Chem Lab
C
Chemistry T1
SCS21H_88 (Period 8) 2025 1
E
English T1 Writing
EES81HW_65 (Period 6) 2025 1
H
Harry Potter Book & Movie Club
G
Gamers Extra Credit
C
Class 808
Regents
Archived classes
Settings
Dictionary ProjectAssignment details
Dictionary Project
Michael Whalen
•
Sep 16
Learning Progress
•
10 points
MAKE SURE TO DOWNLOAD THE MARKDOWN FILE TO ACCOMPANY THISRepo: https://classroom.github.com/a/obOEkGRb

Python Dictionary Project 2025.pdf
PDF

Enumerate and Dicts.md
Text
Class comments
Your work
Assigned
Private comments
### 🗂 What is a Dictionary in Python?

Think of a **dictionary** in Python like a backpack with lots of labeled pockets.

* Each **label** is called a **key**.
* Each **thing inside** the pocket is called a **value**.

For example:

```python
item = {
    "name": "Samsung 55\" 4K UHD TV",
    "price": 429.99,
    "department": "Televisions",
    "description": "55-inch Ultra HD Smart TV with HDR and built-in streaming apps."
}
```

Here:

* `"name"` is a key, and `"Samsung 55\" 4K UHD TV"` is its value.
* `"price"` is a key, and `429.99` is its value.
* `"department"` is a key, and `"Televisions"` is its value.

So this dictionary tells us **information about one Best Buy item**.

---

### 📋 What is `best_buy_items`?

* Instead of just one dictionary, you have a **list of dictionaries**.
* Each dictionary describes **one item** (TV, laptop, camera, etc.).
* All together, it’s like Best Buy’s mini-catalog inside Python.

---

### 🎯 How to Select Specific Properties

If you want **just the name** of the first item, you write:

```python
best_buy_items[0]["name"]
```

* `[0]` → means “the first item in the list” (because Python starts counting at 0).
* `["name"]` → means “look inside that dictionary and grab the name.”

So this prints:

```
Samsung 55" 4K UHD TV
```

If you want the **price** of the second item:

```python
best_buy_items[1]["price"]
```

---

### 🔢 What is `enumerate`?

Normally, when you loop over a list, you just get the items.
But sometimes you also want the **number** (the position in the list).

That’s what `enumerate` does: it gives you **both the index number AND the item**.

Example from your code:

```python
for index, item in enumerate(best_buy_items):
    print(index, ":", item["name"])
```

This does two things:

1. `index` → the position in the list (0, 1, 2, 3, …).
2. `item` → the dictionary at that position.

So the output looks like:

```
0 : Samsung 55" 4K UHD TV
1 : LG 65" OLED TV
2 : Sony Noise Cancelling Headphones
...
```

It’s like making a **numbered shopping list** automatically.

---

✅ **Summary for a middle schooler:**

* A dictionary is like a **labeled backpack pocket** (key = label, value = stuff inside).
* A list of dictionaries is like a **shopping catalog**.
* `["name"]` or `["price"]` lets you pull out a specific piece of info.
* `enumerate` is like saying: “Give me the item AND its number in line.”

---

![Dictionary Diagram](output.png)
Enumerate and Dicts.md
Displaying Enumerate and Dicts.md.