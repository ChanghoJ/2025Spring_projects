# Hypothesis: Shifting Geography of Patent Filings in the United States
- Original AIPD Dataset - [https://www.uspto.gov/ip-policy/economic-research/research-datasets/artificial-intelligence-patent-dataset]
- Secondary Datasets link - [https://patentsview.org/download/data-download-tables]
- Dataset dictionary link - [https://patentsview.org/download/data-download-dictionary] 

Context:
The geographic distribution of US patent filings reflects broader economic & technological shifts. This hypothesis explores how two major events — the COVID-19 pandemic and the ongoing decentralization of tech innovation — have impacted patent location trends in the US (We plan to use only the patents granted datasets for all the following criterias)
- 1. Post-COVID Spatial Dispersion of Innovation (Prisha)
We hypothesize that the geographic distribution of patent filings in the U.S. became more dispersed after the COVID-19 pandemic (2020–2021). This may be due to increased remote work flexibility, allowing inventors to file from less traditional, non-urban tech hubs. We expect to observe more filings from rural or non-coastal counties in the post-2021 period. (2.56 GB of Data) 4,50,000

Datasets: g_location_disambiguated, g_inventor_disambiguated, g_application
- 2. Proximity to Research Institutions and Patent Density (Changho)
We expect that counties with prominent research universities (e.g., Stanford, MIT, UIUC) consistently see higher patent activity. This hypothesis explores whether proximity to academic research hubs correlates with innovation output.

Datasets: g_location_disambiguated, external list of U.S. research universities
- 3. Attorney Involvement and Urban Proximity (Prisha)
We hypothesize that patents filed with attorney organizations involvement are more likely to originate from urban counties or tech-centric states. In contrast, patents without attorney organization involvement may show more geographic spread.

Datasets: g_attorney_disambiguated, g_location_disambiguated, g_application
- 4. Assignee Type and Geographic Concentration (Changho)
We hypothesize that patents assigned to organizations (companies, universities, government) show a more concentrated geographic footprint compared to patents with individual or no clear assignee. Specifically, we expect corporate-assigned patents to cluster around business hubs (California and New York), while individually filed patents may appear more dispersed.

Datasets: g_assignee_disambiguated, g_location_disambiguated, g_application

## Data Preparation Steps

Due to the large size of the datasets involved, we used automated downloading and extraction to efficiently prepare the data for analysis. The following steps were implemented in data_preparation.py:

- Create a data directory:
A ./data folder is created to organize all downloaded and extracted files.
- Download ai_model_predictions.csv.zip:
This file is hosted on the USPTO website, which restricts direct file downloads. To bypass this, we used a headless Chrome browser with Selenium to automate the download.
- Download all secondary datasets (in .zip format):
To minimize transfer size and optimize storage, all .csv and .tsv datasets were downloaded as compressed .zip files from reliable sources such as [https://www.uspto.gov/ip-policy/economic-research/research-datasets/artificial-intelligence-patent-dataset].
- The files include:
  1. g_application.tsv.zip
  2. g_attorney_disambiguated.tsv.zip
  3. g_assignee_disambiguated.tsv.zip
  4. g_location_disambiguated.tsv.zip
  5. g_inventor_disambiguated.tsv.zip
  6. 2025-Public-Data-File.xlsx (Excel format, not zipped)
- Files are only downloaded if not already present to prevent redundant downloads.
- Unzip all .zip files:
Each ZIP file is programmatically checked and extracted into the same data directory.

## Hypothesis 1: Post-COVID Spatial Dispersion of Innovation
### We hypothesize that the geographic distribution of U.S. patent filings became more dispersed after the COVID-19 pandemic (2020–2021), due to the rise of remote work and decentralization of tech innovation. We expected a visible shift from traditional urban tech hubs to a broader range of locations, including rural and non-coastal states.

### Datasets Used:
- ai_model_predictions.csv
- g_inventor_disambiguated.tsv
- g_location_disambiguated.tsv
- g_application.tsv

### Data Import & Filtering
The notebook:
- Loaded all data into Pandas DataFrames.
- Filtered only granted patents (flag_patent == 1).
- Parsed publication dates into year format for temporal analysis.

### Key Analyses & Visualizations
- 1. Interactive Yearly Patent Visualization (Bubble Map)
    - A slider-based choropleth visualizes patent filing density across states from 1976–2023.
    - Users can hover over states to view exact patent counts.
    - Bubble size and color dynamically scale with volume.
- 2. State-Level Patent Share & Growth Analysis
    - Calculates what share of patents came from the top 5 states each year.
    - Compares average patent counts before and after COVID (2018–2019 vs. 2021–2023).
***Output: Identifies states with the most significant changes in patent filings.***
- 3. States Above Average Patent Activity (2018–2023)
    - Gets the average patent count per state each year.
    - Counts how many states exceeded the national average each year.
***Resulting Plot: Shows whether innovation became more evenly distributed or remained concentrated in fewer regions.***

## Hypothesis 2: Proximity to Research Institutions and Patent Density
### We expect that counties with prominent research universities (e.g., Stanford, MIT, UIUC) consistently see higher patent activity. This hypothesis explores whether proximity to academic research hubs correlates with innovation output.
- From feedback, we heard it would be great to make function on distance caculation, but hypothesis 2 is more about gathered around counties rather than distance.

### Datasets Used:
- g_location_disambiguated.tsv
- g_inventor_disambiguated.tsv
- Colleges_and_Universities_-3122497483864735259.csv
- 2025-Public-Data-File.xlsx

### Data Import & Filtering
The notebook:
- Loaded all data into Pandas DataFrames.
- Merged with necessary dataframes (e.g. latitude and longitude in one dataframe to the other).
- Filter out patent location by == 'US'.
- Dropped na value from columns will use

### Key Analyses & Visualizations
- 1. Scatter map
    - This is visualization that blue dots are individual inventors with patents, whereas red starts are very high spending research universities on a U.S. territory map.
    - loc_sample_df, the subsampled version of dataset used for performance issue.
    - Got an assistence from ChatGPT for the plot
- 2. County density map
    - This is a density heatmap based on number of patent application by inventors with red starts as universities
    - Helped from ChatGPT, for the visualization part
- 3. Summary statistics
    - Calculated summary statistics for counties' patent application amount with university vs. without university
    - Helped from ChatGPT

### Summary of Results
- In **scatter map**,
- In a brief sense, it looks like patent applicants (inventors) likely gathered around area nearby research universities.
- Still not clear enough to makes the conclusion, so proceed to the next visualization
- According to **density map**, it is hard to compare counties with and without the universities
- The **summary statistic** results show that high mean, but unreliable due to huge gap between min and max patent application amount.
- So, by checking minimum, median, maximum, we can conclude counties with universities have more patent applicants
- This is comparable result as counties with universities are small (153 vs 3022) but showed higher minimum, median, and maximum patent applicants.
- Therefore, the hypothesis 2, counties with prominent research universities (e.g., Stanford, MIT, UIUC) consistently see higher patent activity, is likely right according to minimum, median, and maximum amount of patent applicants are more around universities.

## Hypothesis 3: Attorney Involvement & Technologically Advanced States
### We hypothesize that patents involving attorney organizations are more likely to be filed from technologically advanced states, while those without attorney involvement may originate from a broader geographic base, including emerging innovation regions. This hypothesis explores how legal representation in patent filings might correlate with technological, and geographic factors.

### Datasets Used:
- ai_model_predictions.csv
- g_inventor_disambiguated.tsv
- g_location_disambiguated.tsv
- g_application.tsv
- g_attorney_disambiguated.tsv

### Data Loading & Preparation
- The notebook:
    - Imports all relevant data into Pandas DataFrames.
    - Filters and merges data on patent ID to correlate attorney involvement with filing location and inventor data.
  - Creates subsets of data:
    - df_attorney: patents with attorney involvement.
    - df_no_attorney: patents without attorney involvement.
   
### Key Analyses & Visualizations
1. Top 5 Attorney Organizations
  - Filters out records with no attorney information.
  - Uses value_counts() to find the most frequently occurring patent attorney organizations globally.
  - Displays the top 5 by total patent count.
2. State-Wise Distribution of Top 5 Attorneys
  - Analyzes where the top attorney organizations primarily file patents within the U.S.
  - Visualizes their geographic influence and concentration using grouped bar charts and heatmaps.
3. Yearly Filing Trends
  - Tracks yearly patent filing volume for the top 5 attorneys from 1976 to 2023.
  - Visualizes trends to highlight growth, decline, or consistency in legal representation across time.
4. Choropleth Maps
- Compares patent filings with vs. without attorney involvement across U.S. states.
- Maps are created using Plotly Express, showing:
  - States with high volumes of attorney-filed patents.
  - States with large numbers of patents without attorney involvement.

### Summary of Results

- Attorney involvement is highly concentrated in states like California, New York, and Massachusetts, reinforcing their roles as traditional tech hubs.
- Non-attorney filings are significantly more geographically dispersed, suggesting independent innovation in less represented regions.
- The gap between attorney-heavy and attorney-light states has remained consistent.

## Hypothesis 4: Assignee Type and Concentration
### We hypothesize that patents assigned to organizations (companies, universities, government) show a more concentrated geographic footprint compared to patents with individual or no clear assignee.
- Specifically, we expect corporate-assigned patents to cluster around business hubs (e.g. California and New York), while individually filed patents may appear more dispersed.
- We checked this by comparing patent amount of individual vs. company by county level
- Prepared 3 visualizations and 1 statistical test
- From feedback, it would be great to see statistics to compare how assignee spreaded compared, so prepared additional statistics.

### Datasets Used:
- g_application.tsv
- g_assignee_disambiguated.tsv
- g_location_disambiguated.tsv
- 2020_UA_COUNTY.xlsx

### Data Import & Filtering
The notebook:
- Loaded all data into Pandas DataFrames.
- Merged with necessary dataframes (e.g. latitude and longitude in one dataframe to the other).
- Filter out patent location by == 'US'.
- Dropped na value from columns will use

### Key Analyses & Visualizations
- 1. Scatter map
    - This visualization shows data points on map by whether patent assignee is individual, government, or company in U.S.
    - Just like in the hypothesis 2, the map used subsampled version for performance issue.
    - Dataset subsetted by around 1/20 due to large sample size (n>10M)
    - Got an assistence from ChatGPT for the plot
- 2. County density map
    - This is the visualization by counties by density of patent application 
    - First visualization shows 3 heatmaps by 'individual', 'company', 'government', how are they concentrate in counties 
    - Second visualization shows map that colored with dominant patent application amount by 'individual', 'company', 'government'. Subset company samples by 50000, similar amount with individuals to check dominance over counties in same size of patent application. 
    - Third is similar with the second but used full dataset that company not subsampled with 50000. 
    - Got an assistence from ChatGPT for the plot
- 3. Bar plot
    - As previous visualizations were lack of explain in the main hypothesis: so assignee from company are more focused in area and individuals more spreaded?
    - We try to show this by state-wise (since county is too many to visualize in bar plot)
    - Prepared 2 bar plots,
    - one for stacked bar plot to see overall amount with concentration on patent application by assginee
    - another for interactive bar plot that user can choose assignee type from drop down menu, can individually check 'individual', 'company', and 'government' patent application density by states.
    - Got an assistence from ChatGPT for the plot
- 4. Summary statistics
    - Still one final question remained, does companies more clustered around busniess hub and individuals are more spreaded?
    - We compared statistics by comparing amount of patent application by counties, Company assignee in urban vs. rural and Individual assignee in urban vs. rural.
    - Then applied Mann–Whitney U Test to check each assignee's patent application in urban and rural counties are different, which if both companies and individuals shown to be different, then the hypothesis likely wrong because they are both distribution are different in counties.

### Summary of Results
- According to the Mann–Whitney U Test, the distributions are significantly different (p-value < 0.05) for company and individual assignees
- we can conclude that the distribution of patent density for companies is significantly different between urban and rural counties.
- Overall, according to the bar plots and Mann–Whitney U Test, individual also concentrated in urban counties, which "hypothesis 4: We hypothesize that patents assigned to organizations (companies, universities, government) show a more concentrated geographic footprint compared to patents with individual or no clear assignee. Specifically, we expect corporate-assigned patents to cluster around business hubs (e.g. California and New York), while individually filed patents may appear more dispersed." is likely not right.

## Brief Dataset description and sources
- AI patent applications dataset, "ai_model_predictions.csv.zip":"https://data.uspto.gov/ui/datasets/products/files/ECOPATAI/2023/ai_model_predictions.csv.zip"
- Patent application dataset, "g_application.tsv":"https://s3.amazonaws.com/data.patentsview.org/download/g_application.tsv.zip"
- Attorney who decided patent dataset, "g_attorney_disambiguated.tsv":"https://s3.amazonaws.com/data.patentsview.org/download/g_attorney_disambiguated.tsv.zip",
- Patent applicant assignee (individual, corporation, government) dataset, "g_assignee_disambiguated.tsv":"https://s3.amazonaws.com/data.patentsview.org/download/g_assignee_disambiguated.tsv.zip"
- Patent application location dataset, "g_location_disambiguated.tsv":"https://s3.amazonaws.com/data.patentsview.org/download/g_location_disambiguated.tsv.zip"
- Patent inventor dataset, "g_inventor_disambiguated.tsv":"https://s3.amazonaws.com/data.patentsview.org/download/g_inventor_disambiguated.tsv.zip"
- List of universities with location information, "Colleges_and_Universities_-3122497483864735259.csv":"https://hifld-geoplatform.hub.arcgis.com/datasets/geoplatform::colleges-and-universities/about"
- List universities with research spending filter, "2025-Public-Data-File.xlsx":"https://carnegieclassifications.acenet.edu/wp-content/uploads/2025/04/2025-Public-Data-File.xlsx"
- Urban information filter on counties, "data/2020_UA_COUNTY.xlsx":"https://www2.census.gov/geo/docs/reference/ua/2020_UA_COUNTY.xlsx"

## AI usage
- Visualizations and statistical analysis codes for the hypothesis 2 and 4 are created by the assistance of ChatGPT
- Scatter map, density map, and bar plot in hypothesis 2 and 4