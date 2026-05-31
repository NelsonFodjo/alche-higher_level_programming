#!/bin/bash
# Sends a GET request with custom header X-HolbertonSchool-User-Id set to 98
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
