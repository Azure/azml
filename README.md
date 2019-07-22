Getting Started
---------------

A workspace is required for AzureML. This is created using

```python
ws = Workspace.create(name='azml_mlhub_image_classification',
                      subscription_id='c7bc....2ddb',
                      resource_group='azml_mlhub_image_classification',
                      create_resource_group=True,
                      location='southeastasia'
                     )
```
This will prompt for interactive authentication:
```console
Performing interactive authentication. Please follow the instructions on the terminal.
Note, we have launched a browser for you to login. 
For old experience with device code, use "az login --use-device-code"
You have logged in. Now let us find all the subscriptions to which you have access...
Interactive authentication successfully completed.
UserWarning: The resource group doesn't exist or was not provided. 
AzureML SDK is creating a resource
group=azml_mlhub_image_classification in
location=southeastasia using subscription=c7bc...2ddb.
Deploying StorageAccount with name azmlmlhustoragecdiuowsz.
Deployed StorageAccount with name azmlmlhustoragecdiuowsz.
Deploying AppInsights with name azmlmlhuinsightsljuocxva.
Deployed AppInsights with name azmlmlhuinsightsljuocxva.
Deploying KeyVault with name azmlmlhukeyvaultawijzmvd.
Deploying ContainerRegistry with name azmlmlhuacryhasweqk.
Deployed ContainerRegistry with name azmlmlhuacryhasweqk.
Deployed KeyVault with name azmlmlhukeyvaultawijzmvd.
Deploying Workspace with name azml_mlhub_image_classification.
Deployed Workspace with name azml_mlhub_image_classification.
>>> 
```

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
