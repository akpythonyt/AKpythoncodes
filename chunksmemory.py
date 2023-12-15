import pandas as pd
import numpy as np
from memory_profiler import profile

# Function for normal pandas processing
@profile
def normal_pandas_processing():
    # Create a large DataFrame with random numbers
    df = pd.DataFrame(np.random.rand(1000000, 5), columns=[f'Column_{i+1}' for i in range(5)])
    
    # Perform some operations
    result_normal = df.groupby('Column_1').mean()
    
    # Display the result (just to do something with it)
    print(result_normal.head())


# Function for chunk pandas processing with memory profiling
@profile
def chunk_pandas_processing():
    # Set the size of the dataset
    rows = 1000000  # 1 million rows
    cols = 5

    # Create a DataFrame with random numbers
    data = np.random.rand(rows, cols)
    df = pd.DataFrame(data, columns=[f'Column_{i+1}' for i in range(cols)])

    # Initialize an empty result DataFrame
    result_chunk = pd.DataFrame()

    # Process the dataset in chunks
    chunk_size = 100000  # 100,000 rows per chunk
    for chunk in np.array_split(df, range(chunk_size, rows, chunk_size)):
        # Perform operations on each chunk
        chunk_result = chunk.groupby('Column_1').mean()

        # Concatenate the results
        result_chunk = pd.concat([result_chunk, chunk_result])

    # Final result after processing all chunks
    result_chunk_final = result_chunk.groupby('Column_1').mean()

    # Display the final result (just to do something with it)
    print(result_chunk_final.head())


# Call the functions
normal_pandas_processing()
chunk_pandas_processing()
