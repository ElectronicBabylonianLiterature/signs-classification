import torch
from tqdm import tqdm
import numpy as np
def train_model(train_data, val_data, model,trained_model_path, batch_size=16, epochs=50):
    train_loader = torch.utils.data.DataLoader(train_data,
                                             batch_size=batch_size, shuffle=True,
                                             num_workers=4)
    val_loader = torch.utils.data.DataLoader(val_data,
                                             batch_size=batch_size, shuffle=True,
                                             num_workers=4)
    min_valid_loss = np.inf
    for epoch in tqdm(range(epochs)):
        train_loss = 0.0
        for data, labels in train_loader:
            if torch.cuda.is_available():
                data, labels = data.cuda(), labels.cuda()
            model.optimizer.zero_grad()
            target = model.model(data.float())
            loss = model.loss(target, labels)
            loss.backward()
            model.optimizer.step()
            train_loss += loss.item()
        val_loss = 0.0
        for data, labels in val_loader:
            if torch.cuda.is_available():
                data, labels = data.cuda(), labels.cuda()
            target = model.model(data.float())
            loss = model.loss(target, labels)
            val_loss = loss.item() * data.size(0)
        print(f'Epoch {epoch+1} \t\t Training Loss: {train_loss / len(train_loader)} \t\t Validation Loss: {val_loss / len(val_loader)}')
        if min_valid_loss > val_loss:
            print(f'Validation Loss Decreased({min_valid_loss:.6f}--->{val_loss:.6f}) \t Saving The Model')
            min_valid_loss = val_loss
            torch.save(model.model.state_dict(), trained_model_path)