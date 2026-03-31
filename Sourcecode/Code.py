# Stock Price Trend Analyzer
# Name: Aditi Tiwari
# Roll No: 25BCE10724
# Course: Fundamentals of AI and ML


# I am importing the libraries needed for this project
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -----------------------------------------------
# STEP 1: I am creating some sample stock price data
# (This is like a small dataset of 30 days of stock prices)
# -----------------------------------------------

# These are the days (Day 1 to Day 30)
days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

# These are the closing stock prices for those days (in rupees)
# I added some random ups and downs to make it look real
prices = np.array([150, 153, 148, 155, 160, 158, 162, 165, 163, 170,
                   172, 169, 175, 178, 174, 180, 182, 179, 185, 188,
                   186, 190, 193, 191, 196, 199, 197, 202, 205, 210])

# -----------------------------------------------
# STEP 2: Preparing data for the ML model
# sklearn needs the input in 2D shape, so I reshape it
# -----------------------------------------------

X = days.reshape(-1, 1)   # This is the input (days)
y = prices                 # This is the output (prices)

# -----------------------------------------------
# STEP 3: Applying Linear Regression
# Linear Regression is a simple ML algorithm that tries to
# find a straight line that best fits the data
# -----------------------------------------------

model = LinearRegression()
model.fit(X, y)   # Training the model on our data

# -----------------------------------------------
# STEP 4: Making Predictions
# -----------------------------------------------

predicted_prices = model.predict(X)

# I also want to predict the price for next 5 days (Day 31 to 35)
future_days = np.array([31, 32, 33, 34, 35]).reshape(-1, 1)
future_prices = model.predict(future_days)

# -----------------------------------------------
# STEP 5: Checking how good the model is
# -----------------------------------------------

mse = mean_squared_error(y, predicted_prices)
r2 = r2_score(y, predicted_prices)

print("=" * 45)
print("   STOCK PRICE TREND ANALYZER RESULTS")
print("=" * 45)
print(f"\nSlope (trend per day)  : {model.coef_[0]:.2f}")
print(f"Intercept              : {model.intercept_:.2f}")
print(f"Mean Squared Error     : {mse:.2f}")
print(f"R² Score               : {r2:.4f}")
print("\nWhat is R² Score?")
print("  It tells how well the line fits the data.")
print("  1.0 means perfect fit, 0 means no fit.")

print("\n--- Predicted prices for next 5 days ---")
for i, day in enumerate([31, 32, 33, 34, 35]):
    print(f"  Day {day}: ₹{future_prices[i]:.2f}")

# -----------------------------------------------
# STEP 6: Plotting the Graph
# I am making 2 graphs:
#   1. Actual vs Predicted prices
#   2. Future price prediction
# -----------------------------------------------

plt.figure(figsize=(12, 5))

# --- Graph 1: Actual vs Predicted ---
plt.subplot(1, 2, 1)
plt.scatter(days, prices, color='blue', label='Actual Prices', zorder=5)
plt.plot(days, predicted_prices, color='red', linewidth=2, label='Regression Line')
plt.title('Stock Price Trend (Linear Regression)')
plt.xlabel('Day')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(True)

# --- Graph 2: Future Prediction ---
plt.subplot(1, 2, 2)
plt.plot(days, prices, color='blue', marker='o', label='Past Prices')
plt.plot([31, 32, 33, 34, 35], future_prices, color='green',
         marker='s', linestyle='--', label='Predicted Future Prices')
plt.axvline(x=30, color='gray', linestyle=':', label='Today')
plt.title('Future Stock Price Prediction')
plt.xlabel('Day')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(True)

plt.suptitle('Stock Price Trend Analyzer - Aditi Tiwari (25BCE10724)', fontsize=11)
plt.tight_layout()
plt.savefig('stock_price_output.png', dpi=150)
plt.show()

print("\nGraph saved as 'stock_price_output.png'")
print("\nProject completed successfully!")
