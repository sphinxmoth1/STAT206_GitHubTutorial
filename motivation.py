import pandas as pd

grades = pd.read_json("grades.json")
new_grades = grades.copy()

# --------------- BEGIN STUDENT CODE --------------- #
# Change id jong029 grade to A:
new_grades.loc[new_grades["id"] == "jong029", "grade"] = "A"
# Alternate method:
#new_grades.loc["jong029", "grade"] = "A"

new_grades.loc[new_grades["id"] == "anago001", "grade"] = "A"


# ---------------- END STUDENT CODE ---------------- #

new_grades.to_json("new_grades.json", index = False)
new_grades
