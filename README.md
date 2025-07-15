# -API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY: CODTECH IT SOLUTIONS

NAME: AMAN YADAV

"INTERN ID: CT06DH2225

"DOMAIN: PYTHON PROGRAMMING 

"DURATION: 6 WEEEKS

*MENTOR: NEELA SANTOSH

The primary goal of this task was to fetch live weather data from a public API and visualize it using Python libraries like matplotlib or seaborn. This task helps understand how APIs are integrated into Python applications and how the retrieved data can be transformed into meaningful visual insights.

Tools and Libraries Used:

requests: A Python library used to make HTTP requests to APIs.

matplotlib: Used for creating static, animated, and interactive visualizations in Python.

seaborn: A data visualization library based on matplotlib, providing a high-level interface for drawing attractive statistical graphics.

Approach:
Initially, I planned to use the OpenWeatherMap API, but it required an API key, and sometimes the free keys take time to activate. To keep the flow smooth, I switched to the wttr.in API which offers a keyless and real-time weather data feed in JSON format. This API provides weather forecasts for any city without registration.

In the script, I fetched the weather data for a city (e.g., Mumbai) using the API. I extracted the average temperatures for the next 3 days from the JSON response. These values were stored in lists along with their respective dates. Using matplotlib and seaborn, I plotted a bar chart that visually displayed how the average temperature varied over those days.

Output and Visualization:
The output was a clean and informative bar chart where:

The x-axis represented dates.

The y-axis represented average temperatures (°C).

Each bar indicated the average temperature for a particular day.
The graph had clear labels and a descriptive title, improving readability and presentation quality.

Learning Outcomes:

Understood how to use the requests library to communicate with external APIs.

Gained experience in handling JSON data responses and parsing relevant fields.

Learned how to convert real-time data into plots using matplotlib and seaborn.

Discovered the importance of choosing reliable and simple APIs for lightweight tasks.

Conclusion:
This task was a great introduction to integrating external data sources (APIs) with Python programs and presenting data visually. It demonstrates how even simple API responses can be transformed into meaningful visual insights with the help of Python’s powerful libraries. This skill is widely used in dashboards, reporting tools, and data-driven decision-making applications.

#output
<img width="1000" height="503" alt="Image" src="https://github.com/user-attachments/assets/3b90e21a-fa43-47eb-8960-337fa559ee52" />
<img width="1000" height="600" alt="Image" src="https://github.com/user-attachments/assets/4bf2632c-48c8-4f33-8d18-130664fc9015" />
<img width="800" height="632" alt="Image" src="https://github.com/user-attachments/assets/35746303-0dcf-4c2e-8c41-e2de6fb82bb3" />

