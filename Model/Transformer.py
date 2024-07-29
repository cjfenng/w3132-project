
import torch.nn as nn
class Transformer(nn.Module):
    def __init__(self, feature_size, num_layers, num_heads, forward_expansion):
        super(Transformer, self).__init__()
        self.encoder_layer = nn.TransformerEncoderLayer(
            d_model=feature_size,
            nhead=num_heads,
            dim_feedforward=feature_size * forward_expansion,
            batch_first=True,
        )
        self.transformer_encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        self.fc_out = nn.Linear(feature_size, 1)

    def forward(self, src):
        transformer_out = self.transformer_encoder(src)
        out = self.fc_out(transformer_out[:,-1,:])
        return out