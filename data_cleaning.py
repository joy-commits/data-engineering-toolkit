import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a pandas DataFrame by handling missing values and duplicates.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Drop rows with any missing values
    cleaned_df = df.dropna()
    
    # Remove duplicate rows
    cleaned_df = cleaned_df.drop_duplicates()
    
    print(f"Original shape: {df.shape}")
    print(f"Cleaned shape: {cleaned_df.shape}")
    
    return cleaned_df

if __name__ == '__main__':
    # Example usage with a sample DataFrame
    data = {'A': [1, 2, 2, 4, np.nan], 
            'B': ['x', 'y', 'y', 'z', 'w'],
            'C': [10, 20, 20, 40, 50]}
    
    sample_df = pd.DataFrame(data)
    
    # Clean the sample data
    cleaned_sample_df = clean_data(sample_df)
    
    print("\nOriginal DataFrame:")
    print(sample_df)
    
    print("\nCleaned DataFrame:")
    print(cleaned_sample_df)
