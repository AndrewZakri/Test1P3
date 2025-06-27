import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Test 1, Problem 3")
st.subheader("The WORST possible plot: A poorly designed visualization that misrepresents the data, is cluttered, lacks readability, or is misleading.")
# WORST possible plot

# Load dataset from BTS
df = pd.read_csv("co2_emission.csv")

# Filter for top 5 countries by total emissions
top5 = df.groupby('Country')['CO2 Emissions'].sum().nlargest(5).index
subset = df[df['Country'].isin(top5)]

# WORST Plot
fig, ax = plt.subplots(figsize=(15, 10))
for country in top5:
    country_data = subset[subset['Country'] == country]
    ax.plot(
        country_data['Year'], 
        country_data['CO2 Emissions'], 
        label=country, 
        linestyle='--', 
        marker='x', 
        linewidth=5
    )

ax.set_title("CO2 Emissions Over Time (Top 5 Countries)")
ax.set_xlabel("Year")
ax.set_ylabel("Emissions")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(True, linestyle='--', linewidth=1)
ax.set_xticklabels(country_data['Year'], rotation=90, fontsize=8)
ax.tick_params(axis='y', labelsize=8)
ax.axhline(1000000, color='red', linestyle=':', linewidth=3)

# Add plot to streamlit
st.pyplot(fig)
plt.clf()

st.write("The first plot is visually confusing. Data is represented in dashed lines and large markers (X). The line width is set at 5, which is too large. A legend is included, but it is outside the plot. This could cause issues when presenting the plot, as it could reduce the size of the plot in order to include the legend. The legend could also be excluded or partially removed due to lack of space (on the dashboard). A trend line (red dashed line) is included and is unnecessary. This line provides little value as it is set at zero and most if not all countries will have data above the line, especially in after the year 1900.")

st.subheader("The IMPROVED version: A refined visualization that enhances clarity, conveys insight effectively, and follows best practices in visual analytics.")

# IMPROVED version

# Set style
sns.set(style="whitegrid")

# Prepare summary data
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=subset, x="Year", y="CO2 Emissions", hue="Country", palette="Set2", ax=ax)

# Titles and labels
ax.set_title("CO2 Emissions Over Time (Top 5 Countries)", fontsize=16)
ax.set_xlabel("Year")
ax.set_ylabel("CO2 Emissions (in million metric tons)")
ax.legend(title="Country")

# Add plot to streamlit
plt.tight_layout()
st.pyplot(fig)

st.write("Visually, the second plot is much easier to view. The dotted red line (trend line) has been removed as it is unnecessary. Data is represented using a line plot which is much cleaner and consistent. A legend is included, however it is located inside the plot so it is readily available regardless of the size of the plot. The plot also takes advantage of the Seaborn toolset.")

