import pandas as pd
import matplotlib.pyplot as plt
import os

# Output dir
output_dir = 'output'

# Load both datasets with '...' treated as NaN
co2 = pd.read_csv('input/co2.csv', na_values='..')
life_gdp = pd.read_csv('input/lifeexpect_gdp.csv', na_values='..')

# Filter the relevant series
co2 = co2[co2['Series Name'] == 'CO2 emissions (metric tons per capita)']
life_exp = life_gdp[life_gdp['Series Name'] == 'Life expectancy at birth, total (years)']
gdp = life_gdp[life_gdp['Series Name'] == 'GDP per capita (current US$)']

# Extract year columns and convert to integers
year_columns = [col for col in co2.columns if '[YR' in col]
years = [int(col.split()[0]) for col in year_columns]

# Function to extract a country's time series from a dataset
def extract_series(df, country):
    row = df[df['Country Name'] == country]
    if not row.empty:
        series = row[year_columns].iloc[0]
        series.index = years
        return pd.to_numeric(series, errors='coerce')
    return pd.Series(dtype='float64')

# Define the countries of interest
countries = ['Burundi', 'Congo, Dem. Rep.']

# # Plot for each country
# for country in countries:
#     co2_series = extract_series(co2, country)
#     life_series = extract_series(life_exp, country)
#     gdp_series = extract_series(gdp, country)

#     fig, ax1 = plt.subplots(figsize=(14, 6))

#     ax1.set_title(f"{country} - CO₂ Emissions, Life Expectancy, and GDP Over Time")
#     ax1.set_xlabel("Year")

#     # CO2 on primary y-axis
#     ax1.plot(co2_series.index, co2_series.values, label='CO₂ per capita (tons)', color='green')
#     ax1.set_ylabel("CO₂ per capita (tons)", color='green')
#     ax1.tick_params(axis='y', labelcolor='green')

#     # Life expectancy on secondary y-axis
#     ax2 = ax1.twinx()
#     ax2.plot(life_series.index, life_series.values, label='Life Expectancy (years)', color='blue')
#     ax2.set_ylabel("Life Expectancy (years)", color='blue')
#     ax2.tick_params(axis='y', labelcolor='blue')

#     # GDP on tertiary y-axis (shifted to the right)
#     ax3 = ax1.twinx()
#     ax3.spines.right.set_position(("axes", 1.1))
#     ax3.plot(gdp_series.index, gdp_series.values, label='GDP per capita (US$)', color='red')
#     ax3.set_ylabel("GDP per capita (US$)", color='red')
#     ax3.tick_params(axis='y', labelcolor='red')

#     # Combine all legends
#     lines, labels = [], []
#     for ax in [ax1, ax2, ax3]:
#         line, label = ax.get_legend_handles_labels()
#         lines += line
#         labels += label
#     ax1.legend(lines, labels, loc='upper left')

#     plt.grid(True)
#     plt.tight_layout()
    
#     # Save the plot
#     filename = os.path.join(output_dir, f"{country.replace(',', '').replace(' ', '_').replace('.', '')}.png")
#     plt.savefig(filename, dpi=300)
#     plt.close()

#     print(f"Saved plot for {country} to {filename}")


### Plot both countries in one


# Extract data
co2_data = {country: extract_series(co2, country) for country in countries}
life_data = {country: extract_series(life_exp, country) for country in countries}
gdp_data = {country: extract_series(gdp, country) for country in countries}

# # A4 page size (portrait) in inches
# A4_SIZE = (8.27, 11.69)

# # Create a single figure with 3 vertical subplots
# fig, axs = plt.subplots(3, 1, figsize=A4_SIZE, sharex=True)


# # # Plot CO₂
# axs[0].set_title("CO₂ Emissions Per Capita (Metric Tons)", fontsize=12)
# for country, series in co2_data.items():
#     axs[0].plot(series.index, series.values, label=country, linewidth=2)
# axs[0].set_ylabel("CO₂ (tons)", fontsize=10)
# axs[0].legend(fontsize=8)
# axs[0].grid(True, linestyle='--', alpha=0.7)

# # Plot Life Expectancy
# axs[1].set_title("Life Expectancy at Birth (Years)", fontsize=12)
# for country, series in life_data.items():
#     axs[1].plot(series.index, series.values, label=country, linewidth=2)
# axs[1].set_ylabel("Years", fontsize=10)
# axs[1].legend(fontsize=8)
# axs[1].grid(True, linestyle='--', alpha=0.7)

# # Plot GDP
# axs[2].set_title("GDP Per Capita (Current US$)", fontsize=12)
# for country, series in gdp_data.items():
#     axs[2].plot(series.index, series.values, label=country, linewidth=2)
# axs[2].set_xlabel("Year", fontsize=10)
# axs[2].set_ylabel("GDP (US$)", fontsize=10)
# axs[2].legend(fontsize=8)
# axs[2].grid(True, linestyle='--', alpha=0.7)

# # Final adjustments and save
# plt.tight_layout()
# pdf_path = os.path.join(output_dir, "A4_country_comparison.pdf")
# fig.savefig(pdf_path, dpi=300)
# plt.close(fig)

# print(f"✅ Saved single A4 page with all plots to: {pdf_path}")


co2_ave = co2[year_columns].mean(axis=1)
print(country, co2_ave)