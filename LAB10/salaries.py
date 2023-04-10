import pandas as pd
df = pd.read_csv(r"C:\Users\amare\Downloads\Salaries.csv")
print(df)


result = df.head(10)
print("First 10 rows of the DataFrame:")
print(result)

print("Male Professor with highest salary:",
      df[(df['rank'] == 'Prof') & (df['sex'] == 'Male')]['salary'].max())
print("Male Professor with lowest salary:",
      df[(df['rank'] == 'Prof') & (df['sex'] == 'Male')]['salary'].min())
print("Female Professor with highest salary:",
      df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')]['salary'].max())
print("Female Professor with lowest salary:",
      df[(df['rank'] == 'Prof') & (df['sex'] == 'Female')]['salary'].min())


print("Professor with highest salary:",
      df[df['rank'] == 'Prof']['salary'].max())
print("Professor with lowest salary:",
      df[df['rank'] == 'Prof']['salary'].min())


# Replacing missing 'Salaries' with the mean of matching salaries
df['salary'] = df.groupby('service')['salary'].transform(
    lambda x: x.fillna(x.mean()))

# Replacing missing 'phd' with the mean of matching 'service'
df['phd'] = df.groupby('service')['phd'].transform(
    lambda x: x.fillna(x.mean()))


# Counting Male Staff and Female Staff
print("Number of Male Staff:",
      df[(df['rank'] == 'Staff') & (df['sex'] == 'Male')].shape[0])

