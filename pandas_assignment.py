"""
Weekly Pandas Assignment
Covers Questions 1–14 from the supplied task sheet.

Run:
    python pandas_assignment.py

The script prints the requested results and creates all required CSV files
in the same folder as this script.
"""

from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path(__file__).resolve().parent


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def main():
    # ------------------------------------------------------------------
    # SECTION A — SERIES (Questions 1–2)
    # ------------------------------------------------------------------
    section("SECTION A: SERIES — QUESTIONS 1–2")

    nigerian_states = ["Lagos", "Kano", "Rivers", "Enugu", "Oyo"]
    states_series = pd.Series(
        nigerian_states,
        index=["a", "b", "c", "d", "e"],
    )

    print("Q1 — Series of five Nigerian states:")
    print(states_series)

    print("\nQ2 — First element (position 0):")
    print(states_series.iloc[0])

    print("\nQ2 — Element with index label 'c':")
    print(states_series.loc["c"])

    print("\nQ2 — Complete Series with index labels:")
    print(states_series)

    # ------------------------------------------------------------------
    # SECTION B — DATAFRAMES (Questions 3–7)
    # ------------------------------------------------------------------
    section("SECTION B: DATAFRAMES — QUESTIONS 3–7")

    data = {
        "name": ["Ada", "John", "Mary", "Peter", "Grace"],
        "age": [21, 24, 19, 27, 23],
        "gender": ["Female", "Male", "Female", "Male", "Female"],
        "city": ["Lagos", "Abuja", "Kano", "Enugu", "Kaduna"],
    }
    df = pd.DataFrame(data)

    print("Q3 — Complete DataFrame:")
    print(df)

    print("\nQ3 — Name column:")
    print(df["name"])

    print("\nQ3 — City column:")
    print(df["city"])

    print("\nQ4 — Students younger than 23:")
    print(df[df["age"] < 23])

    print("\nQ4 — Students aged 23 or above:")
    print(df[df["age"] >= 23])

    print("\nQ4 — Students who live in Kaduna:")
    print(df[df["city"] == "Kaduna"])

    print("\nQ4 — Female students:")
    print(df[df["gender"] == "Female"])

    print("\nQ5 — Average age:")
    print(df["age"].mean())

    print("\nQ5 — Maximum age:")
    print(df["age"].max())

    print("\nQ5 — Minimum age:")
    print(df["age"].min())

    print("\nQ5 — Statistical summary:")
    print(df.describe())

    # Q6: index=False prevents an extra index column in either CSV.
    df.to_csv(OUTPUT_DIR / "class_data.csv", index=False)
    df.to_csv(OUTPUT_DIR / "class_data_backup.csv", index=False)
    print("\nQ6 — Created class_data.csv and class_data_backup.csv (no index column).")

    # Q7: Add one new student while keeping the original DataFrame unchanged.
    new_student = pd.DataFrame(
        [{"name": "Michael", "age": 22, "gender": "Male", "city": "Ibadan"}]
    )
    updated_df = pd.concat([df, new_student], ignore_index=True)

    print("\nQ7 — Updated DataFrame with Michael:")
    print(updated_df)
    updated_df.to_csv(OUTPUT_DIR / "updated_class_data.csv", index=False)
    print("Q7 — Created updated_class_data.csv.")

    # ------------------------------------------------------------------
    # SECTION C — READING CSV FILES (Questions 8–9)
    # ------------------------------------------------------------------
    section("SECTION C: READING CSV FILES — QUESTIONS 8–9")

    data_read = pd.read_csv(OUTPUT_DIR / "class_data.csv")

    print("Q8 — First five rows:")
    print(data_read.head())

    print("\nQ8 — Names as a Python list:")
    print(data_read["name"].tolist())

    print("\nQ8 — Ages as a Python list:")
    print(data_read["age"].tolist())

    print("\nQ8 — Cities as a Python list:")
    print(data_read["city"].tolist())

    print("\nQ9 — All information for Grace:")
    print(data_read[data_read["name"] == "Grace"])

    print("\nQ9 — All information for John:")
    print(data_read[data_read["name"] == "John"])

    print("\nQ9 — Students whose names start with M:")
    print(data_read[data_read["name"].str.startswith("M")])

    # ------------------------------------------------------------------
    # SECTION D — STUDENT SCORES AND SCHOLARSHIPS (Questions 10–12)
    # ------------------------------------------------------------------
    section("SECTION D: STUDENT SCORES AND SCHOLARSHIPS — QUESTIONS 10–12")

    score_data = {
        "name": ["David", "Esther", "Samuel", "Janet", "Peter", "Ruth", "Daniel", "Favour"],
        "age": [20, 22, 24, 21, 19, 25, 22, 23],
        "final_exam_score": [82, 91, 68, 76, 55, 88, 73, 95],
    }
    scores_df = pd.DataFrame(score_data)
    scores_df.to_csv(OUTPUT_DIR / "student_scores.csv", index=False)
    print("Created student_scores.csv.")

    scores_read = pd.read_csv(OUTPUT_DIR / "student_scores.csv")

    print("\nQ10 — Statistical summary:")
    print(scores_read.describe())

    print("\nQ10 — Average final exam score:")
    print(scores_read["final_exam_score"].mean())

    print("\nQ10 — Highest final exam score:")
    print(scores_read["final_exam_score"].max())

    print("\nQ10 — Lowest final exam score:")
    print(scores_read["final_exam_score"].min())

    print("\nQ11 — Students younger than 23:")
    print(scores_read[scores_read["age"] < 23])

    print("\nQ11 — Students with final exam scores of 75 or above:")
    print(scores_read[scores_read["final_exam_score"] >= 75])

    print("\nQ11 — Students who scored below 60:")
    print(scores_read[scores_read["final_exam_score"] < 60])

    print("\nQ11 — Students aged 22 or older who scored at least 75:")
    print(scores_read[
        (scores_read["age"] >= 22) & (scores_read["final_exam_score"] >= 75)
    ])

    # Q12: Scholarship eligibility is a score of 75 or above.
    scholarship_students = scores_read[scores_read["final_exam_score"] >= 75]
    scholarship_path = OUTPUT_DIR / "scholarship_students.csv"
    scholarship_students.to_csv(scholarship_path, index=False)

    print("\nQ12 — Eligible scholarship students:")
    print(scholarship_students)

    print("\nQ12 — Read scholarship_students.csv back into Pandas:")
    scholarship_read = pd.read_csv(scholarship_path)
    print(scholarship_read)

    # ------------------------------------------------------------------
    # BONUS CHALLENGE — QUESTIONS 13–14
    # ------------------------------------------------------------------
    section("BONUS CHALLENGE — QUESTIONS 13–14")

    print("Q13 — Students whose names start with D:")
    students_starting_d = scores_read[scores_read["name"].str.startswith("D")]
    print(students_starting_d)
    students_starting_d.to_csv(OUTPUT_DIR / "students_starting_D.csv", index=False)
    print("Q13 — Created students_starting_D.csv.")

    print("\nQ13 — Students whose names start with S:")
    print(scores_read[scores_read["name"].str.startswith("S")])

    # Q14: An original dataset of ten students, with the requested columns.
    practice_data = {
        "name": ["Amina", "Bola", "Chidi", "Dayo", "Emeka",
                 "Fatima", "Grace", "Hassan", "Ife", "Jide"],
        "age": [18, 20, 19, 21, 17, 22, 19, 20, 18, 23],
        "gender": ["Female", "Female", "Male", "Male", "Male",
                   "Female", "Female", "Male", "Female", "Male"],
        "city": ["Lagos", "Abuja", "Enugu", "Ibadan", "Kano",
                 "Kaduna", "Lagos", "Abuja", "Oyo", "Benin City"],
        "score": [88, 67, 74, 92, 59, 81, 70, 64, 96, 72],
    }
    practice_df = pd.DataFrame(practice_data)

    print("\nQ14.1 — Complete practice DataFrame:")
    print(practice_df)

    passed_students = practice_df[practice_df["score"] >= 70]
    print("\nQ14.2 — Students who scored at least 70:")
    print(passed_students)

    print("\nQ14.3 — Students younger than 20:")
    print(practice_df[practice_df["age"] < 20])

    print("\nQ14.4 — Average score:")
    print(practice_df["score"].mean())

    print("\nQ14.5 — Student(s) with the highest score:")
    highest_score = practice_df["score"].max()
    print(practice_df[practice_df["score"] == highest_score])

    practice_csv = OUTPUT_DIR / "practice_students.csv"
    practice_df.to_csv(practice_csv, index=False)
    print("\nQ14.6 — Created practice_students.csv.")

    print("\nQ14.7 — Read practice_students.csv back into Pandas:")
    practice_read = pd.read_csv(practice_csv)
    print(practice_read)

    practice_read[practice_read["score"] >= 70].to_csv(
        OUTPUT_DIR / "practice_students_70_and_above.csv",
        index=False,
    )
    print("\nQ14.8 — Created practice_students_70_and_above.csv.")

    print("\nALL TASKS FINISHED.")
    print(f"CSV files are saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
