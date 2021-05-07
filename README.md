# jose-cuevas-02201981
 travel agency
[TOC]

## Docker deployment Instructions

1.- docker build .
2.- docker-compoose up -d
3.- If you have Portainer in your docker its more easy manage and test this containers (Read about deploy portainer on Docker)


## Example for Database in MongoDB

{
  "_id": {
    "$oid": "6094164bf0e01e4df08a06fc"
  },
  "id": 1,
  "name": "US",
  "currency": "USD",
  "symbol": "$",
  "centseparator": ".",
  "millionseparator": ",",
  "locale": "en-EN",
  "decimals": "2",
  "displaysymbol": "front"
}

## Example for run Test in Coverage

coverage run -m unittest countries

## Example for run Test in Coverage

python3 manage.py test