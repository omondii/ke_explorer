#!/usr/bin/env python3
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """ App configurations """
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')