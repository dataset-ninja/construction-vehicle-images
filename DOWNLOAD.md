Dataset **Construction Vehicle Images** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/o/t/J5/kHd6wnBwWmJ0aRofunMJZnObOC0JymqJtiK4Ohrxc1qmuw7n7rVkPvs7ejUVJqYeHMuL6PXK3vA2wRv2ECadhz7qOo2UmczUQLlac0Sb91ul1o5OJIp76MgDtxBv.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Construction Vehicle Images', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/dataclusterlabs/construction-vehicle-images/download?datasetVersionNumber=2).