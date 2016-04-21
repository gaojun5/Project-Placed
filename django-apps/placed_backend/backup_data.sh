#!/bin/bash
rsync -avzh -e "ssh -i placed_keypair.pem" --progress ec2-user@ec2-52-18-65-54.eu-west-1.compute.amazonaws.com:/home/ec2-user/realdata.json ./placed_backend/data/real/ 