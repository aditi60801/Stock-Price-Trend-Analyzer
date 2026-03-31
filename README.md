# Stock-Price-Trend-Analyzer
Stock Price Trend Analyzer (Readme File)  
Description 
• This project analyzes stock prices over 30 days and finds a trend pattern in 
them using Machine Learning. 
• I made it because I wanted to apply the Linear Regression algorithm (which 
we studied in class) on a real-world type of problem. 
• It solves the problem of understanding whether stock prices are going up or 
down, and also predicts what the price might be in the next 5 days. 
Features 
This Project ACtively :- 
• Analyzes 30 days of stock price data 
• Applies Linear Regression to find the price trend 
• Predicts stock prices for the next 5 future days 
• Shows a graph of Actual Prices vs Regression Line 
• Shows a Future Prediction graph 
• Prints R² Score and MSE to evaluate the model 
• Saves the output graph as a PNG image automatically 
Technologies Used IN the project 
• Python 3 — Main programming language 
• NumPy — For handling numbers and arrays 
• Matplotlib — For plotting and visualizing graphs 
• Scikit-learn — For the Linear Regression ML model 
• GitHub — For version control and project submission 
Project Structure 
stock-price-trend-analyzer/ 
│── stock_price_analyzer.py    
│── stock_price_output.png     
│── README.md                  
# Main Python code file 
# Graph image (auto-generated on run) 
# This file 
Installation & Setup for project 
Steps to run this project on your computer: 
1. Clone the repository 
git clone <your-repo-link> 
2. Open the folder 
cd stock-price-trend-analyzer 
3. Install the required libraries 
pip install numpy matplotlib scikit-learn 
4. Run the project 
python stock_price_analyzer.py 
How to use 
• Step 1 — Run the Python file using the command above 
• Step 2 — The terminal will show the R² Score, MSE, slope, and predicted 
prices for Day 31 to Day 35 
• Step 3 — A graph window will open showing two charts — one for Actual vs 
Predicted prices and one for Future Prediction 
• Step 4 — The graph is automatically saved as stock_price_output.png in 
the same folder 
• Step 5 — You can change the prices array in the code to use your own stock 
data 
Output 
Graph generated after running the project: 
What I Learned From this project 
• How to apply Linear Regression on a dataset 
• How to visualize data using Matplotlib 
• What R² Score and MSE mean and how to read them 
• How a Machine Learning model is trained and used for predictions 
Limitations 
• The stock data used is sample data, not real market data 
• Linear Regression works best when data follows a straight line trend 
• Real stock prices are more complex and unpredictable 
Project by Aditi Tiwari | Roll No: 25BCE10724 | Fundamentals of AI and ML | Winter 
Sem 2025-26
