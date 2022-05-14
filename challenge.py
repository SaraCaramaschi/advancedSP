import pandas as pd

if __name__ == '_main_':

    # Import tutto quanto
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    # %%
    # LOADING DATA

    df = pd.read_csv("ICU_Challenge_Dataset.csv", sep=",")
    df_description = df.describe()
    # df_description['percentage'] = df_description['count']/6000
    # %%
    # DUPLICATES

    df.duplicated().any()

    # %%

    # MISSING DATA
    print(df[df.columns[df.isna().any()]])

    print(df[df.columns[df.isna().any()]].isna().sum())

    # %%
    # Dropping data

    # %%
    # TARGET VARIABLE

    df['In-hospital_death'].unique()
    fig, ax = plt.subplots()
    ax.hist(df['In-hospital_death'])

    # %%

    # Nan % in Height
    # 2886:6000=x:100
    x = 288600 / 6000
    x

    # Nan % in MechVentStartTime, MechVentDuration, MechVentLast8Hour and UrineOutputSum
    # 2256:6000=x:100
    x = 225600 / 6000
    x

    # %%
    # Variable type categorical / numerical
    print(np.unique(df.dtypes))

    int_var = list(df.columns[df.dtypes == np.int64])
    float_var = list(df.columns[df.dtypes == np.float64])

    cat_var = []
    num_var = []
    for cat in list(df.columns):
        if len(df[cat].unique()) <= 2:
            cat_var.append(cat)
        else:
            num_var.append(cat)

    categorical_df = df[cat_var]
    numerical_df = df[num_var]
    # print(df.columns[df.dtypes == np.int64])

    # %%
    # Numerical data analysis
    # numerical_df.hist(figsize=(10,10))

    sns.pairplot(numerical_df[['Age']], hue=categorical_df['In-hospital_death'])

    print('fine doc')