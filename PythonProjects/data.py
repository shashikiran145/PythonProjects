import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 1. Generate synthetic data
# ----------------------------
np.random.seed(0)

true_mean = 7.0
sigma = 2.0

# simulate 200 observations
y = np.random.normal(true_mean, sigma, size=200)

# ----------------------------
# 2. Online mean prediction
# ----------------------------
predictions = []
means = []  # running means
residuals = []  # for conformal prediction

running_sum = 0

for t in range(len(y)):
    if t == 0:
        # no history yet -> predict 0 or None
        pred = 0
    else:
        pred = running_sum / t  # mean of past observations

    predictions.append(pred)

    # update running statistics
    running_sum += y[t]
    means.append(running_sum / (t + 1))

    # store nonconformity (absolute residual)
    residuals.append(abs(y[t] - pred))

# ----------------------------
# 3. Plot predictions vs true data
# ----------------------------
plt.figure(figsize=(12, 6))
plt.plot(y, label="Observed values")
plt.plot(predictions, label="Online mean predictions")
plt.axhline(true_mean, linestyle="--", color="gray", label="True mean")
plt.legend()
plt.title("Online Mean Predictor Converging to True Mean")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# ----------------------------
# 4. Conformal Prediction Interval (simple version)
# ----------------------------
alpha = 0.1  # 90% prediction interval
quantile = np.quantile(residuals, 1 - alpha)

# prediction interval for next point
next_pred = running_sum / len(y)
lower = next_pred - quantile
upper = next_pred + quantile

print("Next predicted value:", next_pred)
print("Conformal prediction interval:", (lower, upper))
