import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read the data file
file = pd.read_excel("C:/Users/Jalal Ur Rahman/Downloads/student-mat.xlsx")

# extract the data for grade and study time and create a DataFrame
Grade = file["G3"].tolist()
study_t = file["studytime"].tolist() 
data_set = pd.DataFrame({"Grade": Grade, "Study Time": study_t})

# group the data by grade and study time and count the occurrences
data_set = data_set.groupby(["Grade", "Study Time"]).size().reset_index(name="Count")

# reshape the data to create a pivot table
data_set = data_set.pivot("Grade", "Study Time", "Count")

# plot the heatmap
sns.heatmap(data_set, annot=True, fmt="g", cmap="YlGnBu")
plt.title("Relationship between Final Grade and Weekly Study Time")
plt.show()

pas = []
fail = []
df=pd.read_excel("C:/Users/Jalal Ur Rahman/Downloads/student-mat.xlsx")
specific_column=df["G3"].tolist()
study_time = df["studytime"].tolist()
for i in range(len(specific_column)):
  if specific_column[i]>=10:
    pas.append(study_time[i])
  else:
    fail.append(study_time[i])
plt.boxplot([pas,fail],   boxprops=dict(color='Green'), labels=['Pass Study Time','Fail Study Time'])
plt.title("Relation Between Pass & Fail Student Study")
plt.ylabel("Study Time")
plt.show()

std_s = []
std_n_s = []
dfmat = pd.read_excel("C:/Users/Jalal Ur Rahman/Downloads/student-mat.xlsx")
scs = (dfmat["schoolsup"]).tolist()
stt = (dfmat["G3"]).tolist()
for i in range(len(scs)):
    if scs[i]=='yes':
        std_s.append(stt[i])
    else:
        std_n_s.append(stt[i])
sns.violinplot([std_s,std_n_s])
plt.xlabel('School Support')
plt.ylabel('Final Grade (G3)')
plt.xticks([0, 1], ['Student with scholarship', 'Student without scholarship'])
plt.title('Distribution of Final Grades with and without School Support')
plt.show()

