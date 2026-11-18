import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.width', 2000)

df = pd.read_csv("Students exam data.csv")
print(df[[
  "LunchType",
    "TestPrep",
    "ParentMaritalStatus",
    "PracticeSport",
    "IsFirstChild",
    "NrSiblings",
    "TransportMeans",
    "WklyStudyHours", 
    "MathScore",
    "ReadingScore",
    "WritingScore",
]].head(10).to_string(index=False))
print(df.describe())
df.info()
print(df.isnull().sum())
#Change wekly study hours column
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 2000)
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct","5-10")
print(df.head())
#gender distribution
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (4.3, 4.3))
ax =sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show()
#from the above chart we have analysed that:
#the number of females in the data is more than the number of males
gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean',})
print(gb)
plt.figure(figsize=(6.4, 6.4))
sns.heatmap(gb, annot=True, fmt=".0f")
plt.title("Relationship between Parent's Education\nand Student's Score", fontsize=12)
plt.tight_layout()
plt.show()
#from the above chart we have concluded that the education of the parents have a good impact on their score.
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean',})
print(gb1)
plt.figure(figsize=(5.4, 5.4))
sns.heatmap(gb1, annot=True, fmt=".0f", annot_kws={"size":14})

plt.title("Parent's Marital Status vs Student Scores",
          fontsize=12, pad=15)

plt.tight_layout()
plt.show()

#from the above chart we have concluded that there is no/negligible impact on the
#students score, due to dear parents, marital status.
sns.boxenplot(data= df,x ="MathScore")
plt.title("DistributionMathScore")
plt.show()
sns.boxenplot(data= df,x ="ReadingScore")
plt.title("DistributionRedingscore")
plt.show()
sns.boxenplot(data= df,x ="WritingScore")
plt.title("DistributionWritingScore")
plt.show()
print(df["EthnicGroup"].unique())
#Distribution of ethni groups
groupA = df.loc[df["EthnicGroup"] == "group A"].shape[0]
groupB = df.loc[df["EthnicGroup"] == "group B"].shape[0]
groupC = df.loc[df["EthnicGroup"] == "group C"].shape[0]
groupD = df.loc[df["EthnicGroup"] == "group D"].shape[0]
groupE = df.loc[df["EthnicGroup"] == "group E"].shape[0]

mlist = [groupA, groupB, groupC, groupD, groupE]

plt.pie(mlist, labels=["Group A", "Group B", "Group C", "Group D", "Group E"],
            autopct="%1.1f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()