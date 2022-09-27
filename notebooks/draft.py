def coerce_df_columns_to_best_dtype(df, numeric_column_list, datetime_column_list):
    # convert Id to integer and Salary to float datatype
    df[numeric_column_list] = df[numeric_column_list].apply(pd.to_numeric, errors='coerce')
    # convert to datetime format
    df[datetime_column_list] = df[datetime_column_list].apply(pd.to_datetime, errors='coerce')
    # convert object columns to string datatype
    df = df.convert_dtypes()
    # return datatype for each column after coercing
    # select numeric columns
    df_numeric = df.select_dtypes(include=[np.number]).columns.to_list()

    # select non-numeric columns
    df_string = df.select_dtypes(include='string').columns.tolist()

    # print number of numeric column
    print("Number of numeric columns: ", len(df_numeric))
    print("List of numeric columns: ", df_numeric, "\n")

    print("Number of categorical columns: ", len(df_string))
    print("List of string columns: ", df_string, "\n\n")

    return df.info()

coerce_df_columns_to_best_dtype(df, ['Id','Salary'], ['OpenDate', 'CloseDate'])

# female weight variance


# generate a boxplot to see the data distribution by treatments. Using boxplot, we can
# easily detect the differences between different treatments
import matplotlib.pyplot as plt
import seaborn as sns
ax = sns.boxplot(x='region', y='score', data=df, color='#99c2a2')
ax = sns.swarmplot(x="region", y="score", data=df, color='#7d0013')
# set with and height of the figure
plt.figure(figsize=(10,8))
# set title with matplotlib
plt.title('Distribution of scores by region')
plt.show()


