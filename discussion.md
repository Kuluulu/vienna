# Figure Description

**Fig. 1 (A4_country_comparison.pdf):** Three time series of World Bank data dating from 1960 to 2023, comparing two countries. Burundi is represented in orange, the Democratic Republic of Congo in blue. The top figure shows CO2 emissions per capita, the middle figure the life expectancy and the bottom figure the GDP per capita in current USD.

**Fig. 2 (burundi.png):** Life Expectancy, GDP per capita (current USD) and CO2 emissions over time for the country of Burundi.

**Fig. 3 (Congo_Dem_Rep.png):** Life Expectancy, GDP per capita (current USD) and CO2 emissions over time for the Democratic Republic of Congo.

# Discussion

### Key patterns and Insights

First, one noticeable pattern is that although GDP per capita and life expectancy have been tracked consistently from 1960 to 2024, CO2 emissions per capita data is only available between 1990 and 2020.

#### Life expectancy

The Democratic Republic of Congo has seen a constant increase in life expectancy at birth, increasing from 41 to 62 years (which averages to one third of a year per calendar year). There were disruptions during the 1990s though.

Burundi's life expectancy development was less monotonic. Associated to the 1972 Ikiza mass killings (often characterised as a genocide)[^1] and the 1993 ethnic violence following the conflicts between Tutsi and Hutu[^2], there are big dents in the otherwise increasing life expectancy curve. In the 1970s, the life expectancy decreased from around 43 years to 26 years and in the 1990s the life expectancy decreased from about 45 years to 37 years.

[^1]: https://en.wikipedia.org/wiki/Ikiza
[^2]: https://en.wikipedia.org/wiki/1993_ethnic_violence_in_Burundi

In the late 2000s, Burundi's life expectancy has overtaken the Dem. Rep. of Congo's. In recent years, both countries have reached the 60-year mark and are continuing to trend upwards.

#### CO2 emissions

On one hand, the CO2 emissions per capita in the Dem. Rep. of Congo have been slightly decreasing over the observation period. Starting in 1990 with the maximum value in the entire period, 0.088 t, decreased gradually to values around 0.035 t between 2015 and 2020.

Burundi's emissions on the other hand increased from around 0.038 t each year between 1990 and 2000, to 0.058 in the late 2010s.

The CO2 emissions of either country have never added up to more than 0.1 tons per capita per year in any year of the available time period. The average emissions are 0.036 t per capita for Burundi and 0.043 t per capita for the Dem. Rep. Congo.

For comparison, Austria's CO2 emissions per capita were around 6.5 tons per capita in 2023. In the highest year of both countries (0.088 t, 1990, Dem. Rep. Congo) therefore makes up only 1.35 percent of the Austrian CO2 emissions.

#### GDP per Capita

The DR Congo tripled its GDP per capita between the 1960s and the mid 1970s from about 200 to 600 USD, only to face a constant loss down to 100 USD in the late 1990s (related to the introduction of multi-party democracy and culminating in the 1997-99 Civil War[^3]: https://en.wikipedia.org/wiki/1990s_in_the_Republic_of_the_Congo). Since then, the GDP per capita has continued to recover, surpassing the 600 USD in the early 2020s. The 1990 Dem. Rep. Congo CO2 Emissions peak suggests that the rebuilding of the economy happened while actively lowering the CO2 emissions per capita.

Burundi's GDP per capita more than doubled from around 80 USD in the 1960s to about 200 USD in the 2020s. It seems to slightly correlate with the DR Congo's GDP per capita.

### Key Finding I
In both Burundi and DR COngo has the life expectancy been increasing in the past 65 years, but it has also been significantly affected and limited by armed conflict.

### Key Finding II
DR Congo has managed to rebuild their exonomy after conflict while decreasing their carbon emissions per capita. Burundi has not.


### Follow-up Thoughts

Further work would need to go into investigating the methods that were used to generate the World Bank data and to research whether there is information on the associated uncertainties of the data. Also, it needs to be clarified how the World Bank defines the so-called "current" US-Dollar and whether selecting a different option might be more suitable. Comparing to potential local datasets might also be insightful.

Also, it would be interesting to consider the population development in the same time frame as per capita values might be misleading if the underlying numbers of people have changed significantly. The mass killings in Burundi suggest this. 

The Dem. Rep. of Congo's decrease in CO2 emissions during an increasing GDP per capita invites the question of what drives these numbers, e.g. whether low-CO2 emission sectors are thriving, if the total population has changed drastically, and how this relates to education levels of the population.


### Presentation 

How I would present the information, would depend on my audience. If I'd present in front of a non-African working unit, I would show the figures in a few slides, point out the observations above, give details and historical context.

If I were to present in front of an African audience, I would first consult with locals, if possible, on what is relevant to them, where the needs for information are, and how much context is needed.

Generally, I would ensure to work with local partners to avoid "parachute science".

### Long-Term Usability

To ensure long term usability, I would
- Add usage instructions in a README inside a repository and involve a team of people who can use and contribute to the code (introduce the people to git, python, etc., if necessary)
- Invest more time to document the library and python versions for the virtual environment, in order to create a reproducible environment
- Invest more time to make the code use the wbdata library or the World Bank data API, so that the figures can easily be updated
- Publish the figures and code under a Creative Commons license or similar