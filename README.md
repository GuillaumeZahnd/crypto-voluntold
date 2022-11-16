# README

## What? 

Quite elegant (yet perhaps a bit convoluted) way to promote a candidate.

## Why?

Critical need of a truly random process that is resistant against evil-maid attacks.

## How? 

Extra-secure cryptography approach:

```sh
candidate_block = email + previous_hash + stock + token
```

- `email`: Initiate the request (message received from the interlocutor)
- `previous_hash`: Authenticate the blockchain (irreversible history)
- `stock`: Prevent future manipulation with high-entropy last-minute unpredictability (stock market ticker of today)
- `token`: Candidate (name of a potential victim)

A list of tokens is mined, and the block with the minimum hash is selected.

## Example

### Email (template)

> From: Jafar <jafar@wanadoo.fr>
> 
> Sent: Monday, November 14, 2022 6:29 PM
> 
> To: Ratigan <ratigan@yahoo.co.jp>
> 
> Subject: Meeting
> 
> Dear Ratigan,
> 
> Let's have a meeting tomorrow at 15:30 to discuss important topics. 
> 
> YT,
> 
> Jafar

### Previous hash (template)

> 7e6b941a7e322a0570c7ea42097014f20ef739bfe123fceba910813c894459ce

### Stock (example, from `yfinance`)

> 245.66000366210938

### Token list (template)

> SnowWhite
>
> Cinderella
>
> Aurora
>
> Ariel
>
> Belle
>
> Jasmine
>
> Pocahontas
>
> Mulan
>
> Tiana
>
> Rapunzel
>
> Merida
>
> Moana

### Output

```sh
tokens[token_id]: 'SnowWhite'
block_sha: 'd0226b12137f4e700a16aed062b63562f90bb61c93f7236c42501c9fa80489a8'
tokens[token_id]: 'Cinderella'
block_sha: 'ab51516c764d3f936c6922082faa1b27c19f6deddb0d780208a4d5730acac9f4'
tokens[token_id]: 'Aurora'
block_sha: '8e59b2c77054d08b0e9a9c38090da11b96a359594378a6a7b5c29bd6c9c6a658'
tokens[token_id]: 'Ariel'
block_sha: '971285c6eb80a986b6bc277567065900448946e3f069ec7f47c0bbca1a985809'
tokens[token_id]: 'Belle'
block_sha: '0f21533221b0e08366efdca322834f4686b25f023e98d16c0fcbe2e01af3319f'
tokens[token_id]: 'Jasmine'
block_sha: '8ae05b8147d1b05d61ae37c6a22c95134b25cf09626ceabbdaaa5c743f3dbf74'
tokens[token_id]: 'Pocahontas'
block_sha: '25923cf5ff33618256e6af0bf283f2ae24c7e1c686e37ce78096b94c4716195d'
tokens[token_id]: 'Mulan'
block_sha: '23e546d596ed99fb8d15c9a78f9160c87919a5c469ca72ec3c7458dabf4adc33'
tokens[token_id]: 'Tiana'
block_sha: 'a12abbdbd300742c9a2b233d5650f4b1a77e0f7e1946960d3f62e8d34a79ae52'
tokens[token_id]: 'Rapunzel'
block_sha: '9367f4c996331714269994ab30645462828a49066f0918d04babef8bcc4093db'
tokens[token_id]: 'Merida'
block_sha: '569efa5d034e82a58cf9efe8d26005289ca1c1881f6c57028d0f60f7fc524f45'
tokens[token_id]: 'Moana'
block_sha: '3bbc92807f1202f5a8cc498334a62dc45f6870c3bf94bffdf8cc38b84462d4f9'
----------------------------------------------------------------
voluntold token: 'Belle'
sha_min: '0f21533221b0e08366efdca322834f4686b25f023e98d16c0fcbe2e01af3319f'
```

## Howto

```sh
git clone git@github.com:GuillaumeZahnd/crypto_voluntold.git
cd crypto_voluntold
cp templates/* ./
pipenv install
pipenv shell
python mine.py
```
