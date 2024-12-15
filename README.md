# **Enhanced Census Data Collection for Top Counties in the U.S.**

**Welcome to the Enhanced Census Data Collection Repository!** This project allows you to efficiently collect and analyze detailed population and socio-economic data for the top counties across the United States. Using data from the U.S. Census Bureau’s American Community Survey (ACS), this repository automates the retrieval, processing, and saving of essential census data for a wide range of counties.

---

## **🚀 Project Overview**

This project fetches detailed data from the **U.S. Census Bureau’s API** for a set of counties in multiple states and compiles it into a clean, structured format. It gathers data points such as:

- **Total Population**
- **Population Aged 45+**
- **Median Household Income**
- **Educational Attainment**
- **Homeownership Rate**
- **Health Insurance Coverage**
- **Employment Rate**

The data is then saved into a neatly organized Excel file, where each county's details are captured in a separate sheet, making it easy to analyze the data.

---

## **📈 Key Features**

- **Automated Data Collection**: Retrieves real-time U.S. Census data for counties across multiple states.
- **Detailed Demographic Insights**: Includes detailed population breakdowns by age, income, and educational attainment.
- **Smart Data Processing**: Handles errors gracefully and retries API requests using an exponential backoff strategy for better reliability.
- **Flexible Data Export**: Saves the results in an easy-to-use Excel file format, with all data neatly organized by state and county.
- **User-Friendly**: Minimal setup required—simply insert your API key, and the script does the rest.

---

## **🔧 Requirements**

- Python 3.10.12
- `requests` for API calls
- `pandas` for data manipulation
- `openpyxl` for exporting data to Excel

To install the necessary dependencies, simply run:

```bash
pip install requests pandas openpyxl
```

---

## **🔑 Setup and Configuration**

1. **API Key**: To access the U.S. Census data, you need to provide your Census API key. You can get one from the U.S. Census website [here](https://api.census.gov/data/key_signup.html).

2. **Insert the API Key**: Open the script and insert your API key in the following line:

   ```python
   API_KEY = "your-api-key-here"
   ```

3. **Run the Script**: Once you’ve set your API key, run the script:

   ```bash
   python script.py
   ```

   The script will automatically fetch data for the top counties, process it, and save it in an Excel file named `enhanced_state_top_25_counties_census.xlsx`.

---

## **📊 Data Collected**

The following columns are included in the final dataset:

| Column Name                      | Description |
|-----------------------------------|-------------|
| **State**                         | The state in which the county is located. |
| **County**                        | The name of the county. |
| **Census Year**                   | The year the data was collected from the U.S. Census Bureau (default is 2020). |
| **Total Population**              | The total population of the county. |
| **Population Aged 45+**           | The total population of people aged 45 and older. |
| **Population Aged 45-64**         | The population of people aged 45 to 64. |
| **Population Aged 65+**           | The population of people aged 65 and older. |
| **Percent 45+ Population**        | The percentage of the population aged 45+ compared to the total population. |
| **Median Household Income**       | The median income of households in the county. |
| **Employment Rate (%)**           | The employment rate as a percentage of the total population. |
| **Bachelor's Degree or Higher (%)**| The percentage of people with a bachelor's degree or higher. |
| **Homeownership Rate (%)**        | The percentage of homes owned by their residents. |
| **Health Insurance Coverage (%)**| The percentage of people covered by health insurance. |
| **Average Household Size**        | The average number of people per household in the county. |
| **Population Density Score**      | A rough score based on the population density. |
| **Zip Codes**                     | The zip code range for the county. |
| **Sources Used**                  | The source of the data (U.S. Census ACS 5-Year Estimates). |
| **Data Accuracy**                 | Indicates if the data is accurate (default is "Yes"). |
| **Last Updated**                  | The date when the data was last updated. |
| **FIPS Code**                     | The Federal Information Processing Standards code for the state and county. |

---

## **🔄 Data Collection Flow**

1. **API Request**: The script constructs an API request for each county, fetching key demographic and socio-economic variables.
2. **Retry Mechanism**: If the request fails (due to rate limiting or temporary connectivity issues), the script automatically retries with an exponential backoff strategy to ensure reliable data collection.
3. **Data Processing**: Once the data is retrieved, the script processes it to convert raw values into useful metrics (e.g., calculating the percentage of people aged 45+).
4. **Excel Export**: The processed data is saved to an Excel file, with separate sheets for each state.

---

## **🎯 Why Use This Script?**

- **In-Depth Analysis**: By collecting and analyzing data for the top counties in the U.S., you can uncover powerful insights into demographic trends, income levels, educational attainment, and more.
- **Time-Saving**: No need to manually scrape data from different sources—the script does all the hard work for you.
- **Flexible Output**: The Excel format ensures that the data can be easily shared, modified, and analyzed in tools like Excel, Google Sheets, or Power BI.

---

## **📂 Project Structure**

```
├── README.md               # This file
├── script.py               # The main Python script to fetch and process data
├── enhanced_state_top_25_counties_census.xlsx   # Output file (auto-generated)
└── requirements.txt        # Python dependencies
```

---

## **💡 Contributions**

This repository is open-source and welcomes contributions from developers around the world! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a pull request

---

## **🌟 Acknowledgements**

This project utilizes data from the **U.S. Census Bureau’s American Community Survey (ACS)**. Thanks to the Census Bureau for providing accessible and detailed population data.

---

## **📜 License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **🔗 Links**

- [U.S. Census API Documentation](https://www.census.gov/data/developers/data-sets.html)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

---

## **📬 Author**

**Abdul Qadeer**

- **Email**: [itsabdulqadeer.55@gmail.com](mailto:itsabdulqadeer.55@gmail.com)
- **GitHub**: [AbdulQadeer-55](https://github.com/AbdulQadeer-55)

---

### **Enjoy analyzing U.S. Census data, and feel free to star this repository if it helped you! 🌟**