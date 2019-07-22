# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Quick Start published on Azure.
#
# https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-train-models-with-aml
# https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py

from mlhub.pkg import azkey, azrequest, mlask, mlcat, mlpreview

mlcat("Azure Machine Learning API", """\
Welcome to a demo of the Azure Machine Learning framework, built to support
Data Scientists as they run experiments to build models based on best
practice and machine learning algorithms.

This demonstration illustrates the following capabilities:

  * Logging events, particularly experimental model performance;
  * Display logged information on a web-based dashboard.

Note that this demonstration uses a cloud-based workspace which requires you
to have an Azure subscription (free or paid).
""")

# pip3 install azureml-sdk[automl]

from azureml.core import VERSION, Workspace, Experiment

import time
import os
import sys
import webbrowser

import numpy as np
import matplotlib.pyplot as plt

# Share the core SDK version number for information purposes only.

print("We are using Azure ML SDK version: ", VERSION, "\n")

# Constants.

SERVICE   = "Machine Learning"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

# Attempt to load the configuration of an already created AzureML
# workspace. If it does not exists then create a workspace and save
# it. This requires authentication via the web portal. A new resource
# group is created.  The workspace configuration is saved/loaded from
# the config.json file. Might need an az login next time.

try:

    ws = Workspace.from_config()
    print()

except Exception:

    # Request subscription key and endpoint from user.

    subscription_key, endpoint = azkey(KEY_FILE, SERVICE)

    mlask(end="\n")

    mlcat("Create a Cloud Workspace", """\
An Azure Workspace for Machine Learning will now be created within
this subscription at the '{}' data centre. This will take a few minutes
whilst all of the dependent resources are created.
""".format(endpoint))
    
    ws = Workspace.create(name='azml_mlhub_image_classification',
                          subscription_id=subscription_key,
                          resource_group='azml_mlhub_image_classification',
                          create_resource_group=True,
                          location=endpoint,
                          exist_ok=True,
    )   

    # Save the configuration into config.json.  The same workspace can
    # be used in multiple environments through this JSON configuration
    # file. This saves the subscription, resource, and workspace name
    # data.

    mlcat("Saving the Configuration", """\
The configuration of the Workspace will be saved to file for
future use if so desired. The information saved to the file includes
the subscription id, resource group and workspace name.
""", begin="\n")

    ws.write_config(path=".", file_name="config.json")
    
    mlask(begin="\n", end="\n")
    
mlcat("Workspace Parameters", """\
An Azure Machine Learning Workspace will be utilised:

  name: {}
  location: {}
  resource group: {}

This workspace is now ready to support experimentation.

A series of dummy observations of model accuracy will be captured into
the workspace together with a dummy metric. What is the question?
""".format(ws.name, ws.location, ws.resource_group))

mlask(end="\n")

# Create an experiment to track the runs in your workspace. A
# workspace can have multiple experiments:

experiment_name = 'mlhub-demo'

exp = Experiment(workspace=ws, name=experiment_name)

# Start a run and start the logging service.

run = exp.start_logging()

# Log a single  number.

run.log('The Answer', 42)

# Log a list (Sample Accuracies).

run.log_list('Accuracies',
             [0, 50, 60, 70, 75, 80, 85, 87, 89, 90, 90, 91, 90, 93, 88,
              89, 92, 91, 90, 91, 89, 90, 91, 90, 91, 89, 90, 92]) 

# Finish the run.

run.complete()

mlcat("Workspace Dashboard", """\
A dashboard will now be displayed within your web browser. This is the Azure
Machine Learning Dashboard and provides a summary of the experiments 
performed. In this case we have a series of dummy observations of the 
accuracy of a model over a sequence of model builds.
""")

mlask()

# Display the URL in an external web browser. How do I get the result
# as an image here rather than refering to the web page?

url = run.get_portal_url()
webbrowser.open(url, new=2)

# Cleanup - delete all the resources, including the experiment results
# that have been captured! The Workspace can also be deleted using the
# Azure portal.

mlcat("Cleanup", """\
The Workspace you have been using can continue to be used. It can be 
managed through the Azure Portal and through the SDK. Alternatively
you can delete the Workspace here.""", begin="\n")

sys.stderr.write("\nShall I delete the Workspace (y|N)? ")
answer = input()
if len(answer) == 0: answer = "n"

if answer.lower() =="y":
    ws.delete(delete_dependent_resources=True)
    if os.path.exists("aml_config/config.json"):
        os.remove("aml_config/config.json")



# NEXT https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-train-models-with-aml
