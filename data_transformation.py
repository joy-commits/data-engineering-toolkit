import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms a DataFrame by creating a new column based on existing data.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The transformed DataFrame with a new column.
    """
    # Check if required columns exist before performing the transformation
    if 'A' in df.columns and 'C' in df.columns:
        df['A_plus_C'] = df['A'] + df['C']
    else:
        print("Required columns ('A' and 'C') not found. Skipping transformation.")
        
    return df

if __name__ == '__main__':
    # Example usage with a sample DataFrame
    data = {'A': [10, 20, 30, 40], 
            'B': ['x', 'y', 'z', 'w'],
            'C': [1, 2, 3, 4]}
    
    sample_df = pd.DataFrame(data)
    
    # Transform the sample data
    transformed_sample_df = transform_data(sample_df)
    
    print("\nOriginal DataFrame:")
    print(sample_df)
    
    print("\nTransformed DataFrame:")
    print(transformed_sample_df)
