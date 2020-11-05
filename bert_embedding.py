class BertEmbeddings:
 
  def __init__(self):
    self.model = BertModel.from_pretrained('bert-base-uncased',
                                  output_hidden_states = True, # Whether the model returns all hidden-states.
                                  )
    self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    
  def embed_text(self, text_to_embed):
    
    marked_text = "[CLS] " + text_to_embed + " [SEP]"
    tokenized_text = self.tokenizer.tokenize(marked_text)
    indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)
 
    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
 
    with torch.no_grad():
      
      outputs = self.model(tokens_tensor, segments_tensors)
      # Evaluating the model will return a different number of objects based on 
      # how it's  configured in the `from_pretrained` call earlier. In this case, 
      # becase we set `output_hidden_states = True`, the third item will be the 
      # hidden states from all layers. See the documentation for more details:
      # https://huggingface.co/transformers/model_doc/bert.html#bertmodel
      hidden_states = outputs[2]
      
    # Concatenate the tensors for all layers. We use `stack` here to
    # create a new dimension in the tensor.
    token_embeddings = torch.stack(hidden_states, dim=0)
    
    # Remove dimension 1, the "batches".
    token_embeddings = torch.squeeze(token_embeddings, dim=1)
 
    # Swap dimensions 0 and 1.
    token_embeddings = token_embeddings.permute(1,0,2)
 
    # Stores the token vectors, with shape [31 x 768]
    token_vecs_sum = []
 
    # For each token in the sentence...
    for token in token_embeddings:
 
        # `token` is a [12 x 768] tensor
 
        # Sum the vectors from the last four layers.
        sum_vec = torch.sum(token[-4:], dim=0)
        
        # Use `sum_vec` to represent `token`.
        token_vecs_sum.append(sum_vec)
 
    total_vector_sum = torch.zeros([1,768])
 
    for i in range(len(token_vecs_sum)):
        total_vector_sum += token_vecs_sum[i]
 
    return total_vector_sum
