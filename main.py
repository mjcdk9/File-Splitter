from main_psg import *


def split_csv_file(input_file, output_folder, rows_per_file):
    # Load the input CSV file into a pandas dataframe
    df = pd.read_csv(input_file, encoding='latin-1')

    status = "Loading..."

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Calculate the number of output files needed
    num_output_files = len(df) // rows_per_file + 1

    # Split the data and save to output files
    for i in range(num_output_files):
        start_index = (i * rows_per_file) + 1
        end_index = min((i + 1) * rows_per_file, len(df))
        output_file = os.path.join(output_folder, f"output_{i}.csv")
        df_1 = df.iloc[:1]
        frames = [df_1, df]
        df = pd.concat(frames)
        df[start_index:end_index].to_csv(output_file, index=False)

    status = "Complete"


def extract_top_5(input_file_path, output_folder, number_of_rows_in_short_file):
    # Load the input CSV file into a pandas dataframe
    df = pd.read_csv(input_file, encoding='latin-1')

    status = "Loading..."

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Split the data and save to output files
    start_index = (1)
    end_index = (number_of_rows_in_short_file + 1)
    output_short_file = os.path.join(output_folder, "short.csv")
    df_1 = df.iloc[:1]
    frames = [df_1, df]
    df = pd.concat(frames)
    df[start_index:end_index].to_csv(output_short_file, index=False)

    # Trim top X rows off large file and save
    rest_of_df = df.drop(range(number_of_rows_in_short_file))
    output_rest_of_file = os.path.join(output_folder, "output_rest_of_file.csv")
    rest_of_df.to_csv(output_rest_of_file, index=False)

    status = "Complete"


input_file = "file.csv"
output_folder = "output"
rows_per_file = 50000
status = "testing"

# split_csv_file(input_file, output_folder, rows_per_file)
# extract_top_5(input_file, output_folder, 3)


