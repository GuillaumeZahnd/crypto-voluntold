import string
import hashlib
import random
import yfinance as yf
from icecream import ic


if __name__ == '__main__':

  # [Blockchain] --> Current email...
  filename_email = 'email.txt'
  with open(filename_email, 'r') as fid:
    email = fid.read().strip('\n')
  ic(email)
  input('-' * 64)

  # [Blockchain] --> ...and previous hash
  filename_previous_hash = 'previous_hash.txt'
  with open(filename_previous_hash, 'r') as fid:
    previous_hash = fid.read().strip('\n')
  ic(previous_hash)
  input('-' * 64)

  # [Unpredictability] --> Today stock market value
  ticker = 'MSFT'
  stock  = str(yf.Ticker(ticker).history(period='1d')['Close'][0])
  ic(ticker, stock)
  input('-' * 64)

  # [Mining] --> Process of establishing a valid candidate
  leading_zeros = 8     # Difficulty (condition to promote a valid block)
  length_min    = 5     # Shortest possible name (e.g. "BoLiu")
  length_max    = 20    # Longest possible name (e.g., "AmbroseRastapopoulos")
  valid_block   = False # Initial conditions
  itx           = 0     # Initial conditions
  itx_max       = 1e4   # Upper limit to the number of attempts to mint a valid block
  while not valid_block and itx < itx_max:
    itx       +=1
    length    = random.SystemRandom().randint(length_min, length_max)
    token     = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(length))
    block     = email + previous_hash + stock + token
    block_sha = hashlib.sha256(block.encode()).hexdigest()
    if block_sha[:leading_zeros] == '0' * leading_zeros:
      valid_block = True
    ic(itx, token, block_sha, valid_block)
  input('-' * 64)

  # [Token list] --> List of candidates
  filename_token_list = 'token_list.txt'
  with open(filename_token_list, 'r') as fid:
    token_list = fid.read().strip().split()
  ic(token_list)
  input('-' * 64)

  # [Simplified mining] --> Hash-based sorting
  sha_min = 'f' * 64 # Set hash to maximum hexadecimal value
  for token_id in range(len(token_list)):
    block = email + previous_hash + stock + token_list[token_id]
    block_sha = hashlib.sha256(block.encode()).hexdigest()
    ic(token_id, token_list[token_id], block_sha)
    if block_sha < sha_min:
      sha_min = block_sha
      most_acceptable_token_id = token_id
  input('-' * 64)

  # [Promotion] --> Selection of the most acceptable token
  most_acceptable_token = token_list[most_acceptable_token_id]
  ic(most_acceptable_token_id, most_acceptable_token, sha_min)
  input('-' * 64)

  # [Blockchain] --> Store the current hash for future use
  filename_current_hash = 'current_hash.txt'
  with open(filename_current_hash, 'w') as fid:
    fid.write(sha_min)
