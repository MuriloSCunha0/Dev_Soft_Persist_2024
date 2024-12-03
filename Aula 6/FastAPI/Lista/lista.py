import yaml
import json
import logging
from fastapi import FastAPI, HTTPException

app = FastAPI()

#Create a logger object
logger = logging.getLogger(__name__)