# -*- coding: utf-8 -*-
# """
# configs.py
# Created on Dec 17, 2024
# @ Author: Mazhar
# """

import logging
import os

import yaml

logger = logging.getLogger("app.logs")

CRAWL_CONFIGS = "./configs/crawl_config.yaml"
PDF_REPO_CONFIGS = "./configs/pdf_repo_config.yaml"

cfgs_crawl = {}
try:
    with open(CRAWL_CONFIGS, "r") as file:
        cfgs_crawl = yaml.safe_load(file)
except FileNotFoundError:
    logger.error(f"{CRAWL_CONFIGS} not found.")
    cfgs_crawl = {}
finally:
    if not cfgs_crawl:
        logger.error("No configuration found in the YAML file.")
        exit(1)

cfgs_repo = {}
try:
    with open(PDF_REPO_CONFIGS, "r") as file:
        cfgs_repo = yaml.safe_load(file)
except FileNotFoundError:
    logger.error(f"{PDF_REPO_CONFIGS} not found.")
    cfgs_repo = {}
finally:
    if not cfgs_repo:
        logger.error("No configuration found in the YAML file.")
        exit(1)
