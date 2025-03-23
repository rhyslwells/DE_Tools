import pandas as pd

def demonstrate_stack():
    # Sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    
    # Using stack
    stacked_df = df.stack()
    print("\nStacked DataFrame:")
    print(stacked_df)

def demonstrate_stack_multiindex():
    # Creating a MultiIndex DataFrame
    arrays = [['A', 'A', 'B', 'B'], ['One', 'Two', 'One', 'Two']]
    index = pd.MultiIndex.from_tuples(list(zip(*arrays)), names=['Letter', 'Number'])
    data = [[1, 2], [3, 4], [5, 6], [7, 8]]
    df = pd.DataFrame(data, index=index, columns=['X', 'Y'])
    print("\nMultiIndex DataFrame:")
    print(df)
    
    # Stacking
    stacked_df = df.stack()
    print("\nStacked MultiIndex DataFrame:")
    print(stacked_df)

def demonstrate_stack_with_groupby():
    # Sample DataFrame with multi-level columns
    multicol = pd.MultiIndex.from_tuples([('weight', 'kg'), ('height', 'm')])
    df = pd.DataFrame([[1.0, 2.0], [3.0, 4.0]],
                      index=['cat', 'dog'],
                      columns=multicol)
    print("\nMulti-Level Column DataFrame:")
    print(df)
    
    # Stacking the DataFrame
    stacked_df = df.stack()
    print("\nStacked DataFrame:")
    print(stacked_df)
    
    # Grouping by level 1 (units: kg, m)
    grouped = stacked_df.groupby(level=1).mean()
    print("\nGrouped by Level 1 (Average per unit):")
    print(grouped)

def main():
    demonstrate_stack()
    demonstrate_stack_multiindex()
    demonstrate_stack_with_groupby()
main()

import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Year': [2022, 2023, 2024],
    'Sales_A': [100, 120, 140],
    'Sales_B': [80, 90, 100]
})
df

stacked_df = df.set_index('Year').stack().reset_index()
stacked_df.columns = ['Year', 'Product', 'Sales']
stacked_df

sns.lineplot(data=stacked_df, x='Year', y='Sales', hue='Product')
plt.show()
