#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_dBStorage(unittest.TestCase):
    """ Class to test the db storage method """
    