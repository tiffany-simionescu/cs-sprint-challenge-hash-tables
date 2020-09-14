# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions

          - Hashing functions are designed to create hash tables for key / value data storage. You can input any data type and the output will always be a number. The same input will always return the same output, unless you modify the length of the hash table. A programmer has to be aware of possible collisions while creating a hashing function. The average runtime is O(1), the worst case is O(n)

2. Collision resolution

          - Collision resolution is a way to insure that the hash function is deterministic, or the prevention of different values being saved to the same key / index. You can use chaining to hold multiple values to a single key. You can also increase (or decrease) the size of the hash table based on the load factor, which will reassign key/value pairs. This method can be expensive, so it's best to only do this when necessary. 

3. Performance of basic hash table operations

          - The average runtime is Constant O(1).

4. Load factor

          - Load factor is the number of items in a hash table divided by the total number of slots available. The load factor can help determine if the hash table is too large, too small or just right. When you change the size of the hash table based on the load factor's calculation, you can increase the chances of a collision resolution.

5. Automatic resizing

          - When the value of the load factor is 0.7 or greater, you should increase the size of the hash table to double it's size. When the load factor is 0.2 or less, you should decrease the size of the hash table by half it's size. These values are just average case scenarios and are not set in stone. 

6. Various use cases for hash tables

          - Lookups - (phone book, DNS resolution, student records, library system)

          - Duplicate Prevention - (storing users, voting system)

          - Caching - (useful for servers when clients want to retrieve data and having the server not calculate which data to retrieve and/or send every single time)

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

*Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)*

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's  Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
