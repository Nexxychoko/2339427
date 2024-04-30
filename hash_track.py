import hashlib

def hash_data(data, label, encoding='utf-8'):
  """
  Hashes data and concatenates with label hash for potential anomaly detection.

  Args:
      data: A string representing the data to be hashed.
      label: The label (class) of the data point (can be string or integer).
      encoding (str, optional): The encoding to use for converting strings to bytes before hashing. Defaults to 'utf-8'.

  Returns:
      A tuple containing two hash values:
          - data_hash: The hash of the data.
          - combined_hash: The hash of the concatenated data and label.
  """

  # Ensure data is a string
  if not isinstance(data, str):
    raise TypeError("Data must be a string.")

  # Ensure label is a string or integer (for flexibility)
  if not isinstance(label, (str, int)):
    raise TypeError("Label must be a string or an integer.")

  # Convert data and label to bytes using the specified encoding
  data_bytes = data.encode(encoding)
  label_bytes = str(label).encode(encoding)  # Convert label to string first

  # Hash data and combined data + label
  data_hash = hashlib.sha256(data_bytes).hexdigest()
  combined_hash = hashlib.sha256(data_bytes + label_bytes).hexdigest()

  return data_hash, combined_hash

# Example usage
data = "This is some data"
label = "positive"  # Can also use an integer value for label

try:
  original_data_hash, original_combined_hash = hash_data(data, label)

  # Simulate label flipping (change label value)
  flipped_label = "negative"

  flipped_data_hash, flipped_combined_hash = hash_data(data, flipped_label)

  # Check if the combined hash changed significantly (indicating potential flip)
  if original_combined_hash != flipped_combined_hash:
    print("Combined hash changed! Potential label flip detected.")
  else:
    print("Combined hash remains the same. No immediate sign of flipping.")
except TypeError as e:
  print(f"Error: {e}")

# Note: This is a basic example. Implement thresholds and further checks for real-world applications.
