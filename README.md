# Intern Selection using ML Algorithm

## Overview
This repository contains a simple machine learning algorithm to find the best intern out of a pool of candidates. The algorithm utilizes predefined criteria weights to calculate scores for each intern based on their skills and experience in various domains. The intern with the highest score is selected as the best candidate for the position.

## Dataset
The dataset used for the intern selection is stored in a CSV file named `data.csv`. It contains information about the interns, including their scores in different skill areas.

## Usage
To run the intern selection algorithm, follow these steps:

1. Install Dependencies: Make sure you have Python installed on your system. Install the required dependencies by running the following command:
   ```
   pip install pandas
   ```

2. Prepare the Dataset: Place the dataset file (`data.csv`) in the same directory as the Python script.

3. Configure Criteria Weights: Open the Python script and modify the `criteria_weights` dictionary according to your preferences. Adjust the weights for each skill area to reflect the importance you assign to them.

4. Run the Algorithm: Execute the Python script using the following command:
   ```
   python intern_selection.py
   ```

5. View Results: The script will calculate the intern scores, sort the candidates based on the scores, and print the selected intern(s) with the highest score.

## Customization
Feel free to customize the algorithm and dataset according to your specific requirements. You can modify the criteria weights, add or remove skill areas, or even use a different dataset structure.

## Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your proposed changes. We welcome any improvements, bug fixes, or additional features that can enhance the intern selection algorithm.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.
