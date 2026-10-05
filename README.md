# Python MCQ Exam Application

A **GUI-based Python MCQ Examination Application** designed to conduct a Python programming test with random questions, a countdown timer, question navigation, review functionality, automatic submission, and detailed result analysis.

## 📌 Project Overview

The Python MCQ Exam Application allows students to attend a programming examination consisting of **20 multiple-choice questions**.

The application provides an interactive exam interface where students can:

* Answer Python MCQ questions
* Navigate between questions
* Move to previous and next questions
* Mark questions for review
* View remaining exam time
* Automatically submit the exam when the timer ends
* Submit the exam manually
* Calculate the final score
* Calculate percentage
* Display grade
* View question-wise performance analysis

The project was developed as part of the **Career Bridge IT Services – Python Full Stack Mock Test**.

## ✨ Features

### 1. Question Bank

The application maintains a collection of Python programming MCQs.

Each question contains:

* Question text
* Multiple-choice options
* Correct answer

### 2. Random Questions

Questions are selected randomly from the question bank.

This helps provide a different question sequence for different exam attempts.

### 3. Timer

A countdown timer is provided during the examination.

The remaining time is displayed to the student.

When the timer reaches zero, the exam is automatically submitted.

### 4. Previous / Next Navigation

Students can navigate through the questions using:

* Previous
* Next

This allows students to review their answers before submitting the examination.

### 5. Mark for Review

Students can mark questions for review.

This helps identify questions that need to be checked again before final submission.

### 6. Auto Submit

If the examination time expires, the application automatically submits the examination.

This prevents students from continuing the exam after the allotted time.

### 7. Score Calculation

After submission, the application calculates the student's score based on the number of correct answers.

### 8. Percentage

The application calculates the student's percentage based on the total score.

### 9. Grade

A grade is displayed based on the student's performance.

Example:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A     |
| 80–89      | B     |
| 70–79      | C     |
| 60–69      | D     |
| Below 60   | F     |

### 10. Question-wise Analysis

The result section provides question-wise analysis.

It can show:

* Question number
* Student's answer
* Correct answer
* Correct / Incorrect status

This helps the student understand their mistakes.

## 🖥️ Application Flow

```text
Start Application
       ↓
Display Exam Instructions
       ↓
Start Exam
       ↓
Load Random Questions
       ↓
Answer Questions
       ↓
Previous / Next
       ↓
Mark Questions for Review
       ↓
Submit Exam
       ↓
Calculate Score
       ↓
Calculate Percentage
       ↓
Generate Grade
       ↓
Display Result
       ↓
Question-wise Analysis
```

If the timer reaches zero:

```text
Timer Expires
      ↓
Automatic Submission
      ↓
Score Calculation
      ↓
Result
```

## 🛠️ Technologies Used

* **Programming Language:** Python
* **GUI:** Tkinter
* **Data Handling:** Python Data Structures
* **Randomization:** Python `random` module
* **Timer:** Tkinter `after()` method

## 📂 Suggested Project Structure

```text
python_mcq_exam/
│
├── online_exam.py
├── requirements.txt
├── README.md

```

### File Description

| File               | Description                                      |
| ------------------ | ------------------------------------------------ |
| `main.py`          | Starts the application                           |
| `requirements.txt` | Contains project dependencies                    |
| `README.md`        | Project documentation                            |                  |

## ⚙️ Installation

### Step 1: Install Python

Make sure Python is installed on your system.

Check the Python version:

```bash
python --version
```

### Step 2: Clone the Project

```bash
git clone <your-github-repository-url>
```

### Step 3: Open the Project

```bash
cd python_mcq_exam
```

### Step 4: Install Dependencies

If a `requirements.txt` file is provided:

```bash
python -m pip install -r requirements.txt
```

Tkinter is normally included with standard Python installations.

### Step 5: Run the Application

```bash
python main.py
```

## 📝 Exam Rules

* The examination contains **20 MCQs**.
* Questions are selected randomly.
* Students can move between questions.
* Questions can be marked for review.
* Students can submit the examination manually.
* The examination is automatically submitted when the timer expires.
* The final score and percentage are calculated after submission.
* Question-wise analysis is displayed in the result section.

The requirement document specifically states that the application should support question bank, random questions, timer, previous/next navigation, mark for review, auto-submit, score calculation, result, percentage, grade, and question-wise analysis.

## 🎯 Project Objectives

The main objectives of this project are:

1. To develop a user-friendly Python examination application.
2. To conduct Python programming MCQ tests.
3. To randomly select examination questions.
4. To provide a time-limited examination environment.
5. To allow students to review questions.
6. To automatically submit the examination after time expiration.
7. To calculate student performance.
8. To provide detailed question-wise analysis.

## 📊 Example Result

```text
================================
          EXAM RESULT
================================

Total Questions : 20
Attempted       : 18
Correct         : 15
Incorrect       : 3
Unanswered      : 2

Score           : 15 / 20
Percentage      : 75%

Grade           : C

================================
      QUESTION ANALYSIS
================================

Q1  - Correct
Q2  - Correct
Q3  - Incorrect
Q4  - Correct
...
Q20 - Unanswered
```

## 🚀 Future Enhancements

The project can be further improved by adding:

* Student login and registration
* Database integration using MySQL
* Admin panel
* Admin question management
* Multiple subjects
* Difficulty levels
* Exam history
* Leaderboard
* Certificate generation
* Detailed performance charts
* Export results to PDF
* User authentication
* Online examination support

## 👨‍💻 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python Programming
* Object-Oriented Programming
* Tkinter GUI Development
* Functions and Modules
* Lists and Dictionaries
* Randomization
* Event Handling
* Timer Management
* Conditional Statements
* Score Calculation
* User Interface Design
* Application Logic

## 📌 Conclusion

The **Python MCQ Exam Application** is a simple and interactive GUI-based examination system that demonstrates how Python can be used to build a complete desktop application.

The project combines **Python programming, GUI development, random question selection, timer management, examination logic, and result analysis** into a single application.
