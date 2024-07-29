import torch
import time
import torch.nn as nn
from Model.Transformer import Transformer
from DataProvider import stockData
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt


train_data, target_data = stockData.get_multiple_stock_data()

train_data = torch.tensor(train_data, dtype=torch.float32)  # 将数据转换为浮点张量
target_data = torch.tensor(target_data, dtype=torch.float32)

train_dataset = TensorDataset(train_data, target_data)
train_loader = DataLoader(train_dataset, batch_size=30, shuffle=None)


model = Transformer(
    feature_size=5,
    # num_layers=1,
    num_layers=3,
    # num_layers=6,
    num_heads=1,
    forward_expansion=4
)

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)



num_epochs = 50
for epoch in range(num_epochs):
    t1 = time.time()

    for inputs, labels in train_loader:
        outputs = model(inputs)
        loss = criterion(outputs.squeeze(), labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    t2 = time.time()
    print( t2 - t1, '  second' )


test_data, actual_data = stockData.get_test_stock_data()

print(test_data)
print(actual_data)
test_data = torch.tensor(test_data, dtype=torch.float32)
actual_data = torch.tensor(actual_data, dtype=torch.float32)
test_dataset = TensorDataset(test_data, actual_data)
test_loader = DataLoader(test_dataset, batch_size=30, shuffle=False)

model.eval()
predictions = []
actuals = []
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        print(outputs)
        predictions.extend(outputs.squeeze().tolist())
        actuals.extend(labels.tolist())
        actuals = [item[0][0] if isinstance(item, list) and isinstance(item[0], list) else item for item in actuals]

        print(actuals)


plt.figure(figsize=(10, 6))
plt.plot(actuals, label='Actual Values')
plt.plot(predictions, label='Predicted Values')
plt.title('Actual vs Predicted Stock Prices')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.show()
