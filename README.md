# Hypothesis: Shifting Geography of Patent Filings in the United States
Original AIPD Dataset - https://www.uspto.gov/ip-policy/economic-research/research-datasets/artificial-intelligence-patent-dataset
Secondary Datasets link - https://patentsview.org/download/data-download-tables
Dataset dictionary link - https://patentsview.org/download/data-download-dictionary 

Context:
The geographic distribution of US patent filings reflects broader economic & technological shifts. This hypothesis explores how two major events — the COVID-19 pandemic and the ongoing decentralization of tech innovation — have impacted patent location trends in the US (We plan to use only the patents granted datasets for all the following criterias)
- 1. Post-COVID Spatial Dispersion of Innovation
We hypothesize that the geographic distribution of patent filings in the U.S. became more dispersed after the COVID-19 pandemic (2020–2021). This may be due to increased remote work flexibility, allowing inventors to file from less traditional, non-urban tech hubs. We expect to observe more filings from rural or non-coastal counties in the post-2021 period. (2.56 GB of Data) 4,50,000
Datasets: g_location_disambiguated, g_inventor_disambiguated, g_application
- 2. Proximity to Research Institutions and Patent Density
We expect that counties with prominent research universities (e.g., Stanford, MIT, UIUC) consistently see higher patent activity. This hypothesis explores whether proximity to academic research hubs correlates with innovation output.
Datasets: g_location_disambiguated, external list of U.S. research universities
- 3. Attorney Involvement and Urban Proximity
We hypothesize that patents filed with attorney organizations involvement are more likely to originate from urban counties or tech-centric states. In contrast, patents without attorney organization involvement may show more geographic spread.
Datasets: g_attorney_disambiguated, g_location_disambiguated, g_application
- 4. Assignee Type and Geographic Concentration
We hypothesize that patents assigned to organizations (companies, universities, government) show a more concentrated geographic footprint compared to patents with individual or no clear assignee. Specifically, we expect corporate-assigned patents to cluster around business hubs (California and New York), while individually filed patents may appear more dispersed.
Datasets: g_assignee_disambiguated, g_location_disambiguated, g_application
