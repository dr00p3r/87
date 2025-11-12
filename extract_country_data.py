import pandas as pd
import sys

def extract_country_data(input_file, output_file, country_name):
    """
    Extract specific columns from GDP CSV file and filter by country.
    
    Parameters:
    - input_file: Path to the input CSV file
    - output_file: Path to the output CSV file
    - country_name: Name of the country to filter (e.g., 'Spain')
    """ 
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Filter rows where REF_AREA_LABEL matches the country name
        filtered_df = df[df['REF_AREA_NAME'] == country_name]
        
        # Select only the required columns
        result_df = filtered_df[['REF_AREA_NAME', 'FREQ_ID', 'FREQ_NAME', 'TIME_PERIOD', 'OBS_VALUE', 'UNIT_MEASURE_NAME']]
        
        # Save to output CSV
        result_df.to_csv(output_file, index=False)
        
        print(f"Successfully extracted {len(result_df)} rows for {country_name}")
        print(f"Output saved to: {output_file}")
        
        return result_df
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Column {e} not found in the CSV file.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Default parameters
    input_file = "IMF_FSI_NGDP.csv"
    output_file = "spain_gdp_imf_data.csv"
    country_name = "Spain"
    
    # Allow command line arguments
    if len(sys.argv) > 1:
        country_name = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    if len(sys.argv) > 3:
        input_file = sys.argv[3]
    
    # Execute extraction
    extract_country_data(input_file, output_file, country_name)
