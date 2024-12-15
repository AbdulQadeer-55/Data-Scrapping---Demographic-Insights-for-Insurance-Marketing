import requests
import pandas as pd
from datetime import datetime
import sys
import time

API_KEY = ""

# Define the counties for each state (state_code: [county_fips])
counties = {
    "39": [  # Ohio
        "049", "061", "035", "093", "113", "153", "151", "057", "025", "165", 
        "017", "085", "095", "099", "029", "145", "155", "089", "003", "045", 
        "041", "129", "075", "055", "173"
    ],
    "37": [  # North Carolina
        "119", "183", "067", "081", "063", "025", "159", "071", "001", "019",
        "179", "051", "033", "035", "077", "097", "117", "183", "101", "167",
        "029", "139", "163", "115", "021"
    ],
    "13": [  # Georgia
        "121", "089", "067", "135", "063", "151", "245", "077", "113", "057",
        "045", "117", "015", "097", "029", "139", "217", "031", "021", "153",
        "085", "199", "073", "145", "025"
    ],
    "48": [  # Texas
        "201", "113", "029", "439", "157", "085", "121", "141", "453", "355",
        "215", "027", "167", "061", "303", "479", "091", "039", "209", "187",
        "181", "257", "375", "041", "163"
    ],
    "12": [  # Florida
        "086", "011", "099", "057", "095", "031", "071", "103", "033", "105",
        "115", "127", "081", "009", "069", "117", "093", "083", "129", "131",
        "017", "001", "111", "113", "091"
    ],
    "01": [  # Alabama
        "073", "097", "089", "101", "125", "077", "117", "083", "045", "015",
        "021", "095", "051", "069", "055", "047", "081", "049", "009", "043",
        "033", "039", "103", "071", "087"
    ]
}

def generate_zip_ranges():
    """Generate approximate ZIP code ranges for each county."""
    zip_ranges = {
        "39": {},  # Ohio: 43000-45999
        "37": {},  # North Carolina: 27000-28999
        "13": {},  # Georgia: 30000-31999, 39800-39999
        "48": {},  # Texas: 75000-79999, 88500-88599
        "12": {},  # Florida: 32000-34999
        "01": {}   # Alabama: 35000-36999
    }
    
    zip_base = {
        "39": "43",  # Ohio
        "37": "27",  # North Carolina
        "13": "30",  # Georgia
        "48": "75",  # Texas
        "12": "32",  # Florida
        "01": "35"   # Alabama
    }
    
    for state, counties_list in counties.items():
        for i, county in enumerate(counties_list):
            start = f"{zip_base[state]}{str(i*2).zfill(3)}"
            end = f"{zip_base[state]}{str(i*2 + 1).zfill(3)}"
            zip_ranges[state][county] = f"{start}-{end}"
    
    return zip_ranges

def get_enhanced_population_data(state_code, county_code, retries=3):
    """Fetch enhanced population data from Census API with retry mechanism."""
    variables = [
        "NAME",
        "S0101_C01_001E",  # Total population
        "S0101_C01_021E",  # Population 45-64
        "S0101_C01_022E",  # Population 65+
        "S1501_C01_006E",  # Educational attainment: Bachelor's degree or higher
        "S1901_C01_012E",  # Median household income
        "S2301_C04_001E",  # Employment rate
        "S2502_C01_002E",  # Homeownership rate
        "S2701_C05_001E",  # Health insurance coverage
        "S1101_C01_002E",  # Average household size
    ]
    
    url = f"https://api.census.gov/data/2020/acs/acs5/subject?get={','.join(variables)}&for=county:{county_code}&in=state:{state_code}&key={API_KEY}"
    
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 429:  # Rate limit
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            else:
                print(f"Failed attempt {attempt + 1} for state {state_code}, county {county_code}. Status: {response.status_code}")
        except Exception as e:
            print(f"Error on attempt {attempt + 1} for state {state_code}, county {county_code}: {str(e)}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            continue
    return None