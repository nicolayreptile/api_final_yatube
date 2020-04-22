# API Yatube #


## Overview
This describes the resources that make up the Yatube API v1.

## Installation
It is can be installed like usual Django applictaion. 
 
## Current version
By now, Yatube API has only version 1.0

## Schema
All API access is over HTTP. All data is sent and received as JSON.

## Examples
### Authentication

`curl -H "Accept: application/json" -d "username=<user_id>&password=<user_secret>" http://localhost:8000/api/v1/token/`

### Get a list of all posts

`curl -H "Accept: application/json" -H "Authorization: Bearer my_token"  http://localhost:8000/api/v1/posts/`

All API methods describes at http://localhost:8000/redoc/
